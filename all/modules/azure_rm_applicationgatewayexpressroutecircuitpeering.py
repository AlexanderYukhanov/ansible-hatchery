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
module: azure_rm_applicationgatewayexpressroutecircuitpeering
version_added: "2.5"
short_description: Manage ExpressRouteCircuitPeerings instance
description:
    - Create, update and delete instance of ExpressRouteCircuitPeerings

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    circuit_name:
        description:
            - The name of the express route circuit.
        required: True
    peering_name:
        description:
            - The name of the peering.
        required: True
    id:
        description:
            - Resource ID.
    peering_type:
        description:
            - "The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'. Possible values include: 'AzurePubl
               icPeering', 'AzurePrivatePeering', 'MicrosoftPeering'"
    state:
        description:
            - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
    azure_asn:
        description:
            - The Azure ASN.
    peer_asn:
        description:
            - The peer ASN.
    primary_peer_address_prefix:
        description:
            - The primary address prefix.
    secondary_peer_address_prefix:
        description:
            - The secondary address prefix.
    primary_azure_port:
        description:
            - The primary port.
    secondary_azure_port:
        description:
            - The secondary port.
    shared_key:
        description:
            - The shared key.
    vlan_id:
        description:
            - The VLAN ID.
    microsoft_peering_config:
        description:
            - The Microsoft peering configuration.
        suboptions:
            advertised_public_prefixes:
                description:
                    - The reference of AdvertisedPublicPrefixes.
            advertised_communities:
                description:
                    - The communities of bgp peering. Spepcified for microsoft peering
            advertised_public_prefixes_state:
                description:
                    - "AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Configured', and 'Validation
                       Needed'. Possible values include: 'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'"
            legacy_mode:
                description:
                    - The legacy mode of the peering.
            customer_asn:
                description:
                    - The CustomerASN of the peering.
            routing_registry_name:
                description:
                    - The RoutingRegistryName of the configuration.
    stats:
        description:
            - Gets peering stats.
        suboptions:
            primarybytes_in:
                description:
                    - Gets BytesIn of the peering.
            primarybytes_out:
                description:
                    - Gets BytesOut of the peering.
            secondarybytes_in:
                description:
                    - Gets BytesIn of the peering.
            secondarybytes_out:
                description:
                    - Gets BytesOut of the peering.
    provisioning_state:
        description:
            - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
    gateway_manager_etag:
        description:
            - The GatewayManager Etag.
    last_modified_by:
        description:
            - Gets whether the provider or the customer last modified the peering.
    route_filter:
        description:
            - The reference of the RouteFilter resource.
        suboptions:
            id:
                description:
                    - Resource ID.
            location:
                description:
                    - Resource location.
            rules:
                description:
                    - Collection of RouteFilterRules contained within a route filter.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    access:
                        description:
                            - "The access type of the rule. Valid values are: 'Allow', 'Deny'. Possible values include: 'Allow', 'Deny'"
                        required: True
                    route_filter_rule_type:
                        description:
                            - "The rule type of the rule. Valid value is: 'Community'"
                        required: True
                    communities:
                        description:
                            - "The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']"
                        required: True
                    name:
                        description:
                            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                    location:
                        description:
                            - Resource location.
            peerings:
                description:
                    - A collection of references to express route circuit peerings.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    peering_type:
                        description:
                            - "The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'. Possible values inc
                               lude: 'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'"
                    state:
                        description:
                            - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
                    azure_asn:
                        description:
                            - The Azure ASN.
                    peer_asn:
                        description:
                            - The peer ASN.
                    primary_peer_address_prefix:
                        description:
                            - The primary address prefix.
                    secondary_peer_address_prefix:
                        description:
                            - The secondary address prefix.
                    primary_azure_port:
                        description:
                            - The primary port.
                    secondary_azure_port:
                        description:
                            - The secondary port.
                    shared_key:
                        description:
                            - The shared key.
                    vlan_id:
                        description:
                            - The VLAN ID.
                    microsoft_peering_config:
                        description:
                            - The Microsoft peering configuration.
                        suboptions:
                            advertised_public_prefixes:
                                description:
                                    - The reference of AdvertisedPublicPrefixes.
                            advertised_communities:
                                description:
                                    - The communities of bgp peering. Spepcified for microsoft peering
                            advertised_public_prefixes_state:
                                description:
                                    - "AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Configured',
                                        and 'ValidationNeeded'. Possible values include: 'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'"
                            legacy_mode:
                                description:
                                    - The legacy mode of the peering.
                            customer_asn:
                                description:
                                    - The CustomerASN of the peering.
                            routing_registry_name:
                                description:
                                    - The RoutingRegistryName of the configuration.
                    stats:
                        description:
                            - Gets peering stats.
                        suboptions:
                            primarybytes_in:
                                description:
                                    - Gets BytesIn of the peering.
                            primarybytes_out:
                                description:
                                    - Gets BytesOut of the peering.
                            secondarybytes_in:
                                description:
                                    - Gets BytesIn of the peering.
                            secondarybytes_out:
                                description:
                                    - Gets BytesOut of the peering.
                    provisioning_state:
                        description:
                            - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
                    gateway_manager_etag:
                        description:
                            - The GatewayManager Etag.
                    last_modified_by:
                        description:
                            - Gets whether the provider or the customer last modified the peering.
                    route_filter:
                        description:
                            - The reference of the RouteFilter resource.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            location:
                                description:
                                    - Resource location.
                            rules:
                                description:
                                    - Collection of RouteFilterRules contained within a route filter.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    access:
                                        description:
                                            - "The access type of the rule. Valid values are: 'Allow', 'Deny'. Possible values include: 'Allow', 'Deny'"
                                        required: True
                                    route_filter_rule_type:
                                        description:
                                            - "The rule type of the rule. Valid value is: 'Community'"
                                        required: True
                                    communities:
                                        description:
                                            - "The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']"
                                        required: True
                                    name:
                                        description:
                                            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                                    location:
                                        description:
                                            - Resource location.
                            peerings:
                                description:
                                    - A collection of references to express route circuit peerings.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    peering_type:
                                        description:
                                            - "The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'. Pos
                                               sible values include: 'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'"
                                    state:
                                        description:
                                            - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Ena
                                               bled'"
                                    azure_asn:
                                        description:
                                            - The Azure ASN.
                                    peer_asn:
                                        description:
                                            - The peer ASN.
                                    primary_peer_address_prefix:
                                        description:
                                            - The primary address prefix.
                                    secondary_peer_address_prefix:
                                        description:
                                            - The secondary address prefix.
                                    primary_azure_port:
                                        description:
                                            - The primary port.
                                    secondary_azure_port:
                                        description:
                                            - The secondary port.
                                    shared_key:
                                        description:
                                            - The shared key.
                                    vlan_id:
                                        description:
                                            - The VLAN ID.
                                    microsoft_peering_config:
                                        description:
                                            - The Microsoft peering configuration.
                                    stats:
                                        description:
                                            - Gets peering stats.
                                    provisioning_state:
                                        description:
                                            - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Faile
                                               d'."
                                    gateway_manager_etag:
                                        description:
                                            - The GatewayManager Etag.
                                    last_modified_by:
                                        description:
                                            - Gets whether the provider or the customer last modified the peering.
                                    route_filter:
                                        description:
                                            - The reference of the RouteFilter resource.
                                    ipv6_peering_config:
                                        description:
                                            - The IPv6 peering configuration.
                                    name:
                                        description:
                                            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
                    ipv6_peering_config:
                        description:
                            - The IPv6 peering configuration.
                        suboptions:
                            primary_peer_address_prefix:
                                description:
                                    - The primary address prefix.
                            secondary_peer_address_prefix:
                                description:
                                    - The secondary address prefix.
                            microsoft_peering_config:
                                description:
                                    - The Microsoft peering configuration.
                                suboptions:
                                    advertised_public_prefixes:
                                        description:
                                            - The reference of AdvertisedPublicPrefixes.
                                    advertised_communities:
                                        description:
                                            - The communities of bgp peering. Spepcified for microsoft peering
                                    advertised_public_prefixes_state:
                                        description:
                                            - "AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Conf
                                               igured', and 'ValidationNeeded'. Possible values include: 'NotConfigured', 'Configuring', 'Configured', 'Valid
                                               ationNeeded'"
                                    legacy_mode:
                                        description:
                                            - The legacy mode of the peering.
                                    customer_asn:
                                        description:
                                            - The CustomerASN of the peering.
                                    routing_registry_name:
                                        description:
                                            - The RoutingRegistryName of the configuration.
                            route_filter:
                                description:
                                    - The reference of the RouteFilter resource.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                                    rules:
                                        description:
                                            - Collection of RouteFilterRules contained within a route filter.
                                    peerings:
                                        description:
                                            - A collection of references to express route circuit peerings.
                            state:
                                description:
                                    - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
                    name:
                        description:
                            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
    ipv6_peering_config:
        description:
            - The IPv6 peering configuration.
        suboptions:
            primary_peer_address_prefix:
                description:
                    - The primary address prefix.
            secondary_peer_address_prefix:
                description:
                    - The secondary address prefix.
            microsoft_peering_config:
                description:
                    - The Microsoft peering configuration.
                suboptions:
                    advertised_public_prefixes:
                        description:
                            - The reference of AdvertisedPublicPrefixes.
                    advertised_communities:
                        description:
                            - The communities of bgp peering. Spepcified for microsoft peering
                    advertised_public_prefixes_state:
                        description:
                            - "AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Configured', and 'Va
                               lidationNeeded'. Possible values include: 'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'"
                    legacy_mode:
                        description:
                            - The legacy mode of the peering.
                    customer_asn:
                        description:
                            - The CustomerASN of the peering.
                    routing_registry_name:
                        description:
                            - The RoutingRegistryName of the configuration.
            route_filter:
                description:
                    - The reference of the RouteFilter resource.
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    location:
                        description:
                            - Resource location.
                    rules:
                        description:
                            - Collection of RouteFilterRules contained within a route filter.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            access:
                                description:
                                    - "The access type of the rule. Valid values are: 'Allow', 'Deny'. Possible values include: 'Allow', 'Deny'"
                                required: True
                            route_filter_rule_type:
                                description:
                                    - "The rule type of the rule. Valid value is: 'Community'"
                                required: True
                            communities:
                                description:
                                    - "The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']"
                                required: True
                            name:
                                description:
                                    - The name of the resource that is unique within a resource group. This name can be used to access the resource.
                            location:
                                description:
                                    - Resource location.
                    peerings:
                        description:
                            - A collection of references to express route circuit peerings.
                        suboptions:
                            id:
                                description:
                                    - Resource ID.
                            peering_type:
                                description:
                                    - "The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'. Possible va
                                       lues include: 'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'"
                            state:
                                description:
                                    - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
                            azure_asn:
                                description:
                                    - The Azure ASN.
                            peer_asn:
                                description:
                                    - The peer ASN.
                            primary_peer_address_prefix:
                                description:
                                    - The primary address prefix.
                            secondary_peer_address_prefix:
                                description:
                                    - The secondary address prefix.
                            primary_azure_port:
                                description:
                                    - The primary port.
                            secondary_azure_port:
                                description:
                                    - The secondary port.
                            shared_key:
                                description:
                                    - The shared key.
                            vlan_id:
                                description:
                                    - The VLAN ID.
                            microsoft_peering_config:
                                description:
                                    - The Microsoft peering configuration.
                                suboptions:
                                    advertised_public_prefixes:
                                        description:
                                            - The reference of AdvertisedPublicPrefixes.
                                    advertised_communities:
                                        description:
                                            - The communities of bgp peering. Spepcified for microsoft peering
                                    advertised_public_prefixes_state:
                                        description:
                                            - "AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured', 'Configuring', 'Conf
                                               igured', and 'ValidationNeeded'. Possible values include: 'NotConfigured', 'Configuring', 'Configured', 'Valid
                                               ationNeeded'"
                                    legacy_mode:
                                        description:
                                            - The legacy mode of the peering.
                                    customer_asn:
                                        description:
                                            - The CustomerASN of the peering.
                                    routing_registry_name:
                                        description:
                                            - The RoutingRegistryName of the configuration.
                            stats:
                                description:
                                    - Gets peering stats.
                                suboptions:
                                    primarybytes_in:
                                        description:
                                            - Gets BytesIn of the peering.
                                    primarybytes_out:
                                        description:
                                            - Gets BytesOut of the peering.
                                    secondarybytes_in:
                                        description:
                                            - Gets BytesIn of the peering.
                                    secondarybytes_out:
                                        description:
                                            - Gets BytesOut of the peering.
                            provisioning_state:
                                description:
                                    - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
                            gateway_manager_etag:
                                description:
                                    - The GatewayManager Etag.
                            last_modified_by:
                                description:
                                    - Gets whether the provider or the customer last modified the peering.
                            route_filter:
                                description:
                                    - The reference of the RouteFilter resource.
                                suboptions:
                                    id:
                                        description:
                                            - Resource ID.
                                    location:
                                        description:
                                            - Resource location.
                                    rules:
                                        description:
                                            - Collection of RouteFilterRules contained within a route filter.
                                    peerings:
                                        description:
                                            - A collection of references to express route circuit peerings.
                            ipv6_peering_config:
                                description:
                                    - The IPv6 peering configuration.
                                suboptions:
                                    primary_peer_address_prefix:
                                        description:
                                            - The primary address prefix.
                                    secondary_peer_address_prefix:
                                        description:
                                            - The secondary address prefix.
                                    microsoft_peering_config:
                                        description:
                                            - The Microsoft peering configuration.
                                    route_filter:
                                        description:
                                            - The reference of the RouteFilter resource.
                                    state:
                                        description:
                                            - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Ena
                                               bled'"
                            name:
                                description:
                                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
            state:
                description:
                    - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
    name:
        description:
            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) ExpressRouteCircuitPeerings
    azure_rm_applicationgatewayexpressroutecircuitpeering:
      resource_group: resource_group_name
      circuit_name: circuit_name
      peering_name: peering_name
      id: id
      peering_type: peering_type
      state: state
      azure_asn: azure_asn
      peer_asn: peer_asn
      primary_peer_address_prefix: primary_peer_address_prefix
      secondary_peer_address_prefix: secondary_peer_address_prefix
      primary_azure_port: primary_azure_port
      secondary_azure_port: secondary_azure_port
      shared_key: shared_key
      vlan_id: vlan_id
      microsoft_peering_config:
        advertised_public_prefixes:
          - XXXX - list of values -- not implemented str
        advertised_communities:
          - XXXX - list of values -- not implemented str
        advertised_public_prefixes_state: advertised_public_prefixes_state
        legacy_mode: legacy_mode
        customer_asn: customer_asn
        routing_registry_name: routing_registry_name
      stats:
        primarybytes_in: primarybytes_in
        primarybytes_out: primarybytes_out
        secondarybytes_in: secondarybytes_in
        secondarybytes_out: secondarybytes_out
      provisioning_state: provisioning_state
      gateway_manager_etag: gateway_manager_etag
      last_modified_by: last_modified_by
      route_filter:
        id: id
        location: location
        rules:
          - id: id
            access: access
            route_filter_rule_type: route_filter_rule_type
            communities:
              - XXXX - list of values -- not implemented str
            name: name
            location: location
        peerings:
          - id: id
            peering_type: peering_type
            state: state
            azure_asn: azure_asn
            peer_asn: peer_asn
            primary_peer_address_prefix: primary_peer_address_prefix
            secondary_peer_address_prefix: secondary_peer_address_prefix
            primary_azure_port: primary_azure_port
            secondary_azure_port: secondary_azure_port
            shared_key: shared_key
            vlan_id: vlan_id
            microsoft_peering_config:
              advertised_public_prefixes:
                - XXXX - list of values -- not implemented str
              advertised_communities:
                - XXXX - list of values -- not implemented str
              advertised_public_prefixes_state: advertised_public_prefixes_state
              legacy_mode: legacy_mode
              customer_asn: customer_asn
              routing_registry_name: routing_registry_name
            stats:
              primarybytes_in: primarybytes_in
              primarybytes_out: primarybytes_out
              secondarybytes_in: secondarybytes_in
              secondarybytes_out: secondarybytes_out
            provisioning_state: provisioning_state
            gateway_manager_etag: gateway_manager_etag
            last_modified_by: last_modified_by
            route_filter:
              id: id
              location: location
              rules:
                - id: id
                  access: access
                  route_filter_rule_type: route_filter_rule_type
                  communities:
                    - XXXX - list of values -- not implemented str
                  name: name
                  location: location
              peerings:
                - id: id
                  peering_type: peering_type
                  state: state
                  azure_asn: azure_asn
                  peer_asn: peer_asn
                  primary_peer_address_prefix: primary_peer_address_prefix
                  secondary_peer_address_prefix: secondary_peer_address_prefix
                  primary_azure_port: primary_azure_port
                  secondary_azure_port: secondary_azure_port
                  shared_key: shared_key
                  vlan_id: vlan_id
                  microsoft_peering_config: microsoft_peering_config
                  stats: stats
                  provisioning_state: provisioning_state
                  gateway_manager_etag: gateway_manager_etag
                  last_modified_by: last_modified_by
                  route_filter: route_filter
                  ipv6_peering_config: ipv6_peering_config
                  name: name
            ipv6_peering_config:
              primary_peer_address_prefix: primary_peer_address_prefix
              secondary_peer_address_prefix: secondary_peer_address_prefix
              microsoft_peering_config:
                advertised_public_prefixes:
                  - XXXX - list of values -- not implemented str
                advertised_communities:
                  - XXXX - list of values -- not implemented str
                advertised_public_prefixes_state: advertised_public_prefixes_state
                legacy_mode: legacy_mode
                customer_asn: customer_asn
                routing_registry_name: routing_registry_name
              route_filter:
                id: id
                location: location
                rules:
                peerings:
              state: state
            name: name
      ipv6_peering_config:
        primary_peer_address_prefix: primary_peer_address_prefix
        secondary_peer_address_prefix: secondary_peer_address_prefix
        microsoft_peering_config:
          advertised_public_prefixes:
            - XXXX - list of values -- not implemented str
          advertised_communities:
            - XXXX - list of values -- not implemented str
          advertised_public_prefixes_state: advertised_public_prefixes_state
          legacy_mode: legacy_mode
          customer_asn: customer_asn
          routing_registry_name: routing_registry_name
        route_filter:
          id: id
          location: location
          rules:
            - id: id
              access: access
              route_filter_rule_type: route_filter_rule_type
              communities:
                - XXXX - list of values -- not implemented str
              name: name
              location: location
          peerings:
            - id: id
              peering_type: peering_type
              state: state
              azure_asn: azure_asn
              peer_asn: peer_asn
              primary_peer_address_prefix: primary_peer_address_prefix
              secondary_peer_address_prefix: secondary_peer_address_prefix
              primary_azure_port: primary_azure_port
              secondary_azure_port: secondary_azure_port
              shared_key: shared_key
              vlan_id: vlan_id
              microsoft_peering_config:
                advertised_public_prefixes:
                  - XXXX - list of values -- not implemented str
                advertised_communities:
                  - XXXX - list of values -- not implemented str
                advertised_public_prefixes_state: advertised_public_prefixes_state
                legacy_mode: legacy_mode
                customer_asn: customer_asn
                routing_registry_name: routing_registry_name
              stats:
                primarybytes_in: primarybytes_in
                primarybytes_out: primarybytes_out
                secondarybytes_in: secondarybytes_in
                secondarybytes_out: secondarybytes_out
              provisioning_state: provisioning_state
              gateway_manager_etag: gateway_manager_etag
              last_modified_by: last_modified_by
              route_filter:
                id: id
                location: location
                rules:
                peerings:
              ipv6_peering_config:
                primary_peer_address_prefix: primary_peer_address_prefix
                secondary_peer_address_prefix: secondary_peer_address_prefix
                microsoft_peering_config: microsoft_peering_config
                route_filter: route_filter
                state: state
              name: name
        state: state
      name: name
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
state:
    description:
        - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
    returned: always
    type: str
    sample: state
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


class AzureRMExpressRouteCircuitPeerings(AzureRMModuleBase):
    """Configuration class for an Azure RM ExpressRouteCircuitPeerings resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            circuit_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            peering_type=dict(
                type='str',
                required=False
            ),
            state=dict(
                type='str',
                required=False
            ),
            azure_asn=dict(
                type='int',
                required=False
            ),
            peer_asn=dict(
                type='long',
                required=False
            ),
            primary_peer_address_prefix=dict(
                type='str',
                required=False
            ),
            secondary_peer_address_prefix=dict(
                type='str',
                required=False
            ),
            primary_azure_port=dict(
                type='str',
                required=False
            ),
            secondary_azure_port=dict(
                type='str',
                required=False
            ),
            shared_key=dict(
                type='str',
                required=False
            ),
            vlan_id=dict(
                type='int',
                required=False
            ),
            microsoft_peering_config=dict(
                type='dict',
                required=False
            ),
            stats=dict(
                type='dict',
                required=False
            ),
            provisioning_state=dict(
                type='str',
                required=False
            ),
            gateway_manager_etag=dict(
                type='str',
                required=False
            ),
            last_modified_by=dict(
                type='str',
                required=False
            ),
            route_filter=dict(
                type='dict',
                required=False
            ),
            ipv6_peering_config=dict(
                type='dict',
                required=False
            ),
            name=dict(
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
        self.circuit_name = None
        self.peering_name = None
        self.peering_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCircuitPeerings, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                 supports_check_mode=True,
                                                                 supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.peering_parameters["id"] = kwargs[key]
                elif key == "peering_type":
                    self.peering_parameters["peering_type"] = kwargs[key]
                elif key == "state":
                    self.peering_parameters["state"] = kwargs[key]
                elif key == "azure_asn":
                    self.peering_parameters["azure_asn"] = kwargs[key]
                elif key == "peer_asn":
                    self.peering_parameters["peer_asn"] = kwargs[key]
                elif key == "primary_peer_address_prefix":
                    self.peering_parameters["primary_peer_address_prefix"] = kwargs[key]
                elif key == "secondary_peer_address_prefix":
                    self.peering_parameters["secondary_peer_address_prefix"] = kwargs[key]
                elif key == "primary_azure_port":
                    self.peering_parameters["primary_azure_port"] = kwargs[key]
                elif key == "secondary_azure_port":
                    self.peering_parameters["secondary_azure_port"] = kwargs[key]
                elif key == "shared_key":
                    self.peering_parameters["shared_key"] = kwargs[key]
                elif key == "vlan_id":
                    self.peering_parameters["vlan_id"] = kwargs[key]
                elif key == "microsoft_peering_config":
                    self.peering_parameters["microsoft_peering_config"] = kwargs[key]
                elif key == "stats":
                    self.peering_parameters["stats"] = kwargs[key]
                elif key == "provisioning_state":
                    self.peering_parameters["provisioning_state"] = kwargs[key]
                elif key == "gateway_manager_etag":
                    self.peering_parameters["gateway_manager_etag"] = kwargs[key]
                elif key == "last_modified_by":
                    self.peering_parameters["last_modified_by"] = kwargs[key]
                elif key == "route_filter":
                    self.peering_parameters["route_filter"] = kwargs[key]
                elif key == "ipv6_peering_config":
                    self.peering_parameters["ipv6_peering_config"] = kwargs[key]
                elif key == "name":
                    self.peering_parameters["name"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_expressroutecircuitpeerings()

        if not old_response:
            self.log("ExpressRouteCircuitPeerings instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ExpressRouteCircuitPeerings instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ExpressRouteCircuitPeerings instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ExpressRouteCircuitPeerings instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_expressroutecircuitpeerings()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ExpressRouteCircuitPeerings instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_expressroutecircuitpeerings()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_expressroutecircuitpeerings():
                time.sleep(20)
        else:
            self.log("ExpressRouteCircuitPeerings instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]

        return self.results

    def create_update_expressroutecircuitpeerings(self):
        '''
        Creates or updates ExpressRouteCircuitPeerings with the specified configuration.

        :return: deserialized ExpressRouteCircuitPeerings instance state dictionary
        '''
        self.log("Creating / Updating the ExpressRouteCircuitPeerings instance {0}".format(self.peering_name))

        try:
            response = self.mgmt_client.express_route_circuit_peerings.create_or_update(self.resource_group,
                                                                                        self.circuit_name,
                                                                                        self.peering_name,
                                                                                        self.peering_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCircuitPeerings instance.')
            self.fail("Error creating the ExpressRouteCircuitPeerings instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_expressroutecircuitpeerings(self):
        '''
        Deletes specified ExpressRouteCircuitPeerings instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ExpressRouteCircuitPeerings instance {0}".format(self.peering_name))
        try:
            response = self.mgmt_client.express_route_circuit_peerings.delete(self.resource_group,
                                                                              self.circuit_name,
                                                                              self.peering_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCircuitPeerings instance.')
            self.fail("Error deleting the ExpressRouteCircuitPeerings instance: {0}".format(str(e)))

        return True

    def get_expressroutecircuitpeerings(self):
        '''
        Gets the properties of the specified ExpressRouteCircuitPeerings.

        :return: deserialized ExpressRouteCircuitPeerings instance state dictionary
        '''
        self.log("Checking if the ExpressRouteCircuitPeerings instance {0} is present".format(self.peering_name))
        found = False
        try:
            response = self.mgmt_client.express_route_circuit_peerings.get(self.resource_group,
                                                                           self.circuit_name,
                                                                           self.peering_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ExpressRouteCircuitPeerings instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ExpressRouteCircuitPeerings instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMExpressRouteCircuitPeerings()

if __name__ == '__main__':
    main()