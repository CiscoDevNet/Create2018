## WS15A and WS21B - Puppet's Secret Agent(less) Approach to Network Automation on IOS-XE
Tue April 10 - Workshop 4 - 3:00pm - 4:45pm  
Wed April 11 - Workshop 7 - 3:00pm - 4:30pm

### Objectives
The objectives of this workshop are:
* Provide brief introduction to Puppet Enterprise
* Demonstrate how Puppet uses declarative intent for configuration management
* How Puppet leverages industry standard YANG data models
* Deep dive into agentless Puppet
* Use Puppet Tasks for activities such as state validation and configuration rollback

### BYOD Requirements
This workshop leverages Cisco's [DevNet Sandbox](https://developer.cisco.com/site/sandbox/) environment.

The workshop environment will be provisioned for 8 participants per day.  Additional participants are welcome to join but will be required to reserve their own [Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/1b83c4bf-f63e-4e4b-9119-9b385751f1b6?diagramType=Topology) and perform [bootstrapping](#bootstrapping).

To participate please come prepared with:
* Computer with WiFi capability
* [Cisco AnyConnect](https://devnetsandbox.cisco.com/Docs/VPN_Access/AnyConnect_Installation_Guide.pdf) or OpenConnect VPN client installed
* SSH client
* [Modern web browser](https://puppet.com/docs/pe/2017.3/installing/supported_browsers.html)

___
## Workshop Instructions
The following are the step-by-step instructions for the workshop.  This is an instructor led workshop and instructor talking points are included in blockquotes.
>Instructor talking point

### Set up connection to DevNet Sandbox
Using AnyConnect information provided connect to the lab environment.  [Connection Guide](https://devnetsandbox.cisco.com/Docs/VPN_Access/AnyConnect_Connection_Guide.pdf)

### Login to Puppet Enterprise and CSR1000V
Puppet Enterprise Web Console
  * Address: **[https://10.10.20.20](https://10.10.20.20)**
  * Username: **admin**
  * Password: **puppet123**

Puppet Enterprise Shell (SSH)
  * IP: **10.10.20.20**
  * Username: **root**
  * Password: **cisco123**

CSR1000V CLI (SSH)
  * IP: **10.10.20.48**
  * Username: **cisco**
  * Password: **cisco_1234!**

### Puppet Enterprise Console
> Highlevel overview of information available in PE console

1. Open Puppet Enterprise Web Console
2. Navigate to `puppet` node and view Facts
3. View reports of `puppet` node

### Resources in Puppet
> Explain how Puppet abstracts configuration into declarative Resources  
> Benefits of common language for resources  
> Infrastructure as code

1. Open Puppet Enterprise shell
2. Use `puppet resource` to view _user_ and _service_ resources
  ```shell
  [root@puppet ~]# puppet resource user
  [root@puppet ~]# puppet resource service
  ```

> Overview about how we're converting YANG into Puppet resources

### Puppet Modules / Puppet Forge
> How Resources and Puppet code is packaged and distributed

1. Navigate to Puppet Forge: https://forge.puppet.com/
2. Search for `puppet device` module
3. Open [tkishel-puppet_device](https://forge.puppet.com/tkishel/puppet_device) module
> Review information available for module
4. Open Puppet Enterprise Shell
5. Install **tkishel-puppet_device** module
  ```shell
  [root@puppet ~]# puppet module install tkishel-puppet_device
  ```
6. View all installed modules
  ```shell
  [root@puppet ~]# puppet module list
  ```

### Puppet Manifests
> Modules and site.pp

1. Open Puppet Enterprise shell
2. Edit production environment `site.pp` to provision Puppet Device configuration
  ```shell
  [root@puppet ~]# vi /etc/puppetlabs/code/environments/production/manifests/site.pp
  ```
3. Add additional node configuration
> We will be using the tkishel-puppet_device module to generate the Puppet Device configuration

  ```Puppet
  node default {
    # This is where you can declare classes for all nodes.
    # Example:
    #   class { 'my_class': }
  }

  node 'puppet' {
    puppet_device {'csr1kv':
      type   => 'yang_ietf',
      url    => 'netconf://cisco:cisco_1234!@10.10.20.48',
    }
  }
  ```
4. Execute `puppet agent` to implement configuration
  ```shell
  [root@puppet ~]# puppet agent -tv
  ```
5. View generated configuration for Puppet Device
  ```shell
  [root@puppet ~]# cat /etc/puppetlabs/puppet/device.conf
  ```

### Puppet Device
> How Puppet Device works  
> Talk about certificates and autosigning

1. Open Puppet Enterprise shell
2. First run of `puppet device`
  ```shell
  [root@puppet ~]# puppet device -v -w 20
  ```
3. Open Puppet Enterprise Web Console
4. Navigate to `Setup/Unsigned certs`
  * _Use browser refresh if **csr1kv** cert request is not yet visible_
5. Click `Accept` for **csr1kv** certificate  
  ![sign_cert](images/sign_cert.png)
6. Return to Puppet Enterprise shell
7. Verify `puppet device` execution completes
  * _Will take up to 20 seconds to pick up signed cert from server_
> Talk about pluginsync
8. Open Puppet Enterprise Web Console
9. Navigate to **csr1kv** node via `Inspect/Overview` or `Inspect/Nodes`
10. Review `Facts` of node
11. Open Puppet Enterprise shell
12. Use `puppet device --resource` to query current state of **ietf_interfaces** on **csr1kv**
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces
  ```
> Examine how we are getting XML from NETCONF and converting to Puppet resource

### Managing Configuration with Puppet Device
1. Open Puppet Enterprise shell
2. Edit production environment `site.pp` to manage **Loopback10** on **csr1kv** device
  ```shell
  [root@puppet ~]# vi /etc/puppetlabs/code/environments/production/manifests/site.pp
  ```
  ```Puppet
  node default {
    # This is where you can declare classes for all nodes.
    # Example:
    #   class { 'my_class': }
  }

  node 'puppet' {
    puppet_device {'csr1kv':
      type   => 'yang_ietf',
      url    => 'netconf://cisco:cisco_1234!@10.10.20.48',
    }
  }

  node 'csr1kv' {
    ietf_interfaces { 'Loopback10':
      ensure    => 'present',
      interface => Yang_ietf::Interfaces::Interface({
      'name' => 'Loopback10',
      'description' => 'Managed by Puppet',
      'type' => 'ianaift:softwareLoopback',
      'enabled' => true,
      'ipv4' => Yang_ietf::Interfaces::Interface::Ipv4({
        'address' => [
          Yang_ietf::Interfaces::Interface::Ipv4::Address({
            'ip' => '1.1.1.1',
            'netmask' => '255.255.255.0'
          })
        ]
      })
      }),
    }
  }
  ```
3. Execute `puppet device -v` to create **Loopback10** on **csr1kv** device
  ```shell
  [root@puppet ~]# puppet device -v
  ```
  > Show how we are converting from Puppet to NETCONF XML
4. Open CSR1000v CLI
5. Verify **Loopback10**
  ```shell
  csr1000v#sh run interface Loopback10
  ```
6. Open Puppet Enterprise shell
7. Use `puppet device --resource` to query current state of **ietf_interfaces** on **csr1kv**
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces
  ```
8. Use `puppet device --resource` to look for specific interface on **csr1kv**
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback10
  ```
9. Use `puppet device --resource` to look for non-existent interface on **csr1kv**
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback20
  ```

### Classifying Nodes with Puppet Enterprise

1. Open Puppet Enterprise shell
2. View content of module
  ```shell
  [root@puppet ~]# cat /etc/puppetlabs/code/environments/production/modules/yang_ietf/manifests/demo.pp
  ```
  > Variables and code reuse
3. Open Puppet Enterprise Web Console
4. Navigate to `Configure/Classification`
5. Select `Add group`
6. Create new group named `demo`  
  ![class_group_demo](images/class_group_demo.png)
7. Select `Add membership rules` or the `demo` class itself  
  ![class_add_rules](images/class_add_rules.png)
8. Create rule to match `operatingsystem = IOS-XE` and select `Add rule`  
  ![class_rule_os](images/class_rule_os.png)
9. Select `Configuration` tab
10. Enter class `yang_ietf::demo` and select `Add class`
11. Review parameters in class - they should match what was viewed in demo.pp  
  ![class_params_list](images/class_params_list.png)
12. Ensure there are '2' changes to commit, and press `Commit 2 changes`  
  ![commit_2](images/commit_2.png)
13. Open Puppet Enterprise shell
14. Execute `puppet device -v` to create **Loopback20** on **csr1kv** device
  ```shell
  [root@puppet ~]# puppet device -v
  ```
  > Talk about how that demo class added Loopback20
15. Use `puppet device --resource` to confirm **Loopback20** on **csr1kv**
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback20
  ```

### Puppet Enterprise Reports and Node Graph
1. Open Puppet Enterprise Web Console
2. Navigate to `Inspect/Overview`
3. Note **intentional change** status of **csr1kv**
4. Select **Events** of **csr1kv** node  
  ![int_change_csr1kv](images/int_change_csr1kv.png)
5. Select `Intentional change` event of `Ietf_interfaces[Loopback20]`  
  ![event_int_change](images/event_int_change.png)
> Discuss how this information aids in troubleshooting
> Discuss how source control of Puppet Code enhances change management 
6. Return to `Inspect/Overview`
7. Select **Node graph** of **csr1kv** node  
  ![int_change_csr1kv](images/int_change_csr1kv.png)
8. Explore the node graph
> Call attention to how different sources of configuration are represented - site.pp and 'demo' class
9. Select `Ietf_interfaces[Loopback20]` resource and view details
  ![node_graph](images/node_graph.png)

### Idempotence

1. Open Puppet Enterprise shell
2. Execute `puppet device -v`
  ```shell
  [root@puppet ~]# puppet device -v
  ```
3. Note that no changes were made
> Discuss how Puppet ensures idempotent resources  
> Discuss how Puppet only manages the resources it is told to
4. Open Puppet Enterprise Web Console
5. Navigate to `Configure/Classification`
6. Select `demo` group
7. Navigate to `Configuration` tab
8. Select `description` parameter of **yang_ietf::demo** class
9. Modify value and click `Add parameter`
10. Commit the change
  ![modify_class](images/modify_class.png)  

11. Using what you have learned
  * Have Puppet enforce these changes on the device  
  * Verify the changes in various ways  
  
> Yes, there is some odd behaviour with corrective vs intentional change in this module  
> Any issues or any questions before we move on?

### Puppet Tasks
> An introduction to Puppet Tasks - Bolt vs PE

#### Console invocation
1. Open Puppet Enterprise Web Console
2. Navigate to `Run/Task`
3. Find `yang_ietf::enable_archive` task and expand `view task metadata`  
  ![task_metadata](images/task_metadata.png)
> Talk about parameters for Tasks
4. Set `target` task parameter of `yang_ietf::enable_archive` task to **csr1kv**
> Talk about Inventory for Tasks
5. Select Inventory `Node list`
6. Search for `puppet` node and select it  
  ![task_inventory](images/task_inventory.png)  
7. Once node is selected, press `Run job`  
  ![run_job_console](images/run_job_console.png)
8. Task should complete successfully
9. Repeat steps for `yang_ietf::show_archive` Task
10. Review task output shows archive location
  ```json
  {"archives":{},"location":"bootflash:archive","current":1,"status":"success"}
  ```

#### CLI invocation
1. Open Puppet Enterprise shell
2. Request CLI token with `puppet-access`  
  ```shell
  [root@puppet ~]# puppet-access login --lifetime 2h
  Enter your Puppet Enterprise credentials.
  Username: admin
  Password: puppet123
  ```
3. List installed Tasks via `puppet task show`  
  ```shell
  [root@puppet ~]# puppet task show
  ```
4. View details of `yang_ietf::yang_ietf::checkpoint` task  
  ```shell
  [root@puppet ~]# puppet task show yang_ietf::checkpoint
  ```
5. Archive running configuration with `yang_ietf::yang_ietf::checkpoint` task  
  ```shell
  [root@puppet ~]# puppet task run yang_ietf::checkpoint target=csr1kv --nodes puppet
  ```
  * Verify task runs successfully  
    ```
    {"status":"success"}

    Job completed. 1/1 nodes succeeded.
    ```

6. View configuration archive with `yang_ietf::yang_ietf::show_archive` task  
  ```shell
  [root@puppet ~]# puppet task run yang_ietf::show_archive target=csr1kv --nodes puppet
  ```
  * Verify task runs successfully  
    ```
    {"archives":{"1":"bootflash:archive-Apr--3-23-56-43.644-0"},"location":"bootflash:archive","current":1,"status":"success"}

    Job completed. 1/1 nodes succeeded.
    ```

### CI/CD Workflow
>This section ties everything together as a CI/CD Workflow.  If we don't get this far during the workshop it is okay.

>We will now simulate automated configuration deployment and validation.

1. Open Puppet Enterprise Web Console
2. Select `demo` group
3. Navigate to `Configuration` tab
4. Select `description` parameter of **yang_ietf::demo** class
5. Modify value to `demo` and click `Add parameter`
6. Commit the change
  ![modify_class_demo](images/modify_class_demo.png)  
7. Open Puppet Enterprise shell
8. Verify **Loopback20** description does **not** contain `demo`
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback20
  ```  
> In a CI/CD workflow configuration would be pushed automatically.  Prior to that configuration push we will archive the current running configuration.
9. Archive running configuration with `yang_ietf::yang_ietf::checkpoint` task  
  ```shell
  [root@puppet ~]# puppet task run yang_ietf::checkpoint target=csr1kv --nodes puppet
  ```
  * Verify task runs successfully  
    ```
    {"status":"success"}

    Job completed. 1/1 nodes succeeded.
    ```
10. Execute `puppet device -v` to modify **Loopback20** description
  ```shell
  [root@puppet ~]# puppet device -v
  ```  
11. Verify **Loopback20** description **does** contain `demo`
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback20
  ```  
> Now that the configuration has been updated we will simulate some automated testing.  For the demo we are only checking interface descriptions, but in the real world we would be more interested in state information such as routes.
12. Check for forbidden descriptions with `yang_ietf::yang_ietf::forbidden` task
  ```shell
  [root@puppet ~]# puppet task run yang_ietf::forbidden target=csr1kv forbidden=demo --nodes puppet
  ```
  * Task should fail on forbidden keyword  
      ```
      {"status":"failure","error":"Forbidden keyword 'demo' found in interface description on 'csr1kv'"}

      Job failed. 1 node failed, 0 nodes skipped, 0 nodes succeeded.
      ```
> Because "automated" testing failed we will rollback to archived configuration
13. Execute `yang_ietf::rollback` task  
  ```shell
  [root@puppet ~]# puppet task run yang_ietf::rollback target=csr1kv --nodes puppet
  ```
  * Verify task runs successfully  
      ```
      {"status":"success"}

      Job completed. 1/1 nodes succeeded.
      ```
14. Verify **Loopback20** description does **not** contain `demo`
  ```shell
  [root@puppet ~]# puppet device -v --target csr1kv --resource ietf_interfaces Loopback20
  ```  

___
### Bootstrapping
This information is **only** for additional participants (or those who would like to go through this workshop on their own time).

Sandbox reservation requires 10 mins to complete; bootstrapping requires 15-25 minutes to complete (depending on labs bandwidth).

1. Reserve [IOS XE Programmability with NETCONF Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/1b83c4bf-f63e-4e4b-9119-9b385751f1b6?diagramType=Topology)
2. Connect to Sandbox via AnyConnect per provided e-mail instructions
3. SSH to sandbox CentOS server
    * IP: **10.10.20.20** (After VPN connection)
    * Username: **root**
    * Password: **cisco123**
4. Deactivate existing python environment
```bash
(python2) [root@localhost sbx_iosxe]# deactivate
```
5. Download and execute bootstrap script  
_**Note**: the use `nohup` ensures bootstrapping completes even if SSH connection is interrupted_
```bash
[root@localhost sbx_iosxe]# cd ~
[root@localhost ~]# git clone https://github.com/shermdog/devnet_create_2018_bootstrap.git
[root@localhost ~]# cd devnet_create_2018_bootstrap/
[root@localhost devnet_create_2018_bootstrap]# nohup ./bootstrap.sh &
```
6. Monitor / Confirm bootstrapping completes
```bash
[root@localhost devnet_create_2018_bootstrap]# tail -f nohup.out
Setting hostname...
Downloading Puppet Enterprise...
<snip>
Bootstrapping complete.
```