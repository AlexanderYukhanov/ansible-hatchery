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
module: azure_rm_webappserviceplan
version_added: "2.5"
short_description: Manage AppServicePlans instance
description:
    - Create, update and delete instance of AppServicePlans

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of the App Service plan.
        required: True
    kind:
        description:
            - Kind of resource.
    location:
        description:
            - Resource Location.
    app_service_plan_name:
        description:
            - Name for the App Service plan.
    worker_tier_name:
        description:
            - Target worker tier assigned to the App Service plan.
    admin_site_name:
        description:
            - App Service plan administration site.
    hosting_environment_profile:
        description:
            - Specification for the App Service Environment to use for the App Service plan.
        suboptions:
            id:
                description:
                    - Resource ID of the App Service Environment.
    per_site_scaling:
        description:
            - "If <code>true</code>, apps assigned to this App Service plan can be scaled independently.\nIf <code>false</code>, apps assigned to this App Se
               rvice plan will scale to all instances of the plan."
    is_spot:
        description:
            - If <code>true</code>, this App Service Plan owns spot instances.
    spot_expiration_time:
        description:
            - The time when the server farm expires. Valid only if it is a spot server farm.
    reserved:
        description:
            - If Linux app service plan <code>true</code>, <code>false</code> otherwise.
    target_worker_count:
        description:
            - Scaling worker count.
    target_worker_size_id:
        description:
            - Scaling worker size ID.
    sku:
        description:
            -
        suboptions:
            name:
                description:
                    - Name of the resource SKU.
            tier:
                description:
                    - Service tier of the resource SKU.
            size:
                description:
                    - Size specifier of the resource SKU.
            family:
                description:
                    - Family code of the resource SKU.
            capacity:
                description:
                    - Current number of instances assigned to the resource.
            sku_capacity:
                description:
                    - Min, max, and default scale values of the SKU.
                suboptions:
                    minimum:
                        description:
                            - Minimum number of workers for this App Service plan SKU.
                    maximum:
                        description:
                            - Maximum number of workers for this App Service plan SKU.
                    default:
                        description:
                            - Default number of workers for this App Service plan SKU.
                    scale_type:
                        description:
                            - Available scale configurations for an App Service plan.
            locations:
                description:
                    - Locations of the SKU.
            capabilities:
                description:
                    - Capabilities of the SKU, e.g., is traffic manager enabled?
                suboptions:
                    name:
                        description:
                            - Name of the SKU capability.
                    value:
                        description:
                            - Value of the SKU capability.
                    reason:
                        description:
                            - Reason of the SKU capability.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) AppServicePlans
    azure_rm_webappserviceplan:
      resource_group: resource_group_name
      name: name
      kind: kind
      location: location
      app_service_plan_name: app_service_plan_name
      worker_tier_name: worker_tier_name
      admin_site_name: admin_site_name
      hosting_environment_profile:
        id: id
      per_site_scaling: per_site_scaling
      is_spot: is_spot
      spot_expiration_time: spot_expiration_time
      reserved: reserved
      target_worker_count: target_worker_count
      target_worker_size_id: target_worker_size_id
      sku:
        name: name
        tier: tier
        size: size
        family: family
        capacity: capacity
        sku_capacity:
          minimum: minimum
          maximum: maximum
          default: default
          scale_type: scale_type
        locations:
          - XXXX - list of values -- not implemented str
        capabilities:
          - name: name
            value: value
            reason: reason
'''

RETURN = '''
id:
    description:
        - Resource Id.
    returned: always
    type: str
    sample: id
status:
    description:
        - "App Service plan status. Possible values include: 'Ready', 'Pending', 'Creating'"
    returned: always
    type: str
    sample: status
'''

import time
from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.web import WebSiteManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAppServicePlans(AzureRMModuleBase):
    """Configuration class for an Azure RM AppServicePlans resource"""

    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='str',
                required=False
            ),
            location=dict(
                type='str',
                required=False
            ),
            app_service_plan_name=dict(
                type='str',
                required=False
            ),
            worker_tier_name=dict(
                type='str',
                required=False
            ),
            admin_site_name=dict(
                type='str',
                required=False
            ),
            hosting_environment_profile=dict(
                type='dict',
                required=False
            ),
            per_site_scaling=dict(
                type='str',
                required=False
            ),
            is_spot=dict(
                type='str',
                required=False
            ),
            spot_expiration_time=dict(
                type='datetime',
                required=False
            ),
            reserved=dict(
                type='str',
                required=False
            ),
            target_worker_count=dict(
                type='int',
                required=False
            ),
            target_worker_size_id=dict(
                type='int',
                required=False
            ),
            sku=dict(
                type='dict',
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
        self.name = None
        self.app_service_plan = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAppServicePlans, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "kind":
                    self.app_service_plan["kind"] = kwargs[key]
                elif key == "location":
                    self.app_service_plan["location"] = kwargs[key]
                elif key == "app_service_plan_name":
                    self.app_service_plan["app_service_plan_name"] = kwargs[key]
                elif key == "worker_tier_name":
                    self.app_service_plan["worker_tier_name"] = kwargs[key]
                elif key == "admin_site_name":
                    self.app_service_plan["admin_site_name"] = kwargs[key]
                elif key == "hosting_environment_profile":
                    self.app_service_plan["hosting_environment_profile"] = kwargs[key]
                elif key == "per_site_scaling":
                    self.app_service_plan["per_site_scaling"] = kwargs[key]
                elif key == "is_spot":
                    self.app_service_plan["is_spot"] = kwargs[key]
                elif key == "spot_expiration_time":
                    self.app_service_plan["spot_expiration_time"] = kwargs[key]
                elif key == "reserved":
                    self.app_service_plan["reserved"] = kwargs[key]
                elif key == "target_worker_count":
                    self.app_service_plan["target_worker_count"] = kwargs[key]
                elif key == "target_worker_size_id":
                    self.app_service_plan["target_worker_size_id"] = kwargs[key]
                elif key == "sku":
                    self.app_service_plan["sku"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_appserviceplans()

        if not old_response:
            self.log("AppServicePlans instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("AppServicePlans instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if AppServicePlans instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the AppServicePlans instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_appserviceplans()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("AppServicePlans instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_appserviceplans()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_appserviceplans():
                time.sleep(20)
        else:
            self.log("AppServicePlans instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["status"] = response["status"]

        return self.results

    def create_update_appserviceplans(self):
        '''
        Creates or updates AppServicePlans with the specified configuration.

        :return: deserialized AppServicePlans instance state dictionary
        '''
        self.log("Creating / Updating the AppServicePlans instance {0}".format(self.name))

        try:
            response = self.mgmt_client.app_service_plans.create_or_update(self.resource_group,
                                                                           self.name,
                                                                           self.app_service_plan)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the AppServicePlans instance.')
            self.fail("Error creating the AppServicePlans instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_appserviceplans(self):
        '''
        Deletes specified AppServicePlans instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the AppServicePlans instance {0}".format(self.name))
        try:
            response = self.mgmt_client.app_service_plans.delete(self.resource_group,
                                                                 self.name)
        except CloudError as e:
            self.log('Error attempting to delete the AppServicePlans instance.')
            self.fail("Error deleting the AppServicePlans instance: {0}".format(str(e)))

        return True

    def get_appserviceplans(self):
        '''
        Gets the properties of the specified AppServicePlans.

        :return: deserialized AppServicePlans instance state dictionary
        '''
        self.log("Checking if the AppServicePlans instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_plans.get(self.resource_group,
                                                              self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServicePlans instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServicePlans instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMAppServicePlans()

if __name__ == '__main__':
    main()