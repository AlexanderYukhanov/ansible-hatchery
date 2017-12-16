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
module: azure_rm_applicationgatewaynetworkinterface_facts
version_added: "2.5"
short_description: Get NetworkInterfaces facts.
description:
    - Get facts of NetworkInterfaces.

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
            - The name of the network interface.
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
  - name: List instances of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
      resource_group: resource_group_name
      virtual_machine_scale_set_name: virtual_machine_scale_set_name
      virtualmachine_index: virtualmachine_index
      network_interface_name: network_interface_name
      expand: expand

  - name: Get instance of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
      resource_group: resource_group_name
      network_interface_name: network_interface_name
      expand: expand

  - name: List instances of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
      resource_group: resource_group_name
      virtual_machine_scale_set_name: virtual_machine_scale_set_name
      virtualmachine_index: virtualmachine_index

  - name: List instances of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
      resource_group: resource_group_name
      network_interface_name: network_interface_name

  - name: List instances of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
      resource_group: resource_group_name
      virtual_machine_scale_set_name: virtual_machine_scale_set_name

  - name: List instances of NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface_facts:
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


class AzureRMNetworkInterfacesFacts(AzureRMModuleBase):
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
        self.resource_group = None
        self.virtual_machine_scale_set_name = None
        self.virtualmachine_index = None
        self.network_interface_name = None
        self.expand = None
        super(AzureRMNetworkInterfacesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.virtual_machine_scale_set_name is not None and
                self.virtualmachine_index is not None and
                self.network_interface_name is not None):
            self.results['ansible_facts']['list_virtual_machine_scale_set_ip_configurations'] = self.list_virtual_machine_scale_set_ip_configurations()
        elif (self.resource_group_name is not None and
              self.network_interface_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.virtual_machine_scale_set_name is not None and
              self.virtualmachine_index is not None):
            self.results['ansible_facts']['list_virtual_machine_scale_set_vm_network_interfaces'] = self.list_virtual_machine_scale_set_vm_network_interfaces()
        elif (self.resource_group_name is not None and
              self.network_interface_name is not None):
            self.results['ansible_facts']['list_effective_network_security_groups'] = self.list_effective_network_security_groups()
        elif (self.resource_group_name is not None and
              self.virtual_machine_scale_set_name is not None):
            self.results['ansible_facts']['list_virtual_machine_scale_set_network_interfaces'] = self.list_virtual_machine_scale_set_network_interfaces()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def list_virtual_machine_scale_set_ip_configurations(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_ip_configurations(self.resource_group,
                                                                                                            self.virtual_machine_scale_set_name,
                                                                                                            self.virtualmachine_index,
                                                                                                            self.network_interface_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.get(self.resource_group,
                                                               self.network_interface_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_virtual_machine_scale_set_vm_network_interfaces(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_vm_network_interfaces(self.resource_group,
                                                                                                                self.virtual_machine_scale_set_name,
                                                                                                                self.virtualmachine_index)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_effective_network_security_groups(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.list_effective_network_security_groups(self.resource_group,
                                                                                                  self.network_interface_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_virtual_machine_scale_set_network_interfaces(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_network_interfaces(self.resource_group,
                                                                                                             self.virtual_machine_scale_set_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_all(self):
        '''
        Gets facts of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfacesinstance state dictionary
        '''
        found = False
        try:
            response = self.mgmt_client.network_interfaces.list_all()
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMNetworkInterfacesFacts()
if __name__ == '__main__':
    main()
