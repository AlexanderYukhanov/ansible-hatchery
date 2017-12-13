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
module: azure_rm_applicationgatewaysecurityrule_facts
version_added: "2.5"
short_description: Get SecurityRules facts.
description:
    - Get facts of SecurityRules.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_security_group_name:
        description:
            - The name of the network security group.
        required: True
    security_rule_name:
        description:
            - The name of the security rule.
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of SecurityRules
    azure_rm_applicationgatewaysecurityrule_facts:
      resource_group: resource_group_name
      network_security_group_name: network_security_group_name
      security_rule_name: security_rule_name
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


class AzureRMSecurityRulesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_security_group_name=dict(
                type='str',
                required=True
            ),
            security_rule_name=dict(
                type='str',
                required=True
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.network_security_group_name = None
        self.security_rule_name = None
        super(AzureRMSecurityRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.network_security_group_name is not None and
                self.security_rule_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified SecurityRules.

        :return: deserialized SecurityRulesinstance state dictionary
        '''
        self.log("Checking if the SecurityRules instance {0} is present".format(self.security_rule_name))
        found = False
        try:
            response = self.mgmt_client.security_rules.get(self.resource_group,
                                                           self.network_security_group_name,
                                                           self.security_rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SecurityRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SecurityRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMSecurityRulesFacts()
if __name__ == '__main__':
    main()
