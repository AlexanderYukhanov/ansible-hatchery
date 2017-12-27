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
module: azure_rm_authorizationroleassignment
version_added: "2.5"
short_description: Manage RoleAssignments instance.
description:
    - Create, update and delete instance of RoleAssignments.

options:
    scope:
        description:
            - "The scope of the role assignment to create. The scope can be any REST resource instance. For example, use C(/subscriptions/{subscription-id}/)
                for a subscription, C(/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}) for a resource group, and C(/subscriptions/{subs
               cription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}) for a resource."
        required: True
    role_assignment_name:
        description:
            - The name of the role assignment to create. It can be any valid GUID.
        required: True
    parameters:
        description:
            - Parameters for the role assignment.
    properties:
        description:
            - Role assignment properties.
        suboptions:
            role_definition_id:
                description:
                    - The role definition ID used in the role assignment.
            principal_id:
                description:
                    - "The principal ID assigned to the role. This maps to the ID inside the Active Directory. It can point to a user, service principal, or
                       security group."

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) RoleAssignments
    azure_rm_authorizationroleassignment:
      scope: scope
      role_assignment_name: roleAssignmentName
      parameters: parameters
      properties:
        role_definition_id: /subscriptions/4004a9fd-d58e-48dc-aeb2-4a4aec58606f/providers/Microsoft.Authorization/roleDefinitions/de139f84-1756-47ae-9be6-808fbbe84772
        principal_id: d93a38bc-d029-4160-bfb0-fbda779ac214
'''

RETURN = '''
id:
    description:
        - The role assignment ID.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRoleAssignments(AzureRMModuleBase):
    """Configuration class for an Azure RM RoleAssignments resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            role_assignment_name=dict(
                type='str',
                required=True
            ),
            parameters=dict(
                type='dict'
            ),
            properties=dict(
                type='dict'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.role_assignment_name = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRoleAssignments, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-07-01')

        old_response = self.get_roleassignments()

        if not old_response:
            self.log("RoleAssignments instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("RoleAssignments instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if RoleAssignments instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the RoleAssignments instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_roleassignments()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("RoleAssignments instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_roleassignments()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_roleassignments():
                time.sleep(20)
        else:
            self.log("RoleAssignments instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_roleassignments(self):
        '''
        Creates or updates RoleAssignments with the specified configuration.

        :return: deserialized RoleAssignments instance state dictionary
        '''
        self.log("Creating / Updating the RoleAssignments instance {0}".format(self.role_assignment_name))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.role_assignments.create(scope=self.scope,
                                                                    role_assignment_name=self.role_assignment_name,
                                                                    properties=self.properties)
            else:
                response = self.mgmt_client.role_assignments.update()
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the RoleAssignments instance.')
            self.fail("Error creating the RoleAssignments instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_roleassignments(self):
        '''
        Deletes specified RoleAssignments instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the RoleAssignments instance {0}".format(self.role_assignment_name))
        try:
            response = self.mgmt_client.role_assignments.delete(scope=self.scope,
                                                                role_assignment_name=self.role_assignment_name)
        except CloudError as e:
            self.log('Error attempting to delete the RoleAssignments instance.')
            self.fail("Error deleting the RoleAssignments instance: {0}".format(str(e)))

        return True

    def get_roleassignments(self):
        '''
        Gets the properties of the specified RoleAssignments.

        :return: deserialized RoleAssignments instance state dictionary
        '''
        self.log("Checking if the RoleAssignments instance {0} is present".format(self.role_assignment_name))
        found = False
        try:
            response = self.mgmt_client.role_assignments.get(scope=self.scope,
                                                             role_assignment_name=self.role_assignment_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RoleAssignments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RoleAssignments instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMRoleAssignments()

if __name__ == '__main__':
    main()
