# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkdcs.v2.model.add_replication_body import AddReplicationBody
from huaweicloudsdkdcs.v2.model.attrs_object import AttrsObject
from huaweicloudsdkdcs.v2.model.available_zones import AvailableZones
from huaweicloudsdkdcs.v2.model.backup_files_body import BackupFilesBody
from huaweicloudsdkdcs.v2.model.backup_instance_body import BackupInstanceBody
from huaweicloudsdkdcs.v2.model.backup_plan import BackupPlan
from huaweicloudsdkdcs.v2.model.backup_policy import BackupPolicy
from huaweicloudsdkdcs.v2.model.backup_record_response import BackupRecordResponse
from huaweicloudsdkdcs.v2.model.batch_create_or_delete_dcs_tags_request import BatchCreateOrDeleteDcsTagsRequest
from huaweicloudsdkdcs.v2.model.batch_create_or_delete_dcs_tags_response import BatchCreateOrDeleteDcsTagsResponse
from huaweicloudsdkdcs.v2.model.batch_delete_body import BatchDeleteBody
from huaweicloudsdkdcs.v2.model.batch_delete_dcs_instances_request import BatchDeleteDCSInstancesRequest
from huaweicloudsdkdcs.v2.model.batch_delete_dcs_instances_response import BatchDeleteDCSInstancesResponse
from huaweicloudsdkdcs.v2.model.batch_ops_result import BatchOpsResult
from huaweicloudsdkdcs.v2.model.bss_param import BssParam
from huaweicloudsdkdcs.v2.model.change_instance_status_body import ChangeInstanceStatusBody
from huaweicloudsdkdcs.v2.model.cluster_redis_node_monitored_object import ClusterRedisNodeMonitoredObject
from huaweicloudsdkdcs.v2.model.copy_instance_request import CopyInstanceRequest
from huaweicloudsdkdcs.v2.model.copy_instance_response import CopyInstanceResponse
from huaweicloudsdkdcs.v2.model.create_dcs_instance_request import CreateDCSInstanceRequest
from huaweicloudsdkdcs.v2.model.create_dcs_instance_response import CreateDCSInstanceResponse
from huaweicloudsdkdcs.v2.model.create_instance_body import CreateInstanceBody
from huaweicloudsdkdcs.v2.model.create_migration_task_body import CreateMigrationTaskBody
from huaweicloudsdkdcs.v2.model.create_migration_task_request import CreateMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.create_migration_task_response import CreateMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.create_or_delete_instance_tags import CreateOrDeleteInstanceTags
from huaweicloudsdkdcs.v2.model.create_replication_request import CreateReplicationRequest
from huaweicloudsdkdcs.v2.model.create_replication_response import CreateReplicationResponse
from huaweicloudsdkdcs.v2.model.delete_backup_file_request import DeleteBackupFileRequest
from huaweicloudsdkdcs.v2.model.delete_backup_file_response import DeleteBackupFileResponse
from huaweicloudsdkdcs.v2.model.delete_ip_from_domain_name_request import DeleteIpFromDomainNameRequest
from huaweicloudsdkdcs.v2.model.delete_ip_from_domain_name_response import DeleteIpFromDomainNameResponse
from huaweicloudsdkdcs.v2.model.delete_migrate_task_request import DeleteMigrateTaskRequest
from huaweicloudsdkdcs.v2.model.delete_migration_task_request import DeleteMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.delete_migration_task_response import DeleteMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.delete_replication_request import DeleteReplicationRequest
from huaweicloudsdkdcs.v2.model.delete_replication_response import DeleteReplicationResponse
from huaweicloudsdkdcs.v2.model.delete_single_dcs_instance_request import DeleteSingleDCSInstanceRequest
from huaweicloudsdkdcs.v2.model.delete_single_dcs_instance_response import DeleteSingleDCSInstanceResponse
from huaweicloudsdkdcs.v2.model.dim_child import DimChild
from huaweicloudsdkdcs.v2.model.download_backup_files_req import DownloadBackupFilesReq
from huaweicloudsdkdcs.v2.model.files import Files
from huaweicloudsdkdcs.v2.model.flavor_az_object import FlavorAzObject
from huaweicloudsdkdcs.v2.model.flavors_items import FlavorsItems
from huaweicloudsdkdcs.v2.model.instance_group_list_info import InstanceGroupListInfo
from huaweicloudsdkdcs.v2.model.instance_replication_list_info import InstanceReplicationListInfo
from huaweicloudsdkdcs.v2.model.instance_restore_info import InstanceRestoreInfo
from huaweicloudsdkdcs.v2.model.instance_statistic import InstanceStatistic
from huaweicloudsdkdcs.v2.model.instances import Instances
from huaweicloudsdkdcs.v2.model.instances_monitored_object import InstancesMonitoredObject
from huaweicloudsdkdcs.v2.model.links_item import LinksItem
from huaweicloudsdkdcs.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkdcs.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkdcs.v2.model.list_backup_file_links_request import ListBackupFileLinksRequest
from huaweicloudsdkdcs.v2.model.list_backup_file_links_response import ListBackupFileLinksResponse
from huaweicloudsdkdcs.v2.model.list_backup_records_request import ListBackupRecordsRequest
from huaweicloudsdkdcs.v2.model.list_backup_records_response import ListBackupRecordsResponse
from huaweicloudsdkdcs.v2.model.list_ces_monitored_objects_request import ListCESMonitoredObjectsRequest
from huaweicloudsdkdcs.v2.model.list_ces_monitored_objects_response import ListCESMonitoredObjectsResponse
from huaweicloudsdkdcs.v2.model.list_configurations_request import ListConfigurationsRequest
from huaweicloudsdkdcs.v2.model.list_configurations_response import ListConfigurationsResponse
from huaweicloudsdkdcs.v2.model.list_dcs_tags_of_tenant_request import ListDcsTagsOfTenantRequest
from huaweicloudsdkdcs.v2.model.list_dcs_tags_of_tenant_response import ListDcsTagsOfTenantResponse
from huaweicloudsdkdcs.v2.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkdcs.v2.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkdcs.v2.model.list_group_replication_info_request import ListGroupReplicationInfoRequest
from huaweicloudsdkdcs.v2.model.list_group_replication_info_response import ListGroupReplicationInfoResponse
from huaweicloudsdkdcs.v2.model.list_maintenance_windows_request import ListMaintenanceWindowsRequest
from huaweicloudsdkdcs.v2.model.list_maintenance_windows_response import ListMaintenanceWindowsResponse
from huaweicloudsdkdcs.v2.model.list_migration_task_request import ListMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.list_migration_task_response import ListMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.list_monitored_objects_of_instance_request import ListMonitoredObjectsOfInstanceRequest
from huaweicloudsdkdcs.v2.model.list_monitored_objects_of_instance_response import ListMonitoredObjectsOfInstanceResponse
from huaweicloudsdkdcs.v2.model.list_number_of_instances_in_different_status_request import ListNumberOfInstancesInDifferentStatusRequest
from huaweicloudsdkdcs.v2.model.list_number_of_instances_in_different_status_response import ListNumberOfInstancesInDifferentStatusResponse
from huaweicloudsdkdcs.v2.model.list_restore_records_request import ListRestoreRecordsRequest
from huaweicloudsdkdcs.v2.model.list_restore_records_response import ListRestoreRecordsResponse
from huaweicloudsdkdcs.v2.model.list_statistics_of_running_instances_request import ListStatisticsOfRunningInstancesRequest
from huaweicloudsdkdcs.v2.model.list_statistics_of_running_instances_response import ListStatisticsOfRunningInstancesResponse
from huaweicloudsdkdcs.v2.model.maintain_windows import MaintainWindows
from huaweicloudsdkdcs.v2.model.migration_task_list import MigrationTaskList
from huaweicloudsdkdcs.v2.model.modify_instance_body import ModifyInstanceBody
from huaweicloudsdkdcs.v2.model.modify_instance_password_body import ModifyInstancePasswordBody
from huaweicloudsdkdcs.v2.model.modify_ip_whitelist_body import ModifyIpWhitelistBody
from huaweicloudsdkdcs.v2.model.modify_redis_config_body import ModifyRedisConfigBody
from huaweicloudsdkdcs.v2.model.priority_body import PriorityBody
from huaweicloudsdkdcs.v2.model.proxy_node_monitored_object import ProxyNodeMonitoredObject
from huaweicloudsdkdcs.v2.model.query_redis_config import QueryRedisConfig
from huaweicloudsdkdcs.v2.model.query_tenant_quota_resp_quotas import QueryTenantQuotaRespQuotas
from huaweicloudsdkdcs.v2.model.redis_config import RedisConfig
from huaweicloudsdkdcs.v2.model.resource_tag import ResourceTag
from huaweicloudsdkdcs.v2.model.resources import Resources
from huaweicloudsdkdcs.v2.model.restart_or_flush_dcs_instances_request import RestartOrFlushDCSInstancesRequest
from huaweicloudsdkdcs.v2.model.restart_or_flush_dcs_instances_response import RestartOrFlushDCSInstancesResponse
from huaweicloudsdkdcs.v2.model.restore_instance_body import RestoreInstanceBody
from huaweicloudsdkdcs.v2.model.restore_instance_request import RestoreInstanceRequest
from huaweicloudsdkdcs.v2.model.restore_instance_response import RestoreInstanceResponse
from huaweicloudsdkdcs.v2.model.show_dcs_tags_request import ShowDcsTagsRequest
from huaweicloudsdkdcs.v2.model.show_dcs_tags_response import ShowDcsTagsResponse
from huaweicloudsdkdcs.v2.model.show_ip_whitelist_request import ShowIpWhitelistRequest
from huaweicloudsdkdcs.v2.model.show_ip_whitelist_response import ShowIpWhitelistResponse
from huaweicloudsdkdcs.v2.model.show_migration_task_request import ShowMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.show_migration_task_response import ShowMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.show_quota_of_tenant_request import ShowQuotaOfTenantRequest
from huaweicloudsdkdcs.v2.model.show_quota_of_tenant_response import ShowQuotaOfTenantResponse
from huaweicloudsdkdcs.v2.model.source_instance_body import SourceInstanceBody
from huaweicloudsdkdcs.v2.model.status_statistic import StatusStatistic
from huaweicloudsdkdcs.v2.model.stop_migration_task_request import StopMigrationTaskRequest
from huaweicloudsdkdcs.v2.model.stop_migration_task_response import StopMigrationTaskResponse
from huaweicloudsdkdcs.v2.model.tag import Tag
from huaweicloudsdkdcs.v2.model.target_instance_body import TargetInstanceBody
from huaweicloudsdkdcs.v2.model.update_configurations_request import UpdateConfigurationsRequest
from huaweicloudsdkdcs.v2.model.update_configurations_response import UpdateConfigurationsResponse
from huaweicloudsdkdcs.v2.model.update_dcs_instance_request import UpdateDCSInstanceRequest
from huaweicloudsdkdcs.v2.model.update_dcs_instance_response import UpdateDCSInstanceResponse
from huaweicloudsdkdcs.v2.model.update_ip_whitelist_request import UpdateIpWhitelistRequest
from huaweicloudsdkdcs.v2.model.update_ip_whitelist_response import UpdateIpWhitelistResponse
from huaweicloudsdkdcs.v2.model.update_password_request import UpdatePasswordRequest
from huaweicloudsdkdcs.v2.model.update_password_response import UpdatePasswordResponse
from huaweicloudsdkdcs.v2.model.update_slave_priority_request import UpdateSlavePriorityRequest
from huaweicloudsdkdcs.v2.model.update_slave_priority_response import UpdateSlavePriorityResponse
from huaweicloudsdkdcs.v2.model.whitelist import Whitelist
