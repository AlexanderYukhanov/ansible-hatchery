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
module: azure_rm_sqlgeobackuppolicy
version_added: "2.5"
short_description: Manage GeoBackupPolicies instance.
description:
    - Create, update and delete instance of GeoBackupPolicies.

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
    policy_state:
        description:
            - The state of the geo backup policy.
        required: True
        choices: ['disabled', 'enabled']

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) GeoBackupPolicies
    azure_rm_sqlgeobackuppolicy:
      resource_group: sqlcrudtest-4799
      server_name: sqlcrudtest-5961
      database_name: testdw
      geo_backup_policy_name: Default
      policy_state: NOT FOUND
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
state:
    description:
        - The state of the geo backup policy. Possible values include: C(Disabled), C(Enabled)
    returned: always
    type: str
    sample: state
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.sql import SqlManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


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
            policy_state=dict(
                type='str',
                choices=['disabled', 'enabled'],
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.server_name = None
        self.database_name = None
        self.geo_backup_policy_name = None
        self.policy_state = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGeoBackupPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                       supports_check_mode=True,
                                                       supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_geobackuppolicies()

        if not old_response:
            self.log("GeoBackupPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("GeoBackupPolicies instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if GeoBackupPolicies instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the GeoBackupPolicies instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_geobackuppolicies()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("GeoBackupPolicies instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_geobackuppolicies()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_geobackuppolicies():
                time.sleep(20)
        else:
            self.log("GeoBackupPolicies instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]

        return self.results

    def create_update_geobackuppolicies(self):
        '''
        Creates or updates GeoBackupPolicies with the specified configuration.

        :return: deserialized GeoBackupPolicies instance state dictionary
        '''
        self.log("Creating / Updating the GeoBackupPolicies instance {0}".format(self.geo_backup_policy_name))

        try:
            response = self.mgmt_client.geo_backup_policies.create_or_update(resource_group_name=self.resource_group,
                                                                             server_name=self.server_name,
                                                                             database_name=self.database_name,
                                                                             geo_backup_policy_name=self.geo_backup_policy_name,
                                                                             state=self.policy_state)
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
            response = self.mgmt_client.geo_backup_policies.get(resource_group_name=self.resource_group,
                                                                server_name=self.server_name,
                                                                database_name=self.database_name,
                                                                geo_backup_policy_name=self.geo_backup_policy_name)
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
