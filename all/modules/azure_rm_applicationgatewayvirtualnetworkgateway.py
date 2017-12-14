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
module: azure_rm_applicationgatewayvirtualnetworkgateway
version_added: "2.5"
short_description: Manage VirtualNetworkGateways instance
description:
    - Create, update and delete instance of VirtualNetworkGateways

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_gateway_name:
        description:
            - The name of the virtual network gateway.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    ip_configurations:
        description:
            - IP configurations for virtual network gateway.
        suboptions:
            id:
                description:
                    - Resource ID.
            private_ip_allocation_method:
                description:
                    - "The private IP allocation method. Possible values are: 'Static' and 'Dynamic'. Possible values include: 'Static', 'Dynamic'"
            subnet:
                description:
                    - The reference of the subnet resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            public_ip_address:
                description:
                    - The reference of the public IP resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    gateway_type:
        description:
            - "The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'. Possible values include: 'Vpn', 'ExpressRoute'"
    vpn_type:
        description:
            - "The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'. Possible values include: 'PolicyBased', 'RouteB
               ased'"
    enable_bgp:
        description:
            - Whether BGP is enabled for this virtual network gateway or not.
    active_active:
        description:
            - ActiveActive flag
    gateway_default_site:
        description:
            - "The reference of the LocalNetworkGateway resource which represents local network site having default routes. Assign Null value in case of remo
               ving existing default site setting."
        suboptions:
            id:
                description:
                    - Resource ID.
    sku:
        description:
            - The reference of the VirtualNetworkGatewaySku resource which represents the SKU selected for Virtual network gateway.
        suboptions:
            name:
                description:
                    - "Gateway SKU name. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'VpnGw3'"
            tier:
                description:
                    - "Gateway SKU tier. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'VpnGw3'"
            capacity:
                description:
                    - The capacity.
    vpn_client_configuration:
        description:
            - The reference of the VpnClientConfiguration resource which represents the P2S VpnClient configurations.
        suboptions:
            vpn_client_address_pool:
                description:
                    - The reference of the address space resource which represents Address space for P2S VpnClient.
                suboptions:
                    address_prefixes:
                        description:
                            - A list of address blocks reserved for this virtual network in CIDR notation.
            vpn_client_root_certificates:
                description:
                    - VpnClientRootCertificate for virtual network gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    public_cert_data:
                        description:
                            - The certificate public data.
                        required: True
                    name:
                        description:
                            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
            vpn_client_revoked_certificates:
                description:
                    - VpnClientRevokedCertificate for Virtual network gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    thumbprint:
                        description:
                            - The revoked VPN client certificate thumbprint.
                    name:
                        description:
                            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
            vpn_client_protocols:
                description:
                    - VpnClientProtocols for Virtual network gateway.
            radius_server_address:
                description:
                    - The radius server address property of the VirtualNetworkGateway resource for vpn client connection.
            radius_server_secret:
                description:
                    - The radius secret property of the VirtualNetworkGateway resource for vpn client connection.
    bgp_settings:
        description:
            - "Virtual network gateway's BGP speaker settings."
        suboptions:
            asn:
                description:
                    - "The BGP speaker's ASN."
            bgp_peering_address:
                description:
                    - The BGP peering address and BGP identifier of this BGP speaker.
            peer_weight:
                description:
                    - The weight added to routes learned from this BGP speaker.
    resource_guid:
        description:
            - The resource GUID property of the VirtualNetworkGateway resource.
    etag:
        description:
            - Gets a unique read-only string that changes whenever the resource is updated.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) VirtualNetworkGateways
    azure_rm_applicationgatewayvirtualnetworkgateway:
      resource_group: resource_group_name
      virtual_network_gateway_name: virtual_network_gateway_name
      id: id
      location: location
      ip_configurations:
        - id: id
          private_ip_allocation_method: private_ip_allocation_method
          subnet:
            id: id
          public_ip_address:
            id: id
          name: name
          etag: etag
      gateway_type: gateway_type
      vpn_type: vpn_type
      enable_bgp: enable_bgp
      active_active: active_active
      gateway_default_site:
        id: id
      sku:
        name: name
        tier: tier
        capacity: capacity
      vpn_client_configuration:
        vpn_client_address_pool:
          address_prefixes:
            - XXXX - list of values -- not implemented str
        vpn_client_root_certificates:
          - id: id
            public_cert_data: public_cert_data
            name: name
            etag: etag
        vpn_client_revoked_certificates:
          - id: id
            thumbprint: thumbprint
            name: name
            etag: etag
        vpn_client_protocols:
          - XXXX - list of values -- not implemented str
        radius_server_address: radius_server_address
        radius_server_secret: radius_server_secret
      bgp_settings:
        asn: asn
        bgp_peering_address: bgp_peering_address
        peer_weight: peer_weight
      resource_guid: resource_guid
      etag: etag
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
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualNetworkGateways(AzureRMModuleBase):
    """Configuration class for an Azure RM VirtualNetworkGateways resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            virtual_network_gateway_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            location=dict(
                type='str',
                required=False
            ),
            ip_configurations=dict(
                type='list',
                required=False
            ),
            gateway_type=dict(
                type='str',
                required=False
            ),
            vpn_type=dict(
                type='str',
                required=False
            ),
            enable_bgp=dict(
                type='str',
                required=False
            ),
            active_active=dict(
                type='str',
                required=False
            ),
            gateway_default_site=dict(
                type='dict',
                required=False
            ),
            sku=dict(
                type='dict',
                required=False
            ),
            vpn_client_configuration=dict(
                type='dict',
                required=False
            ),
            bgp_settings=dict(
                type='dict',
                required=False
            ),
            resource_guid=dict(
                type='str',
                required=False
            ),
            etag=dict(
                type='str',
                required=False
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.virtual_network_gateway_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworkGateways, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                            supports_check_mode=True,
                                                            supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "ip_configurations":
                    self.parameters["ip_configurations"] = kwargs[key]
                elif key == "gateway_type":
                    self.parameters["gateway_type"] = kwargs[key]
                elif key == "vpn_type":
                    self.parameters["vpn_type"] = kwargs[key]
                elif key == "enable_bgp":
                    self.parameters["enable_bgp"] = kwargs[key]
                elif key == "active_active":
                    self.parameters["active_active"] = kwargs[key]
                elif key == "gateway_default_site":
                    self.parameters["gateway_default_site"] = kwargs[key]
                elif key == "sku":
                    self.parameters["sku"] = kwargs[key]
                elif key == "vpn_client_configuration":
                    self.parameters["vpn_client_configuration"] = kwargs[key]
                elif key == "bgp_settings":
                    self.parameters["bgp_settings"] = kwargs[key]
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_virtualnetworkgateways()

        if not old_response:
            self.log("VirtualNetworkGateways instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("VirtualNetworkGateways instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if VirtualNetworkGateways instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the VirtualNetworkGateways instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_virtualnetworkgateways()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("VirtualNetworkGateways instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_virtualnetworkgateways()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_virtualnetworkgateways():
                time.sleep(20)
        else:
            self.log("VirtualNetworkGateways instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_virtualnetworkgateways(self):
        '''
        Creates or updates VirtualNetworkGateways with the specified configuration.

        :return: deserialized VirtualNetworkGateways instance state dictionary
        '''
        self.log("Creating / Updating the VirtualNetworkGateways instance {0}".format(self.virtual_network_gateway_name))

        try:
            response = self.mgmt_client.virtual_network_gateways.create_or_update(self.resource_group,
                                                                                  self.virtual_network_gateway_name,
                                                                                  self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworkGateways instance.')
            self.fail("Error creating the VirtualNetworkGateways instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_virtualnetworkgateways(self):
        '''
        Deletes specified VirtualNetworkGateways instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the VirtualNetworkGateways instance {0}".format(self.virtual_network_gateway_name))
        try:
            response = self.mgmt_client.virtual_network_gateways.delete(self.resource_group,
                                                                        self.virtual_network_gateway_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworkGateways instance.')
            self.fail("Error deleting the VirtualNetworkGateways instance: {0}".format(str(e)))

        return True

    def get_virtualnetworkgateways(self):
        '''
        Gets the properties of the specified VirtualNetworkGateways.

        :return: deserialized VirtualNetworkGateways instance state dictionary
        '''
        self.log("Checking if the VirtualNetworkGateways instance {0} is present".format(self.virtual_network_gateway_name))
        found = False
        try:
            response = self.mgmt_client.virtual_network_gateways.get(self.resource_group,
                                                                     self.virtual_network_gateway_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("VirtualNetworkGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualNetworkGateways instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMVirtualNetworkGateways()

if __name__ == '__main__':
    main()