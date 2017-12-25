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
module: azure_rm_applicationgatewayvirtualnetworkpeering
version_added: "2.5"
short_description: Manage VirtualNetworkPeerings instance.
description:
    - Create, update and delete instance of VirtualNetworkPeerings.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_name:
        description:
            - The name of the virtual network.
        required: True
    virtual_network_peering_name:
        description:
            - The name of the peering.
        required: True
    id:
        description:
            - Resource ID.
    allow_virtual_network_access:
        description:
            - Whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space.
    allow_forwarded_traffic:
        description:
            - Whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed.
    allow_gateway_transit:
        description:
            - If gateway links can be used in remote virtual networking to link to this virtual network.
    use_remote_gateways:
        description:
            - "If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, vi
               rtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be se
               t if virtual network already has a gateway."
    remote_virtual_network:
        description:
            - "The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register
                for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering)."
        suboptions:
            id:
                description:
                    - Resource ID.
    remote_address_space:
        description:
            - The reference of the remote virtual network address space.
        suboptions:
            address_prefixes:
                description:
                    - A list of address blocks reserved for this virtual network in CIDR notation.
    peering_state:
        description:
            - "The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'. Possible values include: 'Initiat
               ed', 'Connected', 'Disconnected'"
    provisioning_state:
        description:
            - The provisioning state of the resource.
    name:
        description:
            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
    etag:
        description:
            - A unique read-only string that changes whenever the resource is updated.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) VirtualNetworkPeerings
    azure_rm_applicationgatewayvirtualnetworkpeering:
      resource_group: peerTest
      virtual_network_name: vnet1
      virtual_network_peering_name: peer
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualNetworkPeerings(AzureRMModuleBase):
    """Configuration class for an Azure RM VirtualNetworkPeerings resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            virtual_network_name=dict(
                type='str',
                required=True
            ),
            virtual_network_peering_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            allow_virtual_network_access=dict(
                type='str'
            ),
            allow_forwarded_traffic=dict(
                type='str'
            ),
            allow_gateway_transit=dict(
                type='str'
            ),
            use_remote_gateways=dict(
                type='str'
            ),
            remote_virtual_network=dict(
                type='dict'
            ),
            remote_address_space=dict(
                type='dict'
            ),
            peering_state=dict(
                type='str'
            ),
            provisioning_state=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            etag=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.virtual_network_name = None
        self.virtual_network_peering_name = None
        self.virtual_network_peering_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworkPeerings, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                            supports_check_mode=True,
                                                            supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.virtual_network_peering_parameters["id"] = kwargs[key]
                elif key == "allow_virtual_network_access":
                    self.virtual_network_peering_parameters["allow_virtual_network_access"] = kwargs[key]
                elif key == "allow_forwarded_traffic":
                    self.virtual_network_peering_parameters["allow_forwarded_traffic"] = kwargs[key]
                elif key == "allow_gateway_transit":
                    self.virtual_network_peering_parameters["allow_gateway_transit"] = kwargs[key]
                elif key == "use_remote_gateways":
                    self.virtual_network_peering_parameters["use_remote_gateways"] = kwargs[key]
                elif key == "remote_virtual_network":
                    self.virtual_network_peering_parameters["remote_virtual_network"] = kwargs[key]
                elif key == "remote_address_space":
                    self.virtual_network_peering_parameters["remote_address_space"] = kwargs[key]
                elif key == "peering_state":
                    self.virtual_network_peering_parameters["peering_state"] = kwargs[key]
                elif key == "provisioning_state":
                    self.virtual_network_peering_parameters["provisioning_state"] = kwargs[key]
                elif key == "name":
                    self.virtual_network_peering_parameters["name"] = kwargs[key]
                elif key == "etag":
                    self.virtual_network_peering_parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_virtualnetworkpeerings()

        if not old_response:
            self.log("VirtualNetworkPeerings instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("VirtualNetworkPeerings instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if VirtualNetworkPeerings instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the VirtualNetworkPeerings instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_virtualnetworkpeerings()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("VirtualNetworkPeerings instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_virtualnetworkpeerings()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_virtualnetworkpeerings():
                time.sleep(20)
        else:
            self.log("VirtualNetworkPeerings instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_virtualnetworkpeerings(self):
        '''
        Creates or updates VirtualNetworkPeerings with the specified configuration.

        :return: deserialized VirtualNetworkPeerings instance state dictionary
        '''
        self.log("Creating / Updating the VirtualNetworkPeerings instance {0}".format(self.virtual_network_peering_name))

        try:
            response = self.mgmt_client.virtual_network_peerings.create_or_update(self.resource_group,
                                                                                  self.virtual_network_name,
                                                                                  self.virtual_network_peering_name,
                                                                                  self.virtual_network_peering_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworkPeerings instance.')
            self.fail("Error creating the VirtualNetworkPeerings instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_virtualnetworkpeerings(self):
        '''
        Deletes specified VirtualNetworkPeerings instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the VirtualNetworkPeerings instance {0}".format(self.virtual_network_peering_name))
        try:
            response = self.mgmt_client.virtual_network_peerings.delete(self.resource_group,
                                                                        self.virtual_network_name,
                                                                        self.virtual_network_peering_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworkPeerings instance.')
            self.fail("Error deleting the VirtualNetworkPeerings instance: {0}".format(str(e)))

        return True

    def get_virtualnetworkpeerings(self):
        '''
        Gets the properties of the specified VirtualNetworkPeerings.

        :return: deserialized VirtualNetworkPeerings instance state dictionary
        '''
        self.log("Checking if the VirtualNetworkPeerings instance {0} is present".format(self.virtual_network_peering_name))
        found = False
        try:
            response = self.mgmt_client.virtual_network_peerings.get(self.resource_group,
                                                                     self.virtual_network_name,
                                                                     self.virtual_network_peering_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("VirtualNetworkPeerings instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualNetworkPeerings instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMVirtualNetworkPeerings()

if __name__ == '__main__':
    main()
