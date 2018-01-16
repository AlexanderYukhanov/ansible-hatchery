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
module: azure_rm_authorizationclassicadministrator_facts
version_added: "2.5"
short_description: Get Classic Administrator facts.
description:
    - Get facts of Classic Administrator.

options:

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of Classic Administrator
    azure_rm_authorizationclassicadministrator_facts:
'''

RETURN = '''
classic_administrators:
    description: A list of dict results where the key is the name of the Classic Administrator and the values are the facts for that Classic Administrator.
    returned: always
    type: complex
    contains:
        classicadministrator_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMClassicAdministratorsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict()
        )
        self.mgmt_client = None
        super(AzureRMClassicAdministratorsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

            self.results['classic_administrators'] = self.list()
        return self.results

    def list(self):
        '''
        Gets facts of the specified Classic Administrator.

        :return: deserialized Classic Administratorinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.classic_administrators.list()
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for ClassicAdministrators.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMClassicAdministratorsFacts()
if __name__ == '__main__':
    main()
