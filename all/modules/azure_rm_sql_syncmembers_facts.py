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
module: azure_rm_sql_syncmembers_facts
version_added: "2.5"
short_description: Get SyncMembers facts.
description:
    - Get facts of SyncMembers.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    database_name:
        description:
            - The name of the database on which the sync group is hosted.
        required: True
    sync_group_name:
        description:
            - The name of the sync group on which the sync member is hosted.
        required: True
    sync_member_name:
        description:
            - The name of the sync member.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of SyncMembers
    azure_rm_sql_syncmembers_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name
      sync_member_name: sync_member_name

  - name: List instances of SyncMembers
    azure_rm_sql_syncmembers_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name
      sync_member_name: sync_member_name

  - name: List instances of SyncMembers
    azure_rm_sql_syncmembers_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name
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


class AzureRMSyncMembersFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            sync_group_name=dict(
                type='str',
                required=True
            ),
            sync_member_name=dict(
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
        self.server_name = None
        self.database_name = None
        self.sync_group_name = None
        self.sync_member_name = None
        super(AzureRMSyncMembersFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.sync_group_name is not None and
                self.sync_member_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None and
              self.sync_member_name is not None):
            self.results['ansible_facts']['list_member_schemas'] = self.list_member_schemas()
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None):
            self.results['ansible_facts']['list_by_sync_group'] = self.list_by_sync_group()
        return self.results

    def get(self):
        '''
        Gets facts of the specified SyncMembers.

        :return: deserialized SyncMembersinstance state dictionary
        '''
        self.log("Checking if the SyncMembers instance {0} is present".format(self.sync_member_name))
        found = False
        try:
            response = self.mgmt_client.sync_members.get(self.resource_group,
                                                         self.server_name,
                                                         self.database_name,
                                                         self.sync_group_name,
                                                         self.sync_member_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SyncMembers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SyncMembers instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_member_schemas(self):
        '''
        Gets facts of the specified SyncMembers.

        :return: deserialized SyncMembersinstance state dictionary
        '''
        self.log("Checking if the SyncMembers instance {0} is present".format(self.sync_member_name))
        found = False
        try:
            response = self.mgmt_client.sync_members.list_member_schemas(self.resource_group,
                                                                         self.server_name,
                                                                         self.database_name,
                                                                         self.sync_group_name,
                                                                         self.sync_member_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SyncMembers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SyncMembers instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_sync_group(self):
        '''
        Gets facts of the specified SyncMembers.

        :return: deserialized SyncMembersinstance state dictionary
        '''
        self.log("Checking if the SyncMembers instance {0} is present".format(self.sync_member_name))
        found = False
        try:
            response = self.mgmt_client.sync_members.list_by_sync_group(self.resource_group,
                                                                        self.server_name,
                                                                        self.database_name,
                                                                        self.sync_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("SyncMembers instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SyncMembers instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMSyncMembersFacts()
if __name__ == '__main__':
    main()