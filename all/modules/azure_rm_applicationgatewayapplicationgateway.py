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
module: azure_rm_applicationgatewayapplicationgateway
version_added: "2.5"
short_description: Manage ApplicationGateways instance
description:
    - Create, update and delete instance of ApplicationGateways

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    application_gateway_name:
        description:
            - The name of the application gateway.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    sku:
        description:
            - SKU of the application gateway resource.
        suboptions:
            name:
                description:
                    - "Name of an application gateway SKU. Possible values include: 'Standard_Small', 'Standard_Medium', 'Standard_Large', 'WAF_Medium', 'WAF
                       _Large'"
            tier:
                description:
                    - "Tier of an application gateway. Possible values include: 'Standard', 'WAF'"
            capacity:
                description:
                    - Capacity (instance count) of an application gateway.
    ssl_policy:
        description:
            - SSL policy of the application gateway resource.
        suboptions:
            disabled_ssl_protocols:
                description:
                    - Ssl protocols to be disabled on application gateway.
            policy_type:
                description:
                    - "Type of Ssl Policy. Possible values include: 'Predefined', 'Custom'"
            policy_name:
                description:
                    - "Name of Ssl predefined policy. Possible values include: 'AppGwSslPolicy20150501', 'AppGwSslPolicy20170401', 'AppGwSslPolicy20170401S'"
            cipher_suites:
                description:
                    - Ssl cipher suites to be enabled in the specified order to application gateway.
            min_protocol_version:
                description:
                    - "Minimum version of Ssl protocol to be supported on application gateway. Possible values include: 'TLSv1_0', 'TLSv1_1', 'TLSv1_2'"
    gateway_ip_configurations:
        description:
            - Subnets of application the gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            subnet:
                description:
                    - Reference of the subnet resource. A subnet from where application gateway gets its private address.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            provisioning_state:
                description:
                    - "Provisioning state of the application gateway subnet resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    authentication_certificates:
        description:
            - Authentication certificates of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            data:
                description:
                    - Certificate public data.
            provisioning_state:
                description:
                    - "Provisioning state of the authentication certificate resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    ssl_certificates:
        description:
            - SSL certificates of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            data:
                description:
                    - Base-64 encoded pfx certificate. Only applicable in PUT Request.
            password:
                description:
                    - Password for the pfx file specified in data. Only applicable in PUT request.
            public_cert_data:
                description:
                    - Base-64 encoded Public cert data corresponding to pfx specified in data. Only applicable in GET request.
            provisioning_state:
                description:
                    - "Provisioning state of the SSL certificate resource Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    frontend_ip_configurations:
        description:
            - Frontend IP addresses of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            private_ip_address:
                description:
                    - PrivateIPAddress of the network interface IP Configuration.
            private_ip_allocation_method:
                description:
                    - "PrivateIP allocation method. Possible values include: 'Static', 'Dynamic'"
            subnet:
                description:
                    - Reference of the subnet resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            public_ip_address:
                description:
                    - Reference of the PublicIP resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            provisioning_state:
                description:
                    - "Provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    frontend_ports:
        description:
            - Frontend ports of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            port:
                description:
                    - Frontend port
            provisioning_state:
                description:
                    - "Provisioning state of the frontend port resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    probes:
        description:
            - Probes of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            protocol:
                description:
                    - "Protocol. Possible values include: 'Http', 'Https'"
            host:
                description:
                    - Host name to send the probe to.
            path:
                description:
                    - "Relative path of probe. Valid path starts from '/'. Probe is sent to <Protocol>://<host>:<port><path>"
            interval:
                description:
                    - "The probing interval in seconds. This is the time interval between two consecutive probes. Acceptable values are from 1 second to 8640
                       0 seconds."
            timeout:
                description:
                    - "the probe timeout in seconds. Probe marked as failed if valid response is not received with this timeout period. Acceptable values are
                        from 1 second to 86400 seconds."
            unhealthy_threshold:
                description:
                    - "The probe retry count. Backend server is marked down after consecutive probe failure count reaches UnhealthyThreshold. Acceptable valu
                       es are from 1 second to 20."
            pick_host_name_from_backend_http_settings:
                description:
                    - Whether the host header should be picked from the backend http settings. Default value is false.
            min_servers:
                description:
                    - Minimum number of servers that are always marked healthy. Default value is 0.
            match:
                description:
                    - Criterion for classifying a healthy probe response.
                suboptions:
                    body:
                        description:
                            - Body that must be contained in the health response. Default value is empty.
                    status_codes:
                        description:
                            - Allowed ranges of healthy status codes. Default range of healthy status codes is 200-399.
            provisioning_state:
                description:
                    - "Provisioning state of the backend http settings resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    backend_address_pools:
        description:
            - Backend address pool of the application gateway resource.
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
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    application_gateway_backend_address_pools:
                                        description:
                                            - The reference of ApplicationGatewayBackendAddressPool resource.
                                    load_balancer_backend_address_pools:
                                        description:
                                            - The reference of LoadBalancerBackendAddressPool resource.
                                    load_balancer_inbound_nat_rules:
                                        description:
                                            - A list of references of LoadBalancerInboundNatRules.
                                    private_ip_address:
                                        description:
                                            - Private IP address of the IP configuration.
                                    private_ip_allocation_method:
                                        description:
                                            - "Defines how a private IP address is assigned. Possible values are: 'Static' and 'Dynamic'. Possible values inc
                                               lude: 'Static', 'Dynamic'"
                                    private_ip_address_version:
                                        description:
                                            - "Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or I
                                               Pv6. Default is taken as IPv4.  Possible values are: 'IPv4' and 'IPv6'. Possible values include: 'IPv4', 'IPv6
                                               '"
                                    subnet:
                                        description:
                                            - Subnet bound to the IP configuration.
                                    primary:
                                        description:
                                            - Gets whether this is a primary customer address on the network interface.
                                    public_ip_address:
                                        description:
                                            - Public IP address bound to the IP configuration.
                                    application_security_groups:
                                        description:
                                            - Application security groups in which the IP configuration is included.
                                    provisioning_state:
                                        description:
                                            - "The provisioning state of the network interface IP configuration. Possible values are: 'Updating', 'Deleting',
                                                and 'Failed'."
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
                                    - "Provisioning state of the backend address pool resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                                    - "Get provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                                    - "Possible values include: 'Udp', 'Tcp', 'All'"
                            frontend_port:
                                description:
                                    - "The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable val
                                       ues range from 1 to 65534."
                            backend_port:
                                description:
                                    - The port used for the internal endpoint. Acceptable values range from 1 to 65535.
                            idle_timeout_in_minutes:
                                description:
                                    - "The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes
                                       . This element is only used when the protocol is set to TCP."
                            enable_floating_ip:
                                description:
                                    - "Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availabili
                                       ty Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't b
                                       e changed after you create the endpoint."
                            provisioning_state:
                                description:
                                    - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                            - "Defines how a private IP address is assigned. Possible values are: 'Static' and 'Dynamic'. Possible values include: 'Static',
                               'Dynamic'"
                    private_ip_address_version:
                        description:
                            - "Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is
                               taken as IPv4.  Possible values are: 'IPv4' and 'IPv6'. Possible values include: 'IPv4', 'IPv6'"
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
                                    default_security_rules:
                                        description:
                                            - The default security rules of network security group.
                                    resource_guid:
                                        description:
                                            - The resource GUID property of the network security group resource.
                                    provisioning_state:
                                        description:
                                            - "The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                                    provisioning_state:
                                        description:
                                            - "The provisioning state of the resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                                            - "Name of a public IP address SKU. Possible values include: 'Basic', 'Standard'"
                            public_ip_allocation_method:
                                description:
                                    - "The public IP allocation method. Possible values are: 'Static' and 'Dynamic'. Possible values include: 'Static', 'Dyna
                                       mic'"
                            public_ip_address_version:
                                description:
                                    - "The public IP address version. Possible values are: 'IPv4' and 'IPv6'. Possible values include: 'IPv4', 'IPv6'"
                            dns_settings:
                                description:
                                    - The FQDN of the DNS record associated with the public IP address.
                                suboptions:
                                    domain_name_label:
                                        description:
                                            - "Gets or sets the Domain name label.The concatenation of the domain name label and the regionalized DNS zone ma
                                               ke up the fully qualified domain name associated with the public IP address. If a domain name label is specifi
                                               ed, an A DNS record is created for the public IP in the Microsoft Azure DNS system."
                                    fqdn:
                                        description:
                                            - "Gets the FQDN, Fully qualified domain name of the A DNS record associated with the public IP. This is the conc
                                               atenation of the domainNameLabel and the regionalized DNS zone."
                                    reverse_fqdn:
                                        description:
                                            - "Gets or Sets the Reverse FQDN. A user-visible, fully qualified domain name that resolves to this public IP add
                                               ress. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in
                                               -addr.arpa domain to the reverse FQDN. "
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
                                    - "The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                            - "The provisioning state of the network interface IP configuration. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                    - "Provisioning state of the backend address pool resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    backend_http_settings_collection:
        description:
            - Backend http settings of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            port:
                description:
                    - Port
            protocol:
                description:
                    - "Protocol. Possible values include: 'Http', 'Https'"
            cookie_based_affinity:
                description:
                    - "Cookie based affinity. Possible values include: 'Enabled', 'Disabled'"
            request_timeout:
                description:
                    - "Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable va
                       lues are from 1 second to 86400 seconds."
            probe:
                description:
                    - Probe resource of an application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            authentication_certificates:
                description:
                    - Array of references to application gateway authentication certificates.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            connection_draining:
                description:
                    - Connection draining of the backend http settings resource.
                suboptions:
                    enabled:
                        description:
                            - Whether connection draining is enabled or not.
                        required: True
                    drain_timeout_in_sec:
                        description:
                            - The number of seconds connection draining is active. Acceptable values are from 1 second to 3600 seconds.
                        required: True
            host_name:
                description:
                    - Host header to be sent to the backend servers.
            pick_host_name_from_backend_address:
                description:
                    - Whether to pick host header should be picked from the host name of the backend server. Default value is false.
            affinity_cookie_name:
                description:
                    - Cookie name to use for the affinity cookie.
            probe_enabled:
                description:
                    - Whether the probe is enabled. Default value is false.
            path:
                description:
                    - Path which should be used as a prefix for all HTTP requests. Null means no path will be prefixed. Default value is null.
            provisioning_state:
                description:
                    - "Provisioning state of the backend http settings resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    http_listeners:
        description:
            - Http listeners of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            frontend_ip_configuration:
                description:
                    - Frontend IP configuration resource of an application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            frontend_port:
                description:
                    - Frontend port resource of an application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            protocol:
                description:
                    - "Protocol. Possible values include: 'Http', 'Https'"
            host_name:
                description:
                    - Host name of HTTP listener.
            ssl_certificate:
                description:
                    - SSL certificate resource of an application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            require_server_name_indication:
                description:
                    - Applicable only if protocol is https. Enables SNI for multi-hosting.
            provisioning_state:
                description:
                    - "Provisioning state of the HTTP listener resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    url_path_maps:
        description:
            - URL path map of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            default_backend_address_pool:
                description:
                    - Default backend address pool resource of URL path map.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            default_backend_http_settings:
                description:
                    - Default backend http settings resource of URL path map.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            default_redirect_configuration:
                description:
                    - Default redirect configuration resource of URL path map.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            path_rules:
                description:
                    - Path rule of URL path map resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    paths:
                        description:
                            - Path rules of URL path map.
                    backend_address_pool:
                        description:
                            - Backend address pool resource of URL path map path rule.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                    backend_http_settings:
                        description:
                            - Backend http settings resource of URL path map path rule.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                    redirect_configuration:
                        description:
                            - Redirect configuration resource of URL path map path rule.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                    provisioning_state:
                        description:
                            - "Path rule of URL path map resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
                    name:
                        description:
                            - Name of the resource that is unique within a resource group. This name can be used to access the resource.
                    etag:
                        description:
                            - A unique read-only string that changes whenever the resource is updated.
                    type:
                        description:
                            - Type of the resource.
            provisioning_state:
                description:
                    - "Provisioning state of the backend http settings resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    request_routing_rules:
        description:
            - Request routing rules of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            rule_type:
                description:
                    - "Rule type. Possible values include: 'Basic', 'PathBasedRouting'"
            backend_address_pool:
                description:
                    - Backend address pool resource of the application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            backend_http_settings:
                description:
                    - Frontend port resource of the application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            http_listener:
                description:
                    - Http listener resource of the application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            url_path_map:
                description:
                    - URL path map resource of the application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            redirect_configuration:
                description:
                    - Redirect configuration resource of the application gateway.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            provisioning_state:
                description:
                    - "Provisioning state of the request routing rule resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    redirect_configurations:
        description:
            - Redirect configurations of the application gateway resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            redirect_type:
                description:
                    - "Supported http redirection types - Permanent, Temporary, Found, SeeOther. Possible values include: 'Permanent', 'Found', 'SeeOther', '
                       Temporary'"
            target_listener:
                description:
                    - Reference to a listener to redirect the request to.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            target_url:
                description:
                    - Url to redirect the request to.
            include_path:
                description:
                    - Include path in the redirected url.
            include_query_string:
                description:
                    - Include query string in the redirected url.
            request_routing_rules:
                description:
                    - Request routing specifying redirect configuration.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            url_path_maps:
                description:
                    - Url path maps specifying default redirect configuration.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            path_rules:
                description:
                    - Path rules specifying redirect configuration.
                suboptions:
                    id:
                        description:
                            - Resource ID.
            name:
                description:
                    - Name of the resource that is unique within a resource group. This name can be used to access the resource.
            etag:
                description:
                    - A unique read-only string that changes whenever the resource is updated.
            type:
                description:
                    - Type of the resource.
    web_application_firewall_configuration:
        description:
            - Web application firewall configuration.
        suboptions:
            enabled:
                description:
                    - Whether the web application firewall is enabled or not.
                required: True
            firewall_mode:
                description:
                    - "Web application firewall mode. Possible values include: 'Detection', 'Prevention'"
                required: True
            rule_set_type:
                description:
                    - "The type of the web application firewall rule set. Possible values are: 'OWASP'."
                required: True
            rule_set_version:
                description:
                    - The version of the rule set type.
                required: True
            disabled_rule_groups:
                description:
                    - The disabled rule groups.
                suboptions:
                    rule_group_name:
                        description:
                            - The name of the rule group that will be disabled.
                        required: True
                    rules:
                        description:
                            - The list of rules that will be disabled. If null, all rules of the rule group will be disabled.
    resource_guid:
        description:
            - Resource GUID property of the application gateway resource.
    provisioning_state:
        description:
            - "Provisioning state of the application gateway resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
  - name: Create (or update) ApplicationGateways
    azure_rm_applicationgatewayapplicationgateway:
      resource_group: resource_group_name
      application_gateway_name: application_gateway_name
      id: id
      location: location
      sku:
        name: name
        tier: tier
        capacity: capacity
      ssl_policy:
        disabled_ssl_protocols:
          - XXXX - list of values -- not implemented str
        policy_type: policy_type
        policy_name: policy_name
        cipher_suites:
          - XXXX - list of values -- not implemented str
        min_protocol_version: min_protocol_version
      gateway_ip_configurations:
        - id: id
          subnet:
            id: id
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      authentication_certificates:
        - id: id
          data: data
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      ssl_certificates:
        - id: id
          data: data
          password: password
          public_cert_data: public_cert_data
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      frontend_ip_configurations:
        - id: id
          private_ip_address: private_ip_address
          private_ip_allocation_method: private_ip_allocation_method
          subnet:
            id: id
          public_ip_address:
            id: id
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      frontend_ports:
        - id: id
          port: port
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      probes:
        - id: id
          protocol: protocol
          host: host
          path: path
          interval: interval
          timeout: timeout
          unhealthy_threshold: unhealthy_threshold
          pick_host_name_from_backend_http_settings: pick_host_name_from_backend_http_settings
          min_servers: min_servers
          match:
            body: body
            status_codes:
              - XXXX - list of values -- not implemented str
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      backend_address_pools:
        - id: id
          backend_ip_configurations:
            - id: id
              application_gateway_backend_address_pools:
                - id: id
                  backend_ip_configurations:
                    - id: id
                      application_gateway_backend_address_pools:
                      load_balancer_backend_address_pools:
                      load_balancer_inbound_nat_rules:
                      private_ip_address: private_ip_address
                      private_ip_allocation_method: private_ip_allocation_method
                      private_ip_address_version: private_ip_address_version
                      subnet: subnet
                      primary: primary
                      public_ip_address: public_ip_address
                      application_security_groups:
                      provisioning_state: provisioning_state
                      name: name
                      etag: etag
                  backend_addresses:
                    - fqdn: fqdn
                      ip_address: ip_address
                  provisioning_state: provisioning_state
                  name: name
                  etag: etag
                  type: type
              load_balancer_backend_address_pools:
                - id: id
                  provisioning_state: provisioning_state
                  name: name
                  etag: etag
              load_balancer_inbound_nat_rules:
                - id: id
                  frontend_ip_configuration:
                    id: id
                  protocol: protocol
                  frontend_port: frontend_port
                  backend_port: backend_port
                  idle_timeout_in_minutes: idle_timeout_in_minutes
                  enable_floating_ip: enable_floating_ip
                  provisioning_state: provisioning_state
                  name: name
                  etag: etag
              private_ip_address: private_ip_address
              private_ip_allocation_method: private_ip_allocation_method
              private_ip_address_version: private_ip_address_version
              subnet:
                id: id
                address_prefix: address_prefix
                network_security_group:
                  id: id
                  location: location
                  security_rules:
                  default_security_rules:
                  resource_guid: resource_guid
                  provisioning_state: provisioning_state
                  etag: etag
                route_table:
                  id: id
                  location: location
                  routes:
                  provisioning_state: provisioning_state
                  etag: etag
                service_endpoints:
                  - service: service
                    locations:
                      - XXXX - list of values -- not implemented str
                    provisioning_state: provisioning_state
                resource_navigation_links:
                  - id: id
                    linked_resource_type: linked_resource_type
                    link: link
                    name: name
                provisioning_state: provisioning_state
                name: name
                etag: etag
              primary: primary
              public_ip_address:
                id: id
                location: location
                sku:
                  name: name
                public_ip_allocation_method: public_ip_allocation_method
                public_ip_address_version: public_ip_address_version
                dns_settings:
                  domain_name_label: domain_name_label
                  fqdn: fqdn
                  reverse_fqdn: reverse_fqdn
                ip_address: ip_address
                idle_timeout_in_minutes: idle_timeout_in_minutes
                resource_guid: resource_guid
                provisioning_state: provisioning_state
                etag: etag
                zones:
                  - XXXX - list of values -- not implemented str
              application_security_groups:
                - id: id
                  location: location
              provisioning_state: provisioning_state
              name: name
              etag: etag
          backend_addresses:
            - fqdn: fqdn
              ip_address: ip_address
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      backend_http_settings_collection:
        - id: id
          port: port
          protocol: protocol
          cookie_based_affinity: cookie_based_affinity
          request_timeout: request_timeout
          probe:
            id: id
          authentication_certificates:
            - id: id
          connection_draining:
            enabled: enabled
            drain_timeout_in_sec: drain_timeout_in_sec
          host_name: host_name
          pick_host_name_from_backend_address: pick_host_name_from_backend_address
          affinity_cookie_name: affinity_cookie_name
          probe_enabled: probe_enabled
          path: path
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      http_listeners:
        - id: id
          frontend_ip_configuration:
            id: id
          frontend_port:
            id: id
          protocol: protocol
          host_name: host_name
          ssl_certificate:
            id: id
          require_server_name_indication: require_server_name_indication
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      url_path_maps:
        - id: id
          default_backend_address_pool:
            id: id
          default_backend_http_settings:
            id: id
          default_redirect_configuration:
            id: id
          path_rules:
            - id: id
              paths:
                - XXXX - list of values -- not implemented str
              backend_address_pool:
                id: id
              backend_http_settings:
                id: id
              redirect_configuration:
                id: id
              provisioning_state: provisioning_state
              name: name
              etag: etag
              type: type
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      request_routing_rules:
        - id: id
          rule_type: rule_type
          backend_address_pool:
            id: id
          backend_http_settings:
            id: id
          http_listener:
            id: id
          url_path_map:
            id: id
          redirect_configuration:
            id: id
          provisioning_state: provisioning_state
          name: name
          etag: etag
          type: type
      redirect_configurations:
        - id: id
          redirect_type: redirect_type
          target_listener:
            id: id
          target_url: target_url
          include_path: include_path
          include_query_string: include_query_string
          request_routing_rules:
            - id: id
          url_path_maps:
            - id: id
          path_rules:
            - id: id
          name: name
          etag: etag
          type: type
      web_application_firewall_configuration:
        enabled: enabled
        firewall_mode: firewall_mode
        rule_set_type: rule_set_type
        rule_set_version: rule_set_version
        disabled_rule_groups:
          - rule_group_name: rule_group_name
            rules:
              - XXXX - list of values -- not implemented int
      resource_guid: resource_guid
      provisioning_state: provisioning_state
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


class AzureRMApplicationGateways(AzureRMModuleBase):
    """Configuration class for an Azure RM ApplicationGateways resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            application_gateway_name=dict(
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
            sku=dict(
                type='dict',
                required=False
            ),
            ssl_policy=dict(
                type='dict',
                required=False
            ),
            gateway_ip_configurations=dict(
                type='list',
                required=False
            ),
            authentication_certificates=dict(
                type='list',
                required=False
            ),
            ssl_certificates=dict(
                type='list',
                required=False
            ),
            frontend_ip_configurations=dict(
                type='list',
                required=False
            ),
            frontend_ports=dict(
                type='list',
                required=False
            ),
            probes=dict(
                type='list',
                required=False
            ),
            backend_address_pools=dict(
                type='list',
                required=False
            ),
            backend_http_settings_collection=dict(
                type='list',
                required=False
            ),
            http_listeners=dict(
                type='list',
                required=False
            ),
            url_path_maps=dict(
                type='list',
                required=False
            ),
            request_routing_rules=dict(
                type='list',
                required=False
            ),
            redirect_configurations=dict(
                type='list',
                required=False
            ),
            web_application_firewall_configuration=dict(
                type='dict',
                required=False
            ),
            resource_guid=dict(
                type='str',
                required=False
            ),
            provisioning_state=dict(
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
        self.application_gateway_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplicationGateways, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                         supports_check_mode=True,
                                                         supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters.update({"id": kwargs[key]})
                elif key == "location":
                    self.parameters.update({"location": kwargs[key]})
                elif key == "sku":
                    self.parameters.update({"sku": kwargs[key]})
                elif key == "ssl_policy":
                    self.parameters.update({"ssl_policy": kwargs[key]})
                elif key == "gateway_ip_configurations":
                    self.parameters.update({"gateway_ip_configurations": kwargs[key]})
                elif key == "authentication_certificates":
                    self.parameters.update({"authentication_certificates": kwargs[key]})
                elif key == "ssl_certificates":
                    self.parameters.update({"ssl_certificates": kwargs[key]})
                elif key == "frontend_ip_configurations":
                    self.parameters.update({"frontend_ip_configurations": kwargs[key]})
                elif key == "frontend_ports":
                    self.parameters.update({"frontend_ports": kwargs[key]})
                elif key == "probes":
                    self.parameters.update({"probes": kwargs[key]})
                elif key == "backend_address_pools":
                    self.parameters.update({"backend_address_pools": kwargs[key]})
                elif key == "backend_http_settings_collection":
                    self.parameters.update({"backend_http_settings_collection": kwargs[key]})
                elif key == "http_listeners":
                    self.parameters.update({"http_listeners": kwargs[key]})
                elif key == "url_path_maps":
                    self.parameters.update({"url_path_maps": kwargs[key]})
                elif key == "request_routing_rules":
                    self.parameters.update({"request_routing_rules": kwargs[key]})
                elif key == "redirect_configurations":
                    self.parameters.update({"redirect_configurations": kwargs[key]})
                elif key == "web_application_firewall_configuration":
                    self.parameters.update({"web_application_firewall_configuration": kwargs[key]})
                elif key == "resource_guid":
                    self.parameters.update({"resource_guid": kwargs[key]})
                elif key == "provisioning_state":
                    self.parameters.update({"provisioning_state": kwargs[key]})
                elif key == "etag":
                    self.parameters.update({"etag": kwargs[key]})

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_applicationgateways()

        if not old_response:
            self.log("ApplicationGateways instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ApplicationGateways instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ApplicationGateways instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ApplicationGateways instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_applicationgateways()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ApplicationGateways instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_applicationgateways()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_applicationgateways():
                time.sleep(20)
        else:
            self.log("ApplicationGateways instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_applicationgateways(self):
        '''
        Creates or updates ApplicationGateways with the specified configuration.

        :return: deserialized ApplicationGateways instance state dictionary
        '''
        self.log("Creating / Updating the ApplicationGateways instance {0}".format(self.application_gateway_name))

        try:
            response = self.mgmt_client.application_gateways.create_or_update(self.resource_group,
                                                                              self.application_gateway_name,
                                                                              self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ApplicationGateways instance.')
            self.fail("Error creating the ApplicationGateways instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_applicationgateways(self):
        '''
        Deletes specified ApplicationGateways instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ApplicationGateways instance {0}".format(self.application_gateway_name))
        try:
            response = self.mgmt_client.application_gateways.delete(self.resource_group,
                                                                    self.application_gateway_name)
        except CloudError as e:
            self.log('Error attempting to delete the ApplicationGateways instance.')
            self.fail("Error deleting the ApplicationGateways instance: {0}".format(str(e)))

        return True

    def get_applicationgateways(self):
        '''
        Gets the properties of the specified ApplicationGateways.

        :return: deserialized ApplicationGateways instance state dictionary
        '''
        self.log("Checking if the ApplicationGateways instance {0} is present".format(self.application_gateway_name))
        found = False
        try:
            response = self.mgmt_client.application_gateways.get(self.resource_group,
                                                                 self.application_gateway_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ApplicationGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApplicationGateways instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMApplicationGateways()

if __name__ == '__main__':
    main()
