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
module: azure_rm_appgwroutefilterrule
version_added: "2.5"
short_description: Manage Route Filter Rule instance.
description:
    - Create, update and delete instance of Route Filter Rule.

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
            - "The access type of the rule. Valid values are: 'C(allow)', 'C(deny)'."
        required: True
        choices:
            - 'allow'
            - 'deny'
    route_filter_rule_type:
        description:
            - "The rule type of the rule. Valid value is: 'Community'"
        required: True
    communities:
        description:
            - "The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']"
        required: True
        type: list
    name:
        description:
            - The name of the resource that is unique within a resource group. This name can be used to I(access) the resource.
    location:
        description:
            - Resource location. If not set, location from the resource group will be used as default.
    state:
      description:
        - Assert the state of the Route Filter Rule.
        - Use 'present' to create or update an Route Filter Rule and 'absent' to delete it.
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
  - name: Create (or update) Route Filter Rule
    azure_rm_appgwroutefilterrule:
      resource_group: rg1
      route_filter_name: filterName
      rule_name: ruleName
      location: eastus
'''

RETURN = '''
id:
    description:
        - Resource ID.
    returned: always
    type: str
    sample: /subscriptions/subid/resourceGroups/rg1/providers/Microsofot.Network/routeFilters/filterName/routeFilterRules/ruleName
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
    """Configuration class for an Azure RM Route Filter Rule resource"""

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
                type='str'
            ),
            access=dict(
                type='str',
                choices=['allow',
                         'deny'],
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
        self.route_filter_name = None
        self.rule_name = None
        self.parameters = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRouteFilterRules, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                elif key == "access":
                    self.parameters["access"] = _snake_to_camel(kwargs[key], True)
                elif key == "route_filter_rule_type":
                    self.parameters["route_filter_rule_type"] = kwargs[key]
                elif key == "communities":
                    self.parameters["communities"] = kwargs[key]
                elif key == "name":
                    self.parameters["name"] = kwargs[key]
                elif key == "location":
                    self.parameters["location"] = kwargs[key]

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        old_response = self.get_routefilterrule()

        if not old_response:
            self.log("Route Filter Rule instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("Route Filter Rule instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if Route Filter Rule instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the Route Filter Rule instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_routefilterrule()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("Route Filter Rule instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_routefilterrule()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_routefilterrule():
                time.sleep(20)
        else:
            self.log("Route Filter Rule instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]

        return self.results

    def create_update_routefilterrule(self):
        '''
        Creates or updates Route Filter Rule with the specified configuration.

        :return: deserialized Route Filter Rule instance state dictionary
        '''
        self.log("Creating / Updating the Route Filter Rule instance {0}".format(self.rule_name))

        try:
            response = self.mgmt_client.route_filter_rules.create_or_update(resource_group_name=self.resource_group,
                                                                            route_filter_name=self.route_filter_name,
                                                                            rule_name=self.rule_name,
                                                                            route_filter_rule_parameters=self.parameters)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the Route Filter Rule instance.')
            self.fail("Error creating the Route Filter Rule instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_routefilterrule(self):
        '''
        Deletes specified Route Filter Rule instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the Route Filter Rule instance {0}".format(self.rule_name))
        try:
            response = self.mgmt_client.route_filter_rules.delete(resource_group_name=self.resource_group,
                                                                  route_filter_name=self.route_filter_name,
                                                                  rule_name=self.rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the Route Filter Rule instance.')
            self.fail("Error deleting the Route Filter Rule instance: {0}".format(str(e)))

        return True

    def get_routefilterrule(self):
        '''
        Gets the properties of the specified Route Filter Rule.

        :return: deserialized Route Filter Rule instance state dictionary
        '''
        self.log("Checking if the Route Filter Rule instance {0} is present".format(self.rule_name))
        found = False
        try:
            response = self.mgmt_client.route_filter_rules.get(resource_group_name=self.resource_group,
                                                               route_filter_name=self.route_filter_name,
                                                               rule_name=self.rule_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("Route Filter Rule instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Route Filter Rule instance.')
        if found is True:
            return response.as_dict()

        return False


def _snake_to_camel(snake, capitalize_first=False):
    if capitalize_first:
        return ''.join(x.capitalize() or '_' for x in snake.split('_'))
    else:
        return snake.split('_')[0] + ''.join(x.capitalize() or '_' for x in snake.split('_')[1:])


def main():
    """Main execution"""
    AzureRMRouteFilterRules()

if __name__ == '__main__':
    main()
