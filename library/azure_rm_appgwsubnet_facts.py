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
module: azure_rm_appgwsubnet_facts
version_added: "2.5"
short_description: Get Subnet facts.
description:
    - Get facts of Subnet.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_name:
        description:
            - The name of the virtual network.
        required: True
    subnet_name:
        description:
            - The name of the subnet.
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
  - name: Get instance of Subnet
    azure_rm_appgwsubnet_facts:
      resource_group: resource_group_name
      virtual_network_name: virtual_network_name
      subnet_name: subnet_name
      expand: expand
'''

RETURN = '''
subnets:
    description: A list of dict results where the key is the name of the Subnet and the values are the facts for that Subnet.
    returned: always
    type: complex
    contains:
        subnet_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/subnet-test/providers/Microsoft.Network/virtualNetworks/vnetname/subnets/subnet1
                name:
                    description:
                        - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: subnet1
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


class AzureRMSubnetsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            virtual_network_name=dict(
                type='str',
                required=True
            ),
            subnet_name=dict(
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
        self.virtual_network_name = None
        self.subnet_name = None
        self.expand = None
        super(AzureRMSubnetsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.virtual_network_name is not None and
                self.subnet_name is not None):
            self.results['subnets'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Subnet.

        :return: deserialized Subnetinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.subnets.get(resource_group_name=self.resource_group,
                                                    virtual_network_name=self.virtual_network_name,
                                                    subnet_name=self.subnet_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Subnets.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMSubnetsFacts()
if __name__ == '__main__':
    main()
