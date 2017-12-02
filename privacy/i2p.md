Using I2P (Invisible Internet Project) with Qubes
=================================================

"The I2P network provides strong privacy protections for communication over the Internet. Many activities that would risk your privacy on the public Internet can be conducted anonymously inside I2P." - [I2P Website](https://geti2p.net/)


Preparation - Basic
===============

The I2P Software will be running on a Linux-based TemplateVM. Here we are using Debian 9, but you could also use the default Debian 8 Template. So at first you need to install Debian 9 as a TemplateVM. If you want, you can create a dedicated clone of the default Debian-9 TemplateVM. In the Dom0 Terminal, run the command:
~~~
qvm-clone debian-9 debian-9-i2p
~~~


Installation
============
	
1. Next, you need to add the I2P repository and the apt key to the new template. Therefore, you need Internet access in your Template. Start your new TemplateVM, open the firewall configuration and allow full access for 5 minutes (this is neccessary for downloading the apt key for I2P. Now run the following commands (as root):
	~~~
	echo 'deb https://deb.i2p2.de/ stretch main' > /etc/apt/sources.list.d/i2p.list
	echo 'deb-src https://deb.i2p2.de/ stretch main' >> /etc/apt/sources.list.d/i2p.list
	wget https://geti2p.net/_static/i2p-debian-repo.key.asc
	apt-key add i2p-debian-repo.key.asc
	rm -rf i2p-debian-repo.key.asc
	~~~
	
	If you are using Debian 8, replace 'stretch' with 'jessie' in the commands above.

2. Then, update your systems package manager and install the i2p packages:
	~~~
	sudo apt update
	sudo apt install i2p i2p-keyring
	~~~
	
3. From your TemplateVM, you need to make the default i2p configuration directory persistent. This will allow I2P to save its configuration files from the AppVM which will be created later. Without this step, the I2P configuration would be lost when shutting down your AppVM. Now run these commands:
	~~~
	sudo su
	mkdir -p /rw/config/qubes-bind-dirs.d
	echo "binds+=( '/usr/share/i2p' )" > /rw/config/qubes-bind-dirs.d/50_user.conf
	~~~
	
4. Then you need to change the owner of the i2p configuration directory:
	~~~
	chown -R i2psvc:i2psvc /usr/share/i2p/
	~~~

5. Normally, I2P would automatically run from the "i2psvc" user. We need to change that. To do so, run
	~~~
	dpkg-reconfigure i2p
	~~~
	and disable the autorun function. Do not change the other options unless you know exactly what you are doing. Next you 		need to configure a custom autostart option. Run:
	~~~
	nano /etc/rc.local
	~~~
	Insert the following command right before the line which says "exit 0". This will automatically run I2P as "user".
	~~~
	sudo -u user i2prouter start
	~~~

6. In case you want to use the I2P email function, type in the commands below. Otherwise I2P won't be able to save your emails.
	~~~
	mkdir -p /mail
	chown -R i2psvc:i2psvc /mail
	echo "binds+=( '/mail' )" >> /rw/config/qubes-bind-dirs.d/50_user.conf
	~~~

7. Shutdown your TemplateVM and create an AppVM which uses your Template "debian-9-i2p" (or "debian-9" if you did not create a clone). Connect your AppVM to "sys-firewall".

8. Start the AppVM you created. Open Firefox Web Browser and go to Preferences -> Advanced -> Network Settings. Now select "Manual Proxy Configuration" and configure the Proxy Settings: HTTP: 127.0.0.1 port 4444 - HTTPS: 127.0.0.1: port 4445 - No Proxy: localhost, 127.0.0.1

Finally, reboot your AppVM and start browsing the I2P Network. You can reach the I2P Router Console by going to
~~~
localhost:7657
~~~

For more information about I2P, please visit the [I2P Website](https://geti2p.net/).
