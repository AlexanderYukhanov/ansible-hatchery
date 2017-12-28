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
module: azure_rm_applicationgatewayroutefilter
version_added: "2.5"
short_description: Manage RouteFilters instance.
description:
    - Create, update and delete instance of RouteFilters.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    route_filter_name:
        description:
            - The name of the route filter.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    rules:
        description:
            - Collection of RouteFilterRules contained within a route filter.
        suboptions:
            id:
                description:
                    - Resource ID.
            access:
                description:
                    - The access type of the rule. Valid values are: C(Allow), C(Deny). Possible values include: C(Allow), C(Deny)
                required: True
                choices: ['allow', 'deny']
            route_filter_rule_type:
                description:
                    - The rule type of the rule. Valid value is: C(Community)
                required: True
            communities:
                description:
                    - The collection for bgp community values to filter on. e.g. [C(12076:5010),C(12076:5020)]
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
                    - "The PeeringType. Possible values are: C(AzurePublicPeering), C(AzurePrivatePeering), and C(MicrosoftPeering). Possible values include:
                        C(AzurePublicPeering), C(AzurePrivatePeering), C(MicrosoftPeering)"
                choices: ['azure_public_peering', 'azure_private_peering', 'microsoft_peering']
            state:
                description:
                    - The state of peering. Possible values are: C(Disabled) and C(Enabled). Possible values include: C(Disabled), C(Enabled)
                choices: ['disabled', 'enabled']
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
                            - "AdvertisedPublicPrefixState of the Peering resource. Possible values are C(NotConfigured), C(Configuring), C(Configured), and
                               C(ValidationNeeded). Possible values include: C(NotConfigured), C(Configuring), C(Configured), C(ValidationNeeded)"
                        choices: ['not_configured', 'configuring', 'configured', 'validation_needed']
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
                    - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
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
                                    - The access type of the rule. Valid values are: C(Allow), C(Deny). Possible values include: C(Allow), C(Deny)
                                required: True
                                choices: ['allow', 'deny']
                            route_filter_rule_type:
                                description:
                                    - The rule type of the rule. Valid value is: C(Community)
                                required: True
                            communities:
                                description:
                                    - The collection for bgp community values to filter on. e.g. [C(12076:5010),C(12076:5020)]
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
                                    - "The PeeringType. Possible values are: C(AzurePublicPeering), C(AzurePrivatePeering), and C(MicrosoftPeering). Possible
                                        values include: C(AzurePublicPeering), C(AzurePrivatePeering), C(MicrosoftPeering)"
                                choices: ['azure_public_peering', 'azure_private_peering', 'microsoft_peering']
                            state:
                                description:
                                    - The state of peering. Possible values are: C(Disabled) and C(Enabled). Possible values include: C(Disabled), C(Enabled)
                                choices: ['disabled', 'enabled']
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
                                            - "AdvertisedPublicPrefixState of the Peering resource. Possible values are C(NotConfigured), C(Configuring), C(C
                                               onfigured), and C(ValidationNeeded). Possible values include: C(NotConfigured), C(Configuring), C(Configured),
                                                C(ValidationNeeded)"
                                        choices: ['not_configured', 'configuring', 'configured', 'validation_needed']
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
                                    - Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Failed).
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
                                            - "The state of peering. Possible values are: C(Disabled) and C(Enabled). Possible values include: C(Disabled), C
                                               (Enabled)"
                                        choices: ['disabled', 'enabled']
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
                                    - "AdvertisedPublicPrefixState of the Peering resource. Possible values are C(NotConfigured), C(Configuring), C(Configure
                                       d), and C(ValidationNeeded). Possible values include: C(NotConfigured), C(Configuring), C(Configured), C(ValidationNee
                                       ded)"
                                choices: ['not_configured', 'configuring', 'configured', 'validation_needed']
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
                                            - The access type of the rule. Valid values are: C(Allow), C(Deny). Possible values include: C(Allow), C(Deny)
                                        required: True
                                        choices: ['allow', 'deny']
                                    route_filter_rule_type:
                                        description:
                                            - The rule type of the rule. Valid value is: C(Community)
                                        required: True
                                    communities:
                                        description:
                                            - The collection for bgp community values to filter on. e.g. [C(12076:5010),C(12076:5020)]
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
                                            - "The PeeringType. Possible values are: C(AzurePublicPeering), C(AzurePrivatePeering), and C(MicrosoftPeering).
                                               Possible values include: C(AzurePublicPeering), C(AzurePrivatePeering), C(MicrosoftPeering)"
                                        choices: ['azure_public_peering', 'azure_private_peering', 'microsoft_peering']
                                    state:
                                        description:
                                            - "The state of peering. Possible values are: C(Disabled) and C(Enabled). Possible values include: C(Disabled), C
                                               (Enabled)"
                                        choices: ['disabled', 'enabled']
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
                                            - "Gets the provisioning state of the public IP resource. Possible values are: C(Updating), C(Deleting), and C(Fa
                                               iled)."
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
                    state:
                        description:
                            - The state of peering. Possible values are: C(Disabled) and C(Enabled). Possible values include: C(Disabled), C(Enabled)
                        choices: ['disabled', 'enabled']
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
  - name: Create (or update) RouteFilters
    azure_rm_applicationgatewayroutefilter:
      resource_group: rg1
      route_filter_name: filterName
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


class AzureRMRouteFilters(AzureRMModuleBase):
    """Configuration class for an Azure RM RouteFilters resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            route_filter_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            rules=dict(
                type='list'
            ),
            peerings=dict(
                type='list'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.route_filter_name = None
        self.route_filter_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRouteFilters, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.route_filter_parameters["id"] = kwargs[key]
                elif key == "location":
                    self.route_filter_parameters["location"] = kwargs[key]
                elif key == "rules":
                    self.route_filter_parameters["rules"] = kwargs[key]
                elif key == "peerings":
                    self.route_filter_parameters["peerings"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_routefilters()

        if not old_response:
            self.log("RouteFilters instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("RouteFilters instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if RouteFilters instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the RouteFilters instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_routefilters()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("RouteFilters instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_routefilters()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_routefilters():
                time.sleep(20)
        else:
            self.log("RouteFilters instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_routefilters(self):
        '''
        Creates or updates RouteFilters with the specified configuration.

        :return: deserialized RouteFilters instance state dictionary
        '''
        self.log("Creating / Updating the RouteFilters instance {0}".format(self.route_filter_name))

        try:
            response = self.mgmt_client.route_filters.create_or_update(resource_group_name=self.resource_group,
                                                                       route_filter_name=self.route_filter_name,
                                                                       route_filter_parameters=self.route_filter_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the RouteFilters instance.')
            self.fail("Error creating the RouteFilters instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_routefilters(self):
        '''
        Deletes specified RouteFilters instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the RouteFilters instance {0}".format(self.route_filter_name))
        try:
            response = self.mgmt_client.route_filters.delete(resource_group_name=self.resource_group,
                                                             route_filter_name=self.route_filter_name)
        except CloudError as e:
            self.log('Error attempting to delete the RouteFilters instance.')
            self.fail("Error deleting the RouteFilters instance: {0}".format(str(e)))

        return True

    def get_routefilters(self):
        '''
        Gets the properties of the specified RouteFilters.

        :return: deserialized RouteFilters instance state dictionary
        '''
        self.log("Checking if the RouteFilters instance {0} is present".format(self.route_filter_name))
        found = False
        try:
            response = self.mgmt_client.route_filters.get(resource_group_name=self.resource_group,
                                                          route_filter_name=self.route_filter_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RouteFilters instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RouteFilters instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMRouteFilters()

if __name__ == '__main__':
    main()
