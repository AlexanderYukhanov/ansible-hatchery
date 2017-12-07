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
short_description: Get Permissions facts.
description:
    - Get facts of Permissions.

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
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Permissions
    azure_rm_authorizationpermission_facts:
      resource_group: resource_group_name
      resource_provider_namespace: resource_provider_namespace
      parent_resource_path: parent_resource_path
      resource_type: resource_type
      resource_name: resource_name

  - name: List instances of Permissions
    azure_rm_authorizationpermission_facts:
      resource_group: resource_group_name
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
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.resource_provider_namespace = None
        self.parent_resource_path = None
        self.resource_type = None
        self.resource_name = None
        super(AzureRMPermissionsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.resource_provider_namespace is not None and
                self.parent_resource_path is not None and
                self.resource_type is not None and
                self.resource_name is not None):
            self.results['ansible_facts']['list_for_resource'] = self.list_for_resource()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_for_resource_group'] = self.list_for_resource_group()
        return self.results

    def list_for_resource(self):
        '''
        Gets facts of the specified Permissions.

        :return: deserialized Permissionsinstance state dictionary
        '''
        self.log("Checking if the Permissions instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.permissions.list_for_resource(self.resource_group,
                                                                      self.resource_provider_namespace,
                                                                      self.parent_resource_path,
                                                                      self.resource_type,
                                                                      self.resource_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Permissions instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Permissions instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_for_resource_group(self):
        '''
        Gets facts of the specified Permissions.

        :return: deserialized Permissionsinstance state dictionary
        '''
        self.log("Checking if the Permissions instance {0} is present".format(self.))
        found = False
        try:
            response = self.mgmt_client.permissions.list_for_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Permissions instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Permissions instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMPermissionsFacts()
if __name__ == '__main__':
    main()
