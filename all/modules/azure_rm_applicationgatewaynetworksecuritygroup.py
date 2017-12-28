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
module: azure_rm_applicationgatewaynetworksecuritygroup
version_added: "2.5"
short_description: Manage NetworkSecurityGroups instance.
description:
    - Create, update and delete instance of NetworkSecurityGroups.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_security_group_name:
        description:
            - The name of the network security group.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
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
                    - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetwork), C(AzureLoa
                       dBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traffic originates from. "
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
                    - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. Default tags such
                        as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
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
                    - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. T
                       he lower the priority number, the higher the priority of the rule."
            direction:
                description:
                    - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values are: C(
                       Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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
                    - "The CIDR or source IP range. Asterix C(*) can also be used to match all source IPs. Default tags such as C(VirtualNetwork), C(AzureLoa
                       dBalancer) and C(Internet) can also be used. If this is an ingress rule, specifies where network traffic originates from. "
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
                    - "The destination address prefix. CIDR or destination IP range. Asterix C(*) can also be used to match all source IPs. Default tags such
                        as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used."
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
                    - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. T
                       he lower the priority number, the higher the priority of the rule."
            direction:
                description:
                    - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values are: C(
                       Inbound) and C(Outbound). Possible values include: C(Inbound), C(Outbound)"
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

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) NetworkSecurityGroups
    azure_rm_applicationgatewaynetworksecuritygroup:
      resource_group: rg1
      network_security_group_name: testnsg
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


class AzureRMNetworkSecurityGroups(AzureRMModuleBase):
    """Configuration class for an Azure RM NetworkSecurityGroups resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            network_security_group_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            security_rules=dict(
                type='list'
            ),
            default_security_rules=dict(
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
        self.network_security_group_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetworkSecurityGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "security_rules":
                    self.parameters["security_rules"] = kwargs[key]
                elif key == "default_security_rules":
                    self.parameters["default_security_rules"] = kwargs[key]
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

        old_response = self.get_networksecuritygroups()

        if not old_response:
            self.log("NetworkSecurityGroups instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("NetworkSecurityGroups instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if NetworkSecurityGroups instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the NetworkSecurityGroups instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_networksecuritygroups()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("NetworkSecurityGroups instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_networksecuritygroups()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_networksecuritygroups():
                time.sleep(20)
        else:
            self.log("NetworkSecurityGroups instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_networksecuritygroups(self):
        '''
        Creates or updates NetworkSecurityGroups with the specified configuration.

        :return: deserialized NetworkSecurityGroups instance state dictionary
        '''
        self.log("Creating / Updating the NetworkSecurityGroups instance {0}".format(self.network_security_group_name))

        try:
            response = self.mgmt_client.network_security_groups.create_or_update(resource_group_name=self.resource_group,
                                                                                 network_security_group_name=self.network_security_group_name,
                                                                                 parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the NetworkSecurityGroups instance.')
            self.fail("Error creating the NetworkSecurityGroups instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_networksecuritygroups(self):
        '''
        Deletes specified NetworkSecurityGroups instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the NetworkSecurityGroups instance {0}".format(self.network_security_group_name))
        try:
            response = self.mgmt_client.network_security_groups.delete(resource_group_name=self.resource_group,
                                                                       network_security_group_name=self.network_security_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the NetworkSecurityGroups instance.')
            self.fail("Error deleting the NetworkSecurityGroups instance: {0}".format(str(e)))

        return True

    def get_networksecuritygroups(self):
        '''
        Gets the properties of the specified NetworkSecurityGroups.

        :return: deserialized NetworkSecurityGroups instance state dictionary
        '''
        self.log("Checking if the NetworkSecurityGroups instance {0} is present".format(self.network_security_group_name))
        found = False
        try:
            response = self.mgmt_client.network_security_groups.get(resource_group_name=self.resource_group,
                                                                    network_security_group_name=self.network_security_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("NetworkSecurityGroups instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the NetworkSecurityGroups instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMNetworkSecurityGroups()

if __name__ == '__main__':
    main()
