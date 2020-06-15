# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class DcsAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(DcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdcs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def batch_create_or_delete_dcs_tags_async(self, request):
        """批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。

        :param BatchCreateOrDeleteDcsTagsRequest request
        :return: None
        """
        return self.batch_create_or_delete_dcs_tags_with_http_info(request)

    def batch_create_or_delete_dcs_tags_with_http_info(self, request):
        """批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。

        :param BatchCreateOrDeleteDcsTagsRequest request
        :return: None
        """

        all_params = ['instance_id', 'batch_create_or_delete_dcs_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/dcs/{instance_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_dcs_instances_async(self, request):
        """批量删除实例

        批量删除多个缓存实例。

        :param BatchDeleteDcsInstancesRequest request
        :return: BatchDeleteDCSInstancesResponse
        """
        return self.batch_delete_dcs_instances_with_http_info(request)

    def batch_delete_dcs_instances_with_http_info(self, request):
        """批量删除实例

        批量删除多个缓存实例。

        :param BatchDeleteDcsInstancesRequest request
        :return: tuple(BatchDeleteDCSInstancesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['all_failure', 'batch_delete_dcs_instances_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all_failure' in local_var_params:
            query_params.append(('all_failure', local_var_params['all_failure']))

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteDCSInstancesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_instance_async(self, request):
        """备份指定实例

        备份指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param CopyInstanceRequest request
        :return: CopyInstanceResponse
        """
        return self.copy_instance_with_http_info(request)

    def copy_instance_with_http_info(self, request):
        """备份指定实例

        备份指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param CopyInstanceRequest request
        :return: tuple(CopyInstanceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'copy_instance_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/backups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyInstanceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dcs_instance_async(self, request):
        """创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。

        :param CreateDcsInstanceRequest request
        :return: CreateDCSInstanceResponse
        """
        return self.create_dcs_instance_with_http_info(request)

    def create_dcs_instance_with_http_info(self, request):
        """创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。

        :param CreateDcsInstanceRequest request
        :return: tuple(CreateDCSInstanceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_dcs_instance_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDCSInstanceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_migration_task_async(self, request):
        """创建数据迁移任务

        创建数据迁移任务。

        :param CreateMigrationTaskRequest request
        :return: CreateMigrationTaskResponse
        """
        return self.create_migration_task_with_http_info(request)

    def create_migration_task_with_http_info(self, request):
        """创建数据迁移任务

        创建数据迁移任务。

        :param CreateMigrationTaskRequest request
        :return: tuple(CreateMigrationTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_migration_task_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/migration-task', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMigrationTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_replication_async(self, request):
        """添加副本

        为Cluster集群实例的分片添加副本。

        :param CreateReplicationRequest request
        :return: None
        """
        return self.create_replication_with_http_info(request)

    def create_replication_with_http_info(self, request):
        """添加副本

        为Cluster集群实例的分片添加副本。

        :param CreateReplicationRequest request
        :return: None
        """

        all_params = ['instance_id', 'group_id', 'create_replication_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instance/{instance_id}/groups/{group_id}/replications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backup_file_async(self, request):
        """删除备份文件

        删除缓存实例已备份的文件。

        :param DeleteBackupFileRequest request
        :return: None
        """
        return self.delete_backup_file_with_http_info(request)

    def delete_backup_file_with_http_info(self, request):
        """删除备份文件

        删除缓存实例已备份的文件。

        :param DeleteBackupFileRequest request
        :return: None
        """

        all_params = ['backup_id', 'instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/backups/{backup_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ip_from_domain_name_async(self, request):
        """域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。

        :param DeleteIpFromDomainNameRequest request
        :return: DeleteIpFromDomainNameResponse
        """
        return self.delete_ip_from_domain_name_with_http_info(request)

    def delete_ip_from_domain_name_with_http_info(self, request):
        """域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。

        :param DeleteIpFromDomainNameRequest request
        :return: tuple(DeleteIpFromDomainNameResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'group_id', 'node_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/remove-ip', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIpFromDomainNameResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_migration_task_async(self, request):
        """删除数据迁移任务

        删除数据迁移任务。

        :param DeleteMigrationTaskRequest request
        :return: DeleteMigrationTaskResponse
        """
        return self.delete_migration_task_with_http_info(request)

    def delete_migration_task_with_http_info(self, request):
        """删除数据迁移任务

        删除数据迁移任务。

        :param DeleteMigrationTaskRequest request
        :return: tuple(DeleteMigrationTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['delete_migration_task_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/migration-tasks/delete', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMigrationTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_replication_async(self, request):
        """删除副本

        为Cluster集群删除指定副本

        :param DeleteReplicationRequest request
        :return: DeleteReplicationResponse
        """
        return self.delete_replication_with_http_info(request)

    def delete_replication_with_http_info(self, request):
        """删除副本

        为Cluster集群删除指定副本

        :param DeleteReplicationRequest request
        :return: tuple(DeleteReplicationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'group_id', 'node_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteReplicationResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_single_dcs_instance_async(self, request):
        """删除实例

        删除指定的缓存实例，释放该实例的所有资源。  > 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。 

        :param DeleteSingleDcsInstanceRequest request
        :return: None
        """
        return self.delete_single_dcs_instance_with_http_info(request)

    def delete_single_dcs_instance_with_http_info(self, request):
        """删除实例

        删除指定的缓存实例，释放该实例的所有资源。  > 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。 

        :param DeleteSingleDcsInstanceRequest request
        :return: None
        """

        all_params = ['instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_zones_async(self, request):
        """查询可用区信息

        查询所在局点的可用区信息

        :param ListAvailableZonesRequest request
        :return: ListAvailableZonesResponse
        """
        return self.list_available_zones_with_http_info(request)

    def list_available_zones_with_http_info(self, request):
        """查询可用区信息

        查询所在局点的可用区信息

        :param ListAvailableZonesRequest request
        :return: tuple(ListAvailableZonesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/available-zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAvailableZonesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup_file_links_async(self, request):
        """获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。

        :param ListBackupFileLinksRequest request
        :return: ListBackupFileLinksResponse
        """
        return self.list_backup_file_links_with_http_info(request)

    def list_backup_file_links_with_http_info(self, request):
        """获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。

        :param ListBackupFileLinksRequest request
        :return: tuple(ListBackupFileLinksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'backup_id', 'list_backup_file_links_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/backups/{backup_id}/links', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupFileLinksResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup_records_async(self, request):
        """查询实例备份信息

        查询指定缓存实例的备份信息列表。

        :param ListBackupRecordsRequest request
        :return: ListBackupRecordsResponse
        """
        return self.list_backup_records_with_http_info(request)

    def list_backup_records_with_http_info(self, request):
        """查询实例备份信息

        查询指定缓存实例的备份信息列表。

        :param ListBackupRecordsRequest request
        :return: tuple(ListBackupRecordsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'begin_time', 'end_time', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/backups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupRecordsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ces_monitored_objects_async(self, request):
        """查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。 > 该接口当前仅在中国华南区开放。 

        :param ListCesMonitoredObjectsRequest request
        :return: ListCESMonitoredObjectsResponse
        """
        return self.list_ces_monitored_objects_with_http_info(request)

    def list_ces_monitored_objects_with_http_info(self, request):
        """查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。 > 该接口当前仅在中国华南区开放。 

        :param ListCesMonitoredObjectsRequest request
        :return: tuple(ListCESMonitoredObjectsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dim_name', 'offset', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/dims/monitored-objects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCESMonitoredObjectsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_async(self, request):
        """查询实例配置参数

        查询指定实例的配置参数信息。

        :param ListConfigurationsRequest request
        :return: ListConfigurationsResponse
        """
        return self.list_configurations_with_http_info(request)

    def list_configurations_with_http_info(self, request):
        """查询实例配置参数

        查询指定实例的配置参数信息。

        :param ListConfigurationsRequest request
        :return: tuple(ListConfigurationsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/configs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListConfigurationsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dcs_tags_of_tenant_async(self, request):
        """查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。

        :param ListDcsTagsOfTenantRequest request
        :return: ListDcsTagsOfTenantResponse
        """
        return self.list_dcs_tags_of_tenant_with_http_info(request)

    def list_dcs_tags_of_tenant_with_http_info(self, request):
        """查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。

        :param ListDcsTagsOfTenantRequest request
        :return: tuple(ListDcsTagsOfTenantResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/dcs/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDcsTagsOfTenantResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。

        :param ListFlavorsRequest request
        :return: tuple(ListFlavorsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['spec_code', 'cache_mode', 'engine', 'engine_version', 'cpu_type', 'capacity']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'cache_mode' in local_var_params:
            query_params.append(('cache_mode', local_var_params['cache_mode']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'engine_version' in local_var_params:
            query_params.append(('engine_version', local_var_params['engine_version']))
        if 'cpu_type' in local_var_params:
            query_params.append(('cpu_type', local_var_params['cpu_type']))
        if 'capacity' in local_var_params:
            query_params.append(('capacity', local_var_params['capacity']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/flavors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_group_replication_info_async(self, request):
        """查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。

        :param ListGroupReplicationInfoRequest request
        :return: ListGroupReplicationInfoResponse
        """
        return self.list_group_replication_info_with_http_info(request)

    def list_group_replication_info_with_http_info(self, request):
        """查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。

        :param ListGroupReplicationInfoRequest request
        :return: tuple(ListGroupReplicationInfoResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instance/{instance_id}/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGroupReplicationInfoResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_maintenance_windows_async(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ListMaintenanceWindowsRequest request
        :return: ListMaintenanceWindowsResponse
        """
        return self.list_maintenance_windows_with_http_info(request)

    def list_maintenance_windows_with_http_info(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ListMaintenanceWindowsRequest request
        :return: tuple(ListMaintenanceWindowsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/instances/maintain-windows', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMaintenanceWindowsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_migration_task_async(self, request):
        """查询迁移任务列表

        查询迁移任务列表。

        :param ListMigrationTaskRequest request
        :return: ListMigrationTaskResponse
        """
        return self.list_migration_task_with_http_info(request)

    def list_migration_task_with_http_info(self, request):
        """查询迁移任务列表

        查询迁移任务列表。

        :param ListMigrationTaskRequest request
        :return: tuple(ListMigrationTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['offset', 'limit', 'name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/migration-tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMigrationTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_monitored_objects_of_instance_async(self, request):
        """查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id > 该接口当前仅在中国华南区开放。 

        :param ListMonitoredObjectsOfInstanceRequest request
        :return: ListMonitoredObjectsOfInstanceResponse
        """
        return self.list_monitored_objects_of_instance_with_http_info(request)

    def list_monitored_objects_of_instance_with_http_info(self, request):
        """查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id > 该接口当前仅在中国华南区开放。 

        :param ListMonitoredObjectsOfInstanceRequest request
        :return: tuple(ListMonitoredObjectsOfInstanceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'dim_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/dims/monitored-objects/{instance_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMonitoredObjectsOfInstanceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_number_of_instances_in_different_status_async(self, request):
        """查询实例状态

        查询该租户在当前区域下不同状态的实例数。

        :param ListNumberOfInstancesInDifferentStatusRequest request
        :return: ListNumberOfInstancesInDifferentStatusResponse
        """
        return self.list_number_of_instances_in_different_status_with_http_info(request)

    def list_number_of_instances_in_different_status_with_http_info(self, request):
        """查询实例状态

        查询该租户在当前区域下不同状态的实例数。

        :param ListNumberOfInstancesInDifferentStatusRequest request
        :return: tuple(ListNumberOfInstancesInDifferentStatusResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['include_failure']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNumberOfInstancesInDifferentStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_restore_records_async(self, request):
        """查询实例恢复记录

        查询指定缓存实例的恢复记录列表。

        :param ListRestoreRecordsRequest request
        :return: ListRestoreRecordsResponse
        """
        return self.list_restore_records_with_http_info(request)

    def list_restore_records_with_http_info(self, request):
        """查询实例恢复记录

        查询指定缓存实例的恢复记录列表。

        :param ListRestoreRecordsRequest request
        :return: tuple(ListRestoreRecordsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'begin_time', 'end_time', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/restores', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRestoreRecordsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_statistics_of_running_instances_async(self, request):
        """查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。

        :param ListStatisticsOfRunningInstancesRequest request
        :return: ListStatisticsOfRunningInstancesResponse
        """
        return self.list_statistics_of_running_instances_with_http_info(request)

    def list_statistics_of_running_instances_with_http_info(self, request):
        """查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。

        :param ListStatisticsOfRunningInstancesRequest request
        :return: tuple(ListStatisticsOfRunningInstancesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/statistic', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStatisticsOfRunningInstancesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_or_flush_dcs_instances_async(self, request):
        """重启实例或清空数据

        重启运行中的DCS缓存实例。  清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。 

        :param RestartOrFlushDcsInstancesRequest request
        :return: RestartOrFlushDCSInstancesResponse
        """
        return self.restart_or_flush_dcs_instances_with_http_info(request)

    def restart_or_flush_dcs_instances_with_http_info(self, request):
        """重启实例或清空数据

        重启运行中的DCS缓存实例。  清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。 

        :param RestartOrFlushDcsInstancesRequest request
        :return: tuple(RestartOrFlushDCSInstancesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['restart_or_flush_dcs_instances_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartOrFlushDCSInstancesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_instance_async(self, request):
        """恢复指定实例

        恢复指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param RestoreInstanceRequest request
        :return: RestoreInstanceResponse
        """
        return self.restore_instance_with_http_info(request)

    def restore_instance_with_http_info(self, request):
        """恢复指定实例

        恢复指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param RestoreInstanceRequest request
        :return: tuple(RestoreInstanceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'restore_instance_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/restores', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestoreInstanceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dcs_tags_async(self, request):
        """查询单个实例标签

        通过实例id查询标签。

        :param ShowDcsTagsRequest request
        :return: ShowDcsTagsResponse
        """
        return self.show_dcs_tags_with_http_info(request)

    def show_dcs_tags_with_http_info(self, request):
        """查询单个实例标签

        通过实例id查询标签。

        :param ShowDcsTagsRequest request
        :return: tuple(ShowDcsTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDcsTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_migration_task_async(self, request):
        """查询迁移任务详情

        查询迁移任务详情。

        :param ShowMigrationTaskRequest request
        :return: ShowMigrationTaskResponse
        """
        return self.show_migration_task_with_http_info(request)

    def show_migration_task_with_http_info(self, request):
        """查询迁移任务详情

        查询迁移任务详情。

        :param ShowMigrationTaskRequest request
        :return: tuple(ShowMigrationTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['task_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/migration-task/{task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigrationTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_of_tenant_async(self, request):
        """查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。

        :param ShowQuotaOfTenantRequest request
        :return: ShowQuotaOfTenantResponse
        """
        return self.show_quota_of_tenant_with_http_info(request)

    def show_quota_of_tenant_with_http_info(self, request):
        """查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。

        :param ShowQuotaOfTenantRequest request
        :return: tuple(ShowQuotaOfTenantResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/quota', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaOfTenantResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_migration_task_async(self, request):
        """停止数据迁移任务

        停止数据迁移任务。

        :param StopMigrationTaskRequest request
        :return: StopMigrationTaskResponse
        """
        return self.stop_migration_task_with_http_info(request)

    def stop_migration_task_with_http_info(self, request):
        """停止数据迁移任务

        停止数据迁移任务。

        :param StopMigrationTaskRequest request
        :return: tuple(StopMigrationTaskResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['task_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/migration-task/{task_id}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopMigrationTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configurations_async(self, request):
        """修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。

        :param UpdateConfigurationsRequest request
        :return: None
        """
        return self.update_configurations_with_http_info(request)

    def update_configurations_with_http_info(self, request):
        """修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。

        :param UpdateConfigurationsRequest request
        :return: None
        """

        all_params = ['instance_id', 'update_configurations_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/configs', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dcs_instance_async(self, request):
        """修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。

        :param UpdateDcsInstanceRequest request
        :return: None
        """
        return self.update_dcs_instance_with_http_info(request)

    def update_dcs_instance_with_http_info(self, request):
        """修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。

        :param UpdateDcsInstanceRequest request
        :return: None
        """

        all_params = ['instance_id', 'update_dcs_instance_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_password_async(self, request):
        """修改密码

        修改缓存实例的密码。

        :param UpdatePasswordRequest request
        :return: UpdatePasswordResponse
        """
        return self.update_password_with_http_info(request)

    def update_password_with_http_info(self, request):
        """修改密码

        修改缓存实例的密码。

        :param UpdatePasswordRequest request
        :return: tuple(UpdatePasswordResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id', 'update_password_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePasswordResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_slave_priority_async(self, request):
        """设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。

        :param UpdateSlavePriorityRequest request
        :return: None
        """
        return self.update_slave_priority_with_http_info(request)

    def update_slave_priority_with_http_info(self, request):
        """设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。

        :param UpdateSlavePriorityRequest request
        :return: None
        """

        all_params = ['instance_id', 'group_id', 'node_id', 'update_slave_priority_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/slave-priority', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ip_whitelist_async(self, request):
        """查询指定实例的IP白名单

        查询指定实例的IP白名单。

        :param ShowIpWhitelistRequest request
        :return: ShowIpWhitelistResponse
        """
        return self.show_ip_whitelist_with_http_info(request)

    def show_ip_whitelist_with_http_info(self, request):
        """查询指定实例的IP白名单

        查询指定实例的IP白名单。

        :param ShowIpWhitelistRequest request
        :return: tuple(ShowIpWhitelistResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json;charset=UTF-8', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instance/{instance_id}/whitelist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIpWhitelistResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ip_whitelist_async(self, request):
        """设置IP白名单分组

        为指定实例设置IP白名单分组

        :param UpdateIpWhitelistRequest request
        :return: None
        """
        return self.update_ip_whitelist_with_http_info(request)

    def update_ip_whitelist_with_http_info(self, request):
        """设置IP白名单分组

        为指定实例设置IP白名单分组

        :param UpdateIpWhitelistRequest request
        :return: None
        """

        all_params = ['instance_id', 'update_ip_whitelist_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/instance/{instance_id}/whitelist', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type, True)
