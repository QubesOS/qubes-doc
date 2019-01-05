This Howto describes how you can use ExpressVPN with Qubes to run all traffic through a VPN Proxy-VM.
More info about ExpressVPN can be found here:
https://www.expressvpn.com/what-is-vpn/browse-anonymously

This howto will cover:
- Creating a new vpn-template which is based on fedora-28-minimal (named: t-fedora-28-vpn)
- Create an Proxy-AppVM (named: sys-vpn)
- Configure ExpressVPN in the Proxy-AppVM

If you run into any problems with this Howto, do not hesitate to contact me.
The benefit of this setup is:
you can decide which AppVMs should run their traffic through ExpressVPN,
simple by setting their netvm to sys-vpn.

Install fedora-28-minimal template in dom0
```
sudo qubes-dom0-update qubes-template-fedora-28-minimal
```

Clone this template to a new template, which will be used for the VPN AppVM later
Hint: keep the original templates as baseline templates if you run into problems
```
qvm-clone fedora-28-minimal t-fedora-28-vpn
```

Updates packages in the new template and install additional packages
See also: https://www.qubes.org/doc/templates/fedora-minimal
          Section: Package Table for Qubes 4
```
qvm-run --auto --user root t-fedora-28-vpn "xterm -hold -e 'dnf -y update && \
  dnf -y install qubes-core-agent-qrexec qubes-core-agent-systemd qubes-core-agent-networking polkit \
  qubes-core-agent-network-manager notification-daemon qubes-core-agent-dom0-updates  \
  network-manager-applet nano iputils NetworkManager-openvpn NetworkManager-openvpn-gnome gnome-keyring && \
  echo ... Everything completed! Shutdown Template'"
qvm-shutdown t-fedora-28-vpn
```

Create a new AppVM from this template
```
qvm-create --template t-fedora-28-vpn --label orange sys-vpn
```

Set this VM as netvm
```
qvm-prefs --set sys-vpn provides_network True
```

Set sys-net as NetVM (sys-firewall will not work)
```
qvm-prefs --set sys-vpn netvm sys-net
```

Enable Network-Manager for this VM
Open Qubes Setting, Tab: Services
Add network-manager and hit [+], then [Apply]

Start AppVM as root user
```
qvm-run --user root sys-vpn xterm
```

Download the OpenVPN configuration file from ExpressVPN
- Launch a disposable VM or your preferred AppVM to browse the Web
- Login into ExpressVPN and download the OpenVPN configuration package
- Go to the Setup page and choose manual config
- https://www.expressvpn.com/setup#manual
- Download the OpenVPN configuration file for your preferred location
- Click Save File and then open the downloads directory
- Right Click the file and choose "Copy to Other AppVM..."
  copy the file to the AppVM (not the Template)

Configure ExpressVPN
- Import the OpenVPN config file via left click in the AppVM Network Manager Applet
- Choose "VPN Connections" > "Add a VPN Connection..."
- Then choose "Import a saved VPN configuration" and [Create]
- Import  the downloaded OpenVPN configuration file (QubesIncoming/...)
- Beautify the Name, like ExpressVPN-<Locationname>
- Copy & Paste the Username and Password from your ExpressVPN page into correct fields
  (User key password should also contain the password)
- Important: Click on the right Icon in the password field and choose:
- (X) Store the passwords for all users
- Save the dialog

Try to connect via ExpressVPN using the Network Manager applet
If it doesn't work try to reboot the AppVM
```
qvm-shutdown --wait sys-vpn && qvm-start sys-vpn
```
Enable autoconnection of VPN
- Right click on Network Manager Applet and choose "Edit Connections..."
- Choose "VM uplink eth0" and click on the settings icon
- On the "General Tab" enable "Automatically connect to VPN when using this connection"
- Then "Save"

Test autoconnection by disconnecting and reconnecting the VM uplink eth0
Hint: for some reason the autoconnection will be disabled when rebooting the AppVM
Therefore we apply a fix as described in the Qubes Docs
Link: https://www.qubes-os.org/doc/vpn/
```
qvm-run --user root sys-vpn "xterm -hold -e 'vi /rw/config/rc.local'
```

Hit i to switch to insert mode in the vi editor
Add the following 6 lines at the end of the file:
```
# Automatically connect to the VPN once Internet is up
# https://www.qubes-os.org/doc/vpn/
while ! ping -c 1 -W 1 1.1.1.1; do
   sleep 1
done
nmcli connection up ExpressVPN-<Location>
```

ExpressVPN-<Location> has to match the name of the OpenVPN connection.
In my case for example ExpressVPN-Frankfurt

To save the changes, hit Escape-Key and then :wq
(:wq = Write file, then quit)

In case that the VPN connection breaks you want to make sure that not data is leaked.
```
qvm-run --user root sys-vpn "xterm -hold -e 'vi /rw/config/qubes-firewall-user-script'
```

Add those 4 lines (i to enable insert-mode):
```
# Block forwarding of connections through upstream network device
# (in case the vpn tunnel breaks)
iptables -I FORWARD -o eth0 -j DROP
iptables -I FORWARD -i eth0 -j DROP
```
Save the file changes again (Escape, then :wq)

Reboot the AppVM and look if autoconnection is working
```
qvm-shutdown --wait sys-vpn && qvm-start sys-vpn
```

You can now use this AppVM as netvm for all Qubes which should run over the VPN connection:
```
qvm-prefs --set YOUROTHERAPPVM netvm sys-vpn
```

make sure that the VPN is working by running the DNS Leakage test:
https://www.expressvpn.com/de/dns-leak-test
