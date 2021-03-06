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
module: azure_rm_appgwnetworksecuritygroup_facts
version_added: "2.5"
short_description: Get Network Security Group facts.
description:
    - Get facts of Network Security Group.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_security_group_name:
        description:
            - The name of the network security group.
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
  - name: Get instance of Network Security Group
    azure_rm_appgwnetworksecuritygroup_facts:
      resource_group: resource_group_name
      network_security_group_name: network_security_group_name
      expand: expand
'''

RETURN = '''
network_security_groups:
    description: A list of dict results where the key is the name of the Network Security Group and the values are the facts for that Network Security Group.
    returned: always
    type: complex
    contains:
        networksecuritygroup_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: testnsg
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Network/networkSecurityGroups
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: westus
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


class AzureRMNetworkSecurityGroupsFacts(AzureRMModuleBase):
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
        self.network_security_group_name = None
        self.expand = None
        super(AzureRMNetworkSecurityGroupsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.network_security_group_name is not None):
            self.results['network_security_groups'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Network Security Group.

        :return: deserialized Network Security Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.network_security_groups.get(resource_group_name=self.resource_group,
                                                                    network_security_group_name=self.network_security_group_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for NetworkSecurityGroups.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMNetworkSecurityGroupsFacts()
if __name__ == '__main__':
    main()
