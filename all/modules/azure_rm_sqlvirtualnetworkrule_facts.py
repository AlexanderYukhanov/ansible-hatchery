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
module: azure_rm_sqlvirtualnetworkrule_facts
version_added: "2.5"
short_description: Get Virtual Network Rule facts.
description:
    - Get facts of Virtual Network Rule.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    virtual_network_rule_name:
        description:
            - The name of the virtual network rule.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Virtual Network Rule
    azure_rm_sqlvirtualnetworkrule_facts:
      resource_group: resource_group_name
      server_name: server_name
      virtual_network_rule_name: virtual_network_rule_name

  - name: List instances of Virtual Network Rule
    azure_rm_sqlvirtualnetworkrule_facts:
      resource_group: resource_group_name
      server_name: server_name
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/vnet-test-svr/virtualNetworkRules/vnet-f
             irewall-rule"
name:
    description:
        - Resource name.
    returned: always
    type: str
    sample: vnet-firewall-rule
type:
    description:
        - Resource type.
    returned: always
    type: str
    sample: Microsoft.Sql/servers/virtualNetworkRules
state:
    description:
        - Virtual Network Rule State. Possible values include: C(Initializing), C(InProgress), C(Ready), C(Deleting), C(Unknown)
    returned: always
    type: str
    sample: Ready
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


class AzureRMVirtualNetworkRulesFacts(AzureRMModuleBase):
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
            virtual_network_rule_name=dict(
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
        self.virtual_network_rule_name = None
        super(AzureRMVirtualNetworkRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.virtual_network_rule_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None):
            self.results['ansible_facts']['list_by_server'] = self.list_by_server()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Virtual Network Rule.

        :return: deserialized Virtual Network Ruleinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.virtual_network_rules.get(resource_group_name=self.resource_group,
                                                                  server_name=self.server_name,
                                                                  virtual_network_rule_name=self.virtual_network_rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworkRules.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_by_server(self):
        '''
        Gets facts of the specified Virtual Network Rule.

        :return: deserialized Virtual Network Ruleinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.virtual_network_rules.list_by_server(resource_group_name=self.resource_group,
                                                                             server_name=self.server_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworkRules.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMVirtualNetworkRulesFacts()
if __name__ == '__main__':
    main()
