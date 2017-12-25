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
module: azure_rm_applicationgatewaysecurityrule
version_added: "2.5"
short_description: Manage SecurityRules instance.
description:
    - Create, update and delete instance of SecurityRules.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    network_security_group_name:
        description:
            - The name of the network security group.
        required: True
    security_rule_name:
        description:
            - The name of the security rule.
        required: True
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
            - "The CIDR or source IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer'
               and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. "
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
            - "The destination address prefix. CIDR or destination IP range. Asterix '*' can also be used to match all source IPs. Default tags such as 'Virt
               ualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used."
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
            - "The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower
                the priority number, the higher the priority of the rule."
    direction:
        description:
            - "The direction of the rule. The direction specifies if rule will be evaluated on incoming or outcoming traffic. Possible values are: 'Inbound'
               and 'Outbound'. Possible values include: 'Inbound', 'Outbound'"
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

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) SecurityRules
    azure_rm_applicationgatewaysecurityrule:
      resource_group: rg1
      network_security_group_name: testnsg
      security_rule_name: rule1
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


class AzureRMSecurityRules(AzureRMModuleBase):
    """Configuration class for an Azure RM SecurityRules resource"""

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
            security_rule_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            description=dict(
                type='str'
            ),
            protocol=dict(
                type='str',
                required=True
            ),
            source_port_range=dict(
                type='str'
            ),
            destination_port_range=dict(
                type='str'
            ),
            source_address_prefix=dict(
                type='str'
            ),
            source_address_prefixes=dict(
                type='list'
            ),
            source_application_security_groups=dict(
                type='list'
            ),
            destination_address_prefix=dict(
                type='str'
            ),
            destination_address_prefixes=dict(
                type='list'
            ),
            destination_application_security_groups=dict(
                type='list'
            ),
            source_port_ranges=dict(
                type='list'
            ),
            destination_port_ranges=dict(
                type='list'
            ),
            access=dict(
                type='str',
                required=True
            ),
            priority=dict(
                type='int'
            ),
            direction=dict(
                type='str',
                required=True
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
        self.network_security_group_name = None
        self.security_rule_name = None
        self.security_rule_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSecurityRules, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.security_rule_parameters["id"] = kwargs[key]
                elif key == "description":
                    self.security_rule_parameters["description"] = kwargs[key]
                elif key == "protocol":
                    self.security_rule_parameters["protocol"] = kwargs[key]
                elif key == "source_port_range":
                    self.security_rule_parameters["source_port_range"] = kwargs[key]
                elif key == "destination_port_range":
                    self.security_rule_parameters["destination_port_range"] = kwargs[key]
                elif key == "source_address_prefix":
                    self.security_rule_parameters["source_address_prefix"] = kwargs[key]
                elif key == "source_address_prefixes":
                    self.security_rule_parameters["source_address_prefixes"] = kwargs[key]
                elif key == "source_application_security_groups":
                    self.security_rule_parameters["source_application_security_groups"] = kwargs[key]
                elif key == "destination_address_prefix":
                    self.security_rule_parameters["destination_address_prefix"] = kwargs[key]
                elif key == "destination_address_prefixes":
                    self.security_rule_parameters["destination_address_prefixes"] = kwargs[key]
                elif key == "destination_application_security_groups":
                    self.security_rule_parameters["destination_application_security_groups"] = kwargs[key]
                elif key == "source_port_ranges":
                    self.security_rule_parameters["source_port_ranges"] = kwargs[key]
                elif key == "destination_port_ranges":
                    self.security_rule_parameters["destination_port_ranges"] = kwargs[key]
                elif key == "access":
                    self.security_rule_parameters["access"] = kwargs[key]
                elif key == "priority":
                    self.security_rule_parameters["priority"] = kwargs[key]
                elif key == "direction":
                    self.security_rule_parameters["direction"] = kwargs[key]
                elif key == "provisioning_state":
                    self.security_rule_parameters["provisioning_state"] = kwargs[key]
                elif key == "name":
                    self.security_rule_parameters["name"] = kwargs[key]
                elif key == "etag":
                    self.security_rule_parameters["etag"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_securityrules()

        if not old_response:
            self.log("SecurityRules instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("SecurityRules instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if SecurityRules instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the SecurityRules instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_securityrules()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("SecurityRules instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_securityrules()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_securityrules():
                time.sleep(20)
        else:
            self.log("SecurityRules instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_securityrules(self):
        '''
        Creates or updates SecurityRules with the specified configuration.

        :return: deserialized SecurityRules instance state dictionary
        '''
        self.log("Creating / Updating the SecurityRules instance {0}".format(self.security_rule_name))

        try:
            response = self.mgmt_client.security_rules.create_or_update(self.resource_group,
                                                                        self.network_security_group_name,
                                                                        self.security_rule_name,
                                                                        self.security_rule_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the SecurityRules instance.')
            self.fail("Error creating the SecurityRules instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_securityrules(self):
        '''
        Deletes specified SecurityRules instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the SecurityRules instance {0}".format(self.security_rule_name))
        try:
            response = self.mgmt_client.security_rules.delete(self.resource_group,
                                                              self.network_security_group_name,
                                                              self.security_rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the SecurityRules instance.')
            self.fail("Error deleting the SecurityRules instance: {0}".format(str(e)))

        return True

    def get_securityrules(self):
        '''
        Gets the properties of the specified SecurityRules.

        :return: deserialized SecurityRules instance state dictionary
        '''
        self.log("Checking if the SecurityRules instance {0} is present".format(self.security_rule_name))
        found = False
        try:
            response = self.mgmt_client.security_rules.get(self.resource_group,
                                                           self.network_security_group_name,
                                                           self.security_rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SecurityRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SecurityRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMSecurityRules()

if __name__ == '__main__':
    main()
