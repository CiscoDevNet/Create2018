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



