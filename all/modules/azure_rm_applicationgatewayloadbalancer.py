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
module: azure_rm_applicationgatewayloadbalancer
version_added: "2.5"
short_description: Manage LoadBalancers instance.
description:
    - Create, update and delete instance of LoadBalancers.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    sku:
        description:
            - The load balancer SKU.
        suboptions:
            name:
                description:
                    - Name of a load balancer SKU.
                choices: ['basic', 'standard']
    frontend_ip_configurations:
        description:
            - Object representing the frontend IPs to be used for the load balancer
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            private_ip_address:
                description:
                    - The private IP address of the IP configuration.
            private_ip_allocation_method:
                description:
                    - The Private IP allocation method. Possible values are: C(Static) and C(Dynamic).
                choices: ['static', 'dynamic']
            subnet:
                description:
                    - The reference of the subnet resource.
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
                                type: list
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
                                            - "The destination port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match al
                                               l ports."
                                    source_address_prefix:
                                        description:
                                            - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(Vir
                                               tualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies whe
                                               re network traffic originates from. "
                                    source_address_prefixes:
                                        description:
                                            - The CIDR or source IP ranges.
                                        type: list
                                    source_application_security_groups:
                                        description:
                                            - The application security group specified as source.
                                        type: list
                                    destination_address_prefix:
                                        description:
                                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all sourc
                                               e IPs. Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                                    destination_address_prefixes:
                                        description:
                                            - The destination address prefixes. CIDR or destination IP ranges.
                                        type: list
                                    destination_application_security_groups:
                                        description:
                                            - The application security group specified as destination.
                                        type: list
                                    source_port_ranges:
                                        description:
                                            - The source port ranges.
                                        type: list
                                    destination_port_ranges:
                                        description:
                                            - The destination port ranges.
                                        type: list
                                    access:
                                        description:
                                            - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny).
                                        required: True
                                        choices: ['allow', 'deny']
                                    priority:
                                        description:
                                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each r
                                               ule in the collection. The lower the priority number, the higher the priority of the rule."
                                    direction:
                                        description:
                                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic.
                                                Possible values are: C(Inbound) and C(Outbound)."
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
                                type: list
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
                                            - "The destination port or range. Integer or range between 0 and 65535. Asterix C(*) can also be used to match al
                                               l ports."
                                    source_address_prefix:
                                        description:
                                            - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(Vir
                                               tualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies whe
                                               re network traffic originates from. "
                                    source_address_prefixes:
                                        description:
                                            - The CIDR or source IP ranges.
                                        type: list
                                    source_application_security_groups:
                                        description:
                                            - The application security group specified as source.
                                        type: list
                                    destination_address_prefix:
                                        description:
                                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all sourc
                                               e IPs. Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                                    destination_address_prefixes:
                                        description:
                                            - The destination address prefixes. CIDR or destination IP ranges.
                                        type: list
                                    destination_application_security_groups:
                                        description:
                                            - The application security group specified as destination.
                                        type: list
                                    source_port_ranges:
                                        description:
                                            - The source port ranges.
                                        type: list
                                    destination_port_ranges:
                                        description:
                                            - The destination port ranges.
                                        type: list
                                    access:
                                        description:
                                            - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny).
                                        required: True
                                        choices: ['allow', 'deny']
                                    priority:
                                        description:
                                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each r
                                               ule in the collection. The lower the priority number, the higher the priority of the rule."
                                    direction:
                                        description:
                                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic.
                                                Possible values are: C(Inbound) and C(Outbound)."
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
                                type: list
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    address_prefix:
                                        description:
                                            - The destination CIDR to which the route applies.
                                    next_hop_type:
                                        description:
                                            - "The type of Azure hop the packet should be sent to. Possible values are: C(VirtualNetworkGateway), C(VnetLocal
                                               ), C(Internet), C(VirtualAppliance), and C(None)."
                                        required: True
                                        choices: ['virtual_network_gateway', 'vnet_local', 'internet', 'virtual_appliance', 'none']
                                    next_hop_ip_address:
                                        description:
                                            - "The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop t
                                               ype is VirtualAppliance."
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
                        type: list
                        suboptions:
                            service:
                                description:
                                    - The type of the endpoint service.
                            locations:
                                description:
                                    - A list of locations.
                                type: list
                            provisioning_state:
                                description:
                                    - The provisioning state of the resource.
                    resource_navigation_links:
                        description:
                            - Gets an array of references to the external resources using subnet.
                        type: list
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
            public_ip_address:
                description:
                    - The reference of the Public IP resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    location:
                        description:
                            - Resource location.
                    sku:
                        description:
                            - The public IP address SKU.
                        suboptions:
                            name:
                                description:
                                    - Name of a public IP address SKU.
                                choices: ['basic', 'standard']
                    public_ip_allocation_method:
                        description:
                            - The public IP allocation method. Possible values are: C(Static) and C(Dynamic).
                        choices: ['static', 'dynamic']
                    public_ip_address_version:
                        description:
                            - The public IP address version. Possible values are: C(IPv4) and C(IPv6).
                        choices: ['ipv4', 'ipv6']
                    dns_settings:
                        description:
                            - The FQDN of the DNS record associated with the public IP address.
                        suboptions:
                            domain_name_label:
                                description:
                                    - "Gets or sets the Domain name label.The concatenation of the domain name label and the regionalized DNS zone make up th
                                       e fully qualified domain name associated with the public IP address. If a domain name label is specified, an A DNS rec
                                       ord is created for the public IP in the Microsoft Azure DNS system."
                            fqdn:
                                description:
                                    - "Gets the FQDN, Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenatio
                                       n of the domainNameLabel and the regionalized DNS zone."
                            reverse_fqdn:
                                description:
                                    - "Gets or Sets the Reverse FQDN. A user-visible, fully qualified domain name that resolves to this public IP address. If
                                        the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domai
                                       n to the reverse FQDN. "
                    ip_address:
                        description:
                            - The IP address associated with the public IP address resource.
                    idle_timeout_in_minutes:
                        description:
                            - The idle timeout of the public IP address.
                    resource_guid:
                        description:
                            - The resource GUID property of the public IP resource.
                    provisioning_state:
                        description:
                            - The provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
                    zones:
                        description:
                            - A list of availability zones denoting the IP allocated for the resource needs to come from.
                        type: list
            provisioning_state:
                description:
                    - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            zones:
                description:
                    - A list of availability zones denoting the IP allocated for the resource needs to come from.
                type: list
    backend_address_pools:
        description:
            - Collection of backend address pools used by a load balancer
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            provisioning_state:
                description:
                    - Get provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    load_balancing_rules:
        description:
            - Object collection representing the load balancing rules Gets the provisioning
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            frontend_ip_configuration:
                description:
                    - A reference to frontend IP addresses.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            backend_address_pool:
                description:
                    - A reference to a pool of DIPs. Inbound traffic is randomly load balanced across IPs in the backend IPs.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            probe:
                description:
                    - The reference of the load balancer probe used by the load balancing rule.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            protocol:
                description:
                    - Possible values include: C(Udp), C(Tcp), C(All)
                required: True
                choices: ['udp', 'tcp', 'all']
            load_distribution:
                description:
                    - The load distribution policy for this rule. Possible values are C(Default), C(SourceIP), and C(SourceIPProtocol).
                choices: ['default', 'source_ip', 'source_ip_protocol']
            frontend_port:
                description:
                    - "The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values are between
                       0 and 65534. Note that value 0 enables 'Any Port'"
                required: True
            backend_port:
                description:
                    - "The port used for internal connections on the endpoint. Acceptable values are between 0 and 65535. Note that value 0 enables 'Any Port
                       '"
            idle_timeout_in_minutes:
                description:
                    - "The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element i
                       s only used when the protocol is set to TCP."
            enable_floating_ip:
                description:
                    - "Configures a virtual machineC(s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This
                       setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can)t be changed after you create the
                       endpoint."
            disable_outbound_snat:
                description:
                    - Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.
            provisioning_state:
                description:
                    - Gets the provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    probes:
        description:
            - Collection of probe objects used in the load balancer
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            protocol:
                description:
                    - "The protocol of the end point. Possible values are: C(Http) or C(Tcp). If C(Tcp) is specified, a received ACK is required for the prob
                       e to be successful. If C(Http) is specified, a 200 OK response from the specifies URI is required for the probe to be successful."
                required: True
                choices: ['http', 'tcp']
            port:
                description:
                    - The port for communicating the probe. Possible values range from 1 to 65535, inclusive.
                required: True
            interval_in_seconds:
                description:
                    - "The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than ha
                       lf the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default valu
                       e is 15, the minimum value is 5."
            number_of_probes:
                description:
                    - "The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values a
                       llows endpoints to be taken out of rotation faster or slower than the typical times used in Azure."
            request_path:
                description:
                    - "The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. Th
                       ere is no default value."
            provisioning_state:
                description:
                    - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    inbound_nat_rules:
        description:
            - "Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining
               an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machin
               es cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules."
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            frontend_ip_configuration:
                description:
                    - A reference to frontend IP addresses.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            protocol:
                description:
                    - Possible values include: C(Udp), C(Tcp), C(All)
                choices: ['udp', 'tcp', 'all']
            frontend_port:
                description:
                    - "The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1
                        to 65534."
            backend_port:
                description:
                    - The port used for the internal endpoint. Acceptable values range from 1 to 65535.
            idle_timeout_in_minutes:
                description:
                    - "The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element i
                       s only used when the protocol is set to TCP."
            enable_floating_ip:
                description:
                    - "Configures a virtual machineC(s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This
                       setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can)t be changed after you create the
                       endpoint."
            provisioning_state:
                description:
                    - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    inbound_nat_pools:
        description:
            - "Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created
                automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Loa
               d Balancer is mutually exclusive with defining inbound Nat rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that
               are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules."
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            frontend_ip_configuration:
                description:
                    - A reference to frontend IP addresses.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            protocol:
                description:
                    - Possible values include: C(Udp), C(Tcp), C(All)
                required: True
                choices: ['udp', 'tcp', 'all']
            frontend_port_range_start:
                description:
                    - "The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with a load balancer.
                        Acceptable values range between 1 and 65534."
                required: True
            frontend_port_range_end:
                description:
                    - "The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with a load balancer.
                       Acceptable values range between 1 and 65535."
                required: True
            backend_port:
                description:
                    - The port used for internal connections on the endpoint. Acceptable values are between 1 and 65535.
                required: True
            provisioning_state:
                description:
                    - Gets the provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    outbound_nat_rules:
        description:
            - The outbound NAT rules.
        type: list
        suboptions:
            id:
                description:
                    - Resource ID.
            allocated_outbound_ports:
                description:
                    - The number of outbound ports to be used for NAT.
            frontend_ip_configurations:
                description:
                    - The Frontend IP addresses of the load balancer.
                type: list
                suboptions:
                    id:
                        description:
                            - Resource ID.
            backend_address_pool:
                description:
                    - A reference to a pool of DIPs. Outbound traffic is randomly load balanced across IPs in the backend IPs.
                required: True
                suboptions:
                    id:
                        description:
                            - Resource ID.
            provisioning_state:
                description:
                    - Gets the provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    resource_guid:
        description:
            - The resource GUID property of the load balancer resource.
    provisioning_state:
        description:
            - Gets the provisioning state of the PublicIP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
    etag:
        description:
            - A unique read-only string that changes whenever the resource is updated.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) LoadBalancers
    azure_rm_applicationgatewayloadbalancer:
      resource_group: rg1
      load_balancer_name: lb
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


class AzureRMLoadBalancers(AzureRMModuleBase):
    """Configuration class for an Azure RM LoadBalancers resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            load_balancer_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            sku=dict(
                type='dict'
            ),
            frontend_ip_configurations=dict(
                type='list'
            ),
            backend_address_pools=dict(
                type='list'
            ),
            load_balancing_rules=dict(
                type='list'
            ),
            probes=dict(
                type='list'
            ),
            inbound_nat_rules=dict(
                type='list'
            ),
            inbound_nat_pools=dict(
                type='list'
            ),
            outbound_nat_rules=dict(
                type='list'
            ),
            resource_guid=dict(
                type='str'
            ),
            provisioning_state=dict(
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
        self.load_balancer_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLoadBalancers, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "sku":
                    ev = kwargs[key]
                    if 'name' in ev:
                        if ev['name'] == 'basic':
                            ev['name'] = 'Basic'
                        elif ev['name'] == 'standard':
                            ev['name'] = 'Standard'
                    self.parameters["sku"] = ev
                elif key == "frontend_ip_configurations":
                    ev = kwargs[key]
                    if 'private_ip_allocation_method' in ev:
                        if ev['private_ip_allocation_method'] == 'static':
                            ev['private_ip_allocation_method'] = 'Static'
                        elif ev['private_ip_allocation_method'] == 'dynamic':
                            ev['private_ip_allocation_method'] = 'Dynamic'
                    self.parameters["frontend_ip_configurations"] = ev
                elif key == "backend_address_pools":
                    self.parameters["backend_address_pools"] = kwargs[key]
                elif key == "load_balancing_rules":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'udp':
                            ev['protocol'] = 'Udp'
                        elif ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                        elif ev['protocol'] == 'all':
                            ev['protocol'] = 'All'
                    if 'load_distribution' in ev:
                        if ev['load_distribution'] == 'default':
                            ev['load_distribution'] = 'Default'
                        elif ev['load_distribution'] == 'source_ip':
                            ev['load_distribution'] = 'SourceIP'
                        elif ev['load_distribution'] == 'source_ip_protocol':
                            ev['load_distribution'] = 'SourceIPProtocol'
                    self.parameters["load_balancing_rules"] = ev
                elif key == "probes":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'http':
                            ev['protocol'] = 'Http'
                        elif ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                    self.parameters["probes"] = ev
                elif key == "inbound_nat_rules":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'udp':
                            ev['protocol'] = 'Udp'
                        elif ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                        elif ev['protocol'] == 'all':
                            ev['protocol'] = 'All'
                    self.parameters["inbound_nat_rules"] = ev
                elif key == "inbound_nat_pools":
                    ev = kwargs[key]
                    if 'protocol' in ev:
                        if ev['protocol'] == 'udp':
                            ev['protocol'] = 'Udp'
                        elif ev['protocol'] == 'tcp':
                            ev['protocol'] = 'Tcp'
                        elif ev['protocol'] == 'all':
                            ev['protocol'] = 'All'
                    self.parameters["inbound_nat_pools"] = ev
                elif key == "outbound_nat_rules":
                    self.parameters["outbound_nat_rules"] = kwargs[key]
                elif key == "resource_guid":
                    self.parameters["resource_guid"] = kwargs[key]
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "etag":
                    self.parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_loadbalancers()

        if not old_response:
            self.log("LoadBalancers instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("LoadBalancers instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if LoadBalancers instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the LoadBalancers instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_loadbalancers()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("LoadBalancers instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_loadbalancers()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_loadbalancers():
                time.sleep(20)
        else:
            self.log("LoadBalancers instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_loadbalancers(self):
        '''
        Creates or updates LoadBalancers with the specified configuration.

        :return: deserialized LoadBalancers instance state dictionary
        '''
        self.log("Creating / Updating the LoadBalancers instance {0}".format(self.load_balancer_name))

        try:
            response = self.mgmt_client.load_balancers.create_or_update(resource_group_name=self.resource_group,
                                                                        load_balancer_name=self.load_balancer_name,
                                                                        parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the LoadBalancers instance.')
            self.fail("Error creating the LoadBalancers instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_loadbalancers(self):
        '''
        Deletes specified LoadBalancers instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the LoadBalancers instance {0}".format(self.load_balancer_name))
        try:
            response = self.mgmt_client.load_balancers.delete(resource_group_name=self.resource_group,
                                                              load_balancer_name=self.load_balancer_name)
        except CloudError as e:
            self.log('Error attempting to delete the LoadBalancers instance.')
            self.fail("Error deleting the LoadBalancers instance: {0}".format(str(e)))

        return True

    def get_loadbalancers(self):
        '''
        Gets the properties of the specified LoadBalancers.

        :return: deserialized LoadBalancers instance state dictionary
        '''
        self.log("Checking if the LoadBalancers instance {0} is present".format(self.load_balancer_name))
        found = False
        try:
            response = self.mgmt_client.load_balancers.get(resource_group_name=self.resource_group,
                                                           load_balancer_name=self.load_balancer_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("LoadBalancers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the LoadBalancers instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMLoadBalancers()

if __name__ == '__main__':
    main()
