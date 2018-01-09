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
module: azure_rm_authorizationroledefinition_facts
version_added: "2.5"
short_description: Get Role Definition facts.
description:
    - Get facts of Role Definition.

options:
    scope:
        description:
            - The scope of the role definition.
        required: True
    role_definition_id:
        description:
            - The ID of the role definition.
        required: True

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Role Definition
    azure_rm_authorizationroledefinition_facts:
      scope: scope
      role_definition_id: role_definition_id
'''

RETURN = '''
    id:
        description:
            - The role definition ID.
        returned: always
        type: str
        sample: /subscriptions/subID/providers/Microsoft.Authorization/roleDefinitions/roleDefinitionId
    name:
        description:
            - The role definition name.
        returned: always
        type: str
        sample: roleDefinitionId
    type:
        description:
            - The role definition type.
        returned: always
        type: str
        sample: Microsoft.Authorization/roleDefinitions
    properties:
        description:
            - Role definition properties.
        returned: always
        type: complex
        sample: properties
        suboptions:
            description:
                description:
                    - The role definition description.
                returned: always
                type: str
                sample: Role description
            type:
                description:
                    - The role type.
                returned: always
                type: str
                sample: roletype
            permissions:
                description:
                    - Role definition permissions.
                returned: always
                type: complex
                sample: permissions
                suboptions:
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


class AzureRMRoleDefinitionsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            role_definition_id=dict(
                type='str',
                required=True
            )
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        self.scope = None
        self.role_definition_id = None
        super(AzureRMRoleDefinitionsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.scope is not None and
                self.role_definition_id is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Role Definition.

        :return: deserialized Role Definitioninstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.role_definitions.get(scope=self.scope,
                                                             role_definition_id=self.role_definition_id)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for RoleDefinitions.')

        if response is not None:
            results = response.as_dict()

        return results


def main():
    AzureRMRoleDefinitionsFacts()
if __name__ == '__main__':
    main()
