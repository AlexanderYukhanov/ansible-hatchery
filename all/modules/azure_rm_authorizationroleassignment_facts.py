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
short_description: Get RoleAssignments facts.
description:
    - Get facts of RoleAssignments.

options:
    resource_group:
        description:
            - The name of the resource group.
    resource_provider_namespace:
        description:
            - The namespace of the resource provider.
    parent_resource_path:
        description:
            - The parent resource identity.
    resource_type:
        description:
            - The resource type of the resource.
    resource_name:
        description:
            - The name of the resource to get role assignments for.
    filter:
        description:
            - "The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {
               id} to return all role assignments at, above or below the scope for the specified principal."
    scope:
        description:
            - The scope of the role assignment.
    role_assignment_name:
        description:
            - The name of the role assignment to get.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of RoleAssignments
    azure_rm_authorizationroleassignment_facts:
      resource_group: resource_group_name
      resource_provider_namespace: resource_provider_namespace
      parent_resource_path: parent_resource_path
      resource_type: resource_type
      resource_name: resource_name
      filter: filter

  - name: List instances of RoleAssignments
    azure_rm_authorizationroleassignment_facts:
      resource_group: resource_group_name
      filter: filter

  - name: Get instance of RoleAssignments
    azure_rm_authorizationroleassignment_facts:
      scope: scope
      role_assignment_name: role_assignment_name

  - name: List instances of RoleAssignments
    azure_rm_authorizationroleassignment_facts:
      scope: scope
      filter: filter
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
            resource_group=dict(
                type='str',
                required=False
            ),
            resource_provider_namespace=dict(
                type='str',
                required=False
            ),
            parent_resource_path=dict(
                type='str',
                required=False
            ),
            resource_type=dict(
                type='str',
                required=False
            ),
            resource_name=dict(
                type='str',
                required=False
            ),
            filter=dict(
                type='str',
                required=False
            ),
            scope=dict(
                type='str',
                required=False
            ),
            role_assignment_name=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.resource_group = None
        self.resource_provider_namespace = None
        self.parent_resource_path = None
        self.resource_type = None
        self.resource_name = None
        self.filter = None
        self.scope = None
        self.role_assignment_name = None
        super(AzureRMRoleAssignmentsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.resource_provider_namespace is not None and
                self.parent_resource_path is not None and
                self.resource_type is not None and
                self.resource_name is not None):
            self.results['ansible_facts']['list_for_resource'] = self.list_for_resource()
        elif (self.resource_group is not None):
            self.results['ansible_facts']['list_for_resource_group'] = self.list_for_resource_group()
        elif (self.scope is not None and
              self.role_assignment_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.scope is not None):
            self.results['ansible_facts']['list_for_scope'] = self.list_for_scope()
        return self.results

    def list_for_resource(self):
        '''
        Gets facts of the specified RoleAssignments.

        :return: deserialized RoleAssignmentsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.role_assignments.list_for_resource(self.resource_group,
                                                                           self.resource_provider_namespace,
                                                                           self.parent_resource_path,
                                                                           self.resource_type,
                                                                           self.resource_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def list_for_resource_group(self):
        '''
        Gets facts of the specified RoleAssignments.

        :return: deserialized RoleAssignmentsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.role_assignments.list_for_resource_group(self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results

    def get(self):
        '''
        Gets facts of the specified RoleAssignments.

        :return: deserialized RoleAssignmentsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.role_assignments.get(self.scope,
                                                             self.role_assignment_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_for_scope(self):
        '''
        Gets facts of the specified RoleAssignments.

        :return: deserialized RoleAssignmentsinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.role_assignments.list_for_scope(self.scope)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleAssignments.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMRoleAssignmentsFacts()
if __name__ == '__main__':
    main()
