---
layout: doc
title: Management API
permalink: /doc/mgmt1/
---

# Management API

*(This page is the current draft of the proposal. It is not implemented yet.)*

The API should be implemented as a set of qrexec calls. This is to make it easy
to set the policy using current mechanism.

## The calls

<style>
tbody td {
        padding: .1em;
        white-space: nowrap;
}
</style>
<table><thead>
<tr><th>call</th><th>dest</th><th>argument</th><th>inside</th><th>return</th><th>note</th></tr>
</thead><tbody>
<tr><td> mgmt1.vm.List                           </td><td> "dom0"                 </td><td> -             </td><td> -                                         </td><td> "&lt;name&gt; class=&lt;class&gt; state=&lt;state&gt;\n" </td><td></td></tr>
<tr><td> mgmt1.vm.Create                         </td><td> template or "dom0"     </td><td> class         </td><td> "name=&lt;name&gt; label=&lt;label&gt;"   </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.CreateInPool                   </td><td> template or "dom0"     </td><td> class         </td><td> "name=&lt;name&gt; label=&lt;label&gt; pool=&lt;pool&gt;" </td><td> -                       </td><td></td></tr>
<tr><td> mgmt1.vm.CreateTemplate                 </td><td> "dom0"                 </td><td> name          </td><td> root.img                                  </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.property.List                  </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> "&lt;property&gt;\n"                    </td><td></td></tr>
<tr><td> mgmt1.vm.property.Get                   </td><td> vm                     </td><td> property      </td><td> -                                         </td><td> "default={yes|no} &lt;value&gt;"        </td><td></td></tr>
<tr><td> mgmt1.vm.property.Help                  </td><td> vm                     </td><td> property      </td><td> -                                         </td><td> help.rst                                </td><td></td></tr>
<tr><td> mgmt1.vm.property.Reset                 </td><td> vm                     </td><td> property      </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.property.Set                   </td><td> vm                     </td><td> property      </td><td> value                                     </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.feature.List                   </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> "&lt;feature&gt;\n"                     </td><td></td></tr>
<tr><td> mgmt1.vm.feature.Get                    </td><td> vm                     </td><td> feature       </td><td> -                                         </td><td> value                                   </td><td></td></tr>
<tr><td> mgmt1.vm.feature.CheckWithTemplate      </td><td> vm                     </td><td> feature       </td><td> -                                         </td><td> value                                   </td><td></td></tr>
<tr><td> mgmt1.vm.feature.Remove                 </td><td> vm                     </td><td> feature       </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.feature.Set                    </td><td> vm                     </td><td> feature       </td><td> value                                     </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.tag.List                       </td><td> vm                     </td><td> tag           </td><td> -                                         </td><td> "&lt;tag&gt;\n"                         </td><td></td></tr>
<tr><td> mgmt1.vm.tag.Get                        </td><td> vm                     </td><td> tag           </td><td> -                                         </td><td> "0" or "1"                              </td><td>retcode?</td></tr>
<tr><td> mgmt1.vm.tag.Remove                     </td><td> vm                     </td><td> tag           </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.tag.Set                        </td><td> vm                     </td><td> tag           </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.firewall.Get                   </td><td> vm                     </td><td> position      </td><td> -                                         </td><td> "&lt;rule id&gt; &lt;rule&gt;\n"        </td><td></td></tr>
<tr><td> mgmt1.vm.firewall.InsertRule            </td><td> vm                     </td><td> position      </td><td> rule                                      </td><td> rule id                                 </td><td></td></tr>
<tr><td> mgmt1.vm.firewall.RemoveRule            </td><td> vm                     </td><td> rule id       </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.firewall.Flush                 </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.device.&lt;class&gt;.Attach    </td><td> vm                     </td><td> device        </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.device.&lt;class&gt;.Detach    </td><td> vm                     </td><td> device        </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.device.&lt;class&gt;.List      </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> "&lt;device&gt;\n"                      </td><td></td></tr>
<tr><td> mgmt1.vm.device.&lt;class&gt;.Available </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> "&lt;device&gt;\n"                      </td><td></td></tr>
<tr><td> mgmt1.vm.microphone.Attach              </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.microphone.Detach              </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.pool.List                         </td><td> "dom0"                 </td><td> -             </td><td> -                                         </td><td> "&lt;pool&gt;\n"                        </td><td></td></tr>
<tr><td> mgmt1.pool.Info                         </td><td> "dom0"                 </td><td> pool          </td><td> -                                         </td><td> "&lt;property&gt;=&lt;value&gt;\n"      </td><td></td></tr>
<tr><td> mgmt1.pool.Add                          </td><td> "dom0"                 </td><td> pool          </td><td> "&lt;property&gt;=&lt;value&gt;\n"        </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.pool.Remove                       </td><td> "dom0"                 </td><td> pool          </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.pool.volume.List                  </td><td> "dom0"                 </td><td> pool          </td><td> -                                         </td><td> volume id                               </td><td></td></tr>
<tr><td> mgmt1.pool.volume.Info                  </td><td> "dom0"                 </td><td> pool:vid      </td><td> -                                         </td><td> "&lt;property&gt;=&lt;value&gt;\n"      </td><td></td></tr>
<tr><td> mgmt1.pool.volume.ListSnapshots         </td><td> "dom0"                 </td><td> pool:vid      </td><td> -                                         </td><td> "&lt;snapshot&gt;\n"                    </td><td></td></tr>
<tr><td> mgmt1.pool.volume.Snapshot              </td><td> "dom0"                 </td><td> pool:vid      </td><td> -                                         </td><td> snapshot                                </td><td></td></tr>
<tr><td> mgmt1.pool.volume.Revert                </td><td> "dom0"                 </td><td> pool:vid      </td><td> snapshot                                  </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.pool.volume.Extend                </td><td> "dom0"                 </td><td> pool:vid      </td><td> -                                         </td><td> "&lt;size_in_bytes&gt;"                 </td><td></td></tr>
<tr><td> mgmt1.vm.volume.List                    </td><td> vm                     </td><td> -/pool?       </td><td> -                                         </td><td> ?                                       </td><td></td></tr>
<tr><td> mgmt1.vm.volume.Info                    </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> ?                                       </td><td></td></tr>
<tr><td> mgmt1.vm.volume.ListSnapshots           </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> snapshot                                </td><td>duplicate of mgmt1.pool.volume., but with other call params</td></tr>
<tr><td> mgmt1.vm.volume.Snapshot                </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> snapshot                                </td><td>id.</td></tr>
<tr><td> mgmt1.vm.volume.Revert                  </td><td> vm                     </td><td> volume        </td><td> snapshot                                  </td><td> -                                       </td><td>id.</td></tr>
<tr><td> mgmt1.vm.volume.Extend                  </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> "&lt;size_in_bytes&gt;"                 </td><td>id.</td></tr>
<tr><td> mgmt1.vm.volume.Attach                  </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.volume.Detach                  </td><td> vm                     </td><td> volume        </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.Start                          </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.Shutdown                       </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.Pause                          </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.Unpause                        </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.vm.Kill                           </td><td> vm                     </td><td> -             </td><td> -                                         </td><td> -                                       </td><td></td></tr>
<tr><td> mgmt1.backup.Execute                    </td><td> "dom0"                 </td><td> config id     </td><td> -                                         </td><td> -                                       </td><td>config in /etc/qubes/backup/&lt;id&gt;.conf</td></tr>
<tr><td> mgmt1.backup.Info                       </td><td> "dom0"                 </td><td> ?             </td><td> content?                                  </td><td> ?                                       </td><td></td></tr>
<tr><td> mgmt1.backup.Restore                    </td><td> "dom0"                 </td><td> ?             </td><td> content                                   </td><td> ?                                       </td><td></td></tr>
</tbody></table>


## Tags

- created-by-&lt;vm&gt;
- managed-by-&lt;vm&gt;
- backup-&lt;id&gt;

## TODO

- something to configure/update policy
