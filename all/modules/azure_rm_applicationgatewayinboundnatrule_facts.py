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
module: azure_rm_applicationgatewayinboundnatrule_facts
version_added: "2.5"
short_description: Get InboundNatRules facts.
description:
    - Get facts of InboundNatRules.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of InboundNatRules
    azure_rm_applicationgatewayinboundnatrule_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      inbound_nat_rule_name: inbound_nat_rule_name
      expand: expand
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
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
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.load_balancer_name = None
        self.inbound_nat_rule_name = None
        self.expand = None
        super(AzureRMInboundNatRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.load_balancer_name is not None and
                self.inbound_nat_rule_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified InboundNatRules.

        :return: deserialized InboundNatRulesinstance state dictionary
        '''
        self.log("Checking if the InboundNatRules instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.inbound_nat_rules.get(self.resource_group,
                                                              self.load_balancer_name,
                                                              self.inbound_nat_rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("InboundNatRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the InboundNatRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMInboundNatRulesFacts()
if __name__ == '__main__':
    main()