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
module: azure_rm_sqlserverconnectionpolicy_facts
version_added: "2.5"
short_description: Get Server Connection Policy facts.
description:
    - Get facts of Server Connection Policy.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    connection_policy_name:
        description:
            - The name of the connection policy.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Server Connection Policy
    azure_rm_sqlserverconnectionpolicy_facts:
      resource_group: resource_group_name
      server_name: server_name
      connection_policy_name: connection_policy_name
'''

RETURN = '''
server_connection_policies:
    description: A list of dict results where the key is the name of the Server Connection Policy and the values are the facts for that Server Connection Policy.
    returned: always
    type: complex
    contains:
        serverconnectionpolicy_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/test-1234/providers/Microsoft.Sql/servers/test-5678/connectio
                            nPolicies/default"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: default
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Sql/servers/connectionPolicies
                kind:
                    description:
                        - Metadata used for the Azure portal experience.
                    returned: always
                    type: str
                    sample: kind
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: West US
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


class AzureRMServerConnectionPoliciesFacts(AzureRMModuleBase):
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
            connection_policy_name=dict(
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
        self.connection_policy_name = None
        super(AzureRMServerConnectionPoliciesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.connection_policy_name is not None):
            self.results['server_connection_policies'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Server Connection Policy.

        :return: deserialized Server Connection Policyinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.server_connection_policies.get(resource_group_name=self.resource_group,
                                                                       server_name=self.server_name,
                                                                       connection_policy_name=self.connection_policy_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ServerConnectionPolicies.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMServerConnectionPoliciesFacts()
if __name__ == '__main__':
    main()
