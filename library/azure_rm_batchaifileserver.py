#!/usr/bin/python
#
# Copyright (c) 2017 Zim Kalinowski, <zikalino@microsoft.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_batchaifileserver
version_added: "2.5"
short_description: Manage File Server instance.
description:
    - Create, update and delete instance of File Server.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    file_server_name:
        description:
            - "The name of the file server within the specified resource group. File server names can only contain a combination of alphanumeric characters
               along with dash (-) and underscore (_). The name must be from 1 through 64 characters long."
        required: True
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    vm_size:
        description:
            - For information about available VM sizes for fileservers from the Virtual Machines Marketplace, see Sizes for Virtual Machines (Linux).
        required: True
    ssh_configuration:
        description:
        required: True
        suboptions:
            public_ips_to_allow:
                description:
                    - "Default value is '*' can be used to match all source IPs. Maximum number of publicIPs that can be specified are 400."
                type: list
            user_account_settings:
                description:
                required: True
                suboptions:
                    admin_user_name:
                        description:
                        required: True
                    admin_user_ssh_public_key:
                        description:
                    admin_user_password:
                        description:
    data_disks:
        description:
        required: True
        suboptions:
            disk_size_in_gb:
                description:
                required: True
            disk_count:
                description:
                required: True
            storage_account_type:
                description:
                    - "Possible values include: 'C(standard_lrs)', 'C(premium_lrs)'"
                required: True
                choices:
                    - 'standard_lrs'
                    - 'premium_lrs'
    subnet:
        description:
        suboptions:
            id:
                description:
                    - The ID of the resource
                required: True
    state:
      description:
        - Assert the state of the File Server.
        - Use 'present' to create or update an File Server and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) File Server
    azure_rm_batchaifileserver:
      resource_group: demo_resource_group
      file_server_name: demo_nfs
      location: eastus
'''

RETURN = '''
id:
    description:
        - The ID of the resource
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batchai import BatchAIManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFileServers(AzureRMModuleBase):
    """Configuration class for an Azure RM File Server resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            file_server_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str'
            ),
            vm_size=dict(
                type='str',
                required=True
            ),
            ssh_configuration=dict(
                type='dict',
                required=True
            ),
            data_disks=dict(
                type='dict',
                required=True
            ),
            subnet=dict(
                type='dict'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.file_server_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFileServers, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                 supports_check_mode=True,
                                                 supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "vm_size":
                    self.parameters["vm_size"] = kwargs[key]
                elif key == "ssh_configuration":
                    self.parameters["ssh_configuration"] = kwargs[key]
                elif key == "data_disks":
                    ev = kwargs[key]
                    if 'storage_account_type' in ev:
                        if ev['storage_account_type'] == 'standard_lrs':
                            ev['storage_account_type'] = 'Standard_LRS'
                        elif ev['storage_account_type'] == 'premium_lrs':
                            ev['storage_account_type'] = 'Premium_LRS'
                    self.parameters["data_disks"] = ev
                elif key == "subnet":
                    self.parameters["subnet"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(BatchAIManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_fileserver()

        if not old_response:
            self.log("File Server instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("File Server instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if File Server instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the File Server instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_fileserver()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("File Server instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_fileserver()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_fileserver():
                time.sleep(20)
        else:
            self.log("File Server instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_fileserver(self):
        '''
        Creates or updates File Server with the specified configuration.

        :return: deserialized File Server instance state dictionary
        '''
        self.log("Creating / Updating the File Server instance {0}".format(self.file_server_name))

        try:
            response = self.mgmt_client.file_servers.create(resource_group_name=self.resource_group,
                                                                file_server_name=self.file_server_name,
                                                                parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the File Server instance.')
            self.fail("Error creating the File Server instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_fileserver(self):
        '''
        Deletes specified File Server instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the File Server instance {0}".format(self.file_server_name))
        try:
            response = self.mgmt_client.file_servers.delete(resource_group_name=self.resource_group,
                                                            file_server_name=self.file_server_name)
        except CloudError as e:
            self.log('Error attempting to delete the File Server instance.')
            self.fail("Error deleting the File Server instance: {0}".format(str(e)))

        return True

    def get_fileserver(self):
        '''
        Gets the properties of the specified File Server.

        :return: deserialized File Server instance state dictionary
        '''
        self.log("Checking if the File Server instance {0} is present".format(self.file_server_name))
        found = False
        try:
            response = self.mgmt_client.file_servers.get(resource_group_name=self.resource_group,
                                                         file_server_name=self.file_server_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("File Server instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the File Server instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMFileServers()

if __name__ == '__main__':
    main()
