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
module: azure_rm_appgwapplicationsecuritygroup
version_added: "2.5"
short_description: Manage Application Security Group instance.
description:
    - Create, update and delete instance of Application Security Group.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    application_security_group_name:
        description:
            - The name of the application security group.
        required: True
    id:
        description:
            - Resource ID.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    state:
      description:
        - Assert the state of the Application Security Group.
        - Use 'present' to create or update an Application Security Group and 'absent' to delete it.
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
  - name: Create (or update) Application Security Group
    azure_rm_appgwapplicationsecuritygroup:
      resource_group: rg1
      application_security_group_name: test-asg
      location: eastus
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/applicationSecurityGroups/test-asg
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApplicationSecurityGroups(AzureRMModuleBase):
    """Configuration class for an Azure RM Application Security Group resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            application_security_group_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.application_security_group_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplicationSecurityGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                               supports_check_mode=True,
                                                               supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.parameters["id"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_applicationsecuritygroup()

        if not old_response:
            self.log("Application Security Group instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Application Security Group instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Application Security Group instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Application Security Group instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_applicationsecuritygroup()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Application Security Group instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_applicationsecuritygroup()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_applicationsecuritygroup():
                time.sleep(20)
        else:
            self.log("Application Security Group instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_applicationsecuritygroup(self):
        '''
        Creates or updates Application Security Group with the specified configuration.

        :return: deserialized Application Security Group instance state dictionary
        '''
        self.log("Creating / Updating the Application Security Group instance {0}".format(self.application_security_group_name))

        try:
            response = self.mgmt_client.application_security_groups.create_or_update(resource_group_name=self.resource_group,
                                                                                     application_security_group_name=self.application_security_group_name,
                                                                                     parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Application Security Group instance.')
            self.fail("Error creating the Application Security Group instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_applicationsecuritygroup(self):
        '''
        Deletes specified Application Security Group instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Application Security Group instance {0}".format(self.application_security_group_name))
        try:
            response = self.mgmt_client.application_security_groups.delete(resource_group_name=self.resource_group,
                                                                           application_security_group_name=self.application_security_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Application Security Group instance.')
            self.fail("Error deleting the Application Security Group instance: {0}".format(str(e)))

        return True

    def get_applicationsecuritygroup(self):
        '''
        Gets the properties of the specified Application Security Group.

        :return: deserialized Application Security Group instance state dictionary
        '''
        self.log("Checking if the Application Security Group instance {0} is present".format(self.application_security_group_name))
        found = False
        try:
            response = self.mgmt_client.application_security_groups.get(resource_group_name=self.resource_group,
                                                                        application_security_group_name=self.application_security_group_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Application Security Group instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Application Security Group instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMApplicationSecurityGroups()

if __name__ == '__main__':
    main()
