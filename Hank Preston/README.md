# WS4A and WS10A - NetDevOps Developer Environments with Vagrant

## BYOD Requirements
This workshop introduces you to the Open Source tool Vagrant, and how it can be used for network programmability use cases.  

## Objectives

The objective of this workshop is to:

* Provide a quick introduction to vagrant
* Use vagrant to manage network programmability environments
* Combine Vagrant + Ansible for full environment preparation
* Explore how Vagrant fits into other possible NetDevOps Development Environments

## Prerequisites

In order to complete this lab you will need a development workstation with Vagrant and other tools installed.  

### Client Pre-Reqs

*   Python
  *   Python 2.7.10 or higher
  *   Python 3.6.3 or higher
  *   virtual environment (highly suggested but not required)
  *   pip
*   "git" command line tools
*   Vagrant
*   VirtualBox
*   Homebrew (Mac OS X)

## Workstation Setup Instructions

The labs in this module can be fully completed from an OS X or Linux workstation. Most of the labs can be completed from a Windows Workstation, however the lab combining Ansible and Vagrant cannot due to Ansible not currently being supported with Windows as a Control Server.  

If you are a Windows user, it is recommended that you run a Linux VM on your laptop to execute the labs against (though you'll need a hypervisor that supports nested virtualization and note that VirtualBox does **not**).  Otherwise you can observe/watch the lesson on Vagrant/Ansible and not run locally.  

To assist with completion, here are some suggested steps to prepare common platforms.

### CentOS Sample Setup Instructions Example

*   Standard Development Tools

    ```
    sudo yum -y groupinstall development
    ```

*   Python 3.6.2

    ```
    # CentOS 7
    yum install -y gcc zlib-devel openssl-devel wget
    cd /usr/src
    wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
    tar xzf Python-3.6.2.tgz
    cd Python-3.6.2
    ./configure
    make altinstall              
    ```

*   Python 2.7.14

    ```
    # CentOS 7
    yum install -y gcc zlib-devel openssl-devel wget
    cd /usr/src
    wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
    tar xzf Python-2.7.14.tgz
    cd Python-2.7.14
    ./configure
    make altinstall

    wget https://bootstrap.pypa.io/get-pip.py
    python2.7 get-pip.py
    ```


*   OpenSSL Development Library

    ```
    sudo yum -y install openssl-devel
    ```

*   Vagrant and VirtualBox

    ```
    # Add yum Repos
    wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
    mv virtualbox.repo /etc/yum.repos.d
    yum install -y epel-release

    # Download Installation Files
    wget https://releases.hashicorp.com/vagrant/1.9.8/vagrant_1.9.8_x86_64.rpm

    # Install Dependencies
    yum install -y kernel-devel gcc kernel-devel-3.10.0-693.2.2.el7.x86_64

    # Install applications
    yum install -y VirtualBox-5.1
    yum install -y vagrant_1.9.8_x86_64.rpm
    ```

### Mac OS X Installation

*   git installation - [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
*   Python 3.6 installation - [https://www.python.org/downloads/release/python-364/](https://www.python.org/downloads/release/python-364/)
*   Python 2.7 installation - [https://www.python.org/downloads/release/python-2714/](https://www.python.org/downloads/release/python-2714/)
*   Python pip installation

    ```
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
    sudo -H python get-pip.py
    ```


*   Command Line Developer Tools Installation. After running command, complete installation using the GUI.

    ```
    xcode-select --install          
    ```

*   [Vagrant Installation](https://www.vagrantup.com/downloads.html)
*   [VirtualBox Installation](https://www.virtualbox.org/wiki/Downloads)
*   [Homebrew Installation](https://brew.sh)

### Windows Installation

*   git installation - [https://git-scm.com/download/win](https://git-scm.com/download/win)
*   Python 3.6 installation - [https://www.python.org/downloads/release/python-364/](https://www.python.org/downloads/release/python-364/)  

*   Python 2.7 installation - [https://www.python.org/downloads/release/python-2714/](https://www.python.org/downloads/release/python-2714/)  
    **Be sure to check box for "Add Python to PATH" during the installer**
*   [Vagrant Installation](https://www.vagrantup.com/downloads.html)
*   [VirtualBox Installation](https://www.virtualbox.org/wiki/Downloads)
