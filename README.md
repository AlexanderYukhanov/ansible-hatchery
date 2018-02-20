# POC. Using ansible for common BatchAI scenarios 

An example:

``` yaml
- hosts: localhost
  vars:
     location: eastus
     resource_group: ansible
     storage:
       account: "st{{ lookup('password', '/dev/null chars=ascii_lowercase,digits') }}" # unique name
       container: trainingdata
       share: output
     nfs:
       name: nfs
       size: Standard_DS14
       disk_count: 4
       disk_size: 512
       sku: "Standard_LRS"
     cluster:
       name: cluster
       size: Standard_NC6
       nodes: 4
     admin:
       username: "{{ lookup('env','HOME') }}"
       ssh_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
  roles:
    - { role: AlexanderYukhanov.ansible-hatchery }
  tasks:

  - name: Create resource group '{{ resource_group }}'
    azure_rm_resourcegroup:
      location: "{{ location }}"
      name: "{{ resource_group }}"

  - name: Create storage account '{{ storage.account }}'
    azure_rm_storageaccount:
      resource_group: "{{ resource_group }}"
      name: "{{ storage.account }}"
      account_type: Standard_LRS

  - name: Create Azure Storage Container '{{ storage.container }}' under '{{ storage.account }}'
    azure_rm_storageblob:
      resource_group: "{{ resource_group }}"
      storage_account_name: "{{ storage.account }}"
      container: "{{ storage.container }}"

  - name: Create Azure File Share '{{ storage.share }}' under '{{ storage.account }}'
    azure_rm_storageshare:
      resource_group: "{{ resource_group }}"
      storage_account_name: "{{ storage.account }}"
      share: "{{ storage.share }}"

  - name: Create Batch AI managed NFS '{{ nfs.name }}'
    azure_rm_batchaifileserver:
      location: "{{ location }}"
      resource_group: "{{ resource_group }}"
      file_server_name: "{{ nfs.name }}"
      vm_size: "{{ nfs.size }}"
      data_disks:
        disk_size_in_gb: "{{ nfs.disk_size }}"
        disk_count: "{{ nfs.disk_count }}"
        storage_account_type: "{{ nfs.sku }}"
      ssh_configuration:
        user_account_settings:
          admin_user_name: "{{ admin.username }}"
          admin_user_ssh_public_key: "{{ admin.ssh_key }}"
          public_ips_to_allow:
            - "71.231.193.111"
    register: created_nfs

  - name: Create BatchAI cluster '{{ cluster.name }}'
    azure_rm_batchaicluster:
      resource_group: "{{ resource_group }}"
      cluster_name: "{{ cluster.name }}"
      location: "{{ location }}"
      vm_size: "{{ cluster.size }}"
      scale_settings:
        manual:
          target_node_count: "{{ cluster.nodes }}"
      user_account_settings:
        admin_user_name: "{{ admin.username }}"
        admin_user_ssh_public_key: "{{ admin.ssh_key }}"
      node_setup:
        mount_volumes:
          azure_file_shares:
            - account_name: "{{ storage.account }}"
              azure_file_url: "https://{{ storage.account }}.file.core.windows.net/{{ storage.share }}"
              relative_mount_path: "afs"
          azure_blob_file_systems:
            - account_name: "{{ storage.account }}"
              container_name: "{{ storage.container }}"
              relative_mount_path: "bfs"
          file_servers:
            - file_server:
                id: "{{ created_nfs.id }}"
              relative_mount_path: "nfs"
          unmanaged_file_systems:
            - relative_mount_path: "tmpfs"
              mount_command: "mount -t tmpfs -o size=10G,nr_inodes=10k,mode=700 tmpfs"
```
