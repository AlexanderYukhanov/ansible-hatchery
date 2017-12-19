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
module: azure_rm_applicationgatewayroutefilterrule
version_added: "2.5"
short_description: Manage RouteFilterRules instance
description:
    - Create, update and delete instance of RouteFilterRules

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    route_filter_name:
        description:
            - The name of the route filter.
        required: True
    rule_name:
        description:
            - The name of the route filter rule.
        required: True
    id:
        description:
            - Resource ID.
    access:
        description:
            - "The access type of the rule. Valid values are: 'Allow', 'Deny'. Possible values include: 'Allow', 'Deny'"
        required: True
    route_filter_rule_type:
        description:
            - "The rule type of the rule. Valid value is: 'Community'"
        required: True
    communities:
        description:
            - "The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']"
        required: True
    name:
        description:
            - The name of the resource that is unique within a resource group. This name can be used to access the resource.
    location:
        description:
            - Resource location.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) RouteFilterRules
    azure_rm_applicationgatewayroutefilterrule:
      resource_group: rg1
      route_filter_name: filterName
      rule_name: ruleName
      communities:
        - XXXX - list of values -- not implemented str
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
    from azure.mgmt.network import NetworkManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRouteFilterRules(AzureRMModuleBase):
    """Configuration class for an Azure RM RouteFilterRules resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            route_filter_name=dict(
                type='str',
                required=True
            ),
            rule_name=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=False
            ),
            access=dict(
                type='str',
                required=True
            ),
            route_filter_rule_type=dict(
                type='str',
                required=True
            ),
            communities=dict(
                type='list',
                required=True
            ),
            name=dict(
                type='str',
                required=False
            ),
            location=dict(
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
        self.route_filter_name = None
        self.rule_name = None
        self.route_filter_rule_parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRouteFilterRules, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                      supports_check_mode=True,
                                                      supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "id":
                    self.route_filter_rule_parameters["id"] = kwargs[key]
                elif key == "access":
                    self.route_filter_rule_parameters["access"] = kwargs[key]
                elif key == "route_filter_rule_type":
                    self.route_filter_rule_parameters["route_filter_rule_type"] = kwargs[key]
                elif key == "communities":
                    self.route_filter_rule_parameters["communities"] = kwargs[key]
                elif key == "name":
                    self.route_filter_rule_parameters["name"] = kwargs[key]
                elif key == "location":
                    self.route_filter_rule_parameters["location"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_routefilterrules()

        if not old_response:
            self.log("RouteFilterRules instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("RouteFilterRules instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if RouteFilterRules instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the RouteFilterRules instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_routefilterrules()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("RouteFilterRules instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_routefilterrules()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_routefilterrules():
                time.sleep(20)
        else:
            self.log("RouteFilterRules instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_routefilterrules(self):
        '''
        Creates or updates RouteFilterRules with the specified configuration.

        :return: deserialized RouteFilterRules instance state dictionary
        '''
        self.log("Creating / Updating the RouteFilterRules instance {0}".format(self.rule_name))

        try:
            response = self.mgmt_client.route_filter_rules.create_or_update(self.resource_group,
                                                                            self.route_filter_name,
                                                                            self.rule_name,
                                                                            self.route_filter_rule_parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the RouteFilterRules instance.')
            self.fail("Error creating the RouteFilterRules instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_routefilterrules(self):
        '''
        Deletes specified RouteFilterRules instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the RouteFilterRules instance {0}".format(self.rule_name))
        try:
            response = self.mgmt_client.route_filter_rules.delete(self.resource_group,
                                                                  self.route_filter_name,
                                                                  self.rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the RouteFilterRules instance.')
            self.fail("Error deleting the RouteFilterRules instance: {0}".format(str(e)))

        return True

    def get_routefilterrules(self):
        '''
        Gets the properties of the specified RouteFilterRules.

        :return: deserialized RouteFilterRules instance state dictionary
        '''
        self.log("Checking if the RouteFilterRules instance {0} is present".format(self.rule_name))
        found = False
        try:
            response = self.mgmt_client.route_filter_rules.get(self.resource_group,
                                                               self.route_filter_name,
                                                               self.rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("RouteFilterRules instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RouteFilterRules instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMRouteFilterRules()

if __name__ == '__main__':
    main()
