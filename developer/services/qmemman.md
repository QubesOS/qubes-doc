---
layout: doc
permalink: /doc/qmemman/
redirect_from:
- /en/doc/qmemman/
- /doc/Qmemman/
- /wiki/Qmemman/
title: Qmemman
---

qmemman, Qubes memory manager
=============================

Rationale
---------

Traditionally, Xen VMs are assigned a fixed amount of memory. It is not the optimal solution, as some VMs may require more memory than assigned initially, while others underutilize memory. Thus, there is a need for solution capable of shifting free memory from VM to another VM.

The [tmem](https://oss.oracle.com/projects/tmem/) project provides a "pseudo-RAM" that is assigned on per-need basis. However this solution has some disadvantages:

- It does not provide real RAM, just an interface to copy memory to/from fast, RAM-based storage. It is perfect for swap, good for file cache, but not ideal for many tasks.
- It is deeply integrated with the Linux kernel. When Qubes will support Windows guests natively, we would have to port *tmem* to Windows, which may be challenging.

Therefore, in Qubes another solution is used. There is the *qmemman* dom0 daemon. All VMs report their memory usage (via xenstore) to *qmemman*, and it makes decisions on whether to balance memory across domains. The actual mechanism to add/remove memory from a domain (*xc.domain\_set\_target\_mem*) is already supported by both PV Linux guests and Windows guests (the latter via PV drivers).

Similarly, when there is need for Xen free memory (for instance, in order to create a new VM), traditionally the memory is obtained from dom0 only. When *qmemman* is running, it offers an interface to obtain memory from all domains.

To sum up, *qmemman* pros and cons. Pros:

- provides automatic balancing of memory across participating PV and HVM domains, based on their memory demand
- works well in practice, with less than 1% CPU consumption in the idle case
- simple, concise implementation

Cons:

- the algorithm to calculate the memory requirement for a domain is necessarily simple, and may not closely reflect reality
- *qmemman* is notified by a VM about memory usage change not more often than 10 times per second (to limit CPU overhead in VM). Thus, there can be up to 0.1s delay until qmemman starts to react to the new memory requirements
- it takes more time to obtain free Xen memory, as all participating domains need to instructed to yield memory

Interface
---------

*qmemman* listens for the following events:

- writes to `/local/domain/domid/memory/meminfo` xenstore keys by *meminfo-writer* process in VM. The content of this key is taken from the VM's `/proc/meminfo` pseudofile ; *meminfo-writer* just strips some unused lines from it. Note that *meminfo-writer* writes its xenstore key only if the VM memory usage has changed significantly enough since the last update (by default 30MB), to prevent flooding with almost identical data
- commands issued over Unix socket `/var/run/qubes/qmemman.sock`. Currently, the only command recognized is to free the specified amount of memory. The QMemmanClient class implements the protocol.
- if the `/var/run/qubes/do-not-membalance` file exists, *qmemman* suspends memory balancing. It is primarily used when allocating memory for a to-be-created domain, to prevent using up the free Xen memory by the balancing algorithm before the domain creation is completed.

Algorithms basics
-----------------

The core VM property is `prefmem`. It denotes the amount of memory that should be enough for a domain to run efficiently in the nearest future. All *qmemman* algorithms will never shrink domain memory below `prefmem`. Currently, `prefmem` is simply 130% of current memory usage in a domain (without buffers and cache, but including swap). Naturally, `prefmem` is calculated by *qmemman* based on the information passed by *meminfo-writer*.

Whenever *meminfo-writer* running in domain A provides new data on memory usage to *qmemman*, the `prefmem` value for A is updated and the following balance algorithm (*qmemman\_algo.balance*) is triggered. Its output is the list of (domain\_id, new\_memory\_target\_to\_be\_set) pairs:

1. TOTAL\_PREFMEM = sum of `prefmem` of all participating domains
2. TOTAL\_MEMORY = sum of all memory assigned to participating domains plus Xen free memory
3. if TOTAL\_MEMORY \> TOTAL\_PREFMEM, then redistribute TOTAL\_MEMORY across all domains proportionally to their `prefmem`
4. if TOTAL\_MEMORY \< TOTAL\_PREFMEM, then
    1. for all domains whose `prefmem` is less than actual memory, shrink them to their `prefmem`
    2. redistribute memory reclaimed in the previous step between the rest of domains, proportionally to their `prefmem`

In order to avoid too frequent memory redistribution, it is actually executed only if one of the below conditions hold:

- the sum of memory size changes for all domains is more than MIN\_TOTAL\_MEMORY\_TRANSFER (150MB)
- one of the domains is below its `prefmem`, and more than MIN\_MEM\_CHANGE\_WHEN\_UNDER\_PREF (15MB) would be added to it

Additionally, the balance algorithm is tuned so that XEN\_FREE\_MEM\_LEFT (50MB) is always left as Xen free memory, to make coherent memory allocations in driver domains work.

Whenever *qmemman* is asked to return X megabytes of memory to Xen free pool, the following algorithm (*qmemman\_algo.balloon*) is executed:

1. find all domains ("donors") whose actual memory is greater than its `prefmem`
2. calculate how much memory can be reclaimed by shrinking donors to their `prefmem`. If it is less than X, return error.
3. shrink donors, proportionally to their `prefmem`, so that X MB should become free
4. wait BALOON\_DELAY (0.1s)
5. if some domain have not given back any memory, remove it from the donors list, and go to step 2, unless we already did MAX\_TRIES (20) iterations (then return error).

Notes
-----

Conventional means of viewing the memory available to Qubes will give incorrect values for `dom0` since commands such as `free` will only show the memory allocated for `dom0`. Run the `xl info` command in `dom0` and read the `total_memory` field to see the total memory available to Qubes.
