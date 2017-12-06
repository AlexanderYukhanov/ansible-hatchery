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
module: azure_rm_mysqlfirewallrule
version_added: "2.5"
short_description: Manage FirewallRules instance
description:
    - Create, update and delete instance of FirewallRules

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    name:
        description:
            - The name of the server firewall rule.
        required: True
    parameters:
        description:
            - The required parameters for creating or updating a firewall rule.
    start_ip_address:
        description:
            - The start IP address of the server firewall rule. Must be IPv4 format.
    end_ip_address:
        description:
            - The end IP address of the server firewall rule. Must be IPv4 format.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) FirewallRules
    azure_rm_mysqlfirewallrule:
      resource_group: resource_group_name
      server_name: server_name
      name: firewall_rule_name
      parameters: parameters
      start_ip_address: start_ip_address
      end_ip_address: end_ip_address
'''

RETURN = '''
state:
    description: Current state of FirewallRules
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID
            returned: always
            type: str
            sample: id
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.rdbms.mysql import MySQLManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFirewallRules(AzureRMModuleBase):
    """Configuration class for an Azure RM FirewallRules resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            parameters=dict(
                type='dict',
                required=False
            ),
            start_ip_address=dict(
                type='str',
                required=False
            ),
            end_ip_address=dict(
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
        self.server_name = None
        self.name = None
        self.start_ip_address = None
        self.end_ip_address = None

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFirewallRules, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(MySQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_firewallrules()

        if not old_response:
            self.log("FirewallRules instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("FirewallRules instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if FirewallRules instance has to be deleted or may be updated")
                if (self.start_ip_address is not None) and (self.start_ip_address != old_response['start_ip_address']):
                    self.to_do = Actions.Update
                if (self.end_ip_address is not None) and (self.end_ip_address != old_response['end_ip_address']):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the FirewallRules instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_firewallrules()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(self.results['state'])

            # remove unnecessary fields from return state
            self.results['state'].pop('name', None)
            self.results['state'].pop('type', None)
            self.results['state'].pop('start_ip_address', None)
            self.results['state'].pop('end_ip_address', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("FirewallRules instance deleted")
            self.delete_firewallrules()
            self.results['changed'] = True
        else:
            self.log("FirewallRules instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_firewallrules(self):
        '''
        Creates or updates FirewallRules with the specified configuration.

        :return: deserialized FirewallRules instance state dictionary
        '''
        self.log("Creating / Updating the FirewallRules instance {0}".format(self.name))

        try:
            response = self.mgmt_client.firewall_rules.create_or_update(self.resource_group,
                                                                        self.server_name,
                                                                        self.name,
                                                                        self.start_ip_address,
                                                                        self.end_ip_address)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the FirewallRules instance.')
            self.fail("Error creating the FirewallRules instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_firewallrules(self):
        '''
        Deletes specified FirewallRules instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the FirewallRules instance {0}".format(self.name))
        try:
            response = self.mgmt_client.firewall_rules.delete(self.resource_group,
                                                              self.server_name,
                                                              self.name)
        except CloudError as e:
            self.log('Error attempting to delete the FirewallRules instance.')
            self.fail("Error deleting the FirewallRules instance: {0}".format(str(e)))

        return True

    def get_firewallrules(self):
        '''
        Gets the properties of the specified FirewallRules.

        :return: deserialized FirewallRules instance state dictionary
        '''
        self.log("Checking if the FirewallRules instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.firewall_rules.get(self.resource_group,
                                                           self.server_name,
                                                           self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("FirewallRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the FirewallRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMFirewallRules()

if __name__ == '__main__':
    main()