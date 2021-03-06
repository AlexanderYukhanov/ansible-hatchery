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
module: azure_rm_appgwloadbalancerloadbalancingrule_facts
version_added: "2.5"
short_description: Get Load Balancer Load Balancing Rule facts.
description:
    - Get facts of Load Balancer Load Balancing Rule.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    load_balancing_rule_name:
        description:
            - The name of the load balancing rule.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Load Balancer Load Balancing Rule
    azure_rm_appgwloadbalancerloadbalancingrule_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      load_balancing_rule_name: load_balancing_rule_name
'''

RETURN = '''
load_balancer_load_balancing_rules:
    description: A list of dict results where the key is the name of the Load Balancer Load Balancing Rule and the values are the facts for that Load Balancer Load Balancing Rule.
    returned: always
    type: complex
    contains:
        loadbalancerloadbalancingrule_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb1/loadBalancingRules/rule1
                probe:
                    description:
                        - The reference of the load balancer probe used by the load balancing rule.
                    returned: always
                    type: complex
                    sample: probe
                    contains:
                        id:
                            description:
                                - Resource ID.
                            returned: always
                            type: str
                            sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb1/probes/probe1
                protocol:
                    description:
                        - "Possible values include: 'Udp', 'Tcp', 'All'"
                    returned: always
                    type: str
                    sample: Tcp
                name:
                    description:
                        - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: rule1
                etag:
                    description:
                        - A unique read-only string that changes whenever the resource is updated.
                    returned: always
                    type: str
                    sample: "W/\'00000000-0000-0000-0000-000000000000\'"
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


class AzureRMLoadBalancerLoadBalancingRulesFacts(AzureRMModuleBase):
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
            load_balancing_rule_name=dict(
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
        self.load_balancer_name = None
        self.load_balancing_rule_name = None
        super(AzureRMLoadBalancerLoadBalancingRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None and
                self.load_balancing_rule_name is not None):
            self.results['load_balancer_load_balancing_rules'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Load Balancer Load Balancing Rule.

        :return: deserialized Load Balancer Load Balancing Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.load_balancer_load_balancing_rules.get(resource_group_name=self.resource_group,
                                                                               load_balancer_name=self.load_balancer_name,
                                                                               load_balancing_rule_name=self.load_balancing_rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancerLoadBalancingRules.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMLoadBalancerLoadBalancingRulesFacts()
if __name__ == '__main__':
    main()
