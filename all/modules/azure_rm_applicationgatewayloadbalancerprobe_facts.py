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
module: azure_rm_applicationgatewayloadbalancerprobe_facts
version_added: "2.5"
short_description: Get Load Balancer Probe facts.
description:
    - Get facts of Load Balancer Probe.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
    load_balancer_name:
        description:
            - The name of the load balancer.
        required: True
    probe_name:
        description:
            - The name of the probe.

extends_documentation_fragment:
    - azure

author:
    - "Zim Kalinowski (@zikalino)"

'''

EXAMPLES = '''
  - name: Get instance of Load Balancer Probe
    azure_rm_applicationgatewayloadbalancerprobe_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
      probe_name: probe_name

  - name: List instances of Load Balancer Probe
    azure_rm_applicationgatewayloadbalancerprobe_facts:
      resource_group: resource_group_name
      load_balancer_name: load_balancer_name
'''

RETURN = '''
load_balancer_probes:
    description: A list of dict results where the key is the name of the Load Balancer Probe and the values are the facts for that Load Balancer Probe.
    returned: always
    type: complex
    contains:
        loadbalancerprobe_name:
            description: The key is the name of the server that the values relate to.
            type: complex
            contains:
                id:
                    description:
                        - Resource ID.
                    returned: always
                    type: str
                    sample: /subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb/probes/probe1
                protocol:
                    description:
                        - "The protocol of the end point. Possible values are: C(Http) or C(Tcp). If C(Tcp) is specified, a received ACK is required for the
                          probe to be successful. If C(Http) is specified, a 200 OK response from the specifies URI is required for the probe to be successf
                          ul. Possible values include: C(Http), C(Tcp)"
                    returned: always
                    type: str
                    sample: Http
                port:
                    description:
                        - The port for communicating the probe. Possible values range from 1 to 65535, inclusive.
                    returned: always
                    type: int
                    sample: 80
                name:
                    description:
                        - Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
                    returned: always
                    type: str
                    sample: probe1
                etag:
                    description:
                        - A unique read-only string that changes whenever the resource is updated.
                    returned: always
                    type: str
                    sample: "W/\'00000000-0000-0000-0000-000000000000\'"
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


class AzureRMLoadBalancerProbesFacts(AzureRMModuleBase):
    def __init__(self):
        # define user inputs into argument
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            load_balancer_name=dict(
                type='str',
                required=True
            ),
            probe_name=dict(
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
        self.load_balancer_name = None
        self.probe_name = None
        super(AzureRMLoadBalancerProbesFacts, self).__init__(self.module_arg_spec)

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])
        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
                self.load_balancer_name is not None and
                self.probe_name is not None):
            self.results['load_balancer_probes'] = self.get()
        elif (self.resource_group is not None and
              self.load_balancer_name is not None):
            self.results['load_balancer_probes'] = self.list()
        return self.results

    def get(self):
        '''
        Gets facts of the specified Load Balancer Probe.

        :return: deserialized Load Balancer Probeinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.load_balancer_probes.get(resource_group_name=self.resource_group,
                                                                 load_balancer_name=self.load_balancer_name,
                                                                 probe_name=self.probe_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancerProbes.')

        if response is not None:
            results[response.name] = response.as_dict()

        return results

    def list(self):
        '''
        Gets facts of the specified Load Balancer Probe.

        :return: deserialized Load Balancer Probeinstance state dictionary
        '''
        response = None
        results = {}
        try:
            response = self.mgmt_client.load_balancer_probes.list(resource_group_name=self.resource_group,
                                                                  load_balancer_name=self.load_balancer_name)
            self.log("Response : {0}".format(response))
        except CloudError as e:
            self.log('Could not get facts for LoadBalancerProbes.')

        if response is not None:
            for item in response:
                results[item.name] = item.as_dict()

        return results


def main():
    AzureRMLoadBalancerProbesFacts()
if __name__ == '__main__':
    main()
