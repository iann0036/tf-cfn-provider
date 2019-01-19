# OpenTelekomCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opentelekomcloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - (Optional) The access key of the OpenTelekomCloud cloud to use.
  If omitted, the `OS_ACCESS_KEY` environment variable is used.

* `secret_key` - (Optional) The secret key of the OpenTelekomCloud cloud to use.
  If omitted, the `OS_SECRET_KEY` environment variable is used.

* `auth_url` - (Required) The Identity authentication URL. If omitted, the
  `OS_AUTH_URL` environment variable is used.

* `region` - (Optional) The region of the OpenTelekomCloud cloud to use. If omitted,
  the `OS_REGION_NAME` environment variable is used. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region OpenTelekomCloud environments, but this behavior may vary
  depending on the OpenTelekomCloud environment being used.

* `user_name` - (Optional) The Username to login with. If omitted, the
  `OS_USERNAME` environment variable is used.

* `user_id` - (Optional) The User ID to login with. If omitted, the
  `OS_USER_ID` environment variable is used.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_ID` or
  `OS_PROJECT_ID` environment variables are used.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_NAME` or
  `OS_PROJECT_NAME` environment variable are used.

* `password` - (Optional) The Password to login with. If omitted, the
  `OS_PASSWORD` environment variable is used.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform. If omitted, the `OS_AUTH_TOKEN` environment variable is used.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3). If
  If omitted, the following environment variables are checked (in this order):
  `OS_USER_DOMAIN_ID`, `OS_PROJECT_DOMAIN_ID`, `OS_DOMAIN_ID`.

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).
  If omitted, the following environment variables are checked (in this order):
  `OS_USER_DOMAIN_NAME`, `OS_PROJECT_DOMAIN_NAME`, `OS_DOMAIN_NAME`,
  `DEFAULT_DOMAIN`.

* `insecure` - (Optional) Trust self-signed SSL certificates. If omitted, the
  `OS_INSECURE` environment variable is used.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate. If omitted, the `OS_CACERT` environment variable is used.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate. If omitted the `OS_CERT` environment variable is used.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key. If omitted the `OS_KEY` environment variable is used.

* `endpoint_type` - (Optional) Specify which type of endpoint to use from the
  service catalog. It can be set using the OS_ENDPOINT_TYPE environment
  variable. If not set, public endpoints is used.

* `swauth` - (Optional) Set to `true` to authenticate against Swauth, a
  Swift-native authentication system. If omitted, the `OS_SWAUTH` environment
  variable is used. You must also set `username` to the Swauth/Swift username
  such as `username:project`. Set the `password` to the Swauth/Swift key.
  Finally, set `auth_url` as the location of the Swift service. Note that this
  will only work when used with the OpenTelekomCloud Object Storage resources.


## Supported Resources

* [Terraform::OpenTelekomCloud::AntiddosV1](docs/providers/opentelekomcloud/AntiddosV1.md)
* [Terraform::OpenTelekomCloud::AsConfigurationV1](docs/providers/opentelekomcloud/AsConfigurationV1.md)
* [Terraform::OpenTelekomCloud::AsGroupV1](docs/providers/opentelekomcloud/AsGroupV1.md)
* [Terraform::OpenTelekomCloud::AsPolicyV1](docs/providers/opentelekomcloud/AsPolicyV1.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeAttachV2](docs/providers/opentelekomcloud/BlockstorageVolumeAttachV2.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeV2](docs/providers/opentelekomcloud/BlockstorageVolumeV2.md)
* [Terraform::OpenTelekomCloud::CceClusterV3](docs/providers/opentelekomcloud/CceClusterV3.md)
* [Terraform::OpenTelekomCloud::CceNodesV3](docs/providers/opentelekomcloud/CceNodesV3.md)
* [Terraform::OpenTelekomCloud::CesAlarmrule](docs/providers/opentelekomcloud/CesAlarmrule.md)
* [Terraform::OpenTelekomCloud::ComputeBmsServerV2](docs/providers/opentelekomcloud/ComputeBmsServerV2.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2](docs/providers/opentelekomcloud/ComputeFloatingipAssociateV2.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipV2](docs/providers/opentelekomcloud/ComputeFloatingipV2.md)
* [Terraform::OpenTelekomCloud::ComputeInstanceV2](docs/providers/opentelekomcloud/ComputeInstanceV2.md)
* [Terraform::OpenTelekomCloud::ComputeKeypairV2](docs/providers/opentelekomcloud/ComputeKeypairV2.md)
* [Terraform::OpenTelekomCloud::ComputeSecgroupV2](docs/providers/opentelekomcloud/ComputeSecgroupV2.md)
* [Terraform::OpenTelekomCloud::ComputeServergroupV2](docs/providers/opentelekomcloud/ComputeServergroupV2.md)
* [Terraform::OpenTelekomCloud::ComputeVolumeAttachV2](docs/providers/opentelekomcloud/ComputeVolumeAttachV2.md)
* [Terraform::OpenTelekomCloud::CsbsBackupPolicyV1](docs/providers/opentelekomcloud/CsbsBackupPolicyV1.md)
* [Terraform::OpenTelekomCloud::CsbsBackupV1](docs/providers/opentelekomcloud/CsbsBackupV1.md)
* [Terraform::OpenTelekomCloud::CtsTrackerV1](docs/providers/opentelekomcloud/CtsTrackerV1.md)
* [Terraform::OpenTelekomCloud::DcsInstanceV1](docs/providers/opentelekomcloud/DcsInstanceV1.md)
* [Terraform::OpenTelekomCloud::DmsGroupV2](docs/providers/opentelekomcloud/DmsGroupV2.md)
* [Terraform::OpenTelekomCloud::DmsQueueV2](docs/providers/opentelekomcloud/DmsQueueV2.md)
* [Terraform::OpenTelekomCloud::DnsRecordsetV2](docs/providers/opentelekomcloud/DnsRecordsetV2.md)
* [Terraform::OpenTelekomCloud::DnsZoneV2](docs/providers/opentelekomcloud/DnsZoneV2.md)
* [Terraform::OpenTelekomCloud::ElbBackend](docs/providers/opentelekomcloud/ElbBackend.md)
* [Terraform::OpenTelekomCloud::ElbHealth](docs/providers/opentelekomcloud/ElbHealth.md)
* [Terraform::OpenTelekomCloud::ElbListener](docs/providers/opentelekomcloud/ElbListener.md)
* [Terraform::OpenTelekomCloud::ElbLoadbalancer](docs/providers/opentelekomcloud/ElbLoadbalancer.md)
* [Terraform::OpenTelekomCloud::FwFirewallGroupV2](docs/providers/opentelekomcloud/FwFirewallGroupV2.md)
* [Terraform::OpenTelekomCloud::FwPolicyV2](docs/providers/opentelekomcloud/FwPolicyV2.md)
* [Terraform::OpenTelekomCloud::FwRuleV2](docs/providers/opentelekomcloud/FwRuleV2.md)
* [Terraform::OpenTelekomCloud::ImagesImageV2](docs/providers/opentelekomcloud/ImagesImageV2.md)
* [Terraform::OpenTelekomCloud::KmsKeyV1](docs/providers/opentelekomcloud/KmsKeyV1.md)
* [Terraform::OpenTelekomCloud::LbListenerV2](docs/providers/opentelekomcloud/LbListenerV2.md)
* [Terraform::OpenTelekomCloud::LbLoadbalancerV2](docs/providers/opentelekomcloud/LbLoadbalancerV2.md)
* [Terraform::OpenTelekomCloud::LbMemberV2](docs/providers/opentelekomcloud/LbMemberV2.md)
* [Terraform::OpenTelekomCloud::LbMonitorV2](docs/providers/opentelekomcloud/LbMonitorV2.md)
* [Terraform::OpenTelekomCloud::LbPoolV2](docs/providers/opentelekomcloud/LbPoolV2.md)
* [Terraform::OpenTelekomCloud::MaasTaskV1](docs/providers/opentelekomcloud/MaasTaskV1.md)
* [Terraform::OpenTelekomCloud::MrsClusterV1](docs/providers/opentelekomcloud/MrsClusterV1.md)
* [Terraform::OpenTelekomCloud::MrsJobV1](docs/providers/opentelekomcloud/MrsJobV1.md)
* [Terraform::OpenTelekomCloud::NatGatewayV2](docs/providers/opentelekomcloud/NatGatewayV2.md)
* [Terraform::OpenTelekomCloud::NatSnatRuleV2](docs/providers/opentelekomcloud/NatSnatRuleV2.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2](docs/providers/opentelekomcloud/NetworkingFloatingipAssociateV2.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipV2](docs/providers/opentelekomcloud/NetworkingFloatingipV2.md)
* [Terraform::OpenTelekomCloud::NetworkingNetworkV2](docs/providers/opentelekomcloud/NetworkingNetworkV2.md)
* [Terraform::OpenTelekomCloud::NetworkingPortV2](docs/providers/opentelekomcloud/NetworkingPortV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterInterfaceV2](docs/providers/opentelekomcloud/NetworkingRouterInterfaceV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterRouteV2](docs/providers/opentelekomcloud/NetworkingRouterRouteV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterV2](docs/providers/opentelekomcloud/NetworkingRouterV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupRuleV2](docs/providers/opentelekomcloud/NetworkingSecgroupRuleV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupV2](docs/providers/opentelekomcloud/NetworkingSecgroupV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSubnetV2](docs/providers/opentelekomcloud/NetworkingSubnetV2.md)
* [Terraform::OpenTelekomCloud::NetworkingVipAssociateV2](docs/providers/opentelekomcloud/NetworkingVipAssociateV2.md)
* [Terraform::OpenTelekomCloud::NetworkingVipV2](docs/providers/opentelekomcloud/NetworkingVipV2.md)
* [Terraform::OpenTelekomCloud::RdsInstanceV1](docs/providers/opentelekomcloud/RdsInstanceV1.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareConfigV1](docs/providers/opentelekomcloud/RtsSoftwareConfigV1.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1](docs/providers/opentelekomcloud/RtsSoftwareDeploymentV1.md)
* [Terraform::OpenTelekomCloud::RtsStackV1](docs/providers/opentelekomcloud/RtsStackV1.md)
* [Terraform::OpenTelekomCloud::S3BucketObject](docs/providers/opentelekomcloud/S3BucketObject.md)
* [Terraform::OpenTelekomCloud::S3BucketPolicy](docs/providers/opentelekomcloud/S3BucketPolicy.md)
* [Terraform::OpenTelekomCloud::S3Bucket](docs/providers/opentelekomcloud/S3Bucket.md)
* [Terraform::OpenTelekomCloud::SfsFileSystemV2](docs/providers/opentelekomcloud/SfsFileSystemV2.md)
* [Terraform::OpenTelekomCloud::SmnSubscriptionV2](docs/providers/opentelekomcloud/SmnSubscriptionV2.md)
* [Terraform::OpenTelekomCloud::SmnTopicV2](docs/providers/opentelekomcloud/SmnTopicV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupPolicyV2](docs/providers/opentelekomcloud/VbsBackupPolicyV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupShareV2](docs/providers/opentelekomcloud/VbsBackupShareV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupV2](docs/providers/opentelekomcloud/VbsBackupV2.md)
* [Terraform::OpenTelekomCloud::VpcEipV1](docs/providers/opentelekomcloud/VpcEipV1.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2](docs/providers/opentelekomcloud/VpcPeeringConnectionAccepterV2.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionV2](docs/providers/opentelekomcloud/VpcPeeringConnectionV2.md)
* [Terraform::OpenTelekomCloud::VpcRouteV2](docs/providers/opentelekomcloud/VpcRouteV2.md)
* [Terraform::OpenTelekomCloud::VpcSubnetV1](docs/providers/opentelekomcloud/VpcSubnetV1.md)
* [Terraform::OpenTelekomCloud::VpcV1](docs/providers/opentelekomcloud/VpcV1.md)