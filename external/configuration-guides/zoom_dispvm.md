# Running Zoom in a DispVM
## Intro
Zoom is a fairly widely-used video conferencing application that runs on a variety of platforms. In this guide we will go through the process of setting up a Disposable VM for Zoom. 

### Why we will use a DispVM
By running Zoom alone in a Disposable VM, we can improve the safety of using the application. DispVMs ensure that even if a Zoom exploit leads to the entire DispVM being compromised, it is *contained* to the DispVM which is destroyed once you shutdown the Qube or exit Zoom. No persistence, limited attack surface, and zero trust. 

## Step 0: Clone a TemplateVM
1. Open `Qubes Manager`.
2. Right-click on the `debian-10` TemplateVM.
3. Click `Clone Qube`.
4. Name the cloned qube `videoconferencing`.

*Alternatively:*

1. Open Terminal Emulator in dom0
2. Clone the `debian-10` template to new template `videoconferencing`:
	`qvm-clone --verbose debian-10 videoconferencing`

## Step 1: Download Zoom for Debian 8.0+ 64-bit
### Download and import Zoom's signing key: 
1. Open `Xfce Terminal` from `whonix-ws-15-dvm` **Make a note of the Qube name in the title. This will be used in step 2.** 
2. Download Zoom's GPG key using wget:
	`wget "https://zoom.us/linux/download/pubkey"`
3. Import Zoom's Public Key:
	`gpg --import pubkey`
### Download and verify Zoom, then copy to TemplateVM:
1. Download Zoom using `wget`:
	`wget "https://zoom.us/client/latest/zoom_amd64.deb"`
2. Verify `zoom_amd64.deb`:
	`gpg --verify zoom_amd64.deb`
3. Copy `zoom_amd64.deb` to TemplateVM `videoconferencing`:
	`qvm-copy zoom_amd64.deb`
4. Select the `videoconferencing` TemplateVM as the destination to copy `zoom_amd64.deb` to.
5. Shutdown the TemplateVM:
	`sudo shutdown now`

## Step 2: Install Zoom in TemplateVM
### Install Zoom in the `videoconferencing` TemplateVM:
1. Open `Terminal` from TemplateVM `videoconferencing`
2. Check QubesIncoming folder contents:
	`ls QubesIncoming`
3. You should see a folder with the same name as the Qube name in the title from the end of step 2. **In the following example, the Qube name was disp6247.** 
4. Change directory to the location of `zoom_amd64.deb`:
	`cd ~/QubesIncoming/disp6247/`
5. Install Zoom using `apt-get`:
	`sudo apt-get install -y ./zoom_amd64.deb`
6. Shutdown the TemplateVM
	`sudo shutdown now`

## Step 3: Create AppVM and configure it for use as a DispVM
1. Open `Create Qubes VM`.
2. Name the Qube `videoconferencing-dvm` and label it `red` to indicate the lowest level of trust.
3. Select `AppVM` as the type of qube to be created. *This is the default.*
4. Select `videoconferencing` as the template for the AppVM Qube.
5. Choose `sys-firewall` for networking. 
6. Click `OK`.

## Step 4: Add Zoom to the AppVM's list of applications
1. Open `Qube Manager`
2. `Search` for the `videoconferencing` TemplateVM. Right-click it and select `Qube Settings`
3. Click the `Applications` tab. 
4. Click `Zoom` to highlight it, then click the `>` button to add it to the AppVM's application list.
5. Click `OK`.  
