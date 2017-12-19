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
module: azure_rm_applicationgatewayexpressroutecircuit
version_added: "2.5"
short_description: Manage ExpressRouteCircuits instance
description:
    - Create, update and delete instance of ExpressRouteCircuits

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    circuit_name:
        description:
            - The name of the circuit.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location.
    sku:
        description:
            - The SKU.
        suboptions:
            name:
                description:
                    - The name of the SKU.
            tier:
                description:
                    - "The tier of the SKU. Possible values are 'Standard' and 'Premium'. Possible values include: 'Standard', 'Premium'"
            family:
                description:
                    - "The family of the SKU. Possible values are: 'UnlimitedData' and 'MeteredData'. Possible values include: 'UnlimitedData', 'MeteredData'"
    allow_classic_operations:
        description:
            - Allow classic operations
    circuit_provisioning_state:
        description:
            - The CircuitProvisioningState state of the resource.
    service_provider_provisioning_state:
        description:
            - "The ServiceProviderProvisioningState state of the resource. Possible values are 'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovis
               ioning'. Possible values include: 'NotProvisioned', 'Provisioning', 'Provisioned', 'Deprovisioning'"
    authorizations:
        description:
            - The list of authorizations.
        suboptions:
            id:
                description:
                    - Resource ID.
            authorization_key:
                description:
                    - The authorization key.
            authorization_use_status:
                description:
                    - "AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'. Possible values include: 'Available', 'InUse'"
            provisioning_state:
                description:
                    - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
            name:
                description:
                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
    peerings:
        description:
            - The list of peerings.
        suboptions:
            id:
                description:
                    - Resource ID.
            peering_type:
                description:
                    - "The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'. Possible values include: 'A
                       zurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'"
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
                    state:
                        description:
                            - "The state of peering. Possible values are: 'Disabled' and 'Enabled'. Possible values include: 'Disabled', 'Enabled'"
            name:
                description:
                    - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
    service_key:
        description:
            - The ServiceKey.
    service_provider_notes:
        description:
            - The ServiceProviderNotes.
    service_provider_properties:
        description:
            - The ServiceProviderProperties.
        suboptions:
            service_provider_name:
                description:
                    - The serviceProviderName.
            peering_location:
                description:
                    - The peering location.
            bandwidth_in_mbps:
                description:
                    - The BandwidthInMbps.
    provisioning_state:
        description:
            - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
    gateway_manager_etag:
        description:
            - The GatewayManager Etag.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) ExpressRouteCircuits
    azure_rm_applicationgatewayexpressroutecircuit:
      resource_group: NOT FOUND
      circuit_name: NOT FOUND
      authorizations:
      peerings:
        - microsoft_peering_config:
            advertised_public_prefixes:
              - XXXX - list of values -- not implemented str
            advertised_communities:
              - XXXX - list of values -- not implemented str
          route_filter:
            rules:
              - communities:
                  - XXXX - list of values -- not implemented str
            peerings:
              - microsoft_peering_config:
                  advertised_public_prefixes:
                    - XXXX - list of values -- not implemented str
                  advertised_communities:
                    - XXXX - list of values -- not implemented str
                route_filter:
                  rules:
                  peerings:
          ipv6_peering_config:
            microsoft_peering_config:
              advertised_public_prefixes:
                - XXXX - list of values -- not implemented str
              advertised_communities:
                - XXXX - list of values -- not implemented str
            route_filter:
              rules:
                - communities:
                    - XXXX - list of values -- not implemented str
              peerings:
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


class AzureRMExpressRouteCircuits(AzureRMModuleBase):
    """Configuration class for an Azure RM ExpressRouteCircuits resource"""

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
            allow_classic_operations=dict(
                type='str',
                required=False
            ),
            circuit_provisioning_state=dict(
                type='str',
                required=False
            ),
            service_provider_provisioning_state=dict(
                type='str',
                required=False
            ),
            authorizations=dict(
                type='list',
                required=False
            ),
            peerings=dict(
                type='list',
                required=False
            ),
            service_key=dict(
                type='str',
                required=False
            ),
            service_provider_notes=dict(
                type='str',
                required=False
            ),
            service_provider_properties=dict(
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
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.circuit_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCircuits, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "sku":
                    self.parameters["sku"] = kwargs[key]
                elif key == "allow_classic_operations":
                    self.parameters["allow_classic_operations"] = kwargs[key]
                elif key == "circuit_provisioning_state":
                    self.parameters["circuit_provisioning_state"] = kwargs[key]
                elif key == "service_provider_provisioning_state":
                    self.parameters["service_provider_provisioning_state"] = kwargs[key]
                elif key == "authorizations":
                    self.parameters["authorizations"] = kwargs[key]
                elif key == "peerings":
                    self.parameters["peerings"] = kwargs[key]
                elif key == "service_key":
                    self.parameters["service_key"] = kwargs[key]
                elif key == "service_provider_notes":
                    self.parameters["service_provider_notes"] = kwargs[key]
                elif key == "service_provider_properties":
                    self.parameters["service_provider_properties"] = kwargs[key]
                elif key == "provisioning_state":
                    self.parameters["provisioning_state"] = kwargs[key]
                elif key == "gateway_manager_etag":
                    self.parameters["gateway_manager_etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_expressroutecircuits()

        if not old_response:
            self.log("ExpressRouteCircuits instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ExpressRouteCircuits instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ExpressRouteCircuits instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ExpressRouteCircuits instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_expressroutecircuits()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ExpressRouteCircuits instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_expressroutecircuits()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_expressroutecircuits():
                time.sleep(20)
        else:
            self.log("ExpressRouteCircuits instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_expressroutecircuits(self):
        '''
        Creates or updates ExpressRouteCircuits with the specified configuration.

        :return: deserialized ExpressRouteCircuits instance state dictionary
        '''
        self.log("Creating / Updating the ExpressRouteCircuits instance {0}".format(self.circuit_name))

        try:
            response = self.mgmt_client.express_route_circuits.create_or_update(self.resource_group,
                                                                                self.circuit_name,
                                                                                self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCircuits instance.')
            self.fail("Error creating the ExpressRouteCircuits instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_expressroutecircuits(self):
        '''
        Deletes specified ExpressRouteCircuits instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ExpressRouteCircuits instance {0}".format(self.circuit_name))
        try:
            response = self.mgmt_client.express_route_circuits.delete(self.resource_group,
                                                                      self.circuit_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCircuits instance.')
            self.fail("Error deleting the ExpressRouteCircuits instance: {0}".format(str(e)))

        return True

    def get_expressroutecircuits(self):
        '''
        Gets the properties of the specified ExpressRouteCircuits.

        :return: deserialized ExpressRouteCircuits instance state dictionary
        '''
        self.log("Checking if the ExpressRouteCircuits instance {0} is present".format(self.circuit_name))
        found = False
        try:
            response = self.mgmt_client.express_route_circuits.get(self.resource_group,
                                                                   self.circuit_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ExpressRouteCircuits instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ExpressRouteCircuits instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMExpressRouteCircuits()

if __name__ == '__main__':
    main()
