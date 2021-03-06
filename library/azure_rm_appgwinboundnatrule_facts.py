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
module: azure_rm_appgwinboundnatrule_facts
version_added: "2.5"
short_description: Get Inbound Nat Rule facts.
description:
    - Get facts of Inbound Nat Rule.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    inbound_nat_rule_name:
        description:
            - The name of the inbound nat rule.
        required: True
    expand:
        description:
            - Expands referenced resources.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Inbound Nat Rule
    azure_rm_appgwinboundnatrule_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      inbound_nat_rule_name: inbound_nat_rule_name
      expand: expand
'''

RETURN = '''
inbound_nat_rules:
    description: A list of dict results where the key is the name of the Inbound Nat Rule and the values are the facts for that Inbound Nat Rule.
    returned: always
    type: complex
    contains:
        inboundnatrule_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb1/inboundNatRules/natRule1.1
                protocol:
                    description:
                        - "Possible values include: 'Udp', 'Tcp', 'All'"
                    returned: always
                    type: str
                    sample: Tcp
                name:
                    description:
                        - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: natRule1.1
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMInboundNatRulesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            load_balancer_name=dict(
                type='str',
                required=True
            ),
            inbound_nat_rule_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
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
        self.load_balancer_name = None
        self.inbound_nat_rule_name = None
        self.expand = None
        super(AzureRMInboundNatRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None and
                self.inbound_nat_rule_name is not None):
            self.results['inbound_nat_rules'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Inbound Nat Rule.

        :return: deserialized Inbound Nat Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.inbound_nat_rules.get(resource_group_name=self.resource_group,
                                                              load_balancer_name=self.load_balancer_name,
                                                              inbound_nat_rule_name=self.inbound_nat_rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for InboundNatRules.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMInboundNatRulesFacts()
if __name__ == '__main__':
    main()
