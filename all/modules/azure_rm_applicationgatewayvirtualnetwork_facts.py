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
short_description: Get VirtualNetworks facts.
description:
    - Get facts of VirtualNetworks.

options:
    resource_group:
        description:
            - The name of the resource group.
    virtual_network_name:
        description:
            - The name of the virtual network.
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
  - name: Get instance of VirtualNetworks
    azure_rm_applicationgatewayvirtualnetwork_facts:
      resource_group: resource_group_name
      virtual_network_name: virtual_network_name
      expand: expand

  - name: List instances of VirtualNetworks
    azure_rm_applicationgatewayvirtualnetwork_facts:
      resource_group: resource_group_name
      virtual_network_name: virtual_network_name

  - name: List instances of VirtualNetworks
    azure_rm_applicationgatewayvirtualnetwork_facts:
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


class AzureRMVirtualNetworksFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=False
            ),
            virtual_network_name=dict(
                type='str',
                required=False
            ),
            expand=dict(
                type='str',
                required=False
            ),
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
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.virtual_network_name is not None):
            self.results['ansible_facts']['list_usage'] = self.list_usage()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def get(self):
        '''
        Gets facts of the specified VirtualNetworks.

        :return: deserialized VirtualNetworksinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.virtual_networks.get(self.resource_group,
                                                             self.virtual_network_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworks.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_usage(self):
        '''
        Gets facts of the specified VirtualNetworks.

        :return: deserialized VirtualNetworksinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.virtual_networks.list_usage(self.resource_group,
                                                                    self.virtual_network_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworks.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_all(self):
        '''
        Gets facts of the specified VirtualNetworks.

        :return: deserialized VirtualNetworksinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.virtual_networks.list_all()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for VirtualNetworks.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMVirtualNetworksFacts()
if __name__ == '__main__':
    main()
