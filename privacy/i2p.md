Using I2P (Invisible Internet Project) with Qubes
=================================================

"The I2P network provides strong privacy protections for communication over the Internet. Many activities that would risk your privacy on the public Internet can be conducted anonymously inside I2P." - [I2P Website](https://geti2p.net/)


Preparation - Basic
===============

The I2P Software will be installed on a Linux-based TemplateVM. Here we are using Debian 9, but this also works on the old Debian 8 Template. So at first you need to install Debian 9 as a TemplateVM. If you want, you can create a dedicated clone of the default Debian-9 TemplateVM. In this case, inside the Dom0 Terminal, run the command:
~~~
qvm-clone debian-9 debian-9-i2p
~~~


Installation
============
	
1. Next, you need to add the I2P repository and the apt key to the new template. Therefore you need Internet access for your Template. Provided that you have an active Internet connection, start your new TemplateVM, open the Configuration and enable networking (this is neccessary for downloading the apt key for I2P). Now run the following commands (as root):
	~~~
	echo 'deb https://deb.i2p2.de/ stretch main' > /etc/apt/sources.list.d/i2p.list
	echo 'deb-src https://deb.i2p2.de/ stretch main' >> /etc/apt/sources.list.d/i2p.list
	wget https://geti2p.net/_static/i2p-debian-repo.key.asc
	apt-key add i2p-debian-repo.key.asc
	rm -rf i2p-debian-repo.key.asc
	~~~
	
	If you are using Debian 8, replace 'stretch' with 'jessie' in the commands above. Now that you downloaded the Repository key, you can disable networking again.

2. Then, update your package manager, install and configure the i2p packages:
	~~~
	sudo apt update
	sudo apt install i2p i2p-keyring
	sudo dpkg-reconfigure i2p
	~~~
	
3. You also need to change the owner of the i2p configuration directory:
	~~~
	chown -R i2psvc:i2psvc /usr/share/i2p/
	~~~

4. Shutdown your TemplateVM and create an AppVM which uses your Template "debian-9-i2p" (or "debian-9" if you did not create a clone). Connect your AppVM to "sys-firewall".

5. Start your newly created AppVM, open a terminal and run the following commands:

	~~~
	mkdir -p /rw/config/qubes-bind-dirs.d/
	mkdir -p /mail
	echo "binds+=( '/usr/share/i2p' )" > /rw/config/qubes-bind-dirs.d/50_user.conf
	echo "binds+=( '/mail' )" >> /rw/config/qubes-bind-dirs.d/50_user.conf
	echo "binds+=( '/var/lib/i2p' )" >> /rw/config/qubes-bind-dirs.d/50_user.conf
	~~~

6. Reboot your AppVM

7. In your AppVM, open the Firefox Web Browser and go to Preferences -> Advanced -> Network Settings. Now select "Manual Proxy Configuration" and configure the Proxy Settings: HTTP: 127.0.0.1 port 4444 - HTTPS: 127.0.0.1 port 4445 - No Proxy: localhost, 127.0.0.1

You can now start browsing and using the I2P Network. Access the I2P Router Console by typing:
~~~
http://localhost:7657
~~~

For more information about I2P, please visit the [I2P Website](https://geti2p.net/).
