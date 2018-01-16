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
module: azure_rm_authorizationroleassignment_facts
version_added: "2.5"
short_description: Get Role Assignment facts.
description:
    - Get facts of Role Assignment.

options:
    scope:
        description:
            - The scope of the role assignment.
    role_assignment_name:
        description:
            - The name of the role assignment to get.
    filter:
        description:
            - "The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {
              id} to return all role assignments at, above or below the scope for the specified principal."

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Role Assignment
    azure_rm_authorizationroleassignment_facts:
      scope: scope
      role_assignment_name: role_assignment_name

  - name: List instances of Role Assignment
    azure_rm_authorizationroleassignment_facts:
      filter: filter
'''

RETURN = '''
role_assignments:
    description: A list of dict results where the key is the name of the Role Assignment and the values are the facts for that Role Assignment.
    returned: always
    type: complex
    contains:
        roleassignment_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - The role assignment ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subId/resourcegroups/rgname/providers/Microsoft.Authorization/roleAssignments/roleassignmentId
                name:
                    description:
                        - The role assignment name.
                    returned: always
                    type: str
                    sample: raId
                type:
                    description:
                        - The role assignment type.
                    returned: always
                    type: str
                    sample: Microsoft.Authorization/roleAssignments
                properties:
                    description:
                        - Role assignment properties.
                    returned: always
                    type: complex
                    sample: properties
                    contains:
                        scope:
                            description:
                                - The role assignment scope.
                            returned: always
                            type: str
                            sample: /subscriptions/subId/resourcegroups/rgname
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRoleAssignmentsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            scope=dict(
                type='str'
            ),
            role_assignment_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.scope = None
        self.role_assignment_name = None
        self.filter = None
        super(AzureRMRoleAssignmentsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.scope is not None and
                self.role_assignment_name is not None):
            self.results['role_assignments'] = self.get()
            self.results['role_assignments'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Role Assignment.

        :return: deserialized Role Assignmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.role_assignments.get(scope=self.scope,
                                                             role_assignment_name=self.role_assignment_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Role Assignment.

        :return: deserialized Role Assignmentinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.role_assignments.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMRoleAssignmentsFacts()
if __name__ == '__main__':
    main()
