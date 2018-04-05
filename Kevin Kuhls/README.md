#WS47B - Yes, You C'Ansible


# BYOD Requirements

## Prereqs
This workshop will require several components:

* Infrastructure devices - You will receive credentials during the session to access your own dcloud infrastructure pod.
* A developer workstation with Ansible and git loaded. There are several options for this listed by preference:
  * Run our developer container locally using Docker, and your preferred text editor
  * Use the Ubuntu host in your dcloud pod. Access will require either VPN with AnyConnect or Openconnect (preferred) or via https Guacamole client
  * Run Ansible natively on your Linux or OSX workstation. Due to the workshop time constraints, we will most likely not be able to assist with any troubleshooting if you choose this option.

## Setup information


### Docker container:
This option is ideal for users using OSX, Linux, or Windows 10 with virtualization support. This typically excludes Home edition, laptops without virtualization support enabled, and Windows 8 and older.

* Install [Docker for Mac](https://docs.docker.com/engine/installation/mac/) or [Docker for Windows](https://docs.docker.com/engine/installation/windows/) or [Docker for Linux ](https://docs.docker.com/engine/installation/linux/ubuntu/)
* Install your preferred text editor. Popular options include PyCharm, Sublime, Atom, TextWrangler, vim, Notepad++

Once installed, we will walk you through downloading and running our developer container during the workshop.


### Ubuntu jumphost:
This option works best with a local VPN client, but can work without if needed.

* With VPN:
  * Install [Cisco AnyConnect](https://devnetsandbox.cisco.com/Docs/VPN_Access/AnyConnect_Installation_Guide.pdf) or OpenConnect
  * Install VNC client such as [RealVNC](https://www.realvnc.com/en/connect/download/viewer/)
* Without VPN:
  * Install a modern web browser


### Local Install:
This option will assume you have OSX or Linux, and have a solid knowledge of package management for your platform.

* Install Ansible 2.5
Install git
* Install [Cisco AnyConnect](https://devnetsandbox.cisco.com/Docs/VPN_Access/AnyConnect_Installation_Guide.pdf) or OpenConnect
* Install your preferred text editor. Popular options include PyCharm, Sublime, Atom, TextWrangler, vim

