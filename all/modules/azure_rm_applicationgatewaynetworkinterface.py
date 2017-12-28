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
module: azure_rm_applicationgatewaynetworkinterface
version_added: "2.5"
short_description: Manage NetworkInterfaces instance.
description:
    - Create, update and delete instance of NetworkInterfaces.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_interface_name:
        description:
            - The name of the network interface.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    virtual_machine:
        description:
            - The reference of a virtual machine.
        suboptions:
            id:
                description:
                    - Resource ID.
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
                            - Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*). Possible values include: C(Tcp), C(Udp), C(*)
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
                            - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetwork), C(
                               AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traffic originates fr
                               om. "
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
                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. Default t
                               ags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
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
                            - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny). Possible values include: C(Allow), C(Deny)
                        required: True
                        choices: ['allow', 'deny']
                    priority:
                        description:
                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the colle
                               ction. The lower the priority number, the higher the priority of the rule."
                    direction:
                        description:
                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values
                                are: C(Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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
                            - Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*). Possible values include: C(Tcp), C(Udp), C(*)
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
                            - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetwork), C(
                               AzureLoadBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traffic originates fr
                               om. "
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
                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. Default t
                               ags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
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
                            - The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny). Possible values include: C(Allow), C(Deny)
                        required: True
                        choices: ['allow', 'deny']
                    priority:
                        description:
                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the colle
                               ction. The lower the priority number, the higher the priority of the rule."
                    direction:
                        description:
                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values
                                are: C(Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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
    ip_configurations:
        description:
            - A list of IPConfigurations of the network interface.
        suboptions:
            id:
                description:
                    - Resource ID.
            application_gateway_backend_address_pools:
                description:
                    - The reference of ApplicationGatewayBackendAddressPool resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    backend_ip_configurations:
                        description:
                            - Collection of references to IPs defined in network interfaces.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            application_gateway_backend_address_pools:
                                description:
                                    - The reference of ApplicationGatewayBackendAddressPool resource.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    backend_ip_configurations:
                                        description:
                                            - Collection of references to IPs defined in network interfaces.
                                    backend_addresses:
                                        description:
                                            - Backend addresses
                                    provisioning_state:
                                        description:
                                            - "Provisioning state of the backend address pool resource. Possible values are: C(Updating), C(Deleting), and C(
                                               Failed)."
                                    name:
                                        description:
                                            - Resource that is unique within a resource group. This name can be used to access the resource.
                                    etag:
                                        description:
                                            - A unique read-only string that changes whenever the resource is updated.
                                    type:
                                        description:
                                            - Type of the resource.
                            load_balancer_backend_address_pools:
                                description:
                                    - The reference of LoadBalancerBackendAddressPool resource.
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
                            load_balancer_inbound_nat_rules:
                                description:
                                    - A list of references of LoadBalancerInboundNatRules.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    frontend_ip_configuration:
                                        description:
                                            - A reference to frontend IP addresses.
                                    protocol:
                                        description:
                                            - Possible values include: C(Udp), C(Tcp), C(All)
                                        choices: ['udp', 'tcp', 'all']
                                    frontend_port:
                                        description:
                                            - "The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Accept
                                               able values range from 1 to 65534."
                                    backend_port:
                                        description:
                                            - The port used for the internal endpoint. Acceptable values range from 1 to 65535.
                                    idle_timeout_in_minutes:
                                        description:
                                            - "The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4
                                                minutes. This element is only used when the protocol is set to TCP."
                                    enable_floating_ip:
                                        description:
                                            - "Configures a virtual machineC(s endpoint for the floating IP capability required to configure a SQL AlwaysOn A
                                               vailability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. Thi
                                               s setting can)t be changed after you create the endpoint."
                                    provisioning_state:
                                        description:
                                            - "Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Fa
                                               iled)."
                                    name:
                                        description:
                                            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
                                    etag:
                                        description:
                                            - A unique read-only string that changes whenever the resource is updated.
                            private_ip_address:
                                description:
                                    - Private IP address of the IP configuration.
                            private_ip_allocation_method:
                                description:
                                    - "Defines how a private IP address is assigned. Possible values are: C(Static) and C(Dynamic). Possible values include:
                                       C(Static), C(Dynamic)"
                                choices: ['static', 'dynamic']
                            private_ip_address_version:
                                description:
                                    - "Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Def
                                       ault is taken as IPv4.  Possible values are: C(IPv4) and C(IPv6). Possible values include: C(IPv4), C(IPv6)"
                                choices: ['ipv4', 'ipv6']
                            subnet:
                                description:
                                    - Subnet bound to the IP configuration.
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
                                    route_table:
                                        description:
                                            - The reference of the RouteTable resource.
                                    service_endpoints:
                                        description:
                                            - An array of service endpoints.
                                    resource_navigation_links:
                                        description:
                                            - Gets an array of references to the external resources using subnet.
                                    provisioning_state:
                                        description:
                                            - The provisioning state of the resource.
                                    name:
                                        description:
                                            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                                    etag:
                                        description:
                                            - A unique read-only string that changes whenever the resource is updated.
                            primary:
                                description:
                                    - Gets whether this is a primary customer address on the network interface.
                            public_ip_address:
                                description:
                                    - Public IP address bound to the IP configuration.
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
                                    public_ip_allocation_method:
                                        description:
                                            - "The public IP allocation method. Possible values are: C(Static) and C(Dynamic). Possible values include: C(Sta
                                               tic), C(Dynamic)"
                                        choices: ['static', 'dynamic']
                                    public_ip_address_version:
                                        description:
                                            - The public IP address version. Possible values are: C(IPv4) and C(IPv6). Possible values include: C(IPv4), C(IPv6)
                                        choices: ['ipv4', 'ipv6']
                                    dns_settings:
                                        description:
                                            - The FQDN of the DNS record associated with the public IP address.
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
                            application_security_groups:
                                description:
                                    - Application security groups in which the IP configuration is included.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                            provisioning_state:
                                description:
                                    - "The provisioning state of the network interface IP configuration. Possible values are: C(Updating), C(Deleting), and C
                                       (Failed)."
                            name:
                                description:
                                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                            etag:
                                description:
                                    - A unique read-only string that changes whenever the resource is updated.
                    backend_addresses:
                        description:
                            - Backend addresses
                        suboptions:
                            fqdn:
                                description:
                                    - Fully qualified domain name (FQDN).
                            ip_address:
                                description:
                                    - IP address
                    provisioning_state:
                        description:
                            - Provisioning state of the backend address pool resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                    name:
                        description:
                            - Resource that is unique within a resource group. This name can be used to access the resource.
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
                    type:
                        description:
                            - Type of the resource.
            load_balancer_backend_address_pools:
                description:
                    - The reference of LoadBalancerBackendAddressPool resource.
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
            load_balancer_inbound_nat_rules:
                description:
                    - A list of references of LoadBalancerInboundNatRules.
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
                            - "The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values rang
                               e from 1 to 65534."
                    backend_port:
                        description:
                            - The port used for the internal endpoint. Acceptable values range from 1 to 65535.
                    idle_timeout_in_minutes:
                        description:
                            - "The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This e
                               lement is only used when the protocol is set to TCP."
                    enable_floating_ip:
                        description:
                            - "Configures a virtual machineC(s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Grou
                               p. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can)t be changed after
                                you create the endpoint."
                    provisioning_state:
                        description:
                            - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
                    name:
                        description:
                            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
            private_ip_address:
                description:
                    - Private IP address of the IP configuration.
            private_ip_allocation_method:
                description:
                    - "Defines how a private IP address is assigned. Possible values are: C(Static) and C(Dynamic). Possible values include: C(Static), C(Dyn
                       amic)"
                choices: ['static', 'dynamic']
            private_ip_address_version:
                description:
                    - "Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as
                        IPv4.  Possible values are: C(IPv4) and C(IPv6). Possible values include: C(IPv4), C(IPv6)"
                choices: ['ipv4', 'ipv6']
            subnet:
                description:
                    - Subnet bound to the IP configuration.
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
                                            - "Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*). Possible values include:
                                               C(Tcp), C(Udp), C(*)"
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
                                    source_application_security_groups:
                                        description:
                                            - The application security group specified as source.
                                    destination_address_prefix:
                                        description:
                                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all sourc
                                               e IPs. Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                                    destination_address_prefixes:
                                        description:
                                            - The destination address prefixes. CIDR or destination IP ranges.
                                    destination_application_security_groups:
                                        description:
                                            - The application security group specified as destination.
                                    source_port_ranges:
                                        description:
                                            - The source port ranges.
                                    destination_port_ranges:
                                        description:
                                            - The destination port ranges.
                                    access:
                                        description:
                                            - "The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny). Possible values include:
                                               C(Allow), C(Deny)"
                                        required: True
                                        choices: ['allow', 'deny']
                                    priority:
                                        description:
                                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each r
                                               ule in the collection. The lower the priority number, the higher the priority of the rule."
                                    direction:
                                        description:
                                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic.
                                                Possible values are: C(Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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
                                            - "Network protocol this rule applies to. Possible values are C(Tcp), C(Udp), and C(*). Possible values include:
                                               C(Tcp), C(Udp), C(*)"
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
                                    source_application_security_groups:
                                        description:
                                            - The application security group specified as source.
                                    destination_address_prefix:
                                        description:
                                            - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all sourc
                                               e IPs. Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
                                    destination_address_prefixes:
                                        description:
                                            - The destination address prefixes. CIDR or destination IP ranges.
                                    destination_application_security_groups:
                                        description:
                                            - The application security group specified as destination.
                                    source_port_ranges:
                                        description:
                                            - The source port ranges.
                                    destination_port_ranges:
                                        description:
                                            - The destination port ranges.
                                    access:
                                        description:
                                            - "The network traffic is allowed or denied. Possible values are: C(Allow) and C(Deny). Possible values include:
                                               C(Allow), C(Deny)"
                                        required: True
                                        choices: ['allow', 'deny']
                                    priority:
                                        description:
                                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each r
                                               ule in the collection. The lower the priority number, the higher the priority of the rule."
                                    direction:
                                        description:
                                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic.
                                                Possible values are: C(Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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
                                            - "The type of Azure hop the packet should be sent to. Possible values are: C(VirtualNetworkGateway), C(VnetLocal
                                               ), C(Internet), C(VirtualAppliance), and C(None). Possible values include: C(VirtualNetworkGateway), C(VnetLoc
                                               al), C(Internet), C(VirtualAppliance), C(None)"
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
            primary:
                description:
                    - Gets whether this is a primary customer address on the network interface.
            public_ip_address:
                description:
                    - Public IP address bound to the IP configuration.
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
                                    - Name of a public IP address SKU. Possible values include: C(Basic), C(Standard)
                                choices: ['basic', 'standard']
                    public_ip_allocation_method:
                        description:
                            - The public IP allocation method. Possible values are: C(Static) and C(Dynamic). Possible values include: C(Static), C(Dynamic)
                        choices: ['static', 'dynamic']
                    public_ip_address_version:
                        description:
                            - The public IP address version. Possible values are: C(IPv4) and C(IPv6). Possible values include: C(IPv4), C(IPv6)
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
            application_security_groups:
                description:
                    - Application security groups in which the IP configuration is included.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    location:
                        description:
                            - Resource location.
            provisioning_state:
                description:
                    - The provisioning state of the network interface IP configuration. Possible values are: C(Updating), C(Deleting), and C(Failed).
            name:
                description:
                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
    dns_settings:
        description:
            - The DNS settings in network interface.
        suboptions:
            dns_servers:
                description:
                    - "List of DNS servers IP addresses. Use C(AzureProvidedDNS) to switch to azure provided DNS resolution. C(AzureProvidedDNS) value cannot
                        be combined with other IPs, it must be the only value in dnsServers collection."
            applied_dns_servers:
                description:
                    - "If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that
                       are part of the Availability Set. This property is what is configured on each of those VMs."
            internal_dns_name_label:
                description:
                    - Relative DNS name for this NIC used for internal communications between VMs in the same virtual network.
            internal_fqdn:
                description:
                    - Fully qualified DNS name supporting internal communications between VMs in the same virtual network.
            internal_domain_name_suffix:
                description:
                    - "Even if internalDnsNameLabel is not specified, a DNS entry is created for the primary NIC of the VM. This DNS name can be constructed
                       by concatenating the VM name with the value of internalDomainNameSuffix."
    mac_address:
        description:
            - The MAC address of the network interface.
    primary:
        description:
            - Gets whether this is a primary network interface on a virtual machine.
    enable_accelerated_networking:
        description:
            - If the network interface is accelerated networking enabled.
    enable_ip_forwarding:
        description:
            - Indicates whether IP forwarding is enabled on this network interface.
    resource_guid:
        description:
            - The resource GUID property of the network interface resource.
    provisioning_state:
        description:
            - The provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
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
  - name: Create (or update) NetworkInterfaces
    azure_rm_applicationgatewaynetworkinterface:
      resource_group: rg1
      network_interface_name: test-nic
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


class AzureRMNetworkInterfaces(AzureRMModuleBase):
    """Configuration class for an Azure RM NetworkInterfaces resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_interface_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            virtual_machine=dict(
                type='dict'
            ),
            network_security_group=dict(
                type='dict'
            ),
            ip_configurations=dict(
                type='list'
            ),
            dns_settings=dict(
                type='dict'
            ),
            mac_address=dict(
                type='str'
            ),
            primary=dict(
                type='str'
            ),
            enable_accelerated_networking=dict(
                type='str'
            ),
            enable_ip_forwarding=dict(
                type='str'
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
        self.network_interface_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetworkInterfaces, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "virtual_machine":
                    self.parameters["virtual_machine"] = kwargs[key]
                elif key == "network_security_group":
                    self.parameters["network_security_group"] = kwargs[key]
                elif key == "ip_configurations":
                    self.parameters["ip_configurations"] = kwargs[key]
                elif key == "dns_settings":
                    self.parameters["dns_settings"] = kwargs[key]
                elif key == "mac_address":
                    self.parameters["mac_address"] = kwargs[key]
                elif key == "primary":
                    self.parameters["primary"] = kwargs[key]
                elif key == "enable_accelerated_networking":
                    self.parameters["enable_accelerated_networking"] = kwargs[key]
                elif key == "enable_ip_forwarding":
                    self.parameters["enable_ip_forwarding"] = kwargs[key]
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

        old_response = self.get_networkinterfaces()

        if not old_response:
            self.log("NetworkInterfaces instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("NetworkInterfaces instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if NetworkInterfaces instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the NetworkInterfaces instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_networkinterfaces()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("NetworkInterfaces instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_networkinterfaces()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_networkinterfaces():
                time.sleep(20)
        else:
            self.log("NetworkInterfaces instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_networkinterfaces(self):
        '''
        Creates or updates NetworkInterfaces with the specified configuration.

        :return: deserialized NetworkInterfaces instance state dictionary
        '''
        self.log("Creating / Updating the NetworkInterfaces instance {0}".format(self.network_interface_name))

        try:
            response = self.mgmt_client.network_interfaces.create_or_update(resource_group_name=self.resource_group,
                                                                            network_interface_name=self.network_interface_name,
                                                                            parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the NetworkInterfaces instance.')
            self.fail("Error creating the NetworkInterfaces instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_networkinterfaces(self):
        '''
        Deletes specified NetworkInterfaces instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the NetworkInterfaces instance {0}".format(self.network_interface_name))
        try:
            response = self.mgmt_client.network_interfaces.delete(resource_group_name=self.resource_group,
                                                                  network_interface_name=self.network_interface_name)
        except CloudError as e:
            self.log('Error attempting to delete the NetworkInterfaces instance.')
            self.fail("Error deleting the NetworkInterfaces instance: {0}".format(str(e)))

        return True

    def get_networkinterfaces(self):
        '''
        Gets the properties of the specified NetworkInterfaces.

        :return: deserialized NetworkInterfaces instance state dictionary
        '''
        self.log("Checking if the NetworkInterfaces instance {0} is present".format(self.network_interface_name))
        found = False
        try:
            response = self.mgmt_client.network_interfaces.get(resource_group_name=self.resource_group,
                                                               network_interface_name=self.network_interface_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkInterfaces instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkInterfaces instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMNetworkInterfaces()

if __name__ == '__main__':
    main()
