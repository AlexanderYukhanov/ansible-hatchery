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
module: azure_rm_authorizationroledefinition
version_added: "2.5"
short_description: Manage Role Definition instance.
description:
    - Create, update and delete instance of Role Definition.

options:
    scope:
        description:
            - The scope of the role definition.
        required: True
    role_definition_id:
        description:
            - The ID of the role definition.
        required: True
    properties_role_name:
        description:
            - The role name.
    properties_description:
        description:
            - The role definition description.
    properties_type:
        description:
            - The role type.
    properties_permissions:
        description:
            - Role definition permissions.
        type: list
        suboptions:
            actions:
                description:
                    - Allowed actions.
                type: list
            not_actions:
                description:
                    - Denied I(actions).
                type: list
    properties_assignable_scopes:
        description:
            - Role definition assignable scopes.
        type: list
    state:
      description:
        - Assert the state of the Role Definition.
        - Use 'present' to create or update an Role Definition and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Role Definition
    azure_rm_authorizationroledefinition:
      scope: scope
      role_definition_id: roleDefinitionId
'''

RETURN = '''
id:
    description:
        - The role definition ID.
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


class AzureRMRoleDefinitions(AzureRMModuleBase):
    """Configuration class for an Azure RM Role Definition resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            role_definition_id=dict(
                type='str',
                required=True
            ),
            properties_role_name=dict(
                type='str'
            ),
            properties_description=dict(
                type='str'
            ),
            properties_type=dict(
                type='str'
            ),
            properties_permissions=dict(
                type='list'
            ),
            properties_assignable_scopes=dict(
                type='list'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.role_definition_id = None
        self.role_definition = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRoleDefinitions, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "properties_role_name":
                    self.role_definition.setdefault("properties", {})["role_name"] = kwargs[key]
                elif key == "properties_description":
                    self.role_definition.setdefault("properties", {})["description"] = kwargs[key]
                elif key == "properties_type":
                    self.role_definition.setdefault("properties", {})["type"] = kwargs[key]
                elif key == "properties_permissions":
                    self.role_definition.setdefault("properties", {})["permissions"] = kwargs[key]
                elif key == "properties_assignable_scopes":
                    self.role_definition.setdefault("properties", {})["assignable_scopes"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        old_response = self.get_roledefinition()

        if not old_response:
            self.log("Role Definition instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Role Definition instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Role Definition instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Role Definition instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_roledefinition()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Role Definition instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_roledefinition()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_roledefinition():
                time.sleep(20)
        else:
            self.log("Role Definition instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_roledefinition(self):
        '''
        Creates or updates Role Definition with the specified configuration.

        :return: deserialized Role Definition instance state dictionary
        '''
        self.log("Creating / Updating the Role Definition instance {0}".format(self.role_definition_id))

        try:
            response = self.mgmt_client.role_definitions.create_or_update(scope=self.scope,
                                                                          role_definition_id=self.role_definition_id,
                                                                          role_definition=self.role_definition)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Role Definition instance.')
            self.fail("Error creating the Role Definition instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_roledefinition(self):
        '''
        Deletes specified Role Definition instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Role Definition instance {0}".format(self.role_definition_id))
        try:
            response = self.mgmt_client.role_definitions.delete(scope=self.scope,
                                                                role_definition_id=self.role_definition_id)
        except CloudError as e:
            self.log('Error attempting to delete the Role Definition instance.')
            self.fail("Error deleting the Role Definition instance: {0}".format(str(e)))

        return True

    def get_roledefinition(self):
        '''
        Gets the properties of the specified Role Definition.

        :return: deserialized Role Definition instance state dictionary
        '''
        self.log("Checking if the Role Definition instance {0} is present".format(self.role_definition_id))
        found = False
        try:
            response = self.mgmt_client.role_definitions.get(scope=self.scope,
                                                             role_definition_id=self.role_definition_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Role Definition instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Role Definition instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMRoleDefinitions()

if __name__ == '__main__':
    main()
