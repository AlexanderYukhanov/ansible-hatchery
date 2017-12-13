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
module: azure_rm_applicationgatewaylocalnetworkgateway
version_added: "2.5"
short_description: Manage LocalNetworkGateways instance
description:
    - Create, update and delete instance of LocalNetworkGateways

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    local_network_gateway_name:
        description:
            - The name of the local network gateway.
        required: True
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

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) LocalNetworkGateways
    azure_rm_applicationgatewaylocalnetworkgateway:
      resource_group: resource_group_name
      local_network_gateway_name: local_network_gateway_name
      id: id
      location: location
      local_network_address_space:
        address_prefixes:
          - XXXX - list of values -- not implemented str
      gateway_ip_address: gateway_ip_address
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


class AzureRMLocalNetworkGateways(AzureRMModuleBase):
    """Configuration class for an Azure RM LocalNetworkGateways resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            local_network_gateway_name=dict(
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
            local_network_address_space=dict(
                type='dict',
                required=False
            ),
            gateway_ip_address=dict(
                type='str',
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
        self.local_network_gateway_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLocalNetworkGateways, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "local_network_address_space":
                    self.parameters.update({"local_network_address_space": kwargs[key]})
                elif key == "gateway_ip_address":
                    self.parameters.update({"gateway_ip_address": kwargs[key]})
                elif key == "bgp_settings":
                    self.parameters.update({"bgp_settings": kwargs[key]})
                elif key == "resource_guid":
                    self.parameters.update({"resource_guid": kwargs[key]})
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

        old_response = self.get_localnetworkgateways()

        if not old_response:
            self.log("LocalNetworkGateways instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("LocalNetworkGateways instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if LocalNetworkGateways instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the LocalNetworkGateways instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_localnetworkgateways()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("LocalNetworkGateways instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_localnetworkgateways()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_localnetworkgateways():
                time.sleep(20)
        else:
            self.log("LocalNetworkGateways instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_localnetworkgateways(self):
        '''
        Creates or updates LocalNetworkGateways with the specified configuration.

        :return: deserialized LocalNetworkGateways instance state dictionary
        '''
        self.log("Creating / Updating the LocalNetworkGateways instance {0}".format(self.local_network_gateway_name))

        try:
            response = self.mgmt_client.local_network_gateways.create_or_update(self.resource_group,
                                                                                self.local_network_gateway_name,
                                                                                self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the LocalNetworkGateways instance.')
            self.fail("Error creating the LocalNetworkGateways instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_localnetworkgateways(self):
        '''
        Deletes specified LocalNetworkGateways instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the LocalNetworkGateways instance {0}".format(self.local_network_gateway_name))
        try:
            response = self.mgmt_client.local_network_gateways.delete(self.resource_group,
                                                                      self.local_network_gateway_name)
        except CloudError as e:
            self.log('Error attempting to delete the LocalNetworkGateways instance.')
            self.fail("Error deleting the LocalNetworkGateways instance: {0}".format(str(e)))

        return True

    def get_localnetworkgateways(self):
        '''
        Gets the properties of the specified LocalNetworkGateways.

        :return: deserialized LocalNetworkGateways instance state dictionary
        '''
        self.log("Checking if the LocalNetworkGateways instance {0} is present".format(self.local_network_gateway_name))
        found = False
        try:
            response = self.mgmt_client.local_network_gateways.get(self.resource_group,
                                                                   self.local_network_gateway_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("LocalNetworkGateways instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the LocalNetworkGateways instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMLocalNetworkGateways()

if __name__ == '__main__':
    main()
