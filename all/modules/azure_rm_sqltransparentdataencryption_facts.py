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
module: azure_rm_sqltransparentdataencryption_facts
version_added: "2.5"
short_description: Get Transparent Data Encryption facts.
description:
    - Get facts of Transparent Data Encryption.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    database_name:
        description:
            - The name of the database for which the transparent data encryption applies.
        required: True
    transparent_data_encryption_name:
        description:
            - The name of the transparent data encryption configuration.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Transparent Data Encryption
    azure_rm_sqltransparentdataencryption_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      transparent_data_encryption_name: transparent_data_encryption_name
'''

RETURN = '''
transparent_data_encryptions:
    description: A list of dict results where the key is the name of the Transparent Data Encryption and the values are the facts for that Transparent Data Encryption.
    returned: always
    type: complex
    contains:
        transparentdataencryption_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/sqlcrudtest-6852/providers/Microsoft.Sql/servers/sqlcrudtest-
                            2080/databases/sqlcrudtest-9187/transparentDataEncryption/current"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: current
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Sql/servers/databases/transparentDataEncryption
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: North Europe
                status:
                    description:
                        - "The status of the database transparent data encryption. Possible values include: C(Enabled), C(Disabled)"
                    returned: always
                    type: str
                    sample: Enabled
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTransparentDataEncryptionsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            transparent_data_encryption_name=dict(
                type='str',
                required=True
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.server_name = None
        self.database_name = None
        self.transparent_data_encryption_name = None
        super(AzureRMTransparentDataEncryptionsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.transparent_data_encryption_name is not None):
            self.results['transparent_data_encryptions'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Transparent Data Encryption.

        :return: deserialized Transparent Data Encryptioninstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.transparent_data_encryptions.get(resource_group_name=self.resource_group,
                                                                         server_name=self.server_name,
                                                                         database_name=self.database_name,
                                                                         transparent_data_encryption_name=self.transparent_data_encryption_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for TransparentDataEncryptions.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMTransparentDataEncryptionsFacts()
if __name__ == '__main__':
    main()
