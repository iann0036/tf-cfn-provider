# OpenTelekomCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opentelekomcloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - (Optional) The access key of the OpenTelekomCloud cloud to use.

* `secret_key` - (Optional) The secret key of the OpenTelekomCloud cloud to use.

* `auth_url` - (Required) The Identity authentication URL.

* `region` - (Optional) The region of the OpenTelekomCloud cloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region OpenTelekomCloud environments, but this behavior may vary
  depending on the OpenTelekomCloud environment being used.

* `user_name` - (Optional) The Username to login with.

* `user_id` - (Optional) The User ID to login with.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `password` - (Optional) The Password to login with.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3).

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).

* `insecure` - (Optional) Trust self-signed SSL certificates.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key.

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

* [Terraform::OpenTelekomCloud::AntiddosV1](AntiddosV1.md)
* [Terraform::OpenTelekomCloud::AsConfigurationV1](AsConfigurationV1.md)
* [Terraform::OpenTelekomCloud::AsGroupV1](AsGroupV1.md)
* [Terraform::OpenTelekomCloud::AsPolicyV1](AsPolicyV1.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeAttachV2](BlockstorageVolumeAttachV2.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeV2](BlockstorageVolumeV2.md)
* [Terraform::OpenTelekomCloud::CceClusterV3](CceClusterV3.md)
* [Terraform::OpenTelekomCloud::CceNodesV3](CceNodesV3.md)
* [Terraform::OpenTelekomCloud::CesAlarmrule](CesAlarmrule.md)
* [Terraform::OpenTelekomCloud::ComputeBmsServerV2](ComputeBmsServerV2.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2](ComputeFloatingipAssociateV2.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipV2](ComputeFloatingipV2.md)
* [Terraform::OpenTelekomCloud::ComputeInstanceV2](ComputeInstanceV2.md)
* [Terraform::OpenTelekomCloud::ComputeKeypairV2](ComputeKeypairV2.md)
* [Terraform::OpenTelekomCloud::ComputeSecgroupV2](ComputeSecgroupV2.md)
* [Terraform::OpenTelekomCloud::ComputeServergroupV2](ComputeServergroupV2.md)
* [Terraform::OpenTelekomCloud::ComputeVolumeAttachV2](ComputeVolumeAttachV2.md)
* [Terraform::OpenTelekomCloud::CsbsBackupPolicyV1](CsbsBackupPolicyV1.md)
* [Terraform::OpenTelekomCloud::CsbsBackupV1](CsbsBackupV1.md)
* [Terraform::OpenTelekomCloud::CtsTrackerV1](CtsTrackerV1.md)
* [Terraform::OpenTelekomCloud::DcsInstanceV1](DcsInstanceV1.md)
* [Terraform::OpenTelekomCloud::DmsGroupV2](DmsGroupV2.md)
* [Terraform::OpenTelekomCloud::DmsQueueV2](DmsQueueV2.md)
* [Terraform::OpenTelekomCloud::DnsRecordsetV2](DnsRecordsetV2.md)
* [Terraform::OpenTelekomCloud::DnsZoneV2](DnsZoneV2.md)
* [Terraform::OpenTelekomCloud::ElbBackend](ElbBackend.md)
* [Terraform::OpenTelekomCloud::ElbHealth](ElbHealth.md)
* [Terraform::OpenTelekomCloud::ElbListener](ElbListener.md)
* [Terraform::OpenTelekomCloud::ElbLoadbalancer](ElbLoadbalancer.md)
* [Terraform::OpenTelekomCloud::FwFirewallGroupV2](FwFirewallGroupV2.md)
* [Terraform::OpenTelekomCloud::FwPolicyV2](FwPolicyV2.md)
* [Terraform::OpenTelekomCloud::FwRuleV2](FwRuleV2.md)
* [Terraform::OpenTelekomCloud::IdentityGroupMembershipV3](IdentityGroupMembershipV3.md)
* [Terraform::OpenTelekomCloud::IdentityGroupV3](IdentityGroupV3.md)
* [Terraform::OpenTelekomCloud::IdentityProjectV3](IdentityProjectV3.md)
* [Terraform::OpenTelekomCloud::IdentityRoleAssignmentV3](IdentityRoleAssignmentV3.md)
* [Terraform::OpenTelekomCloud::IdentityRoleV3](IdentityRoleV3.md)
* [Terraform::OpenTelekomCloud::IdentityUserV3](IdentityUserV3.md)
* [Terraform::OpenTelekomCloud::ImagesImageV2](ImagesImageV2.md)
* [Terraform::OpenTelekomCloud::KmsKeyV1](KmsKeyV1.md)
* [Terraform::OpenTelekomCloud::LbListenerV2](LbListenerV2.md)
* [Terraform::OpenTelekomCloud::LbLoadbalancerV2](LbLoadbalancerV2.md)
* [Terraform::OpenTelekomCloud::LbMemberV2](LbMemberV2.md)
* [Terraform::OpenTelekomCloud::LbMonitorV2](LbMonitorV2.md)
* [Terraform::OpenTelekomCloud::LbPoolV2](LbPoolV2.md)
* [Terraform::OpenTelekomCloud::MaasTaskV1](MaasTaskV1.md)
* [Terraform::OpenTelekomCloud::MrsClusterV1](MrsClusterV1.md)
* [Terraform::OpenTelekomCloud::MrsJobV1](MrsJobV1.md)
* [Terraform::OpenTelekomCloud::NatGatewayV2](NatGatewayV2.md)
* [Terraform::OpenTelekomCloud::NatSnatRuleV2](NatSnatRuleV2.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2](NetworkingFloatingipAssociateV2.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipV2](NetworkingFloatingipV2.md)
* [Terraform::OpenTelekomCloud::NetworkingNetworkV2](NetworkingNetworkV2.md)
* [Terraform::OpenTelekomCloud::NetworkingPortV2](NetworkingPortV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterInterfaceV2](NetworkingRouterInterfaceV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterRouteV2](NetworkingRouterRouteV2.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterV2](NetworkingRouterV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupRuleV2](NetworkingSecgroupRuleV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupV2](NetworkingSecgroupV2.md)
* [Terraform::OpenTelekomCloud::NetworkingSubnetV2](NetworkingSubnetV2.md)
* [Terraform::OpenTelekomCloud::NetworkingVipAssociateV2](NetworkingVipAssociateV2.md)
* [Terraform::OpenTelekomCloud::NetworkingVipV2](NetworkingVipV2.md)
* [Terraform::OpenTelekomCloud::RdsInstanceV1](RdsInstanceV1.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareConfigV1](RtsSoftwareConfigV1.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1](RtsSoftwareDeploymentV1.md)
* [Terraform::OpenTelekomCloud::RtsStackV1](RtsStackV1.md)
* [Terraform::OpenTelekomCloud::S3BucketObject](S3BucketObject.md)
* [Terraform::OpenTelekomCloud::S3BucketPolicy](S3BucketPolicy.md)
* [Terraform::OpenTelekomCloud::S3Bucket](S3Bucket.md)
* [Terraform::OpenTelekomCloud::SfsFileSystemV2](SfsFileSystemV2.md)
* [Terraform::OpenTelekomCloud::SmnSubscriptionV2](SmnSubscriptionV2.md)
* [Terraform::OpenTelekomCloud::SmnTopicV2](SmnTopicV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupPolicyV2](VbsBackupPolicyV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupShareV2](VbsBackupShareV2.md)
* [Terraform::OpenTelekomCloud::VbsBackupV2](VbsBackupV2.md)
* [Terraform::OpenTelekomCloud::VpcEipV1](VpcEipV1.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2](VpcPeeringConnectionAccepterV2.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionV2](VpcPeeringConnectionV2.md)
* [Terraform::OpenTelekomCloud::VpcRouteV2](VpcRouteV2.md)
* [Terraform::OpenTelekomCloud::VpcSubnetV1](VpcSubnetV1.md)
* [Terraform::OpenTelekomCloud::VpcV1](VpcV1.md)