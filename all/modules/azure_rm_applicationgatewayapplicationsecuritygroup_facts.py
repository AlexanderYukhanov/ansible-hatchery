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
module: azure_rm_applicationgatewayapplicationsecuritygroup_facts
version_added: "2.5"
short_description: Get Application Security Group facts.
description:
    - Get facts of Application Security Group.

options:
    resource_group:
        description:
            - The name of the resource group.
    application_security_group_name:
        description:
            - The name of the application security group.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Application Security Group
    azure_rm_applicationgatewayapplicationsecuritygroup_facts:
      resource_group: resource_group_name
      application_security_group_name: application_security_group_name

  - name: List instances of Application Security Group
    azure_rm_applicationgatewayapplicationsecuritygroup_facts:
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/applicationSecurityGroups/test-asg
name:
    description:
        - Resource name.
    returned: always
    type: str
    sample: test-asg
type:
    description:
        - Resource type.
    returned: always
    type: str
    sample: Microsoft.Network/applicationSecurityGroups
location:
    description:
        - Resource location.
    returned: always
    type: str
    sample: westus
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMApplicationSecurityGroupsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            application_security_group_name=dict(
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
        self.application_security_group_name = None
        super(AzureRMApplicationSecurityGroupsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.application_security_group_name is not None):
            self.results['ansible_facts']['get'] = self.get()
            self.results['ansible_facts']['list_all'] = self.list_all()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Application Security Group.

        :return: deserialized Application Security Groupinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.application_security_groups.get(resource_group_name=self.resource_group,
                                                                        application_security_group_name=self.application_security_group_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ApplicationSecurityGroups.')

        if response is not None:
            results = response.as_dict()

        return results

    def list_all(self):
        '''
        Gets facts of the specified Application Security Group.

        :return: deserialized Application Security Groupinstance state dictionary
        '''
        response = None
        results = False
        try:
            response = self.mgmt_client.application_security_groups.list_all()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ApplicationSecurityGroups.')

        if response is not None:
            results = []
            for item in response:
                results.append(item.as_dict())

        return results


def main():
    AzureRMApplicationSecurityGroupsFacts()
if __name__ == '__main__':
    main()
