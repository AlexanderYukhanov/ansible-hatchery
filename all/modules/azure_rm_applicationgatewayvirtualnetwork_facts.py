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
module: azure_rm_applicationgatewayvirtualnetwork_facts
version_added: "2.5"
short_description: Get Virtual Network facts.
description:
    - Get facts of Virtual Network.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_name:
        description:
            - The name of the virtual network.
    expand:
        description:
            - Expands referenced resources.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Virtual Network
    azure_rm_applicationgatewayvirtualnetwork_facts:
      resource_group: resource_group_name
      virtual_network_name: virtual_network_name
      expand: expand

  - name: List instances of Virtual Network
    azure_rm_applicationgatewayvirtualnetwork_facts:
      resource_group: resource_group_name
'''

RETURN = '''
virtual_networks:
    description: A list of dict results where the key is the name of the Virtual Network and the values are the facts for that Virtual Network.
    returned: always
    type: complex
    contains:
        virtualnetwork_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: test-vnet
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Network/virtualNetworks
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: westus
                subnets:
                    description:
                        - A list of subnets in a Virtual Network.
                    returned: always
                    type: complex
                    sample: subnets
                    contains:
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


class AzureRMVirtualNetworksFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            virtual_network_name=dict(
                type='str'
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
        self.expand = None
        super(AzureRMVirtualNetworksFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.virtual_network_name is not None):
            self.results['virtual_networks'] = self.get()
        elif (self.resource_group is not None):
            self.results['virtual_networks'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Virtual Network.

        :return: deserialized Virtual Networkinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.virtual_networks.get(resource_group_name=self.resource_group,
                                                             virtual_network_name=self.virtual_network_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworks.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Virtual Network.

        :return: deserialized Virtual Networkinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.virtual_networks.list(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworks.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMVirtualNetworksFacts()
if __name__ == '__main__':
    main()
