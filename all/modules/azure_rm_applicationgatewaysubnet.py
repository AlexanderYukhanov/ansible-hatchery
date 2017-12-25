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
module: azure_rm_applicationgatewaysubnet
version_added: "2.5"
short_description: Manage Subnets instance.
description:
    - Create, update and delete instance of Subnets.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    virtual_network_name:
        description:
            - The name of the virtual network.
        required: True
    subnet_name:
        description:
            - The name of the subnet.
        required: True
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
                            - "Network protocol this rule applies to. Possible values are 'Tcp', 'Udp', and '*'. Possible values include: 'Tcp', 'Udp', '*'"
                        required: True
                    source_port_range:
                        description:
                            - "The source port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports."
                    destination_port_range:
                        description:
                            - "The destination port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports."
                    source_address_prefix:
                        description:
                            - "The CIDR or source IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'Azu
                               reLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. "
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
                            - "The destination address prefix. CIDR or destination IP range. Asterix '*' can also be used to match all source IPs. Default ta
                               gs such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used."
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
                            - "The network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'. Possible values include: 'Allow', 'Deny'"
                        required: True
                    priority:
                        description:
                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the colle
                               ction. The lower the priority number, the higher the priority of the rule."
                    direction:
                        description:
                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values
                                are: 'Inbound' and 'Outbound'. Possible values include: 'Inbound', 'Outbound'"
                        required: True
                    provisioning_state:
                        description:
                            - "The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                            - "Network protocol this rule applies to. Possible values are 'Tcp', 'Udp', and '*'. Possible values include: 'Tcp', 'Udp', '*'"
                        required: True
                    source_port_range:
                        description:
                            - "The source port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports."
                    destination_port_range:
                        description:
                            - "The destination port or range. Integer or range between 0 and 65535. Asterix '*' can also be used to match all ports."
                    source_address_prefix:
                        description:
                            - "The CIDR or source IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'Azu
                               reLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. "
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
                            - "The destination address prefix. CIDR or destination IP range. Asterix '*' can also be used to match all source IPs. Default ta
                               gs such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used."
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
                            - "The network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'. Possible values include: 'Allow', 'Deny'"
                        required: True
                    priority:
                        description:
                            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the colle
                               ction. The lower the priority number, the higher the priority of the rule."
                    direction:
                        description:
                            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values
                                are: 'Inbound' and 'Outbound'. Possible values include: 'Inbound', 'Outbound'"
                        required: True
                    provisioning_state:
                        description:
                            - "The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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
                suboptions:
                    id:
                        description:
                            - Resource ID.
                    address_prefix:
                        description:
                            - The destination CIDR to which the route applies.
                    next_hop_type:
                        description:
                            - "The type of Azure hop the packet should be sent to. Possible values are: 'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'Vi
                               rtualAppliance', and 'None'. Possible values include: 'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance', 'N
                               one'"
                        required: True
                    next_hop_ip_address:
                        description:
                            - "The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAp
                               pliance."
                    provisioning_state:
                        description:
                            - "The provisioning state of the resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
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

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Subnets
    azure_rm_applicationgatewaysubnet:
      resource_group: subnet-test
      virtual_network_name: vnetname
      subnet_name: subnet1
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


class AzureRMSubnets(AzureRMModuleBase):
    """Configuration class for an Azure RM Subnets resource"""

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
            subnet_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            address_prefix=dict(
                type='str'
            ),
            network_security_group=dict(
                type='dict'
            ),
            route_table=dict(
                type='dict'
            ),
            service_endpoints=dict(
                type='list'
            ),
            resource_navigation_links=dict(
                type='list'
            ),
            provisioning_state=dict(
                type='str'
            ),
            name=dict(
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
        self.subnet_name = None
        self.subnet_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSubnets, self).__init__(derived_arg_spec=self.module_arg_spec,
                                             supports_check_mode=True,
                                             supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.subnet_parameters["id"] = kwargs[key]
                elif key == "address_prefix":
                    self.subnet_parameters["address_prefix"] = kwargs[key]
                elif key == "network_security_group":
                    self.subnet_parameters["network_security_group"] = kwargs[key]
                elif key == "route_table":
                    self.subnet_parameters["route_table"] = kwargs[key]
                elif key == "service_endpoints":
                    self.subnet_parameters["service_endpoints"] = kwargs[key]
                elif key == "resource_navigation_links":
                    self.subnet_parameters["resource_navigation_links"] = kwargs[key]
                elif key == "provisioning_state":
                    self.subnet_parameters["provisioning_state"] = kwargs[key]
                elif key == "name":
                    self.subnet_parameters["name"] = kwargs[key]
                elif key == "etag":
                    self.subnet_parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_subnets()

        if not old_response:
            self.log("Subnets instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Subnets instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Subnets instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Subnets instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_subnets()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Subnets instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_subnets()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_subnets():
                time.sleep(20)
        else:
            self.log("Subnets instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_subnets(self):
        '''
        Creates or updates Subnets with the specified configuration.

        :return: deserialized Subnets instance state dictionary
        '''
        self.log("Creating / Updating the Subnets instance {0}".format(self.subnet_name))

        try:
            response = self.mgmt_client.subnets.create_or_update(resource_group_name=self.resource_group,
                                                                 virtual_network_name=self.virtual_network_name,
                                                                 subnet_name=self.subnet_name,
                                                                 subnet_parameters=self.subnet_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Subnets instance.')
            self.fail("Error creating the Subnets instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_subnets(self):
        '''
        Deletes specified Subnets instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Subnets instance {0}".format(self.subnet_name))
        try:
            response = self.mgmt_client.subnets.delete(resource_group_name=self.resource_group,
                                                       virtual_network_name=self.virtual_network_name,
                                                       subnet_name=self.subnet_name)
        except CloudError as e:
            self.log('Error attempting to delete the Subnets instance.')
            self.fail("Error deleting the Subnets instance: {0}".format(str(e)))

        return True

    def get_subnets(self):
        '''
        Gets the properties of the specified Subnets.

        :return: deserialized Subnets instance state dictionary
        '''
        self.log("Checking if the Subnets instance {0} is present".format(self.subnet_name))
        found = False
        try:
            response = self.mgmt_client.subnets.get(resource_group_name=self.resource_group,
                                                    virtual_network_name=self.virtual_network_name,
                                                    subnet_name=self.subnet_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Subnets instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Subnets instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMSubnets()

if __name__ == '__main__':
    main()
