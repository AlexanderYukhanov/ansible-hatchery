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
module: azure_rm_applicationgatewayvirtualnetworkgatewayconnection
version_added: "2.5"
short_description: Manage VirtualNetworkGatewayConnections instance.
description:
    - Create, update and delete instance of VirtualNetworkGatewayConnections.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_gateway_connection_name:
        description:
            - The name of the virtual network gateway connection.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    authorization_key:
        description:
            - The authorizationKey.
    virtual_network_gateway1:
        description:
            - The reference to virtual network gateway resource.
        required: True
        suboptions:
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
                    - "The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'. Possible values include: 'Vpn', 'ExpressRoute
                       '"
            vpn_type:
                description:
                    - "The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'. Possible values include: 'PolicyBased',
                        'RouteBased'"
            enable_bgp:
                description:
                    - Whether BGP is enabled for this virtual network gateway or not.
            active_active:
                description:
                    - ActiveActive flag
            gateway_default_site:
                description:
                    - "The reference of the LocalNetworkGateway resource which represents local network site having default routes. Assign Null value in case
                        of removing existing default site setting."
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
                            - "Gateway SKU name. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'Vp
                               nGw3'"
                    tier:
                        description:
                            - "Gateway SKU tier. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'Vp
                               nGw3'"
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
    virtual_network_gateway2:
        description:
            - The reference to virtual network gateway resource.
        suboptions:
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
                    - "The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'. Possible values include: 'Vpn', 'ExpressRoute
                       '"
            vpn_type:
                description:
                    - "The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'. Possible values include: 'PolicyBased',
                        'RouteBased'"
            enable_bgp:
                description:
                    - Whether BGP is enabled for this virtual network gateway or not.
            active_active:
                description:
                    - ActiveActive flag
            gateway_default_site:
                description:
                    - "The reference of the LocalNetworkGateway resource which represents local network site having default routes. Assign Null value in case
                        of removing existing default site setting."
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
                            - "Gateway SKU name. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'Vp
                               nGw3'"
                    tier:
                        description:
                            - "Gateway SKU tier. Possible values include: 'Basic', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw2', 'Vp
                               nGw3'"
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
    local_network_gateway2:
        description:
            - The reference to local network gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            location:
                description:
                    - Resource location.
            local_network_address_space:
                description:
                    - Local network site address space.
                suboptions:
                    address_prefixes:
                        description:
                            - A list of address blocks reserved for this virtual network in CIDR notation.
            gateway_ip_address:
                description:
                    - IP address of local network gateway.
            bgp_settings:
                description:
                    - "Local network gateway's BGP speaker settings."
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
                    - The resource GUID property of the LocalNetworkGateway resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    connection_type:
        description:
            - "Gateway connection type. Possible values are: 'Ipsec','Vnet2Vnet','ExpressRoute', and 'VPNClient. Possible values include: 'IPsec', 'Vnet2Vnet
               ', 'ExpressRoute', 'VPNClient'"
        required: True
    routing_weight:
        description:
            - The routing weight.
    shared_key:
        description:
            - The IPSec shared key.
    peer:
        description:
            - The reference to peerings resource.
        suboptions:
            id:
                description:
                    - Resource ID.
    enable_bgp:
        description:
            - EnableBgp flag
    use_policy_based_traffic_selectors:
        description:
            - Enable policy-based traffic selectors.
    ipsec_policies:
        description:
            - The IPSec Policies to be considered by this connection.
        suboptions:
            sa_life_time_seconds:
                description:
                    - The IPSec Security Association (also called Quick Mode or Phase 2 SA) lifetime in seconds for a site to site VPN tunnel.
                required: True
            sa_data_size_kilobytes:
                description:
                    - The IPSec Security Association (also called Quick Mode or Phase 2 SA) payload size in KB for a site to site VPN tunnel.
                required: True
            ipsec_encryption:
                description:
                    - "The IPSec encryption algorithm (IKE phase 1). Possible values include: 'None', 'DES', 'DES3', 'AES128', 'AES192', 'AES256', 'GCMAES128
                       ', 'GCMAES192', 'GCMAES256'"
                required: True
            ipsec_integrity:
                description:
                    - "The IPSec integrity algorithm (IKE phase 1). Possible values include: 'MD5', 'SHA1', 'SHA256', 'GCMAES128', 'GCMAES192', 'GCMAES256'"
                required: True
            ike_encryption:
                description:
                    - "The IKE encryption algorithm (IKE phase 2). Possible values include: 'DES', 'DES3', 'AES128', 'AES192', 'AES256'"
                required: True
            ike_integrity:
                description:
                    - "The IKE integrity algorithm (IKE phase 2). Possible values include: 'MD5', 'SHA1', 'SHA256', 'SHA384'"
                required: True
            dh_group:
                description:
                    - "The DH Groups used in IKE Phase 1 for initial SA. Possible values include: 'None', 'DHGroup1', 'DHGroup2', 'DHGroup14', 'DHGroup2048',
                        'ECP256', 'ECP384', 'DHGroup24'"
                required: True
            pfs_group:
                description:
                    - "The DH Groups used in IKE Phase 2 for new child SA. Possible values include: 'None', 'PFS1', 'PFS2', 'PFS2048', 'ECP256', 'ECP384', 'P
                       FS24'"
                required: True
    resource_guid:
        description:
            - The resource GUID property of the VirtualNetworkGatewayConnection resource.
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
  - name: Create (or update) VirtualNetworkGatewayConnections
    azure_rm_applicationgatewayvirtualnetworkgatewayconnection:
      resource_group: NOT FOUND
      virtual_network_gateway_connection_name: NOT FOUND
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


class AzureRMVirtualNetworkGatewayConnections(AzureRMModuleBase):
    """Configuration class for an Azure RM VirtualNetworkGatewayConnections resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            virtual_network_gateway_connection_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            authorization_key=dict(
                type='str'
            ),
            virtual_network_gateway1=dict(
                type='dict',
                required=True
            ),
            virtual_network_gateway2=dict(
                type='dict'
            ),
            local_network_gateway2=dict(
                type='dict'
            ),
            connection_type=dict(
                type='str',
                required=True
            ),
            routing_weight=dict(
                type='int'
            ),
            shared_key=dict(
                type='str'
            ),
            peer=dict(
                type='dict'
            ),
            enable_bgp=dict(
                type='str'
            ),
            use_policy_based_traffic_selectors=dict(
                type='str'
            ),
            ipsec_policies=dict(
                type='list'
            ),
            resource_guid=dict(
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
        self.virtual_network_gateway_connection_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworkGatewayConnections, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "authorization_key":
                    self.parameters["authorization_key"] = kwargs[key]
                elif key == "virtual_network_gateway1":
                    self.parameters["virtual_network_gateway1"] = kwargs[key]
                elif key == "virtual_network_gateway2":
                    self.parameters["virtual_network_gateway2"] = kwargs[key]
                elif key == "local_network_gateway2":
                    self.parameters["local_network_gateway2"] = kwargs[key]
                elif key == "connection_type":
                    self.parameters["connection_type"] = kwargs[key]
                elif key == "routing_weight":
                    self.parameters["routing_weight"] = kwargs[key]
                elif key == "shared_key":
                    self.parameters["shared_key"] = kwargs[key]
                elif key == "peer":
                    self.parameters["peer"] = kwargs[key]
                elif key == "enable_bgp":
                    self.parameters["enable_bgp"] = kwargs[key]
                elif key == "use_policy_based_traffic_selectors":
                    self.parameters["use_policy_based_traffic_selectors"] = kwargs[key]
                elif key == "ipsec_policies":
                    self.parameters["ipsec_policies"] = kwargs[key]
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_virtualnetworkgatewayconnections()

        if not old_response:
            self.log("VirtualNetworkGatewayConnections instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("VirtualNetworkGatewayConnections instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if VirtualNetworkGatewayConnections instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the VirtualNetworkGatewayConnections instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_virtualnetworkgatewayconnections()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("VirtualNetworkGatewayConnections instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_virtualnetworkgatewayconnections()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_virtualnetworkgatewayconnections():
                time.sleep(20)
        else:
            self.log("VirtualNetworkGatewayConnections instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_virtualnetworkgatewayconnections(self):
        '''
        Creates or updates VirtualNetworkGatewayConnections with the specified configuration.

        :return: deserialized VirtualNetworkGatewayConnections instance state dictionary
        '''
        self.log("Creating / Updating the VirtualNetworkGatewayConnections instance {0}".format(self.virtual_network_gateway_connection_name))

        try:
            response = self.mgmt_client.virtual_network_gateway_connections.create_or_update(self.resource_group,
                                                                                             self.virtual_network_gateway_connection_name,
                                                                                             self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworkGatewayConnections instance.')
            self.fail("Error creating the VirtualNetworkGatewayConnections instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_virtualnetworkgatewayconnections(self):
        '''
        Deletes specified VirtualNetworkGatewayConnections instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the VirtualNetworkGatewayConnections instance {0}".format(self.virtual_network_gateway_connection_name))
        try:
            response = self.mgmt_client.virtual_network_gateway_connections.delete(self.resource_group,
                                                                                   self.virtual_network_gateway_connection_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworkGatewayConnections instance.')
            self.fail("Error deleting the VirtualNetworkGatewayConnections instance: {0}".format(str(e)))

        return True

    def get_virtualnetworkgatewayconnections(self):
        '''
        Gets the properties of the specified VirtualNetworkGatewayConnections.

        :return: deserialized VirtualNetworkGatewayConnections instance state dictionary
        '''
        self.log("Checking if the VirtualNetworkGatewayConnections instance {0} is present".format(self.virtual_network_gateway_connection_name))
        found = False
        try:
            response = self.mgmt_client.virtual_network_gateway_connections.get(self.resource_group,
                                                                                self.virtual_network_gateway_connection_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("VirtualNetworkGatewayConnections instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualNetworkGatewayConnections instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMVirtualNetworkGatewayConnections()

if __name__ == '__main__':
    main()
