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
short_description: Get RoleDefinitions facts.
description:
    - Get facts of RoleDefinitions.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of RoleDefinitions
    azure_rm_authorizationroledefinition_facts:
      scope: scope
      role_definition_id: role_definition_id
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
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.scope = None
        self.role_definition_id = None
        super(AzureRMRoleDefinitionsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.scope is not None and
                self.role_definition_id is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified RoleDefinitions.

        :return: deserialized RoleDefinitionsinstance state dictionary
        '''
        self.log("Checking if the RoleDefinitions instance {0} is present".format(self.role_definition_id))
        found = False
        try:
            response = self.mgmt_client.role_definitions.get(self.scope,
                                                             self.role_definition_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RoleDefinitions instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RoleDefinitions instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMRoleDefinitionsFacts()
if __name__ == '__main__':
    main()
