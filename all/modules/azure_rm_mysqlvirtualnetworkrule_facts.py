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
module: azure_rm_mysqlvirtualnetworkrule_facts
version_added: "2.5"
short_description: Get MySQL Virtual Network Rule facts.
description:
    - Get facts of MySQL Virtual Network Rule.

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
  - name: Get instance of MySQL Virtual Network Rule
    azure_rm_mysqlvirtualnetworkrule_facts:
      resource_group: resource_group_name
      server_name: server_name
      virtual_network_rule_name: virtual_network_rule_name

  - name: List instances of MySQL Virtual Network Rule
    azure_rm_mysqlvirtualnetworkrule_facts:
      resource_group: resource_group_name
      server_name: server_name
'''

RETURN = '''
virtual_network_rules:
    description: A list of dict results where the key is the name of the MySQL Virtual Network Rule and the values are the facts for that MySQL Virtual Network Rule.
    returned: always
    type: complex
    contains:
        mysqlvirtualnetworkrule_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID
                    returned: always
                    type: str
                    sample: "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/TestGroup/providers/Microsoft.DBforMySQL/servers/vnet-test-sv
                            r/virtualNetworkRules/vnet-firewall-rule"
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
                    sample: Microsoft.DBforMySQL/servers/virtualNetworkRules
                state:
                    description:
                        - "Virtual Network Rule State. Possible values include: C(Initializing), C(InProgress), C(Ready), C(Deleting), C(Unknown)"
                    returned: always
                    type: str
                    sample: Ready
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.rdbms.mysql import MySQLManagementClient
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
        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.virtual_network_rule_name is not None):
            self.results['virtual_network_rules'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None):
            self.results['virtual_network_rules'] = self.list_by_server()
        return self.results

    def get(self):
        '''
        Gets facts of the specified MySQL Virtual Network Rule.

        :return: deserialized MySQL Virtual Network Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.virtual_network_rules.get(resource_group_name=self.resource_group,
                                                                  server_name=self.server_name,
                                                                  virtual_network_rule_name=self.virtual_network_rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworkRules.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_server(self):
        '''
        Gets facts of the specified MySQL Virtual Network Rule.

        :return: deserialized MySQL Virtual Network Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.virtual_network_rules.list_by_server(resource_group_name=self.resource_group,
                                                                             server_name=self.server_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworkRules.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMVirtualNetworkRulesFacts()
if __name__ == '__main__':
    main()
