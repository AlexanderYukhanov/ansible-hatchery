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
module: azure_rm_appgwnetworkinterface_facts
version_added: "2.5"
short_description: Get Network Interface facts.
description:
    - Get facts of Network Interface.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_interface_name:
        description:
            - The name of the network interface.
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
  - name: Get instance of Network Interface
    azure_rm_appgwnetworkinterface_facts:
      resource_group: resource_group_name
      network_interface_name: network_interface_name
      expand: expand
'''

RETURN = '''
network_interfaces:
    description: A list of dict results where the key is the name of the Network Interface and the values are the facts for that Network Interface.
    returned: always
    type: complex
    contains:
        networkinterface_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/test-nic
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: test-nic
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Network/networkInterfaces
                location:
                    description:
                        - Resource location.
                    returned: always
                    type: str
                    sample: eastus
                primary:
                    description:
                        - Gets whether this is a primary network interface on a virtual machine.
                    returned: always
                    type: str
                    sample: True
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


class AzureRMNetworkInterfacesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_interface_name=dict(
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
        self.network_interface_name = None
        self.expand = None
        super(AzureRMNetworkInterfacesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.network_interface_name is not None):
            self.results['network_interfaces'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Network Interface.

        :return: deserialized Network Interfaceinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.network_interfaces.get(resource_group_name=self.resource_group,
                                                               network_interface_name=self.network_interface_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for NetworkInterfaces.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results


def main():
    AzureRMNetworkInterfacesFacts()
if __name__ == '__main__':
    main()
