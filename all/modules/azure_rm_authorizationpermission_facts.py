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
module: azure_rm_authorizationpermission_facts
version_added: "2.5"
short_description: Get Permission facts.
description:
    - Get facts of Permission.

options:
    resource_group:
        description:
            - The name of the resource group containing the resource. The name is case insensitive.
        required: True
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
            - The name of the resource to get the permissions for.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Permission
    azure_rm_authorizationpermission_facts:
      resource_group: resource_group_name
      resource_provider_namespace: resource_provider_namespace
      parent_resource_path: parent_resource_path
      resource_type: resource_type
      resource_name: resource_name

  - name: List instances of Permission
    azure_rm_authorizationpermission_facts:
      resource_group: resource_group_name
'''

RETURN = '''
permissions:
    description: A list of dict results where the key is the name of the Permission and the values are the facts for that Permission.
    returned: always
    type: complex
    contains:
        permission_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
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


class AzureRMPermissionsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            resource_provider_namespace=dict(
                type='str'
            ),
            parent_resource_path=dict(
                type='str'
            ),
            resource_type=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
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
        super(AzureRMPermissionsFacts, self).__init__(self.module_arg_spec)

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
            self.results['permissions'] = self.list_for_resource()
        elif (self.resource_group is not None):
            self.results['permissions'] = self.list_for_resource_group()
        return self.results

    def list_for_resource(self):
        '''
        Gets facts of the specified Permission.

        :return: deserialized Permissioninstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.permissions.list_for_resource(resource_group_name=self.resource_group,
                                                                      resource_provider_namespace=self.resource_provider_namespace,
                                                                      parent_resource_path=self.parent_resource_path,
                                                                      resource_type=self.resource_type,
                                                                      resource_name=self.resource_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Permissions.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_for_resource_group(self):
        '''
        Gets facts of the specified Permission.

        :return: deserialized Permissioninstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.permissions.list_for_resource_group(resource_group_name=self.resource_group)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for Permissions.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMPermissionsFacts()
if __name__ == '__main__':
    main()
