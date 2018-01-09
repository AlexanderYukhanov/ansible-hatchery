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
module: azure_rm_sqldatabasethreatdetectionpolicy_facts
version_added: "2.5"
short_description: Get Database Threat Detection Policy facts.
description:
    - Get facts of Database Threat Detection Policy.

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

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Database Threat Detection Policy
    azure_rm_sqldatabasethreatdetectionpolicy_facts:
      resource_group: resource_group_name
      server_name: server_name
      database_name: database_name
      security_alert_policy_name: security_alert_policy_name
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/securityalert-6852/providers/Microsoft.Sql/servers/securityalert-2080/databases/
             testdb"
name:
    description:
        - Resource name.
    returned: always
    type: str
    sample: default
type:
    description:
        - Resource type.
    returned: always
    type: str
    sample: Microsoft.Sql/servers/databases/securityAlertPolicies
location:
    description:
        - The geo-location where the resource lives
    returned: always
    type: str
    sample: Japan East
kind:
    description:
        - Resource kind.
    returned: always
    type: str
    sample: V12
state:
    description:
        - "Specifies the state of the policy. If state is Enabled, storageEndpoint and storageAccountAccessKey are required. Possible values include: C(New),
            C(Enabled), C(Disabled)"
    returned: always
    type: str
    sample: Enabled
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


class AzureRMDatabaseThreatDetectionPoliciesFacts(AzureRMModuleBase):
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
            security_alert_policy_name=dict(
                type='str',
                required=True
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
        self.security_alert_policy_name = None
        super(AzureRMDatabaseThreatDetectionPoliciesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.server_name is not None and
                self.database_name is not None and
                self.security_alert_policy_name is not None):
            self.results['ansible_facts']['get'] = self.get()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Database Threat Detection Policy.

        :return: deserialized Database Threat Detection Policyinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.database_threat_detection_policies.get(resource_group_name=self.resource_group,
                                                                               server_name=self.server_name,
                                                                               database_name=self.database_name,
                                                                               security_alert_policy_name=self.security_alert_policy_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for DatabaseThreatDetectionPolicies.')

        if response is not None:
            results = response.as_dict()

        return results


def main():
    AzureRMDatabaseThreatDetectionPoliciesFacts()
if __name__ == '__main__':
    main()
