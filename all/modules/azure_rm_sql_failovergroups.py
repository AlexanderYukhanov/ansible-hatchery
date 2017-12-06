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
module: azure_rm_sql_failovergroups
version_added: "2.5"
short_description: Manage FailoverGroups instance
description:
    - Create, update and delete instance of FailoverGroups

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server containing the failover group.
        required: True
    failover_group_name:
        description:
            - The name of the failover group.
        required: True
    tags:
        description:
            - Resource tags.
    read_write_endpoint:
        description:
            - Read-write endpoint of the failover group instance.
        required: True
        suboptions:
            failover_policy:
                description:
                    - "Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriod
                       Minutes is required. Possible values include: 'Manual', 'Automatic'"
                required: True
            failover_with_data_loss_grace_period_minutes:
                description:
                    - "Grace period before failover with data loss is attempted for the read-write endpoint. If failoverPolicy is Automatic then failoverWith
                       DataLossGracePeriodMinutes is required."
    read_only_endpoint:
        description:
            - Read-only endpoint of the failover group instance.
        suboptions:
            failover_policy:
                description:
                    - "Failover policy of the read-only endpoint for the failover group. Possible values include: 'Disabled', 'Enabled'"
    partner_servers:
        description:
            - List of partner server information for the failover group.
        required: True
        suboptions:
            id:
                description:
                    - Resource identifier of the partner server.
                required: True
    databases:
        description:
            - List of databases in the failover group.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) FailoverGroups
    azure_rm_sql_failovergroups:
      resource_group: resource_group_name
      server_name: server_name
      failover_group_name: failover_group_name
      tags: tags
      read_write_endpoint:
        failover_policy: failover_policy
        failover_with_data_loss_grace_period_minutes: failover_with_data_loss_grace_period_minutes
      read_only_endpoint:
        failover_policy: failover_policy
      partner_servers:
        id: id
      databases:
        - XXXX - list of values -- not implemented str
'''

RETURN = '''
state:
    description: Current state of FailoverGroups
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID.
            returned: always
            type: str
            sample: id
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFailoverGroups(AzureRMModuleBase):
    """Configuration class for an Azure RM FailoverGroups resource"""

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
            failover_group_name=dict(
                type='str',
                required=True
            ),
            tags=dict(
                type='dict',
                required=False
            ),
            read_write_endpoint=dict(
                type='dict',
                required=True
            ),
            read_only_endpoint=dict(
                type='dict',
                required=False
            ),
            partner_servers=dict(
                type='dict',
                required=True
            ),
            databases=dict(
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
        self.failover_group_name = None
        self.parameters = dict()

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFailoverGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif key == "tags":
                self.parameters["tags"] = kwargs[key]
            elif key == "read_write_endpoint":
                self.parameters["read_write_endpoint"] = kwargs[key]
            elif key == "read_only_endpoint":
                self.parameters["read_only_endpoint"] = kwargs[key]
            elif key == "partner_servers":
                self.parameters["partner_servers"] = kwargs[key]
            elif key == "databases":
                self.parameters["databases"] = kwargs[key]

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_failovergroups()

        if not old_response:
            self.log("FailoverGroups instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("FailoverGroups instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if FailoverGroups instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the FailoverGroups instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_failovergroups()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(self.results['state'])

            # remove unnecessary fields from return state
            self.results['state'].pop('name', None)
            self.results['state'].pop('type', None)
            self.results['state'].pop('location', None)
            self.results['state'].pop('tags', None)
            self.results['state'].pop('read_write_endpoint', None)
            self.results['state'].pop('read_only_endpoint', None)
            self.results['state'].pop('replication_role', None)
            self.results['state'].pop('replication_state', None)
            self.results['state'].pop('partner_servers', None)
            self.results['state'].pop('databases', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("FailoverGroups instance deleted")
            self.delete_failovergroups()
            self.results['changed'] = True
        else:
            self.log("FailoverGroups instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_failovergroups(self):
        '''
        Creates or updates FailoverGroups with the specified configuration.

        :return: deserialized FailoverGroups instance state dictionary
        '''
        self.log("Creating / Updating the FailoverGroups instance {0}".format(self.failover_group_name))

        try:
            response = self.mgmt_client.failover_groups.create_or_update(self.resource_group,
                                                                         self.server_name,
                                                                         self.failover_group_name,
                                                                         self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the FailoverGroups instance.')
            self.fail("Error creating the FailoverGroups instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_failovergroups(self):
        '''
        Deletes specified FailoverGroups instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the FailoverGroups instance {0}".format(self.failover_group_name))
        try:
            response = self.mgmt_client.failover_groups.delete(self.resource_group,
                                                               self.server_name,
                                                               self.failover_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the FailoverGroups instance.')
            self.fail("Error deleting the FailoverGroups instance: {0}".format(str(e)))

        return True

    def get_failovergroups(self):
        '''
        Gets the properties of the specified FailoverGroups.

        :return: deserialized FailoverGroups instance state dictionary
        '''
        self.log("Checking if the FailoverGroups instance {0} is present".format(self.failover_group_name))
        found = False
        try:
            response = self.mgmt_client.failover_groups.get(self.resource_group,
                                                            self.server_name,
                                                            self.failover_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("FailoverGroups instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the FailoverGroups instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMFailoverGroups()

if __name__ == '__main__':
    main()
