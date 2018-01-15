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
module: azure_rm_sqlsyncgroup_facts
version_added: "2.5"
short_description: Get Sync Group facts.
description:
    - Get facts of Sync Group.

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    server_name:
        description:
            - The name of the server.
    database_name:
        description:
            - The name of the database on which the sync group is hosted.
    sync_group_name:
        description:
            - The name of the sync group.
    start_time:
        description:
            - Get logs generated after this time.
    end_time:
        description:
            - Get logs generated before this time.
    type:
        description:
            - The types of logs to retrieve.
    continuation_token:
        description:
            - The continuation token for this operation.
    location_name:
        description:
            - The name of the region where the resource is located.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Sync Group
    azure_rm_sqlsyncgroup_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name
      start_time: start_time
      end_time: end_time
      type: type
      continuation_token: continuation_token

  - name: List instances of Sync Group
    azure_rm_sqlsyncgroup_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name

  - name: Get instance of Sync Group
    azure_rm_sqlsyncgroup_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      sync_group_name: sync_group_name

  - name: List instances of Sync Group
    azure_rm_sqlsyncgroup_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name

  - name: List instances of Sync Group
    azure_rm_sqlsyncgroup_facts:
      location_name: location_name
'''

RETURN = '''
sync_groups:
    description: A list of dict results where the key is the name of the Sync Group and the values are the facts for that Sync Group.
    returned: always
    type: complex
    contains:
        syncgroup_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/syncgroupcrud-3521/providers/Microsoft.Sql/servers/syncgroupc
                            rud-8475/databases/syncgroupcrud-4328/syncGroups/syncgroupcrud-3187"
                name:
                    description:
                        - Resource name.
                    returned: always
                    type: str
                    sample: syncgroupcrud-3187
                type:
                    description:
                        - Resource type.
                    returned: always
                    type: str
                    sample: Microsoft.Sql/servers/databases/syncGroups
                interval:
                    description:
                        - Sync interval of the sync group.
                    returned: always
                    type: int
                    sample: -1
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


class AzureRMSyncGroupsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            server_name=dict(
                type='str'
            ),
            database_name=dict(
                type='str'
            ),
            sync_group_name=dict(
                type='str'
            ),
            start_time=dict(
                type='str'
            ),
            end_time=dict(
                type='str'
            ),
            type=dict(
                type='str'
            ),
            continuation_token=dict(
                type='str'
            ),
            location_name=dict(
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
        self.server_name = None
        self.database_name = None
        self.sync_group_name = None
        self.start_time = None
        self.end_time = None
        self.type = None
        self.continuation_token = None
        self.location_name = None
        super(AzureRMSyncGroupsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.sync_group_name is not None and
                self.start_time is not None and
                self.end_time is not None and
                self.type is not None):
            self.results['sync_groups'] = self.list_logs()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None):
            self.results['sync_groups'] = self.list_hub_schemas()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.database_name is not None and
              self.sync_group_name is not None):
            self.results['sync_groups'] = self.get()
        elif (self.resource_group is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['sync_groups'] = self.list_by_database()
        elif (self.location_name is not None):
            self.results['sync_groups'] = self.list_sync_database_ids()
        return self.results

    def list_logs(self):
        '''
        Gets facts of the specified Sync Group.

        :return: deserialized Sync Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.sync_groups.list_logs(resource_group_name=self.resource_group,
                                                              server_name=self.server_name,
                                                              database_name=self.database_name,
                                                              sync_group_name=self.sync_group_name,
                                                              start_time=self.start_time,
                                                              end_time=self.end_time,
                                                              type=self.type)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SyncGroups.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_hub_schemas(self):
        '''
        Gets facts of the specified Sync Group.

        :return: deserialized Sync Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.sync_groups.list_hub_schemas(resource_group_name=self.resource_group,
                                                                     server_name=self.server_name,
                                                                     database_name=self.database_name,
                                                                     sync_group_name=self.sync_group_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SyncGroups.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def get(self):
        '''
        Gets facts of the specified Sync Group.

        :return: deserialized Sync Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.sync_groups.get(resource_group_name=self.resource_group,
                                                        server_name=self.server_name,
                                                        database_name=self.database_name,
                                                        sync_group_name=self.sync_group_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SyncGroups.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list_by_database(self):
        '''
        Gets facts of the specified Sync Group.

        :return: deserialized Sync Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.sync_groups.list_by_database(resource_group_name=self.resource_group,
                                                                     server_name=self.server_name,
                                                                     database_name=self.database_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SyncGroups.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results

    def list_sync_database_ids(self):
        '''
        Gets facts of the specified Sync Group.

        :return: deserialized Sync Groupinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.sync_groups.list_sync_database_ids(location_name=self.location_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for SyncGroups.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMSyncGroupsFacts()
if __name__ == '__main__':
    main()
