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
module: azure_rm_sqldatabasethreatdetectionpolicy
version_added: "2.5"
short_description: Manage DatabaseThreatDetectionPolicies instance.
description:
    - Create, update and delete instance of DatabaseThreatDetectionPolicies.

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
            - The name of the database for which database Threat Detection policy is defined.
        required: True
    security_alert_policy_name:
        description:
            - The name of the security alert policy.
        required: True
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    state:
        description:
            - Specifies the state of the policy. If state is Enabled, storageEndpoint and storageAccountAccessKey are required.
        required: True
        choices: ['new', 'enabled', 'disabled']
    disabled_alerts:
        description:
            - "Specifies the semicolon-separated list of alerts that are disabled, or empty string to disable no alerts. Possible values: Sql_Injection; Sql_
               Injection_Vulnerability; Access_Anomaly; Usage_Anomaly."
    email_addresses:
        description:
            - Specifies the semicolon-separated list of e-mail addresses to which the alert is sent.
    email_account_admins:
        description:
            - Specifies that the alert is sent to the account administrators.
        choices: ['enabled', 'disabled']
    storage_endpoint:
        description:
            - "Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit log
               s. If state is Enabled, storageEndpoint is required."
    storage_account_access_key:
        description:
            - Specifies the identifier key of the Threat Detection audit storage account. If state is Enabled, storageAccountAccessKey is required.
    retention_days:
        description:
            - Specifies the number of days to keep in the Threat Detection audit logs.
    use_server_default:
        description:
            - Specifies whether to use the default server policy.
        choices: ['enabled', 'disabled']

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) DatabaseThreatDetectionPolicies
    azure_rm_sqldatabasethreatdetectionpolicy:
      resource_group: securityalert-4799
      server_name: securityalert-6440
      database_name: testdb
      security_alert_policy_name: default
      location: eastus
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
        - "Specifies the state of the policy. If state is Enabled, storageEndpoint and storageAccountAccessKey are required. Possible values include: C(New),
            C(Enabled), C(Disabled)"
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


class AzureRMDatabaseThreatDetectionPolicies(AzureRMModuleBase):
    """Configuration class for an Azure RM DatabaseThreatDetectionPolicies resource"""

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
            security_alert_policy_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str'
            ),
            state=dict(
                type='str',
                choices=['new', 'enabled', 'disabled'],
                required=True
            ),
            disabled_alerts=dict(
                type='str'
            ),
            email_addresses=dict(
                type='str'
            ),
            email_account_admins=dict(
                type='str',
                choices=['enabled', 'disabled']
            ),
            storage_endpoint=dict(
                type='str'
            ),
            storage_account_access_key=dict(
                type='str'
            ),
            retention_days=dict(
                type='int'
            ),
            use_server_default=dict(
                type='str',
                choices=['enabled', 'disabled']
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
        self.security_alert_policy_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabaseThreatDetectionPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                     supports_check_mode=True,
                                                                     supports_tags=False)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "location":
                    self.parameters["location"] = kwargs[key]
                elif key == "state":
                    ev = kwargs[key]
                    if ev == 'new':
                        ev = 'New'
                    elif ev == 'enabled':
                        ev = 'Enabled'
                    elif ev == 'disabled':
                        ev = 'Disabled'
                    self.parameters["state"] = ev
                elif key == "disabled_alerts":
                    self.parameters["disabled_alerts"] = kwargs[key]
                elif key == "email_addresses":
                    self.parameters["email_addresses"] = kwargs[key]
                elif key == "email_account_admins":
                    ev = kwargs[key]
                    if ev == 'enabled':
                        ev = 'Enabled'
                    elif ev == 'disabled':
                        ev = 'Disabled'
                    self.parameters["email_account_admins"] = ev
                elif key == "storage_endpoint":
                    self.parameters["storage_endpoint"] = kwargs[key]
                elif key == "storage_account_access_key":
                    self.parameters["storage_account_access_key"] = kwargs[key]
                elif key == "retention_days":
                    self.parameters["retention_days"] = kwargs[key]
                elif key == "use_server_default":
                    ev = kwargs[key]
                    if ev == 'enabled':
                        ev = 'Enabled'
                    elif ev == 'disabled':
                        ev = 'Disabled'
                    self.parameters["use_server_default"] = ev

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_databasethreatdetectionpolicies()

        if not old_response:
            self.log("DatabaseThreatDetectionPolicies instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("DatabaseThreatDetectionPolicies instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if DatabaseThreatDetectionPolicies instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the DatabaseThreatDetectionPolicies instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_databasethreatdetectionpolicies()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("DatabaseThreatDetectionPolicies instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_databasethreatdetectionpolicies()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_databasethreatdetectionpolicies():
                time.sleep(20)
        else:
            self.log("DatabaseThreatDetectionPolicies instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]

        return self.results

    def create_update_databasethreatdetectionpolicies(self):
        '''
        Creates or updates DatabaseThreatDetectionPolicies with the specified configuration.

        :return: deserialized DatabaseThreatDetectionPolicies instance state dictionary
        '''
        self.log("Creating / Updating the DatabaseThreatDetectionPolicies instance {0}".format(self.security_alert_policy_name))

        try:
            response = self.mgmt_client.database_threat_detection_policies.create_or_update(resource_group_name=self.resource_group,
                                                                                            server_name=self.server_name,
                                                                                            database_name=self.database_name,
                                                                                            security_alert_policy_name=self.security_alert_policy_name,
                                                                                            parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the DatabaseThreatDetectionPolicies instance.')
            self.fail("Error creating the DatabaseThreatDetectionPolicies instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_databasethreatdetectionpolicies(self):
        '''
        Deletes specified DatabaseThreatDetectionPolicies instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the DatabaseThreatDetectionPolicies instance {0}".format(self.security_alert_policy_name))
        try:
            response = self.mgmt_client.database_threat_detection_policies.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DatabaseThreatDetectionPolicies instance.')
            self.fail("Error deleting the DatabaseThreatDetectionPolicies instance: {0}".format(str(e)))

        return True

    def get_databasethreatdetectionpolicies(self):
        '''
        Gets the properties of the specified DatabaseThreatDetectionPolicies.

        :return: deserialized DatabaseThreatDetectionPolicies instance state dictionary
        '''
        self.log("Checking if the DatabaseThreatDetectionPolicies instance {0} is present".format(self.security_alert_policy_name))
        found = False
        try:
            response = self.mgmt_client.database_threat_detection_policies.get(resource_group_name=self.resource_group,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name,
                                                                               security_alert_policy_name=self.security_alert_policy_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("DatabaseThreatDetectionPolicies instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DatabaseThreatDetectionPolicies instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMDatabaseThreatDetectionPolicies()

if __name__ == '__main__':
    main()
