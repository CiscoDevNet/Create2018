# WS19 & WS51 - Cisco Spark as the Communications Hub and Digital Project Manager
Session times:
Tuesday 4/10/2018 3:00pm-4:30pm @ Workshop 5 - WS19
Wednesday 4/11/2018 10:15am-11:45am @ Workshop 7 - WS51

## Objectives
The objective of this workshop is to:

* Acquire digital data about a real world process occuring in network infrastructure
* Interpret the data in the context of a migration event occuring in a timed window
* Create relevant progress metrics and display them in a visually appealing way
* Leverage the Cisco Spark API and application to share the progress with a team

## BYOD Requirements
### Bring a 20ft Ethernet cable and an Ethernet dongle if your laptop requires one
During the workshop you will be interacting with a pair of switches. Without an ability to attach to the switches... well, let's just say you won't get much value from the workshop!

---

### Sign Up for a Cisco Spark Account
Cisco Spark is a cloud-based team messaging, meeting and calling client. You can sign up for a basic/free account if you don't have one already from http://www.ciscospark.com. Once you have an account you can also familiarize yourself with the Spark API found at http://developer.ciscospark.com.

---
### Install Cisco Spark Client
Cisco Spark can be consumed from the www.ciscospark.com webpage, but the experience is best had on the Windows or Mac clients. You can and should also install Spark on iOS and Android mobile devices!

---

### git, Python3, and pip Installation
You will need git to obtain the code we'll be editing, and the workshop will leverage git branches to ensure everyone is able to have running code at each step along the way. The code we will be running was written in Python3, so you'll need that installed. pip is a package manager which will allow you to install the dependencies upon which our application is built. The major components we're leveraging are pysnmp, requests, Flask and SQLalchemy. Those will be installed during a later step.

**Mac OS X Installation

* Mac Command Line Developer Tools Installation. After running command, complete installation using the GUI.

  `xcode-select --install`          

* git installation - https://git-scm.com/download/mac

* Python 3.6.5 installation - https://www.python.org/downloads/release/python-365/

* Python pip installation

  `curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py`
  
  `sudo -H python get-pip.py`

**Windows Installation

* git installation - https://git-scm.com/download/win

* Python 3.6.5 installation - https://www.python.org/downloads/release/python-365/

* Python pip installation - https://pip.pypa.io/en/stable/installing/

---

### Configure your system to connect to GitHub with SSH keys
* https://help.github.com/articles/connecting-to-github-with-ssh/

---

### Install PyCharm Community Edition (free Python IDE)
https://www.jetbrains.com/pycharm/download/

---

### Clone the repo
`git clone git@github.com:paulgiblin/digital-project-manager.git`

---

### Open code as a project in PyCharm CE and configure VENV

* File -> Open -> select the directory -> click Open

  This will open the project in PyCharm, if you did it correctly, the top level directory should have run.py in it.
  
* Open Preferences -> "Project:digital-project-manager" -> Project Interpreter -> click on the gear icon -> choose "Add local..."

* Make sure new Virtualenv Environment is selected, and it points to your Python 3.6 instance for the base interpreter

  Virtualenv is installed as part of PyCharm, but can also be run independently. Virtualenv copies the interpreter to a local directory, and any packages installed are also copied. This gives us a clean environment to work with, independent of any global configuration your operating system may have.
  
* Click "Install Packaging tools" if prompted

* Open run.py -> banner at the head should prompt to install requirements, install them

* Click the Run/Debug Configuration drop down (next to the play icon) and select edit configurations

* Click +, then Python

* Enter python3.6-dpm for the name and configure the Script Path field to point to run.py in the root directory of the project

* Click play, Flask should indicate the application is running
