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
module: azure_rm_vault
version_added: "2.5"
short_description: Manage Vault instance.
description:
    - Create, update and delete instance of Vault.

options:
    resource_group:
        description:
            - The name of the Resource Group to which the server belongs.
        required: True
    vault_name:
        description:
            - Name of the vault
        required: True
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    properties:
        description:
            - Properties of the vault
        required: True
        suboptions:
            tenant_id:
                description:
                    - The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
                required: True
            sku:
                description:
                    - SKU details
                required: True
                suboptions:
                    family:
                        description:
                            - SKU family name
                        required: True
                    name:
                        description:
                            - SKU name to specify whether the key vault is a standard vault or a premium vault.
                        required: True
                        choices: ['standard', 'premium']
            access_policies:
                description:
                    - "An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key v
                       ault's tenant ID."
                type: list
                suboptions:
                    tenant_id:
                        description:
                            - The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
                        required: True
                    object_id:
                        description:
                            - "The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID
                                must be unique for the list of access policies."
                        required: True
                    application_id:
                        description:
                            -  Application ID of the client making request on behalf of a principal
                    permissions:
                        description:
                            - Permissions the identity has for keys, secrets and certificates.
                        required: True
                        suboptions:
                            keys:
                                description:
                                    - Permissions to keys
                                type: list
                            secrets:
                                description:
                                    - Permissions to secrets
                                type: list
                            certificates:
                                description:
                                    - Permissions to certificates
                                type: list
                            storage:
                                description:
                                    - Permissions to storage accounts
                                type: list
            vault_uri:
                description:
                    - The URI of the vault for performing operations on keys and secrets.
            enabled_for_deployment:
                description:
                    - Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
            enabled_for_disk_encryption:
                description:
                    - Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
            enabled_for_template_deployment:
                description:
                    - Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
            enable_soft_delete:
                description:
                    - Property to specify whether the C(soft delete) functionality is enabled for this key vault. It does not accept false value.
            create_mode:
                description:
                    - "The vault's create mode to indicate whether the vault need to be recovered or not."
                choices: ['recover', 'default']

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Vault
    azure_rm_vault:
      resource_group: NOT FOUND
      vault_name: NOT FOUND
      location: eastus
'''

RETURN = '''
id:
    description:
        - The Azure Resource Manager resource ID for the key vault.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.keyvault import KeyVaultManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVaults(AzureRMModuleBase):
    """Configuration class for an Azure RM Vault resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vault_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str'
            ),
            properties=dict(
                type='dict',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.vault_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVaults, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "properties":
                    self.parameters["properties"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(KeyVaultManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_vault()

        if not old_response:
            self.log("Vault instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Vault instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Vault instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Vault instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_vault()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Vault instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_vault()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_vault():
                time.sleep(20)
        else:
            self.log("Vault instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_vault(self):
        '''
        Creates or updates Vault with the specified configuration.

        :return: deserialized Vault instance state dictionary
        '''
        self.log("Creating / Updating the Vault instance {0}".format(self.vault_name))

        try:
            response = self.mgmt_client.vaults.create_or_update(resource_group_name=self.resource_group,
                                                                vault_name=self.vault_name,
                                                                parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Vault instance.')
            self.fail("Error creating the Vault instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_vault(self):
        '''
        Deletes specified Vault instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Vault instance {0}".format(self.vault_name))
        try:
            response = self.mgmt_client.vaults.delete(resource_group_name=self.resource_group,
                                                      vault_name=self.vault_name)
        except CloudError as e:
            self.log('Error attempting to delete the Vault instance.')
            self.fail("Error deleting the Vault instance: {0}".format(str(e)))

        return True

    def get_vault(self):
        '''
        Gets the properties of the specified Vault.

        :return: deserialized Vault instance state dictionary
        '''
        self.log("Checking if the Vault instance {0} is present".format(self.vault_name))
        found = False
        try:
            response = self.mgmt_client.vaults.get(resource_group_name=self.resource_group,
                                                   vault_name=self.vault_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Vault instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Vault instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMVaults()

if __name__ == '__main__':
    main()