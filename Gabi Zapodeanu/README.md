# WS17A -  NetDevOps Engineer Everyday Skills 

### BYOD Requirements

This worskhop will require you to bring a laptop with Python 2.7 and 3.x installed. You will need the requests and ncclient Python libraries. 

During the workshop you will need these accounts:
 - DevNet account
 - CiscoSpark account
 - Developer Service Now account (optional)

### Skills

The application will require familiarity with:
 - Cisco CLI
 - Embedded Event Manager
 - IOS XE Guest Shell
 - YANG and NETCONF/RESTCONF
 - basic Linux and a text editor skills
 - basic knowledge of git operations

### Lab Equipment

You will be provided a sandbox that will include a CSR1000V router that you will use to create a ChaOps application.
You will access this DevNet Sandbox using the Cisco AnyConnect VPN Client.

### Lab Overview

The application that will be created will detect any router configuration changes, the hostname of the device, the user that made the configurations and will create an approval request in Spark. 
If the changes will be approved, they will become the new baseline configuration. 
If the changes will not be approved, or no response received to the approval request, the router configuration will be restored to the previous baseline configuration.

The router will also create a ServiceNow incident to record the changes and the response to the requested approval.
