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
module: azure_rm_sqldatamaskingpolicy
version_added: "2.5"
short_description: Manage DataMaskingPolicies instance
description:
    - Create, update and delete instance of DataMaskingPolicies

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
    data_masking_policy_name:
        description:
            - The name of the database for which the data masking rule applies.
        required: True
    data_masking_state:
        description:
            - "The state of the data masking policy. Possible values include: 'Disabled', 'Enabled'"
        required: True
    exempt_principals:
        description:
            - "The list of the exempt principals. Specifies the semicolon-separated list of database users for which the data masking policy does not apply.
               The specified users receive data results without masking for all of the database queries."

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) DataMaskingPolicies
    azure_rm_sqldatamaskingpolicy:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      data_masking_policy_name: data_masking_policy_name
      data_masking_state: data_masking_state
      exempt_principals: exempt_principals
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
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


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataMaskingPolicies(AzureRMModuleBase):
    """Configuration class for an Azure RM DataMaskingPolicies resource"""

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
            data_masking_policy_name=dict(
                type='str',
                required=True
            ),
            data_masking_state=dict(
                type='str',
                required=True
            ),
            exempt_principals=dict(
                type='str',
                required=False
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
        self.data_masking_policy_name = None
        self.data_masking_state = None
        self.exempt_principals = None

        self.results = dict(changed=False, state=dict())
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataMaskingPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        old_response = self.get_datamaskingpolicies()

        if not old_response:
            self.log("DataMaskingPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("DataMaskingPolicies instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if DataMaskingPolicies instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the DataMaskingPolicies instance")

            if self.check_mode:
                return self.results

            response = self.create_update_datamaskingpolicies()
            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.results.update(response)

            # remove unnecessary fields from return state
            self.results.pop('name', None)
            self.results.pop('type', None)
            self.results.pop('data_masking_state', None)
            self.results.pop('exempt_principals', None)
            self.results.pop('application_principals', None)
            self.results.pop('masking_level', None)
            self.results.pop('location', None)
            self.results.pop('kind', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("DataMaskingPolicies instance deleted")
            self.delete_datamaskingpolicies()
            self.results['changed'] = True
        else:
            self.log("DataMaskingPolicies instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_datamaskingpolicies(self):
        '''
        Creates or updates DataMaskingPolicies with the specified configuration.

        :return: deserialized DataMaskingPolicies instance state dictionary
        '''
        self.log("Creating / Updating the DataMaskingPolicies instance {0}".format(self.data_masking_policy_name))

        try:
            response = self.mgmt_client.data_masking_policies.create_or_update(self.resource_group,
                                                                               self.server_name,
                                                                               self.database_name,
                                                                               self.data_masking_policy_name,
                                                                               self.data_masking_state)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the DataMaskingPolicies instance.')
            self.fail("Error creating the DataMaskingPolicies instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_datamaskingpolicies(self):
        '''
        Deletes specified DataMaskingPolicies instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the DataMaskingPolicies instance {0}".format(self.data_masking_policy_name))
        try:
            response = self.mgmt_client.data_masking_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DataMaskingPolicies instance.')
            self.fail("Error deleting the DataMaskingPolicies instance: {0}".format(str(e)))

        return True

    def get_datamaskingpolicies(self):
        '''
        Gets the properties of the specified DataMaskingPolicies.

        :return: deserialized DataMaskingPolicies instance state dictionary
        '''
        self.log("Checking if the DataMaskingPolicies instance {0} is present".format(self.data_masking_policy_name))
        found = False
        try:
            response = self.mgmt_client.data_masking_policies.get(self.resource_group,
                                                                  self.server_name,
                                                                  self.database_name,
                                                                  self.data_masking_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("DataMaskingPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DataMaskingPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMDataMaskingPolicies()

if __name__ == '__main__':
    main()