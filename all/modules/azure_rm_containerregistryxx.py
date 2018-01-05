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
module: azure_rm_containerregistryxx
version_added: "2.5"
short_description: Manage Registries instance.
description:
    - Create, update and delete instance of Registries.

options:
    resource_group:
        description:
            - The name of the resource group to which the container registry belongs.
        required: True
    registry_name:
        description:
            - The name of the container registry.
        required: True
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    sku:
        description:
            - The SKU of the container registry.
        required: True
        suboptions:
            name:
                description:
                    - The SKU name of the container registry. Required for registry creation.
                required: True
                choices: ['classic', 'basic', 'standard', 'premium']
    admin_user_enabled:
        description:
            - The value that indicates whether the admin user is enabled.
    storage_account:
        description:
            - The properties of the storage account for the container registry. Only applicable to Classic SKU.
        suboptions:
            id:
                description:
                    - The resource ID of the storage account.
                required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Registries
    azure_rm_containerregistryxx:
      resource_group: myResourceGroup
      registry_name: myRegistry
      location: eastus
      sku:
        name: Standard
'''

RETURN = '''
id:
    description:
        - The resource ID.
    returned: always
    type: str
    sample: id
status:
    description:
        - The status of the container registry at the time the operation was called.
    returned: always
    type: complex
    sample: status
    suboptions:
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.containerregistry import ContainerRegistryManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRegistries(AzureRMModuleBase):
    """Configuration class for an Azure RM Registries resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str'
            ),
            sku=dict(
                type='dict',
                required=True
            ),
            admin_user_enabled=dict(
                type='str'
            ),
            storage_account=dict(
                type='dict'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.registry_name = None
        self.registry = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRegistries, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                supports_check_mode=True,
                                                supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "location":
                    self.registry["location"] = kwargs[key]
                elif key == "sku":
                    ev = kwargs[key]
                    if 'name' in ev:
                        if ev['name'] == 'classic':
                            ev['name'] = 'Classic'
                        elif ev['name'] == 'basic':
                            ev['name'] = 'Basic'
                        elif ev['name'] == 'standard':
                            ev['name'] = 'Standard'
                        elif ev['name'] == 'premium':
                            ev['name'] = 'Premium'
                    self.registry["sku"] = ev
                elif key == "admin_user_enabled":
                    self.registry["admin_user_enabled"] = kwargs[key]
                elif key == "storage_account":
                    self.registry["storage_account"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_registries()

        if not old_response:
            self.log("Registries instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Registries instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Registries instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Registries instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_registries()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Registries instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_registries()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_registries():
                time.sleep(20)
        else:
            self.log("Registries instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["status"] = response["status"]

        return self.results

    def create_update_registries(self):
        '''
        Creates or updates Registries with the specified configuration.

        :return: deserialized Registries instance state dictionary
        '''
        self.log("Creating / Updating the Registries instance {0}".format(self.registry_name))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.registries.create(resource_group_name=self.resource_group,
                                                              registry_name=self.registry_name,
                                                              registry=self.registry)
            else:
                response = self.mgmt_client.registries.update(resource_group_name=self.resource_group,
                                                              registry_name=self.registry_name,
                                                              registry_update_parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Registries instance.')
            self.fail("Error creating the Registries instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_registries(self):
        '''
        Deletes specified Registries instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Registries instance {0}".format(self.registry_name))
        try:
            response = self.mgmt_client.registries.delete(resource_group_name=self.resource_group,
                                                          registry_name=self.registry_name)
        except CloudError as e:
            self.log('Error attempting to delete the Registries instance.')
            self.fail("Error deleting the Registries instance: {0}".format(str(e)))

        return True

    def get_registries(self):
        '''
        Gets the properties of the specified Registries.

        :return: deserialized Registries instance state dictionary
        '''
        self.log("Checking if the Registries instance {0} is present".format(self.registry_name))
        found = False
        try:
            response = self.mgmt_client.registries.get(resource_group_name=self.resource_group,
                                                       registry_name=self.registry_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Registries instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Registries instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMRegistries()

if __name__ == '__main__':
    main()
