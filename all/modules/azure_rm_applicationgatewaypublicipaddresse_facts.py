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
module: azure_rm_applicationgatewaypublicipaddresse_facts
version_added: "2.5"
short_description: Get PublicIPAddresses facts.
description:
    - Get facts of PublicIPAddresses.

options:
    resource_group:
        description:
            - The name of the resource group.
    virtual_machine_scale_set_name:
        description:
            - The name of the virtual machine scale set.
    virtualmachine_index:
        description:
            - The virtual machine index.
    network_interface_name:
        description:
            - The network interface name.
    ip_configuration_name:
        description:
            - The IP configuration name.
    public_ip_address_name:
        description:
            - The name of the subnet.
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
  - name: List instances of PublicIPAddresses
    azure_rm_applicationgatewaypublicipaddresse_facts:
      resource_group: resource_group_name
      virtual_machine_scale_set_name: virtual_machine_scale_set_name
      virtualmachine_index: virtualmachine_index
      network_interface_name: network_interface_name
      ip_configuration_name: ip_configuration_name

  - name: Get instance of PublicIPAddresses
    azure_rm_applicationgatewaypublicipaddresse_facts:
      resource_group: resource_group_name
      public_ip_address_name: public_ip_address_name
      expand: expand

  - name: List instances of PublicIPAddresses
    azure_rm_applicationgatewaypublicipaddresse_facts:
      resource_group: resource_group_name
      virtual_machine_scale_set_name: virtual_machine_scale_set_name

  - name: List instances of PublicIPAddresses
    azure_rm_applicationgatewaypublicipaddresse_facts:
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


class AzureRMPublicIPAddressesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=False
            ),
            virtual_machine_scale_set_name=dict(
                type='str',
                required=False
            ),
            virtualmachine_index=dict(
                type='str',
                required=False
            ),
            network_interface_name=dict(
                type='str',
                required=False
            ),
            ip_configuration_name=dict(
                type='str',
                required=False
            ),
            public_ip_address_name=dict(
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
        self.virtual_machine_scale_set_name = None
        self.virtualmachine_index = None
        self.network_interface_name = None
        self.ip_configuration_name = None
        self.public_ip_address_name = None
        self.expand = None
        super(AzureRMPublicIPAddressesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.virtual_machine_scale_set_name is not None and
                self.virtualmachine_index is not None and
                self.network_interface_name is not None and
                self.ip_configuration_name is not None):
            self.results['ansible_facts']['list_virtual_machine_scale_set_vm_public_ip_addresses'] = self.list_virtual_machine_scale_set_vm_public_ip_addresses()
        elif (self.resource_group is not None and
              self.public_ip_address_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group is not None and
              self.virtual_machine_scale_set_name is not None):
            self.results['ansible_facts']['list_virtual_machine_scale_set_public_ip_addresses'] = self.list_virtual_machine_scale_set_public_ip_addresses()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def list_virtual_machine_scale_set_vm_public_ip_addresses(self):
        '''
        Gets facts of the specified PublicIPAddresses.

        :return: deserialized PublicIPAddressesinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.public_ip_addresses.list_virtual_machine_scale_set_vm_public_ip_addresses(resource_group_name=self.resource_group,
                                                                                                                  virtual_machine_scale_set_name=self.virtual_machine_scale_set_name,
                                                                                                                  virtualmachine_index=self.virtualmachine_index,
                                                                                                                  network_interface_name=self.network_interface_name,
                                                                                                                  ip_configuration_name=self.ip_configuration_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PublicIPAddresses.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def get(self):
        '''
        Gets facts of the specified PublicIPAddresses.

        :return: deserialized PublicIPAddressesinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.public_ip_addresses.get(resource_group_name=self.resource_group,
                                                                public_ip_address_name=self.public_ip_address_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PublicIPAddresses.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_virtual_machine_scale_set_public_ip_addresses(self):
        '''
        Gets facts of the specified PublicIPAddresses.

        :return: deserialized PublicIPAddressesinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.public_ip_addresses.list_virtual_machine_scale_set_public_ip_addresses(resource_group_name=self.resource_group,
                                                                                                               virtual_machine_scale_set_name=self.virtual_machine_scale_set_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PublicIPAddresses.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_all(self):
        '''
        Gets facts of the specified PublicIPAddresses.

        :return: deserialized PublicIPAddressesinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.public_ip_addresses.list_all()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for PublicIPAddresses.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMPublicIPAddressesFacts()
if __name__ == '__main__':
    main()
