#  WS24 Intro to Napalm Devnet Create 2018



## BYOD Requirements
This workshop introduces you to the network automation python module Naplam, and how it can be used for network automation.  

## Objectives

This workshops gets you up-and-running with NAPALM in a Devnet Sandbox environment so you can see it in action in under an hour. We’ll cover the following:

* What is Napalm
* Installing the required tools
* Napalm Command Line Tool
* Manually applying configuration to the device using NAPALM
* Driving NAPALM through Python code


## Prerequisites (Not recomended, full sandbox lab is provided for the entire workshop)

In order to complete this lab you will need a workstation with Python, Napalm and other tools installed.  

### Client Pre-Reqs

* Python
  * Python 2.7.10 or higher
  * Python 3.6.3 or higher
  * virtual environment (highly suggested but not required)
  * pip
* "git" command line tools
* Homebrew (Mac OS X)
* Native ssh or ssh client


## Workstation Setup Instructions

The labs in this module can be fully completed from an OS X or Linux workstation.

If you are a Windows user, it is recommended that you run a Linux VM on your laptop to execute the labs against. Otherwise you can observe/watch the lesson or connect to the sandbox as advised above.

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

# SSH Access

For this lab an ssh client is require to connect to the devbox. Using Mac/Linux directly use the OS native SSH client. For connecting using an SSH client such as PuTTY.

```
ssh root@10.10.20.20 / password cisco123

```
Putty Dowload link 
```
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html 

```


# Create a new directory

```
mkdir napalm
```

# Clone the Repo

```
git clone https://github.com/bigevilbeard/napalm_create.git
```

# Installing Napalm

When installing Napalm installed the latest version 2.X as there were fundamental changes that happened between Naplm 1.X and 2.X.
You can install napalm with pip:

```
pip install -r requirements.txt
```



