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
module: azure_rm_batchmanagementapplication
version_added: "2.5"
short_description: Manage Application instance.
description:
    - Create, update and delete instance of Application.

options:
    resource_group:
        description:
            - The name of the resource group that contains the Batch account.
        required: True
    account_name:
        description:
            - The name of the Batch account.
        required: True
    application_id:
        description:
            - The ID of the application.
        required: True
    allow_updates:
        description:
            - A value indicating whether packages within the application may be overwritten using the same version string.
    display_name:
        description:
            - The display name for the application.
    state:
      description:
        - Assert the state of the Application.
        - Use 'present' to create or update an Application and 'absent' to delete it.
      default: present
      choices:
        - absent
        - present

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) Application
    azure_rm_batchmanagementapplication:
      resource_group: NOT FOUND
      account_name: NOT FOUND
      application_id: NOT FOUND
'''

RETURN = '''
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.batch import BatchManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApplication(AzureRMModuleBase):
    """Configuration class for an Azure RM Application resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            application_id=dict(
                type='str',
                required=True
            ),
            allow_updates=dict(
                type='str'
            ),
            display_name=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.application_id = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplication, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                 supports_check_mode=True,
                                                 supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "allow_updates":
                    self.parameters["allow_updates"] = kwargs[key]
                elif key == "display_name":
                    self.parameters["display_name"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_application()

        if not old_response:
            self.log("Application instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Application instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Application instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Application instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_application()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = False
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Application instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_application()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_application():
                time.sleep(20)
        else:
            self.log("Application instance unchanged")
            self.results['changed'] = False
            response = old_response


        return self.results

    def create_update_application(self):
        '''
        Creates or updates Application with the specified configuration.

        :return: deserialized Application instance state dictionary
        '''
        self.log("Creating / Updating the Application instance {0}".format(self.application_id))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.application.create(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               application_id=self.application_id)
            else:
                response = self.mgmt_client.application.update(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               application_id=self.application_id,
                                                               parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Application instance.')
            self.fail("Error creating the Application instance: {0}".format(str(exc)))
        if response is not None:
            return response.as_dict()
        else:
            return None

    def delete_application(self):
        '''
        Deletes specified Application instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Application instance {0}".format(self.application_id))
        try:
            response = self.mgmt_client.application.delete(resource_group_name=self.resource_group,
                                                           account_name=self.account_name,
                                                           application_id=self.application_id)
        except CloudError as e:
            self.log('Error attempting to delete the Application instance.')
            self.fail("Error deleting the Application instance: {0}".format(str(e)))

        return True

    def get_application(self):
        '''
        Gets the properties of the specified Application.

        :return: deserialized Application instance state dictionary
        '''
        self.log("Checking if the Application instance {0} is present".format(self.application_id))
        found = False
        try:
            response = self.mgmt_client.application.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        application_id=self.application_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Application instance : {0} found".format(response.id))
        except CloudError as e:
            self.log('Did not find the Application instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMApplication()

if __name__ == '__main__':
    main()
