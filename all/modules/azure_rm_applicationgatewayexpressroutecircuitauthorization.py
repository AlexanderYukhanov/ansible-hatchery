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
module: azure_rm_applicationgatewayexpressroutecircuitauthorization
version_added: "2.5"
short_description: Manage ExpressRouteCircuitAuthorizations instance
description:
    - Create, update and delete instance of ExpressRouteCircuitAuthorizations

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    circuit_name:
        description:
            - The name of the express route circuit.
        required: True
    authorization_name:
        description:
            - The name of the authorization.
        required: True
    id:
        description:
            - Resource ID.
    authorization_key:
        description:
            - The authorization key.
    authorization_use_status:
        description:
            - "AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'. Possible values include: 'Available', 'InUse'"
    provisioning_state:
        description:
            - "Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'."
    name:
        description:
            - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) ExpressRouteCircuitAuthorizations
    azure_rm_applicationgatewayexpressroutecircuitauthorization:
      resource_group: NOT FOUND
      circuit_name: NOT FOUND
      authorization_name: NOT FOUND
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: id
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.applicationgateway import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMExpressRouteCircuitAuthorizations(AzureRMModuleBase):
    """Configuration class for an Azure RM ExpressRouteCircuitAuthorizations resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            circuit_name=dict(
                type='str',
                required=True
            ),
            authorization_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            authorization_key=dict(
                type='str',
                required=False
            ),
            authorization_use_status=dict(
                type='str',
                required=False
            ),
            provisioning_state=dict(
                type='str',
                required=False
            ),
            name=dict(
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
        self.circuit_name = None
        self.authorization_name = None
        self.authorization_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCircuitAuthorizations, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                       supports_check_mode=True,
                                                                       supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.authorization_parameters["id"] = kwargs[key]
                elif key == "authorization_key":
                    self.authorization_parameters["authorization_key"] = kwargs[key]
                elif key == "authorization_use_status":
                    self.authorization_parameters["authorization_use_status"] = kwargs[key]
                elif key == "provisioning_state":
                    self.authorization_parameters["provisioning_state"] = kwargs[key]
                elif key == "name":
                    self.authorization_parameters["name"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_expressroutecircuitauthorizations()

        if not old_response:
            self.log("ExpressRouteCircuitAuthorizations instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("ExpressRouteCircuitAuthorizations instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if ExpressRouteCircuitAuthorizations instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the ExpressRouteCircuitAuthorizations instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_expressroutecircuitauthorizations()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("ExpressRouteCircuitAuthorizations instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_expressroutecircuitauthorizations()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_expressroutecircuitauthorizations():
                time.sleep(20)
        else:
            self.log("ExpressRouteCircuitAuthorizations instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_expressroutecircuitauthorizations(self):
        '''
        Creates or updates ExpressRouteCircuitAuthorizations with the specified configuration.

        :return: deserialized ExpressRouteCircuitAuthorizations instance state dictionary
        '''
        self.log("Creating / Updating the ExpressRouteCircuitAuthorizations instance {0}".format(self.authorization_name))

        try:
            response = self.mgmt_client.express_route_circuit_authorizations.create_or_update(self.resource_group,
                                                                                              self.circuit_name,
                                                                                              self.authorization_name,
                                                                                              self.authorization_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCircuitAuthorizations instance.')
            self.fail("Error creating the ExpressRouteCircuitAuthorizations instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_expressroutecircuitauthorizations(self):
        '''
        Deletes specified ExpressRouteCircuitAuthorizations instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the ExpressRouteCircuitAuthorizations instance {0}".format(self.authorization_name))
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.delete(self.resource_group,
                                                                                    self.circuit_name,
                                                                                    self.authorization_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCircuitAuthorizations instance.')
            self.fail("Error deleting the ExpressRouteCircuitAuthorizations instance: {0}".format(str(e)))

        return True

    def get_expressroutecircuitauthorizations(self):
        '''
        Gets the properties of the specified ExpressRouteCircuitAuthorizations.

        :return: deserialized ExpressRouteCircuitAuthorizations instance state dictionary
        '''
        self.log("Checking if the ExpressRouteCircuitAuthorizations instance {0} is present".format(self.authorization_name))
        found = False
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.get(self.resource_group,
                                                                                 self.circuit_name,
                                                                                 self.authorization_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("ExpressRouteCircuitAuthorizations instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ExpressRouteCircuitAuthorizations instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMExpressRouteCircuitAuthorizations()

if __name__ == '__main__':
    main()
