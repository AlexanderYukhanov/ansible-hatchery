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
module: azure_rm_postgresqlconfiguration
version_added: "2.5"
short_description: Manage Configurations instance
description:
    - Create, update and delete instance of Configurations

options:
    resource_group:
        description:
            - The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        required: True
    server_name:
        description:
            - The name of the server.
        required: True
    configuration_name:
        description:
            - The name of the server configuration.
        required: True
    value:
        description:
            - Value of the configuration.
    source:
        description:
            - Source of the configuration.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Configurations
    azure_rm_postgresqlconfiguration:
      resource_group: resource_group_name
      server_name: server_name
      configuration_name: configuration_name
      value: value
      source: source
'''

RETURN = '''
id:
    description:
        - Resource ID
    returned: always
    type: str
    sample: id
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMConfigurations(AzureRMModuleBase):
    """Configuration class for an Azure RM Configurations resource"""

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
            configuration_name=dict(
                type='str',
                required=True
            ),
            value=dict(
                type='str',
                required=False
            ),
            source=dict(
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
        self.configuration_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMConfigurations, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif key == "value" and kwargs[key] is not None:
                self.parameters.update({"value": kwargs[key]})
            elif key == "source" and kwargs[key] is not None:
                self.parameters.update({"source": kwargs[key]})

        old_response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(PostgreSQLManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_configurations()

        if not old_response:
            self.log("Configurations instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Configurations instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Configurations instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Configurations instance")

            if self.check_mode:
                return self.results

            response = self.create_update_configurations()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)

            self.results.update(response)

            # remove unnecessary fields from return state
            self.results.pop('name', None)
            self.results.pop('type', None)
            self.results.pop('value', None)
            self.results.pop('description', None)
            self.results.pop('default_value', None)
            self.results.pop('data_type', None)
            self.results.pop('allowed_values', None)
            self.results.pop('source', None)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Configurations instance deleted")
            self.delete_configurations()
            self.results['changed'] = True
        else:
            self.log("Configurations instance unchanged")
            self.results['state'] = old_response
            self.results['changed'] = False

        return self.results

    def create_update_configurations(self):
        '''
        Creates or updates Configurations with the specified configuration.

        :return: deserialized Configurations instance state dictionary
        '''
        self.log("Creating / Updating the Configurations instance {0}".format(self.configuration_name))

        try:
            response = self.mgmt_client.configurations.create_or_update(self.resource_group,
                                                                        self.server_name,
                                                                        self.configuration_name,
                                                                        self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Configurations instance.')
            self.fail("Error creating the Configurations instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_configurations(self):
        '''
        Deletes specified Configurations instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Configurations instance {0}".format(self.configuration_name))
        try:
            response = self.mgmt_client.configurations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Configurations instance.')
            self.fail("Error deleting the Configurations instance: {0}".format(str(e)))

        return True

    def get_configurations(self):
        '''
        Gets the properties of the specified Configurations.

        :return: deserialized Configurations instance state dictionary
        '''
        self.log("Checking if the Configurations instance {0} is present".format(self.configuration_name))
        found = False
        try:
            response = self.mgmt_client.configurations.get(self.resource_group,
                                                           self.server_name,
                                                           self.configuration_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Configurations instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Configurations instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMConfigurations()

if __name__ == '__main__':
    main()
