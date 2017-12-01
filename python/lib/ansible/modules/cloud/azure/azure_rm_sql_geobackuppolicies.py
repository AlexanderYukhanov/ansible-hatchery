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
module: azure_rm_sql_geobackuppolicies
version_added: "2.5"
short_description: Manage GeoBackupPolicies instance
description:
    - Create, update and delete instance of GeoBackupPolicies

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
            - The name of the database.
        required: True
    geo_backup_policy_name:
        description:
            - The name of the geo backup policy.
        required: True
    state:
        description:
            - "The state of the geo backup policy. Possible values include: 'Disabled', 'Enabled'"
        required: True

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) GeoBackupPolicies
    azure_rm_sql_geobackuppolicies:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      geo_backup_policy_name: geo_backup_policy_name
      state: state
'''

RETURN = '''
state:
    description: Current state of GeoBackupPolicies
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource ID.
            returned: always
            type: str
            sample: id
        name:
            description:
                - Resource name.
            returned: always
            type: str
            sample: name
        type:
            description:
                - Resource type.
            returned: always
            type: str
            sample: type
        state:
            description:
                - "The state of the geo backup policy. Possible values include: 'Disabled', 'Enabled'"
            returned: always
            type: str
            sample: state
        storage_type:
            description:
                - The storage type of the geo backup policy.
            returned: always
            type: str
            sample: storage_type
        kind:
            description:
                - Kind of geo backup policy.  This is metadata used for the Azure portal experience.
            returned: always
            type: str
            sample: kind
        location:
            description:
                - Backup policy location.
            returned: always
            type: str
            sample: location
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


class AzureRMGeoBackupPolicies(AzureRMModuleBase):
    """Configuration class for an Azure RM GeoBackupPolicies resource"""

    def __init__(self):
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
            geo_backup_policy_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                required=False,
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.server_name = None
        self.database_name = None
        self.geo_backup_policy_name = None
        self.state = None

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None

        super(AzureRMGeoBackupPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                       supports_check_mode=True,
                                                       supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        try:
            resource_group = self.get_resource_group(self.resource_group)
        except CloudError:
            self.fail('resource group {0} not found'.format(self.resource_group))

        old_response = self.get_geobackuppolicies()

        if not old_response:
            self.log("GeoBackupPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
        else:
            self.log("GeoBackupPolicies instance already exists")
            if self.state == 'absent':
                self.delete_geobackuppolicies()
                self.results['changed'] = True
                self.log("GeoBackupPolicies instance deleted")
            elif self.state == 'present':
                self.log("Need to check if GeoBackupPolicies instance has to be deleted or may be updated")

        if self.state == 'present':

            self.log("Need to Create / Update the GeoBackupPolicies instance")

            if self.check_mode:
                return self.results

            self.results['state'] = self.create_update_geobackuppolicies()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = (cmp(old_response, self.results['state']) != 0)

            self.log("Creation / Update done")

        return self.results

    def create_update_geobackuppolicies(self):
        '''
        Creates or updates GeoBackupPolicies with the specified configuration.

        :return: deserialized GeoBackupPolicies instance state dictionary
        '''
        self.log("Creating / Updating the GeoBackupPolicies instance {0}".format(self.geo_backup_policy_name))

        try:
            response = self.mgmt_client.geo_backup_policies.create_or_update(self.resource_group,
                                                                             self.server_name,
                                                                             self.database_name,
                                                                             self.geo_backup_policy_name,
                                                                             self.state)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the GeoBackupPolicies instance.')
            self.fail("Error creating the GeoBackupPolicies instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_geobackuppolicies(self):
        '''
        Deletes specified GeoBackupPolicies instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the GeoBackupPolicies instance {0}".format(self.geo_backup_policy_name))
        try:
            response = self.mgmt_client.geo_backup_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the GeoBackupPolicies instance.')
            self.fail("Error deleting the GeoBackupPolicies instance: {0}".format(str(e)))

        return True

    def get_geobackuppolicies(self):
        '''
        Gets the properties of the specified GeoBackupPolicies.

        :return: deserialized GeoBackupPolicies instance state dictionary
        '''
        self.log("Checking if the GeoBackupPolicies instance {0} is present".format(self.geo_backup_policy_name))
        found = False
        try:
            response = self.mgmt_client.geo_backup_policies.get(self.resource_group,
                                                                self.server_name,
                                                                self.database_name,
                                                                self.geo_backup_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("GeoBackupPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the GeoBackupPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMGeoBackupPolicies()

if __name__ == '__main__':
    main()
