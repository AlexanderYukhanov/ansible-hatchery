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
module: azure_rm_webwebapp
version_added: "2.5"
short_description: Manage WebApps instance
description:
    - Create, update and delete instance of WebApps

options:
    resource_group:
        description:
            - Name of the resource group to which the resource belongs.
        required: True
    name:
        description:
            - Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
        required: True
    kind:
        description:
            - Kind of resource.
    location:
        description:
            - Resource Location.
    enabled:
        description:
            - <code>true</code> if the app is enabled; otherwise, <code>false</code>. Setting this value to false disables the app (takes the app offline).
    host_name_ssl_states:
        description:
            - "Hostname SSL states are used to manage the SSL bindings for app's hostnames."
        suboptions:
            name:
                description:
                    - Hostname.
            ssl_state:
                description:
                    - "SSL type. Possible values include: 'Disabled', 'SniEnabled', 'IpBasedEnabled'"
            virtual_ip:
                description:
                    - Virtual IP address assigned to the hostname if IP based SSL is enabled.
            thumbprint:
                description:
                    - SSL certificate thumbprint.
            to_update:
                description:
                    - Set to <code>true</code> to update existing hostname.
            host_type:
                description:
                    - "Indicates whether the hostname is a standard or repository hostname. Possible values include: 'Standard', 'Repository'"
    server_farm_id:
        description:
            - "Resource ID of the associated App Service plan, formatted as: '/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.
               Web/serverfarms/{appServicePlanName}'."
    reserved:
        description:
            - <code>true</code> if reserved; otherwise, <code>false</code>.
    site_config:
        description:
            - Configuration of the app.
        suboptions:
            number_of_workers:
                description:
                    - Number of workers.
            default_documents:
                description:
                    - Default documents.
            net_framework_version:
                description:
                    - .NET Framework version.
            php_version:
                description:
                    - Version of PHP.
            python_version:
                description:
                    - Version of Python.
            node_version:
                description:
                    - Version of Node.js.
            linux_fx_version:
                description:
                    - Linux App Framework and version
            request_tracing_enabled:
                description:
                    - <code>true</code> if request tracing is enabled; otherwise, <code>false</code>.
            request_tracing_expiration_time:
                description:
                    - Request tracing expiration time.
            remote_debugging_enabled:
                description:
                    - <code>true</code> if remote debugging is enabled; otherwise, <code>false</code>.
            remote_debugging_version:
                description:
                    - Remote debugging version.
            http_logging_enabled:
                description:
                    - <code>true</code> if HTTP logging is enabled; otherwise, <code>false</code>.
            logs_directory_size_limit:
                description:
                    - HTTP logs directory size limit.
            detailed_error_logging_enabled:
                description:
                    - <code>true</code> if detailed error logging is enabled; otherwise, <code>false</code>.
            publishing_username:
                description:
                    - Publishing user name.
            app_settings:
                description:
                    - Application settings.
                suboptions:
                    name:
                        description:
                            - Pair name.
                    value:
                        description:
                            - Pair value.
            connection_strings:
                description:
                    - Connection strings.
                suboptions:
                    name:
                        description:
                            - Name of connection string.
                    connection_string:
                        description:
                            - Connection string value.
                    type:
                        description:
                            - "Type of database. Possible values include: 'MySql', 'SQLServer', 'SQLAzure', 'Custom', 'NotificationHub', 'ServiceBus', 'Event
                               Hub', 'ApiHub', 'DocDb', 'RedisCache', 'PostgreSQL'"
            handler_mappings:
                description:
                    - Handler mappings.
                suboptions:
                    extension:
                        description:
                            - Requests with this extension will be handled using the specified FastCGI application.
                    script_processor:
                        description:
                            - The absolute path to the FastCGI application.
                    arguments:
                        description:
                            - Command-line arguments to be passed to the script processor.
            document_root:
                description:
                    - Document root.
            scm_type:
                description:
                    - "SCM type. Possible values include: 'None', 'Dropbox', 'Tfs', 'LocalGit', 'GitHub', 'CodePlexGit', 'CodePlexHg', 'BitbucketGit', 'Bitbu
                       cketHg', 'ExternalGit', 'ExternalHg', 'OneDrive', 'VSO'"
            use32_bit_worker_process:
                description:
                    - <code>true</code> to use 32-bit worker process; otherwise, <code>false</code>.
            web_sockets_enabled:
                description:
                    - <code>true</code> if WebSocket is enabled; otherwise, <code>false</code>.
            always_on:
                description:
                    - <code>true</code> if Always On is enabled; otherwise, <code>false</code>.
            java_version:
                description:
                    - Java version.
            java_container:
                description:
                    - Java container.
            java_container_version:
                description:
                    - Java container version.
            app_command_line:
                description:
                    - App command line to launch.
            managed_pipeline_mode:
                description:
                    - "Managed pipeline mode. Possible values include: 'Integrated', 'Classic'"
            virtual_applications:
                description:
                    - Virtual applications.
                suboptions:
                    virtual_path:
                        description:
                            - Virtual path.
                    physical_path:
                        description:
                            - Physical path.
                    preload_enabled:
                        description:
                            - <code>true</code> if preloading is enabled; otherwise, <code>false</code>.
                    virtual_directories:
                        description:
                            - Virtual directories for virtual application.
                        suboptions:
                            virtual_path:
                                description:
                                    - Path to virtual application.
                            physical_path:
                                description:
                                    - Physical path.
            load_balancing:
                description:
                    - "Site load balancing. Possible values include: 'WeightedRoundRobin', 'LeastRequests', 'LeastResponseTime', 'WeightedTotalTraffic', 'Req
                       uestHash'"
            experiments:
                description:
                    - This is work around for polymophic types.
                suboptions:
                    ramp_up_rules:
                        description:
                            - List of ramp-up rules.
                        suboptions:
                            action_host_name:
                                description:
                                    - Hostname of a slot to which the traffic will be redirected if decided to. E.g. myapp-stage.azurewebsites.net.
                            reroute_percentage:
                                description:
                                    - Percentage of the traffic which will be redirected to <code>ActionHostName</code>.
                            change_step:
                                description:
                                    - "In auto ramp up scenario this is the step to to add/remove from <code>ReroutePercentage</code> until it reaches \n<cod
                                       e>MinReroutePercentage</code> or <code>MaxReroutePercentage</code>. Site metrics are checked every N minutes specifice
                                       d in <code>ChangeIntervalInMinutes</code>.\nCustom decision algorithm can be provided in TiPCallback site extension wh
                                       ich URL can be specified in <code>ChangeDecisionCallbackUrl</code>."
                            change_interval_in_minutes:
                                description:
                                    - Specifies interval in mimuntes to reevaluate ReroutePercentage.
                            min_reroute_percentage:
                                description:
                                    - Specifies lower boundary above which ReroutePercentage will stay.
                            max_reroute_percentage:
                                description:
                                    - Specifies upper boundary below which ReroutePercentage will stay.
                            change_decision_callback_url:
                                description:
                                    - "Custom decision algorithm can be provided in TiPCallback site extension which URL can be specified. See TiPCallback si
                                       te extension for the scaffold and contracts.\nhttps://www.siteextensions.net/packages/TiPCallback/"
                            name:
                                description:
                                    - "Name of the routing rule. The recommended name would be to point to the slot which will receive the traffic in the exp
                                       eriment."
            limits:
                description:
                    - Site limits.
                suboptions:
                    max_percentage_cpu:
                        description:
                            - Maximum allowed CPU usage percentage.
                    max_memory_in_mb:
                        description:
                            - Maximum allowed memory usage in MB.
                    max_disk_size_in_mb:
                        description:
                            - Maximum allowed disk size usage in MB.
            auto_heal_enabled:
                description:
                    - <code>true</code> if Auto Heal is enabled; otherwise, <code>false</code>.
            auto_heal_rules:
                description:
                    - Auto Heal rules.
                suboptions:
                    triggers:
                        description:
                            - Conditions that describe when to execute the auto-heal actions.
                        suboptions:
                            requests:
                                description:
                                    - A rule based on total requests.
                                suboptions:
                                    count:
                                        description:
                                            - Request Count.
                                    time_interval:
                                        description:
                                            - Time interval.
                            private_bytes_in_kb:
                                description:
                                    - A rule based on private bytes.
                            status_codes:
                                description:
                                    - A rule based on status codes.
                                suboptions:
                                    status:
                                        description:
                                            - HTTP status code.
                                    sub_status:
                                        description:
                                            - Request Sub Status.
                                    win32_status:
                                        description:
                                            - Win32 error code.
                                    count:
                                        description:
                                            - Request Count.
                                    time_interval:
                                        description:
                                            - Time interval.
                            slow_requests:
                                description:
                                    - A rule based on request execution time.
                                suboptions:
                                    time_taken:
                                        description:
                                            - Time taken.
                                    count:
                                        description:
                                            - Request Count.
                                    time_interval:
                                        description:
                                            - Time interval.
                    actions:
                        description:
                            - Actions to be executed when a rule is triggered.
                        suboptions:
                            action_type:
                                description:
                                    - "Predefined action to be taken. Possible values include: 'Recycle', 'LogEvent', 'CustomAction'"
                            custom_action:
                                description:
                                    - Custom action to be taken.
                                suboptions:
                                    exe:
                                        description:
                                            - Executable to be run.
                                    parameters:
                                        description:
                                            - Parameters for the executable.
                            min_process_execution_time:
                                description:
                                    - "Minimum time the process must execute\nbefore taking the action"
            tracing_options:
                description:
                    - Tracing options.
            vnet_name:
                description:
                    - Virtual Network name.
            cors:
                description:
                    - Cross-Origin Resource Sharing (CORS) settings.
                suboptions:
                    allowed_origins:
                        description:
                            - "Gets or sets the list of origins that should be allowed to make cross-origin\ncalls (for example: http://example.com:12345). U
                               se '*' to allow all."
            push:
                description:
                    - Push endpoint settings.
                suboptions:
                    kind:
                        description:
                            - Kind of resource.
                    is_push_enabled:
                        description:
                            - Gets or sets a flag indicating whether the Push endpoint is enabled.
                    tag_whitelist_json:
                        description:
                            - Gets or sets a JSON string containing a list of tags that are whitelisted for use by the push registration endpoint.
                    tags_requiring_auth:
                        description:
                            - "Gets or sets a JSON string containing a list of tags that require user authentication to be used in the push registration endp
                               oint.\nTags can consist of alphanumeric characters and the following:\n'_', '@', '#', '.', ':', '-'. \nValidation should be pe
                               rformed at the PushRequestHandler."
                    dynamic_tags_json:
                        description:
                            - "Gets or sets a JSON string containing a list of dynamic tags that will be evaluated from user claims in the push registration
                               endpoint."
            api_definition:
                description:
                    - Information about the formal API definition for the app.
                suboptions:
                    url:
                        description:
                            - The URL of the API definition.
            auto_swap_slot_name:
                description:
                    - Auto-swap slot name.
            local_my_sql_enabled:
                description:
                    - <code>true</code> to enable local MySQL; otherwise, <code>false</code>.
            ip_security_restrictions:
                description:
                    - IP security restrictions.
                suboptions:
                    ip_address:
                        description:
                            - IP address the security restriction is valid for.
                        required: True
                    subnet_mask:
                        description:
                            - Subnet mask for the range of IP addresses the restriction is valid for.
    scm_site_also_stopped:
        description:
            - <code>true</code> to stop SCM (KUDU) site when the app is stopped; otherwise, <code>false</code>. The default is <code>false</code>.
    hosting_environment_profile:
        description:
            - App Service Environment to use for the app.
        suboptions:
            id:
                description:
                    - Resource ID of the App Service Environment.
    client_affinity_enabled:
        description:
            - "<code>true</code> to enable client affinity; <code>false</code> to stop sending session affinity cookies, which route client requests in the s
               ame session to the same instance. Default is <code>true</code>."
    client_cert_enabled:
        description:
            - "<code>true</code> to enable client certificate authentication (TLS mutual authentication); otherwise, <code>false</code>. Default is <code>fal
               se</code>."
    host_names_disabled:
        description:
            - "<code>true</code> to disable the public hostnames of the app; otherwise, <code>false</code>.\n If <code>true</code>, the app is only accessibl
               e via API management process."
    container_size:
        description:
            - Size of the function container.
    daily_memory_time_quota:
        description:
            - Maximum allowed daily memory-time quota (applicable on dynamic apps only).
    cloning_info:
        description:
            - If specified during app creation, the app is cloned from a source app.
        suboptions:
            correlation_id:
                description:
                    - "Correlation ID of cloning operation. This ID ties multiple cloning operations\ntogether to use the same snapshot."
            overwrite:
                description:
                    - <code>true</code> to overwrite destination app; otherwise, <code>false</code>.
            clone_custom_host_names:
                description:
                    - <code>true</code> to clone custom hostnames from source app; otherwise, <code>false</code>.
            clone_source_control:
                description:
                    - <code>true</code> to clone source control from source app; otherwise, <code>false</code>.
            source_web_app_id:
                description:
                    - "ARM resource ID of the source app. App resource ID is of the form \n/subscriptions/{subId}/resourceGroups/{resourceGroupName}/provider
                       s/Microsoft.Web/sites/{siteName} for production slots and \n/subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Micros
                       oft.Web/sites/{siteName}/slots/{slotName} for other slots."
                required: True
            hosting_environment:
                description:
                    - App Service Environment.
            app_settings_overrides:
                description:
                    - "Application setting overrides for cloned app. If specified, these settings override the settings cloned \nfrom source app. Otherwise,
                       application settings from source app are retained."
            configure_load_balancing:
                description:
                    - <code>true</code> to configure load balancing for source and destination app.
            traffic_manager_profile_id:
                description:
                    - "ARM resource ID of the Traffic Manager profile to use, if it exists. Traffic Manager resource ID is of the form \n/subscriptions/{subI
                       d}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}."
            traffic_manager_profile_name:
                description:
                    - Name of Traffic Manager profile to create. This is only needed if Traffic Manager profile does not already exist.
            ignore_quotas:
                description:
                    - <code>true</code> if quotas should be ignored; otherwise, <code>false</code>.
    snapshot_info:
        description:
            - If specified during app creation, the app is created from a previous snapshot.
        suboptions:
            kind:
                description:
                    - Kind of resource.
            snapshot_time:
                description:
                    - Point in time in which the app recovery should be attempted, formatted as a DateTime string.
            recovery_target:
                description:
                    - Specifies the web app that snapshot contents will be written to.
                suboptions:
                    location:
                        description:
                            - Geographical location of the target web app, e.g. SouthEastAsia, SouthCentralUS
                    id:
                        description:
                            - "ARM resource ID of the target app. \n/subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{
                               siteName} for production slots and \n/subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{
                               siteName}/slots/{slotName} for other slots."
            overwrite:
                description:
                    - If <code>true</code> the recovery operation can overwrite source app; otherwise, <code>false</code>.
            recover_configuration:
                description:
                    - If true, site configuration, in addition to content, will be reverted.
            ignore_conflicting_host_names:
                description:
                    - "If true, custom hostname conflicts will be ignored when recovering to a target web app.\nThis setting is only necessary when RecoverCo
                       nfiguration is enabled."
    https_only:
        description:
            - "HttpsOnly: configures a web site to accept only https requests. Issues redirect for\nhttp requests"
    identity:
        description:
            -
        suboptions:
            type:
                description:
                    - Type of managed service identity.
    skip_dns_registration:
        description:
            - "If true web app hostname is not registered with DNS on creation. This parameter is\n only used for app creation."
    skip_custom_domain_verification:
        description:
            - If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    force_dns_registration:
        description:
            - If true, web app hostname is force registered with DNS.
    ttl_in_seconds:
        description:
            - "Time to live in seconds for web app's default domain name."

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Create (or update) WebApps
    azure_rm_webwebapp:
      resource_group: resource_group_name
      name: name
      kind: kind
      location: location
      enabled: enabled
      host_name_ssl_states:
        - name: name
          ssl_state: ssl_state
          virtual_ip: virtual_ip
          thumbprint: thumbprint
          to_update: to_update
          host_type: host_type
      server_farm_id: server_farm_id
      reserved: reserved
      site_config:
        number_of_workers: number_of_workers
        default_documents:
          - XXXX - list of values -- not implemented str
        net_framework_version: net_framework_version
        php_version: php_version
        python_version: python_version
        node_version: node_version
        linux_fx_version: linux_fx_version
        request_tracing_enabled: request_tracing_enabled
        request_tracing_expiration_time: request_tracing_expiration_time
        remote_debugging_enabled: remote_debugging_enabled
        remote_debugging_version: remote_debugging_version
        http_logging_enabled: http_logging_enabled
        logs_directory_size_limit: logs_directory_size_limit
        detailed_error_logging_enabled: detailed_error_logging_enabled
        publishing_username: publishing_username
        app_settings:
          - name: name
            value: value
        connection_strings:
          - name: name
            connection_string: connection_string
            type: type
        handler_mappings:
          - extension: extension
            script_processor: script_processor
            arguments: arguments
        document_root: document_root
        scm_type: scm_type
        use32_bit_worker_process: use32_bit_worker_process
        web_sockets_enabled: web_sockets_enabled
        always_on: always_on
        java_version: java_version
        java_container: java_container
        java_container_version: java_container_version
        app_command_line: app_command_line
        managed_pipeline_mode: managed_pipeline_mode
        virtual_applications:
          - virtual_path: virtual_path
            physical_path: physical_path
            preload_enabled: preload_enabled
            virtual_directories:
              - virtual_path: virtual_path
                physical_path: physical_path
        load_balancing: load_balancing
        experiments:
          ramp_up_rules:
            - action_host_name: action_host_name
              reroute_percentage: reroute_percentage
              change_step: change_step
              change_interval_in_minutes: change_interval_in_minutes
              min_reroute_percentage: min_reroute_percentage
              max_reroute_percentage: max_reroute_percentage
              change_decision_callback_url: change_decision_callback_url
              name: name
        limits:
          max_percentage_cpu: max_percentage_cpu
          max_memory_in_mb: max_memory_in_mb
          max_disk_size_in_mb: max_disk_size_in_mb
        auto_heal_enabled: auto_heal_enabled
        auto_heal_rules:
          triggers:
            requests:
              count: count
              time_interval: time_interval
            private_bytes_in_kb: private_bytes_in_kb
            status_codes:
              - status: status
                sub_status: sub_status
                win32_status: win32_status
                count: count
                time_interval: time_interval
            slow_requests:
              time_taken: time_taken
              count: count
              time_interval: time_interval
          actions:
            action_type: action_type
            custom_action:
              exe: exe
              parameters: parameters
            min_process_execution_time: min_process_execution_time
        tracing_options: tracing_options
        vnet_name: vnet_name
        cors:
          allowed_origins:
            - XXXX - list of values -- not implemented str
        push:
          kind: kind
          is_push_enabled: is_push_enabled
          tag_whitelist_json: tag_whitelist_json
          tags_requiring_auth: tags_requiring_auth
          dynamic_tags_json: dynamic_tags_json
        api_definition:
          url: url
        auto_swap_slot_name: auto_swap_slot_name
        local_my_sql_enabled: local_my_sql_enabled
        ip_security_restrictions:
          - ip_address: ip_address
            subnet_mask: subnet_mask
      scm_site_also_stopped: scm_site_also_stopped
      hosting_environment_profile:
        id: id
      client_affinity_enabled: client_affinity_enabled
      client_cert_enabled: client_cert_enabled
      host_names_disabled: host_names_disabled
      container_size: container_size
      daily_memory_time_quota: daily_memory_time_quota
      cloning_info:
        correlation_id: correlation_id
        overwrite: overwrite
        clone_custom_host_names: clone_custom_host_names
        clone_source_control: clone_source_control
        source_web_app_id: source_web_app_id
        hosting_environment: hosting_environment
        app_settings_overrides: app_settings_overrides
        configure_load_balancing: configure_load_balancing
        traffic_manager_profile_id: traffic_manager_profile_id
        traffic_manager_profile_name: traffic_manager_profile_name
        ignore_quotas: ignore_quotas
      snapshot_info:
        kind: kind
        snapshot_time: snapshot_time
        recovery_target:
          location: location
          id: id
        overwrite: overwrite
        recover_configuration: recover_configuration
        ignore_conflicting_host_names: ignore_conflicting_host_names
      https_only: https_only
      identity:
        type: type
      skip_dns_registration: skip_dns_registration
      skip_custom_domain_verification: skip_custom_domain_verification
      force_dns_registration: force_dns_registration
      ttl_in_seconds: ttl_in_seconds
'''

RETURN = '''
id:
    description:
        - Resource Id.
    returned: always
    type: str
    sample: id
state:
    description:
        - Current state of the app.
    returned: always
    type: str
    sample: state
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


class AzureRMWebApps(AzureRMModuleBase):
    """Configuration class for an Azure RM WebApps resource"""

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
            enabled=dict(
                type='str',
                required=False
            ),
            host_name_ssl_states=dict(
                type='list',
                required=False
            ),
            server_farm_id=dict(
                type='str',
                required=False
            ),
            reserved=dict(
                type='str',
                required=False
            ),
            site_config=dict(
                type='dict',
                required=False
            ),
            scm_site_also_stopped=dict(
                type='str',
                required=False
            ),
            hosting_environment_profile=dict(
                type='dict',
                required=False
            ),
            client_affinity_enabled=dict(
                type='str',
                required=False
            ),
            client_cert_enabled=dict(
                type='str',
                required=False
            ),
            host_names_disabled=dict(
                type='str',
                required=False
            ),
            container_size=dict(
                type='int',
                required=False
            ),
            daily_memory_time_quota=dict(
                type='int',
                required=False
            ),
            cloning_info=dict(
                type='dict',
                required=False
            ),
            snapshot_info=dict(
                type='dict',
                required=False
            ),
            https_only=dict(
                type='str',
                required=False
            ),
            identity=dict(
                type='dict',
                required=False
            ),
            skip_dns_registration=dict(
                type='str',
                required=False
            ),
            skip_custom_domain_verification=dict(
                type='str',
                required=False
            ),
            force_dns_registration=dict(
                type='str',
                required=False
            ),
            ttl_in_seconds=dict(
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
        self.name = None
        self.site_envelope = dict()
        self.skip_dns_registration = None
        self.skip_custom_domain_verification = None
        self.force_dns_registration = None
        self.ttl_in_seconds = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMWebApps, self).__init__(derived_arg_spec=self.module_arg_spec,
                                             supports_check_mode=True,
                                             supports_tags=True)

    def exec_module(self, **kwargs):
        """Main module execution method"""

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                if key == "kind":
                    self.site_envelope["kind"] = kwargs[key]
                elif key == "location":
                    self.site_envelope["location"] = kwargs[key]
                elif key == "enabled":
                    self.site_envelope["enabled"] = kwargs[key]
                elif key == "host_name_ssl_states":
                    self.site_envelope["host_name_ssl_states"] = kwargs[key]
                elif key == "server_farm_id":
                    self.site_envelope["server_farm_id"] = kwargs[key]
                elif key == "reserved":
                    self.site_envelope["reserved"] = kwargs[key]
                elif key == "site_config":
                    self.site_envelope["site_config"] = kwargs[key]
                elif key == "scm_site_also_stopped":
                    self.site_envelope["scm_site_also_stopped"] = kwargs[key]
                elif key == "hosting_environment_profile":
                    self.site_envelope["hosting_environment_profile"] = kwargs[key]
                elif key == "client_affinity_enabled":
                    self.site_envelope["client_affinity_enabled"] = kwargs[key]
                elif key == "client_cert_enabled":
                    self.site_envelope["client_cert_enabled"] = kwargs[key]
                elif key == "host_names_disabled":
                    self.site_envelope["host_names_disabled"] = kwargs[key]
                elif key == "container_size":
                    self.site_envelope["container_size"] = kwargs[key]
                elif key == "daily_memory_time_quota":
                    self.site_envelope["daily_memory_time_quota"] = kwargs[key]
                elif key == "cloning_info":
                    self.site_envelope["cloning_info"] = kwargs[key]
                elif key == "snapshot_info":
                    self.site_envelope["snapshot_info"] = kwargs[key]
                elif key == "https_only":
                    self.site_envelope["https_only"] = kwargs[key]
                elif key == "identity":
                    self.site_envelope["identity"] = kwargs[key]

        old_response = None
        response = None
        results = dict()

        self.mgmt_client = self.get_mgmt_svc_client(WebSiteManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if "location" not in self.parameters:
            self.parameters["location"] = resource_group.location

        old_response = self.get_webapps()

        if not old_response:
            self.log("WebApps instance doesn't exist")
            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log("WebApps instance already exists")
            if self.state == 'absent':
                self.to_do = Actions.Delete
            elif self.state == 'present':
                self.log("Need to check if WebApps instance has to be deleted or may be updated")
                self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log("Need to Create / Update the WebApps instance")

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_webapps()

            if not old_response:
                self.results['changed'] = True
            else:
                self.results['changed'] = old_response.__ne__(response)
            self.log("Creation / Update done")
        elif self.to_do == Actions.Delete:
            self.log("WebApps instance deleted")
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_webapps()
            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_webapps():
                time.sleep(20)
        else:
            self.log("WebApps instance unchanged")
            self.results['changed'] = False
            response = old_response

        if response:
            self.results["id"] = response["id"]
            self.results["state"] = response["state"]

        return self.results

    def create_update_webapps(self):
        '''
        Creates or updates WebApps with the specified configuration.

        :return: deserialized WebApps instance state dictionary
        '''
        self.log("Creating / Updating the WebApps instance {0}".format(self.name))

        try:
            response = self.mgmt_client.web_apps.create_or_update(self.resource_group,
                                                                  self.name,
                                                                  self.site_envelope)
            if isinstance(response, AzureOperationPoller):
                response = self.get_poller_result(response)

        except CloudError as exc:
            self.log('Error attempting to create the WebApps instance.')
            self.fail("Error creating the WebApps instance: {0}".format(str(exc)))
        return response.as_dict()

    def delete_webapps(self):
        '''
        Deletes specified WebApps instance in the specified subscription and resource group.

        :return: True
        '''
        self.log("Deleting the WebApps instance {0}".format(self.name))
        try:
            response = self.mgmt_client.web_apps.delete(self.resource_group,
                                                        self.name)
        except CloudError as e:
            self.log('Error attempting to delete the WebApps instance.')
            self.fail("Error deleting the WebApps instance: {0}".format(str(e)))

        return True

    def get_webapps(self):
        '''
        Gets the properties of the specified WebApps.

        :return: deserialized WebApps instance state dictionary
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


def main():
    """Main execution"""
    AzureRMWebApps()

if __name__ == '__main__':
    main()
