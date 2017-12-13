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
module: azure_rm_webwebapp_facts
version_added: "2.5"
short_description: Get WebApps facts.
description:
    - Get facts of WebApps.

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Name of web app.
    backup_id:
        description:
            - ID of backup.
    request:
        description:
            - Information on backup request.
    slot:
        description:
            - Name of web app slot. If not specified then will default to production slot.
    namespace_name:
        description:
            - The namespace for this hybrid connection.
    relay_name:
        description:
            - The relay name for this hybrid connection.
    process_id:
        description:
            - PID.
    instance_id:
        description:
            - "ID of a specific scaled-out instance. This is the value of the name property in the JSON response from 'GET api/sites/{siteName}/instances'."
    details:
        description:
            - "Specify 'true' to include metric details in the response. It is 'false' by default."
    filter:
        description:
            - "Return only metrics specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') an
               d startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'."
    target_slot:
        description:
            - Destination deployment slot during swap operation.
    preserve_vnet:
        description:
            - <code>true</code> to preserve Virtual Network to the slot during swap; otherwise, <code>false</code>.
    id:
        description:
            - "The ID of a specific deployment. This is the value of the name property in the JSON response from 'GET /api/sites/{siteName}/deployments'."
    function_name:
        description:
            - Function name.
    view:
        description:
            - "The type of view. This can either be 'summary' or 'detailed'."
    format:
        description:
            - "Name of the format. Valid values are: \nFileZilla3\nWebDeploy -- default\nFtp. Possible values include: 'FileZilla3', 'WebDeploy', 'Ftp'"
    web_job_name:
        description:
            - Name of Web Job.
    include_slots:
        description:
            - Specify <strong>true</strong> to include deployment slots in results. The default is false, which only gives you the production slot of all apps.

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      backup_id: backup_id
      request: request
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      slot: slot
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      slot: slot
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      details: details
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      target_slot: target_slot
      preserve_vnet: preserve_vnet

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      backup_id: backup_id
      request: request

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      namespace_name: namespace_name
      relay_name: relay_name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      details: details
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      id: id
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      function_name: function_name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      view: view
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      format: format

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      web_job_name: web_job_name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      target_slot: target_slot
      preserve_vnet: preserve_vnet

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      id: id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      function_name: function_name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      instance_id: instance_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      view: view

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      process_id: process_id

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      format: format

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      slot: slot

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      web_job_name: web_job_name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
      filter: filter

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      include_slots: include_slots

  - name: Get instance of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name

  - name: List instances of WebApps
    azure_rm_webwebapp_facts:
      resource_group: resource_group_name
      name: name
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase

try:
    from msrestazure.azure_exceptions import CloudError
    from msrestazure.azure_operation import AzureOperationPoller
    from azure.mgmt.web import WebSiteManagementClient
    from msrest.serialization import Model
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWebAppsFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=False
            ),
            backup_id=dict(
                type='str',
                required=False
            ),
            request=dict(
                type='dict',
                required=False
            ),
            slot=dict(
                type='str',
                required=False
            ),
            namespace_name=dict(
                type='str',
                required=False
            ),
            relay_name=dict(
                type='str',
                required=False
            ),
            process_id=dict(
                type='str',
                required=False
            ),
            instance_id=dict(
                type='str',
                required=False
            ),
            details=dict(
                type='str',
                required=False
            ),
            filter=dict(
                type='str',
                required=False
            ),
            target_slot=dict(
                type='str',
                required=False
            ),
            preserve_vnet=dict(
                type='str',
                required=False
            ),
            id=dict(
                type='str',
                required=False
            ),
            function_name=dict(
                type='str',
                required=False
            ),
            view=dict(
                type='str',
                required=False
            ),
            format=dict(
                type='str',
                required=False
            ),
            web_job_name=dict(
                type='str',
                required=False
            ),
            include_slots=dict(
                type='str',
                required=False
            ),
        )
        # store the results of the module operation
        self.results = dict(
            changed=False,
            ansible_facts=dict(azure_dnsrecordset=[])
        )
        self.resource_group = None
        self.name = None
        self.backup_id = None
        self.request = None
        self.slot = None
        self.namespace_name = None
        self.relay_name = None
        self.process_id = None
        self.instance_id = None
        self.details = None
        self.filter = None
        self.target_slot = None
        self.preserve_vnet = None
        self.id = None
        self.function_name = None
        self.view = None
        self.format = None
        self.web_job_name = None
        self.include_slots = None
        super(AzureRMWebAppsFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if (self.resource_group_name is not None and
                self.name is not None and
                self.backup_id is not None and
                self.request is not None and
                self.slot is not None):
            self.results['ansible_facts']['list_backup_status_secrets_slot'] = self.list_backup_status_secrets_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.namespace_name is not None and
              self.relay_name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_hybrid_connection_keys_slot'] = self.list_hybrid_connection_keys_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.slot is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_process_modules_slot'] = self.list_instance_process_modules_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.slot is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_process_threads_slot'] = self.list_instance_process_threads_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_metrics_slot'] = self.list_metrics_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None and
              self.target_slot is not None and
              self.preserve_vnet is not None):
            self.results['ansible_facts']['list_slot_differences_slot'] = self.list_slot_differences_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.backup_id is not None and
              self.request is not None):
            self.results['ansible_facts']['list_backup_status_secrets'] = self.list_backup_status_secrets()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.namespace_name is not None and
              self.relay_name is not None):
            self.results['ansible_facts']['list_hybrid_connection_keys'] = self.list_hybrid_connection_keys()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_process_modules'] = self.list_instance_process_modules()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_process_threads'] = self.list_instance_process_threads()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metrics'] = self.list_metrics()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.id is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_deployment_log_slot'] = self.list_deployment_log_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.function_name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_function_secrets_slot'] = self.list_function_secrets_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_processes_slot'] = self.list_instance_processes_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.view is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_network_features_slot'] = self.list_network_features_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_perf_mon_counters_slot'] = self.list_perf_mon_counters_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_process_modules_slot'] = self.list_process_modules_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_process_threads_slot'] = self.list_process_threads_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_publishing_profile_xml_with_secrets_slot'] = self.list_publishing_profile_xml_with_secrets_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.web_job_name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_triggered_web_job_history_slot'] = self.list_triggered_web_job_history_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_usages_slot'] = self.list_usages_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.target_slot is not None and
              self.preserve_vnet is not None):
            self.results['ansible_facts']['list_slot_differences_from_production'] = self.list_slot_differences_from_production()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.id is not None):
            self.results['ansible_facts']['list_deployment_log'] = self.list_deployment_log()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.function_name is not None):
            self.results['ansible_facts']['list_function_secrets'] = self.list_function_secrets()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.instance_id is not None):
            self.results['ansible_facts']['list_instance_processes'] = self.list_instance_processes()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.view is not None):
            self.results['ansible_facts']['list_network_features'] = self.list_network_features()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_perf_mon_counters'] = self.list_perf_mon_counters()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None):
            self.results['ansible_facts']['list_process_modules'] = self.list_process_modules()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.process_id is not None):
            self.results['ansible_facts']['list_process_threads'] = self.list_process_threads()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_publishing_profile_xml_with_secrets'] = self.list_publishing_profile_xml_with_secrets()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_backups_slot'] = self.list_backups_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_configurations_slot'] = self.list_configurations_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_application_settings_slot'] = self.list_application_settings_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_connection_strings_slot'] = self.list_connection_strings_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_metadata_slot'] = self.list_metadata_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_publishing_credentials_slot'] = self.list_publishing_credentials_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_site_push_settings_slot'] = self.list_site_push_settings_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_configuration_snapshot_info_slot'] = self.list_configuration_snapshot_info_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_continuous_web_jobs_slot'] = self.list_continuous_web_jobs_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_deployments_slot'] = self.list_deployments_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_domain_ownership_identifiers_slot'] = self.list_domain_ownership_identifiers_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_instance_functions_slot'] = self.list_instance_functions_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_host_name_bindings_slot'] = self.list_host_name_bindings_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_hybrid_connections_slot'] = self.list_hybrid_connections_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_relay_service_connections_slot'] = self.list_relay_service_connections_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_instance_identifiers_slot'] = self.list_instance_identifiers_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_sync_function_triggers_slot'] = self.list_sync_function_triggers_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_metric_definitions_slot'] = self.list_metric_definitions_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_premier_add_ons_slot'] = self.list_premier_add_ons_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_processes_slot'] = self.list_processes_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_public_certificates_slot'] = self.list_public_certificates_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_site_extensions_slot'] = self.list_site_extensions_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_snapshots_slot'] = self.list_snapshots_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_triggered_web_jobs_slot'] = self.list_triggered_web_jobs_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_vnet_connections_slot'] = self.list_vnet_connections_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.slot is not None):
            self.results['ansible_facts']['list_web_jobs_slot'] = self.list_web_jobs_slot()
        elif (self.resource_group_name is not None and
              self.name is not None and
              self.web_job_name is not None):
            self.results['ansible_facts']['list_triggered_web_job_history'] = self.list_triggered_web_job_history()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_usages'] = self.list_usages()
        elif (self.resource_group_name is not None):
            self.results['ansible_facts']['list_by_resource_group'] = self.list_by_resource_group()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['get'] = self.get()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_backups'] = self.list_backups()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_configurations'] = self.list_configurations()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_application_settings'] = self.list_application_settings()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_connection_strings'] = self.list_connection_strings()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metadata'] = self.list_metadata()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_publishing_credentials'] = self.list_publishing_credentials()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_site_push_settings'] = self.list_site_push_settings()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_slot_configuration_names'] = self.list_slot_configuration_names()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_configuration_snapshot_info'] = self.list_configuration_snapshot_info()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_continuous_web_jobs'] = self.list_continuous_web_jobs()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_deployments'] = self.list_deployments()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_domain_ownership_identifiers'] = self.list_domain_ownership_identifiers()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_functions'] = self.list_functions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_host_name_bindings'] = self.list_host_name_bindings()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_hybrid_connections'] = self.list_hybrid_connections()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_relay_service_connections'] = self.list_relay_service_connections()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_instance_identifiers'] = self.list_instance_identifiers()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_sync_function_triggers'] = self.list_sync_function_triggers()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_metric_definitions'] = self.list_metric_definitions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_premier_add_ons'] = self.list_premier_add_ons()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_processes'] = self.list_processes()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_public_certificates'] = self.list_public_certificates()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_site_extensions'] = self.list_site_extensions()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_slots'] = self.list_slots()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_snapshots'] = self.list_snapshots()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_triggered_web_jobs'] = self.list_triggered_web_jobs()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_vnet_connections'] = self.list_vnet_connections()
        elif (self.resource_group_name is not None and
              self.name is not None):
            self.results['ansible_facts']['list_web_jobs'] = self.list_web_jobs()
        return self.results

    def list_backup_status_secrets_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_backup_status_secrets_slot(self.resource_group,
                                                                                 self.name,
                                                                                 self.backup_id,
                                                                                 self.request,
                                                                                 self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_hybrid_connection_keys_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_hybrid_connection_keys_slot(self.resource_group,
                                                                                  self.name,
                                                                                  self.namespace_name,
                                                                                  self.relay_name,
                                                                                  self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_process_modules_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_process_modules_slot(self.resource_group,
                                                                                    self.name,
                                                                                    self.process_id,
                                                                                    self.slot,
                                                                                    self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_process_threads_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_process_threads_slot(self.resource_group,
                                                                                    self.name,
                                                                                    self.process_id,
                                                                                    self.slot,
                                                                                    self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metrics_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metrics_slot(self.resource_group,
                                                                   self.name,
                                                                   self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_slot_differences_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_slot_differences_slot(self.resource_group,
                                                                            self.name,
                                                                            self.slot,
                                                                            self.target_slot,
                                                                            self.preserve_vnet)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_backup_status_secrets(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_backup_status_secrets(self.resource_group,
                                                                            self.name,
                                                                            self.backup_id,
                                                                            self.request)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_hybrid_connection_keys(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_hybrid_connection_keys(self.resource_group,
                                                                             self.name,
                                                                             self.namespace_name,
                                                                             self.relay_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_process_modules(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_process_modules(self.resource_group,
                                                                               self.name,
                                                                               self.process_id,
                                                                               self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_process_threads(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_process_threads(self.resource_group,
                                                                               self.name,
                                                                               self.process_id,
                                                                               self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metrics(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metrics(self.resource_group,
                                                              self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_deployment_log_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_deployment_log_slot(self.resource_group,
                                                                          self.name,
                                                                          self.id,
                                                                          self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_function_secrets_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_function_secrets_slot(self.resource_group,
                                                                            self.name,
                                                                            self.function_name,
                                                                            self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_processes_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_processes_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot,
                                                                              self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_network_features_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_network_features_slot(self.resource_group,
                                                                            self.name,
                                                                            self.view,
                                                                            self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_perf_mon_counters_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_perf_mon_counters_slot(self.resource_group,
                                                                             self.name,
                                                                             self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_process_modules_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_process_modules_slot(self.resource_group,
                                                                           self.name,
                                                                           self.process_id,
                                                                           self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_process_threads_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_process_threads_slot(self.resource_group,
                                                                           self.name,
                                                                           self.process_id,
                                                                           self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_publishing_profile_xml_with_secrets_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_publishing_profile_xml_with_secrets_slot(self.resource_group,
                                                                                               self.name,
                                                                                               self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_triggered_web_job_history_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_triggered_web_job_history_slot(self.resource_group,
                                                                                     self.name,
                                                                                     self.web_job_name,
                                                                                     self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_usages_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_usages_slot(self.resource_group,
                                                                  self.name,
                                                                  self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_slot_differences_from_production(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_slot_differences_from_production(self.resource_group,
                                                                                       self.name,
                                                                                       self.target_slot,
                                                                                       self.preserve_vnet)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_deployment_log(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_deployment_log(self.resource_group,
                                                                     self.name,
                                                                     self.id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_function_secrets(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_function_secrets(self.resource_group,
                                                                       self.name,
                                                                       self.function_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_processes(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_processes(self.resource_group,
                                                                         self.name,
                                                                         self.instance_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_network_features(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_network_features(self.resource_group,
                                                                       self.name,
                                                                       self.view)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_perf_mon_counters(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_perf_mon_counters(self.resource_group,
                                                                        self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_process_modules(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_process_modules(self.resource_group,
                                                                      self.name,
                                                                      self.process_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_process_threads(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_process_threads(self.resource_group,
                                                                      self.name,
                                                                      self.process_id)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_publishing_profile_xml_with_secrets(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_publishing_profile_xml_with_secrets(self.resource_group,
                                                                                          self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_backups_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_backups_slot(self.resource_group,
                                                                   self.name,
                                                                   self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_configurations_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_configurations_slot(self.resource_group,
                                                                          self.name,
                                                                          self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_application_settings_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_application_settings_slot(self.resource_group,
                                                                                self.name,
                                                                                self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_connection_strings_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_connection_strings_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metadata_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metadata_slot(self.resource_group,
                                                                    self.name,
                                                                    self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_publishing_credentials_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_publishing_credentials_slot(self.resource_group,
                                                                                  self.name,
                                                                                  self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_site_push_settings_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_site_push_settings_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_configuration_snapshot_info_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_configuration_snapshot_info_slot(self.resource_group,
                                                                                       self.name,
                                                                                       self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_continuous_web_jobs_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_continuous_web_jobs_slot(self.resource_group,
                                                                               self.name,
                                                                               self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_deployments_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_deployments_slot(self.resource_group,
                                                                       self.name,
                                                                       self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_domain_ownership_identifiers_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_domain_ownership_identifiers_slot(self.resource_group,
                                                                                        self.name,
                                                                                        self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_functions_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_functions_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_host_name_bindings_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_host_name_bindings_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_hybrid_connections_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_hybrid_connections_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_relay_service_connections_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_relay_service_connections_slot(self.resource_group,
                                                                                     self.name,
                                                                                     self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_identifiers_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_identifiers_slot(self.resource_group,
                                                                                self.name,
                                                                                self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_sync_function_triggers_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_sync_function_triggers_slot(self.resource_group,
                                                                                  self.name,
                                                                                  self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metric_definitions_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metric_definitions_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_premier_add_ons_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_premier_add_ons_slot(self.resource_group,
                                                                           self.name,
                                                                           self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_processes_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_processes_slot(self.resource_group,
                                                                     self.name,
                                                                     self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_public_certificates_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_public_certificates_slot(self.resource_group,
                                                                               self.name,
                                                                               self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_site_extensions_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_site_extensions_slot(self.resource_group,
                                                                           self.name,
                                                                           self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_snapshots_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_snapshots_slot(self.resource_group,
                                                                     self.name,
                                                                     self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_triggered_web_jobs_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_triggered_web_jobs_slot(self.resource_group,
                                                                              self.name,
                                                                              self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_vnet_connections_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_vnet_connections_slot(self.resource_group,
                                                                            self.name,
                                                                            self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_jobs_slot(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_web_jobs_slot(self.resource_group,
                                                                    self.name,
                                                                    self.slot)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_triggered_web_job_history(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_triggered_web_job_history(self.resource_group,
                                                                                self.name,
                                                                                self.web_job_name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_usages(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_usages(self.resource_group,
                                                             self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_by_resource_group(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_by_resource_group(self.resource_group)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def get(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.get(self.resource_group,
                                                     self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_backups(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_backups(self.resource_group,
                                                              self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_configurations(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_configurations(self.resource_group,
                                                                     self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_application_settings(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_application_settings(self.resource_group,
                                                                           self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_connection_strings(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_connection_strings(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metadata(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metadata(self.resource_group,
                                                               self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_publishing_credentials(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_publishing_credentials(self.resource_group,
                                                                             self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_site_push_settings(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_site_push_settings(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_slot_configuration_names(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_slot_configuration_names(self.resource_group,
                                                                               self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_configuration_snapshot_info(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_configuration_snapshot_info(self.resource_group,
                                                                                  self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_continuous_web_jobs(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_continuous_web_jobs(self.resource_group,
                                                                          self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_deployments(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_deployments(self.resource_group,
                                                                  self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_domain_ownership_identifiers(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_domain_ownership_identifiers(self.resource_group,
                                                                                   self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_functions(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_functions(self.resource_group,
                                                                self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_host_name_bindings(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_host_name_bindings(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_hybrid_connections(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_hybrid_connections(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_relay_service_connections(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_relay_service_connections(self.resource_group,
                                                                                self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_instance_identifiers(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_instance_identifiers(self.resource_group,
                                                                           self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_sync_function_triggers(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_sync_function_triggers(self.resource_group,
                                                                             self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_metric_definitions(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_metric_definitions(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_premier_add_ons(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_premier_add_ons(self.resource_group,
                                                                      self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_processes(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_processes(self.resource_group,
                                                                self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_public_certificates(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_public_certificates(self.resource_group,
                                                                          self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_site_extensions(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_site_extensions(self.resource_group,
                                                                      self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_slots(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_slots(self.resource_group,
                                                            self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_snapshots(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_snapshots(self.resource_group,
                                                                self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_triggered_web_jobs(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_triggered_web_jobs(self.resource_group,
                                                                         self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_vnet_connections(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_vnet_connections(self.resource_group,
                                                                       self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False

    def list_web_jobs(self):
        '''
        Gets facts of the specified WebApps.

        :return: deserialized WebAppsinstance state dictionary
        '''
        self.log("Checking if the WebApps instance {0} is present".format(self.name))
        found = False
        try:
            response = self.mgmt_client.web_apps.list_web_jobs(self.resource_group,
                                                               self.name)
            found = True
            self.log("Response : {0}".format(response))
            self.log("WebApps instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApps instance.')
        if found is True:
            return response.as_dict()

        return False


def main():
    AzureRMWebAppsFacts()
if __name__ == '__main__':
    main()
