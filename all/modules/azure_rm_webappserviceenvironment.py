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
module: azure_rm_webappserviceenvironment
version_added: "2.5"
short_description: Manage AppServiceEnvironments instance
description:
    - Create, update and delete instance of AppServiceEnvironments

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of the App Service Environment.
        required: True
    kind:
        description:
            - Kind of resource.
    location:
        description:
            - Resource Location.
    app_service_environment_resource_name:
        description:
            - Name of the App Service Environment.
        required: True
    app_service_environment_resource_location:
        description:
            - "Location of the App Service Environment, e.g. 'West US'."
        required: True
    vnet_name:
        description:
            - Name of the Virtual Network for the App Service Environment.
    vnet_resource_group_name:
        description:
            - Resource group of the Virtual Network.
    vnet_subnet_name:
        description:
            - Subnet of the Virtual Network.
    virtual_network:
        description:
            - Description of the Virtual Network.
        required: True
        suboptions:
            id:
                description:
                    - Resource id of the Virtual Network.
            subnet:
                description:
                    - Subnet within the Virtual Network.
    internal_load_balancing_mode:
        description:
            - "Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. Possible values include: 'None', 'Web',
               'Publishing'"
    multi_size:
        description:
            - "Front-end VM size, e.g. 'Medium', 'Large'."
    multi_role_count:
        description:
            - Number of front-end instances.
    worker_pools:
        description:
            - Description of worker pools with worker size IDs, VM sizes, and number of workers in each pool.
        required: True
        suboptions:
            worker_size_id:
                description:
                    - Worker size ID for referencing this worker pool.
            compute_mode:
                description:
                    - "Shared or dedicated app hosting. Possible values include: 'Shared', 'Dedicated', 'Dynamic'"
            worker_size:
                description:
                    - VM size of the worker pool instances.
            worker_count:
                description:
                    - Number of instances in the worker pool.
    ipssl_address_count:
        description:
            - Number of IP SSL addresses reserved for the App Service Environment.
    dns_suffix:
        description:
            - DNS suffix of the App Service Environment.
    network_access_control_list:
        description:
            - Access control list for controlling traffic to the App Service Environment.
        suboptions:
            action:
                description:
                    - "Action object. Possible values include: 'Permit', 'Deny'"
            description:
                description:
                    - Description of network access control entry.
            order:
                description:
                    - Order of precedence.
            remote_subnet:
                description:
                    - Remote subnet.
    front_end_scale_factor:
        description:
            - Scale factor for front-ends.
    api_management_account_id:
        description:
            - API Management Account associated with the App Service Environment.
    suspended:
        description:
            - "<code>true</code> if the App Service Environment is suspended; otherwise, <code>false</code>. The environment can be suspended, e.g. when the
               management endpoint is no longer available\n (most likely because NSG blocked the incoming traffic)."
    dynamic_cache_enabled:
        description:
            - "True/false indicating whether the App Service Environment is suspended. The environment can be suspended e.g. when the management endpoint is
               no longer available\n(most likely because NSG blocked the incoming traffic)."
    cluster_settings:
        description:
            - Custom settings for changing the behavior of the App Service Environment.
        suboptions:
            name:
                description:
                    - Pair name.
            value:
                description:
                    - Pair value.
    user_whitelisted_ip_ranges:
        description:
            - User added ip ranges to whitelist on ASE db

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) AppServiceEnvironments
    azure_rm_webappserviceenvironment:
      resource_group: resource_group_name
      name: name
      kind: kind
      location: location
      app_service_environment_resource_name: app_service_environment_resource_name
      app_service_environment_resource_location: app_service_environment_resource_location
      vnet_name: vnet_name
      vnet_resource_group_name: vnet_resource_group_name
      vnet_subnet_name: vnet_subnet_name
      virtual_network:
        id: id
        subnet: subnet
      internal_load_balancing_mode: internal_load_balancing_mode
      multi_size: multi_size
      multi_role_count: multi_role_count
      worker_pools:
        - worker_size_id: worker_size_id
          compute_mode: compute_mode
          worker_size: worker_size
          worker_count: worker_count
      ipssl_address_count: ipssl_address_count
      dns_suffix: dns_suffix
      network_access_control_list:
        - action: action
          description: description
          order: order
          remote_subnet: remote_subnet
      front_end_scale_factor: front_end_scale_factor
      api_management_account_id: api_management_account_id
      suspended: suspended
      dynamic_cache_enabled: dynamic_cache_enabled
      cluster_settings:
        - name: name
          value: value
      user_whitelisted_ip_ranges:
        - XXXX - list of values -- not implemented str
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
        - "Current status of the App Service Environment. Possible values include: 'Preparing', 'Ready', 'Scaling', 'Deleting'"
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


class AzureRMAppServiceEnvironments(AzureRMModuleBase):
    """Configuration class for an Azure RM AppServiceEnvironments resource"""

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
            app_service_environment_resource_name=dict(
                type='str',
                required=True
            ),
            app_service_environment_resource_location=dict(
                type='str',
                required=True
            ),
            vnet_name=dict(
                type='str',
                required=False
            ),
            vnet_resource_group_name=dict(
                type='str',
                required=False
            ),
            vnet_subnet_name=dict(
                type='str',
                required=False
            ),
            virtual_network=dict(
                type='dict',
                required=True
            ),
            internal_load_balancing_mode=dict(
                type='str',
                required=False
            ),
            multi_size=dict(
                type='str',
                required=False
            ),
            multi_role_count=dict(
                type='int',
                required=False
            ),
            worker_pools=dict(
                type='list',
                required=True
            ),
            ipssl_address_count=dict(
                type='int',
                required=False
            ),
            dns_suffix=dict(
                type='str',
                required=False
            ),
            network_access_control_list=dict(
                type='list',
                required=False
            ),
            front_end_scale_factor=dict(
                type='int',
                required=False
            ),
            api_management_account_id=dict(
                type='str',
                required=False
            ),
            suspended=dict(
                type='str',
                required=False
            ),
            dynamic_cache_enabled=dict(
                type='str',
                required=False
            ),
            cluster_settings=dict(
                type='list',
                required=False
            ),
            user_whitelisted_ip_ranges=dict(
                type='list',
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
        self.hosting_environment_envelope = dict()

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAppServiceEnvironments, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                            supports_check_mode=True,
                                                            supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "kind":
                    self.hosting_environment_envelope["kind"] = kwargs[key]
                elif key == "location":
                    self.hosting_environment_envelope["location"] = kwargs[key]
                elif key == "app_service_environment_resource_name":
                    self.hosting_environment_envelope["app_service_environment_resource_name"] = kwargs[key]
                elif key == "app_service_environment_resource_location":
                    self.hosting_environment_envelope["app_service_environment_resource_location"] = kwargs[key]
                elif key == "vnet_name":
                    self.hosting_environment_envelope["vnet_name"] = kwargs[key]
                elif key == "vnet_resource_group_name":
                    self.hosting_environment_envelope["vnet_resource_group_name"] = kwargs[key]
                elif key == "vnet_subnet_name":
                    self.hosting_environment_envelope["vnet_subnet_name"] = kwargs[key]
                elif key == "virtual_network":
                    self.hosting_environment_envelope["virtual_network"] = kwargs[key]
                elif key == "internal_load_balancing_mode":
                    self.hosting_environment_envelope["internal_load_balancing_mode"] = kwargs[key]
                elif key == "multi_size":
                    self.hosting_environment_envelope["multi_size"] = kwargs[key]
                elif key == "multi_role_count":
                    self.hosting_environment_envelope["multi_role_count"] = kwargs[key]
                elif key == "worker_pools":
                    self.hosting_environment_envelope["worker_pools"] = kwargs[key]
                elif key == "ipssl_address_count":
                    self.hosting_environment_envelope["ipssl_address_count"] = kwargs[key]
                elif key == "dns_suffix":
                    self.hosting_environment_envelope["dns_suffix"] = kwargs[key]
                elif key == "network_access_control_list":
                    self.hosting_environment_envelope["network_access_control_list"] = kwargs[key]
                elif key == "front_end_scale_factor":
                    self.hosting_environment_envelope["front_end_scale_factor"] = kwargs[key]
                elif key == "api_management_account_id":
                    self.hosting_environment_envelope["api_management_account_id"] = kwargs[key]
                elif key == "suspended":
                    self.hosting_environment_envelope["suspended"] = kwargs[key]
                elif key == "dynamic_cache_enabled":
                    self.hosting_environment_envelope["dynamic_cache_enabled"] = kwargs[key]
                elif key == "cluster_settings":
                    self.hosting_environment_envelope["cluster_settings"] = kwargs[key]
                elif key == "user_whitelisted_ip_ranges":
                    self.hosting_environment_envelope["user_whitelisted_ip_ranges"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_appserviceenvironments()

        if not old_response:
            self.log("AppServiceEnvironments instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("AppServiceEnvironments instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if AppServiceEnvironments instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the AppServiceEnvironments instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_appserviceenvironments()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("AppServiceEnvironments instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_appserviceenvironments()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_appserviceenvironments():
                time.sleep(20)
        else:
            self.log("AppServiceEnvironments instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["status"] = response["status"]

        return self.results

    def create_update_appserviceenvironments(self):
        '''
        Creates or updates AppServiceEnvironments with the specified configuration.

        :return: deserialized AppServiceEnvironments instance state dictionary
        '''
        self.log("Creating / Updating the AppServiceEnvironments instance {0}".format(self.name))

        try:
            response = self.mgmt_client.app_service_environments.create_or_update(self.resource_group,
                                                                                  self.name,
                                                                                  self.hosting_environment_envelope)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the AppServiceEnvironments instance.')
            self.fail("Error creating the AppServiceEnvironments instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_appserviceenvironments(self):
        '''
        Deletes specified AppServiceEnvironments instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the AppServiceEnvironments instance {0}".format(self.name))
        try:
            response = self.mgmt_client.app_service_environments.delete(self.resource_group,
                                                                        self.name)
        except CloudError as e:
            self.log('Error attempting to delete the AppServiceEnvironments instance.')
            self.fail("Error deleting the AppServiceEnvironments instance: {0}".format(str(e)))

        return True

    def get_appserviceenvironments(self):
        '''
        Gets the properties of the specified AppServiceEnvironments.

        :return: deserialized AppServiceEnvironments instance state dictionary
        '''
        self.log("Checking if the AppServiceEnvironments instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.app_service_environments.get(self.resource_group,
                                                                     self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("AppServiceEnvironments instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AppServiceEnvironments instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    """Main execution"""
    AzureRMAppServiceEnvironments()

if __name__ == '__main__':
    main()