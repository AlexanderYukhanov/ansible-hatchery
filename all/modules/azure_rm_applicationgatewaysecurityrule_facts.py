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
short_description: Get Security Rule facts.
description:
    - Get facts of Security Rule.

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

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Security Rule
    azure_rm_applicationgatewaysecurityrule_facts:
      resource_group: resource_group_name
      network_security_group_name: network_security_group_name
      security_rule_name: security_rule_name

  - name: List instances of Security Rule
    azure_rm_applicationgatewaysecurityrule_facts:
      resource_group: resource_group_name
      network_security_group_name: network_security_group_name
'''

RETURN = '''
security_rules:
    description: A list of dict results where the key is the name of the Security Rule and the values are the facts for that Security Rule.
    returned: always
    type: complex
    contains:
        securityrule_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/securityRules/rule1
                protocol:
                    description:
                        - "Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*). Possible values include: C(Tcp), C(Udp), C(*)"
                    returned: always
                    type: str
                    sample: *
                access:
                    description:
                        - "The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny). Possible values include: C(Allow), C(Deny)"
                    returned: always
                    type: str
                    sample: Allow
                priority:
                    description:
                        - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collectio
                          n. The lower the priority number, the higher the priority of the rule."
                    returned: always
                    type: int
                    sample: 130
                direction:
                    description:
                        - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values are
                          : C(Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
                    returned: always
                    type: str
                    sample: Inbound
                name:
                    description:
                        - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: rule1
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
        self.network_security_group_name = None
        self.security_rule_name = None
        super(AzureRMSecurityRulesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.network_security_group_name is not None and
                self.security_rule_name is not None):
            self.results['security_rules'] = self.get()
        elif (self.resource_group is not None and
              self.network_security_group_name is not None):
            self.results['security_rules'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Security Rule.

        :return: deserialized Security Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.security_rules.get(resource_group_name=self.resource_group,
                                                           network_security_group_name=self.network_security_group_name,
                                                           security_rule_name=self.security_rule_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SecurityRules.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Security Rule.

        :return: deserialized Security Ruleinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.security_rules.list(resource_group_name=self.resource_group,
                                                            network_security_group_name=self.network_security_group_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SecurityRules.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMSecurityRulesFacts()
if __name__ == '__main__':
    main()
