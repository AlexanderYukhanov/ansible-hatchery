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
module: azure_rm_sqlserverazureadadministrator_facts
version_added: "2.5"
short_description: Get Server Azure A D Administrator facts.
description:
    - Get facts of Server Azure A D Administrator.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    administrator_name:
        description:
            - Name of the server administrator resource.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Server Azure A D Administrator
    azure_rm_sqlserverazureadadministrator_facts:
      resource_group: resource_group_name
      server_name: server_name
      administrator_name: administrator_name

  - name: List instances of Server Azure A D Administrator
    azure_rm_sqlserverazureadadministrator_facts:
      resource_group: resource_group_name
      server_name: server_name
'''

RETURN = '''
server_azure_ad_administrators:
    description: A list of dict results where the key is the name of the Server Azure A D Administrator and the values are the facts for that Server Azure A D Administrator.
    returned: always
    type: complex
    contains:
        serverazureadadministrator_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/sqlcrudtest-4799/providers/Microsoft.Sql/servers/sqlcrudtest-
                            6440/administrators/activeDirectory"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: activeDirectory
                login:
                    description:
                        - The server administrator login value.
                    returned: always
                    type: str
                    sample: bob@contoso.com
                sid:
                    description:
                        - The server administrator Sid (Secure ID).
                    returned: always
                    type: str
                    sample: c6b82b90-a647-49cb-8a62-0d2d3cb7ac7c
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


class AzureRMServerAzureADAdministratorsFacts(AzureRMModuleBase):
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
            administrator_name=dict(
                type='str'
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
        self.administrator_name = None
        super(AzureRMServerAzureADAdministratorsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.administrator_name is not None):
            self.results['server_azure_ad_administrators'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None):
            self.results['server_azure_ad_administrators'] = self.list_by_server()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Server Azure A D Administrator.

        :return: deserialized Server Azure A D Administratorinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.server_azure_ad_administrators.get(resource_group_name=self.resource_group,
                                                                           server_name=self.server_name,
                                                                           administrator_name=self.administrator_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ServerAzureADAdministrators.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_server(self):
        '''
        Gets facts of the specified Server Azure A D Administrator.

        :return: deserialized Server Azure A D Administratorinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.server_azure_ad_administrators.list_by_server(resource_group_name=self.resource_group,
                                                                                      server_name=self.server_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ServerAzureADAdministrators.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMServerAzureADAdministratorsFacts()
if __name__ == '__main__':
    main()
