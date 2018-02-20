#!/usr/bin/python
#
# Copyright (c) 2018 Alexander Yukhanov <alyukha@microsoft.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: azure_rm_storageshare
short_description: Manage Azure File Share objects.
version_added: ""
description:
    - Create, update and delete Azure File Shares.
options:
    storage_account_name:
        description:
            - Name of the storage account to use.
        required: true
        aliases:
            - account_name
            - storage_account
    share:
        description:
            - Name of a share.
        required: true
        aliases:
            - share_name
    resource_group:
        description:
            - Name of the resource group to use.
        required: true
        aliases:
            - resource_group_name
    state:
        description:
            - Assert the state of a file share.
            - Use state 'absent' to delete a file share.
            - Use state 'present' to create a share.
        default: present
        required: false
        choices:
            - absent
            - present

extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Alexander Yukhanov (@AlexanderYukhanov)"

'''

EXAMPLES = '''
- name: Create File Share 'foo'
  azure_rm_storageshare:
    resource_group: testing
    storage_account_name: mystorageacc
    share: foo

- name: Delete File Share 'foo'
  azure_rm_storageshare:
    resource_group: testing
    storage_account_name: mystorageacc
    share: foo
    state: absent
'''

RETURN = '''
share:
    description: Facts about the current state of the file share.
    returned: always
    type: dict
    sample: {
        "name": "myfileshare"
    }
'''

from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from azure.storage.file import FileService


class AzureRMStorageShare(AzureRMModuleBase):

    def __init__(self):
        self.module_arg_spec = dict(
            storage_account_name=dict(required=True, type='str', aliases=['account_name', 'storage_account']),
            share=dict(type='str', aliases=['share_name']),
            resource_group=dict(required=True, type='str', aliases=['resource_group_name']),
            state=dict(type='str', default='present', choices=['absent', 'present']),
        )
        self.storage_account_name = None
        self.resource_group = None
        self.share = None
        self.state = None
        self.file_service = None  # type: FileService
        self.results = dict(
            changed=False,
            share=dict(),
        )

        super(AzureRMStorageShare, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            setattr(self, key, kwargs[key])
        self.file_service = self.get_file_service(self.resource_group, self.storage_account_name)
        self.results['check_mode'] = self.check_mode
        self.results['share'] = self.get_share()
        self.results['changed'] = False
        if self.check_mode:
            return self.results
        if self.state == 'present' and self.results['share'] is None:
            self.create_share()
        elif self.state == 'absent' and self.results['share'] is not None:
            self.delete_share()
        return self.results

    def get_share(self):
        if self.file_service.exists(self.share):
            return {'name': self.share}
        return None

    def get_file_service(self, resource_group_name, storage_account_name):
        try:
            # Get keys from the storage account
            self.log('Getting keys')
            account_keys = self.storage_client.storage_accounts.list_keys(resource_group_name, storage_account_name)
        except Exception as exc:
            self.fail('Error getting keys for account {0} - {1}'.format(storage_account_name, str(exc)))

        try:
            self.log('Create file service')
            return FileService(storage_account_name, account_keys.keys[0].value)
        except Exception as exc:
            self.fail(
                'Error creating file service client for storage account {0} - {1}'.format(storage_account_name, exc))

    def create_share(self):
        try:
            self.file_service.create_share(self.share, fail_on_exist=False)
        except Exception as exc:
            self.fail(
                'Error creating file share {0} in account {1} - {2}'.format(self.share, self.storage_account_name, exc))
        self.results['share'] = {'name': self.share}
        self.results['changed'] = True

    def delete_share(self):
        try:
            self.file_service.delete_share(self.share, fail_not_exist=False)
        except Exception as exc:
            self.fail(
                'Error deleting file share {0} in account {1} - {2}'.format(self.share, self.storage_account_name, exc))
        self.results['share'] = None
        self.results['changed'] = True


def main():
    AzureRMStorageShare()


if __name__ == '__main__':
    main()
