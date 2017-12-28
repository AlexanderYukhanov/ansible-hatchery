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
module: azure_rm_applicationgatewayvirtualnetwork
version_added: "2.5"
short_description: Manage VirtualNetworks instance.
description:
    - Create, update and delete instance of VirtualNetworks.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_name:
        description:
            - The name of the virtual network.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    address_space:
        description:
            - The AddressSpace that contains an array of IP address ranges that can be used by subnets.
        suboptions:
            address_prefixes:
                description:
                    - A list of address blocks reserved for this virtual network in CIDR notation.
    dhcp_options:
        description:
            - The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.
        suboptions:
            dns_servers:
                description:
                    - The list of DNS servers IP addresses.
    subnets:
        description:
            - A list of subnets in a Virtual Network.
        suboptions:
            id:
                description:
                    - Resource ID.
            address_prefix:
                description:
                    - The address prefix for the subnet.
            network_security_group:
                description:
                    - The reference of the NetworkSecurityGroup resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    location:
                        description:
                            - Resource location.
                    security_rules:
                        description:
                            - A collection of security rules of the network security group.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            description:
                                description:
                                    - A description for this rule. Restricted to 140 chars.
                            protocol:
                                description:
                                    - Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*).
                                required: True
                                choices: ['tcp', 'udp', '*']
                            source_port_range:
                                description:
                                    - The source port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match all ports.
                            destination_port_range:
                                description:
                                    - The destination port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match all ports.
                            source_address_prefix:
                                description:
                                    - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetw
                                       ork), C(AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traff
                                       ic originates from. "
                            source_address_prefixes:
                                description:
                                    - The CIDR or source IP ranges.
                            source_application_security_groups:
                                description:
                                    - The application security group specified as source.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                            destination_address_prefix:
                                description:
                                    - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. D
                                       efault tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                            destination_address_prefixes:
                                description:
                                    - The destination address prefixes. CIDR or destination IP ranges.
                            destination_application_security_groups:
                                description:
                                    - The application security group specified as destination.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                            source_port_ranges:
                                description:
                                    - The source port ranges.
                            destination_port_ranges:
                                description:
                                    - The destination port ranges.
                            access:
                                description:
                                    - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny).
                                required: True
                                choices: ['allow', 'deny']
                            priority:
                                description:
                                    - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in t
                                       he collection. The lower the priority number, the higher the priority of the rule."
                            direction:
                                description:
                                    - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possibl
                                       e values are: C(Inbound) and C(Outbound)."
                                required: True
                                choices: ['inbound', 'outbound']
                            provisioning_state:
                                description:
                                    - The provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                            name:
                                description:
                                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                            etag:
                                description:
                                    - A unique read-only string that changes whenever the resource is updated.
                    default_security_rules:
                        description:
                            - The default security rules of network security group.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            description:
                                description:
                                    - A description for this rule. Restricted to 140 chars.
                            protocol:
                                description:
                                    - Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*).
                                required: True
                                choices: ['tcp', 'udp', '*']
                            source_port_range:
                                description:
                                    - The source port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match all ports.
                            destination_port_range:
                                description:
                                    - The destination port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match all ports.
                            source_address_prefix:
                                description:
                                    - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetw
                                       ork), C(AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traff
                                       ic originates from. "
                            source_address_prefixes:
                                description:
                                    - The CIDR or source IP ranges.
                            source_application_security_groups:
                                description:
                                    - The application security group specified as source.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                            destination_address_prefix:
                                description:
                                    - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. D
                                       efault tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                            destination_address_prefixes:
                                description:
                                    - The destination address prefixes. CIDR or destination IP ranges.
                            destination_application_security_groups:
                                description:
                                    - The application security group specified as destination.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                            source_port_ranges:
                                description:
                                    - The source port ranges.
                            destination_port_ranges:
                                description:
                                    - The destination port ranges.
                            access:
                                description:
                                    - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny).
                                required: True
                                choices: ['allow', 'deny']
                            priority:
                                description:
                                    - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in t
                                       he collection. The lower the priority number, the higher the priority of the rule."
                            direction:
                                description:
                                    - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possibl
                                       e values are: C(Inbound) and C(Outbound)."
                                required: True
                                choices: ['inbound', 'outbound']
                            provisioning_state:
                                description:
                                    - The provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                            name:
                                description:
                                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                            etag:
                                description:
                                    - A unique read-only string that changes whenever the resource is updated.
                    resource_guid:
                        description:
                            - The resource GUID property of the network security group resource.
                    provisioning_state:
                        description:
                            - The provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
            route_table:
                description:
                    - The reference of the RouteTable resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    location:
                        description:
                            - Resource location.
                    routes:
                        description:
                            - Collection of routes contained within a route table.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            address_prefix:
                                description:
                                    - The destination CIDR to which the route applies.
                            next_hop_type:
                                description:
                                    - "The type of Azure hop the packet should be sent to. Possible values are: C(VirtualNetworkGateway), C(VnetLocal), C(Int
                                       ernet), C(VirtualAppliance), and C(None)."
                                required: True
                                choices: ['virtual_network_gateway', 'vnet_local', 'internet', 'virtual_appliance', 'none']
                            next_hop_ip_address:
                                description:
                                    - "The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is V
                                       irtualAppliance."
                            provisioning_state:
                                description:
                                    - The provisioning state of the resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                            name:
                                description:
                                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                            etag:
                                description:
                                    - A unique read-only string that changes whenever the resource is updated.
                    disable_bgp_route_propagation:
                        description:
                            - Gets or sets whether to disable the routes learned by BGP on that route table. True means disable.
                    provisioning_state:
                        description:
                            - The provisioning state of the resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                    etag:
                        description:
                            - Gets a unique read-only string that changes whenever the resource is updated.
            service_endpoints:
                description:
                    - An array of service endpoints.
                suboptions:
                    service:
                        description:
                            - The type of the endpoint service.
                    locations:
                        description:
                            - A list of locations.
                    provisioning_state:
                        description:
                            - The provisioning state of the resource.
            resource_navigation_links:
                description:
                    - Gets an array of references to the external resources using subnet.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    linked_resource_type:
                        description:
                            - Resource type of the linked resource.
                    link:
                        description:
                            - Link to the external resource
                    name:
                        description:
                            - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            provisioning_state:
                description:
                    - The provisioning state of the resource.
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    virtual_network_peerings:
        description:
            - A list of peerings in a Virtual Network.
        suboptions:
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
                    - "If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also
                       true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This f
                       lag cannot be set if virtual network already has a gateway."
            remote_virtual_network:
                description:
                    - "The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to
                       register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering)."
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
                    - The status of the virtual network peering. Possible values are C(Initiated), C(Connected), and C(Disconnected).
                choices: ['initiated', 'connected', 'disconnected']
            provisioning_state:
                description:
                    - The provisioning state of the resource.
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    resource_guid:
        description:
            - The resourceGuid property of the Virtual Network resource.
    provisioning_state:
        description:
            - The provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
    enable_ddos_protection:
        description:
            - Indicates if DDoS protection is enabled for all the protected resources in a Virtual Network.
    enable_vm_protection:
        description:
            - Indicates if Vm protection is enabled for all the subnets in a Virtual Network.
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
  - name: Create (or update) VirtualNetworks
    azure_rm_applicationgatewayvirtualnetwork:
      resource_group: rg1
      virtual_network_name: test-vnet
      location: eastus
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


class AzureRMVirtualNetworks(AzureRMModuleBase):
    """Configuration class for an Azure RM VirtualNetworks resource"""

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
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            address_space=dict(
                type='dict'
            ),
            dhcp_options=dict(
                type='dict'
            ),
            subnets=dict(
                type='list'
            ),
            virtual_network_peerings=dict(
                type='list'
            ),
            resource_guid=dict(
                type='str'
            ),
            provisioning_state=dict(
                type='str'
            ),
            enable_ddos_protection=dict(
                type='str'
            ),
            enable_vm_protection=dict(
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
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworks, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "address_space":
                    self.parameters["address_space"] = kwargs[key]
                elif key == "dhcp_options":
                    self.parameters["dhcp_options"] = kwargs[key]
                elif key == "subnets":
                    self.parameters["subnets"] = kwargs[key]
                elif key == "virtual_network_peerings":
                    ev = kwargs[key]
                    if 'peering_state' in ev:
                        if ev['peering_state'] == 'initiated':
                            ev['peering_state'] = 'Initiated'
                        elif ev['peering_state'] == 'connected':
                            ev['peering_state'] = 'Connected'
                        elif ev['peering_state'] == 'disconnected':
                            ev['peering_state'] = 'Disconnected'
                    self.parameters["virtual_network_peerings"] = ev
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "enable_ddos_protection":
                    self.parameters["enable_ddos_protection"] = kwargs[key]
                elif key == "enable_vm_protection":
                    self.parameters["enable_vm_protection"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_virtualnetworks()

        if not old_response:
            self.log("VirtualNetworks instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("VirtualNetworks instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if VirtualNetworks instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the VirtualNetworks instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_virtualnetworks()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("VirtualNetworks instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_virtualnetworks()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_virtualnetworks():
                time.sleep(20)
        else:
            self.log("VirtualNetworks instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_virtualnetworks(self):
        '''
        Creates or updates VirtualNetworks with the specified configuration.

        :return: deserialized VirtualNetworks instance state dictionary
        '''
        self.log("Creating / Updating the VirtualNetworks instance {0}".format(self.virtual_network_name))

        try:
            response = self.mgmt_client.virtual_networks.create_or_update(resource_group_name=self.resource_group,
                                                                          virtual_network_name=self.virtual_network_name,
                                                                          parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetworks instance.')
            self.fail("Error creating the VirtualNetworks instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_virtualnetworks(self):
        '''
        Deletes specified VirtualNetworks instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the VirtualNetworks instance {0}".format(self.virtual_network_name))
        try:
            response = self.mgmt_client.virtual_networks.delete(resource_group_name=self.resource_group,
                                                                virtual_network_name=self.virtual_network_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetworks instance.')
            self.fail("Error deleting the VirtualNetworks instance: {0}".format(str(e)))

        return True

    def get_virtualnetworks(self):
        '''
        Gets the properties of the specified VirtualNetworks.

        :return: deserialized VirtualNetworks instance state dictionary
        '''
        self.log("Checking if the VirtualNetworks instance {0} is present".format(self.virtual_network_name))
        found = False
        try:
            response = self.mgmt_client.virtual_networks.get(resource_group_name=self.resource_group,
                                                             virtual_network_name=self.virtual_network_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("VirtualNetworks instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualNetworks instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMVirtualNetworks()

if __name__ == '__main__':
    main()
