# HuaweiCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/huaweicloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - (Optional) The access key of the HuaweiCloud to use.

* `secret_key` - (Optional) The secret key of the HuaweiCloud to use.

* `auth_url` - (Required) The Identity authentication URL.

* `region` - (Optional) The region of the HuaweiCloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region HuaweiCloud environments, but this behavior may vary
  depending on the HuaweiCloud environment being used.

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
  will only work when used with the HuaweiCloud Object Storage resources.

* `use_octavia` - (Optional) If set to `true`, API requests will go the Load Balancer
  service (Octavia) instead of the Networking service (Neutron).


## Supported Resources

* [Terraform::HuaweiCloud::AsConfigurationV1](AsConfigurationV1.md)
* [Terraform::HuaweiCloud::AsGroupV1](AsGroupV1.md)
* [Terraform::HuaweiCloud::AsPolicyV1](AsPolicyV1.md)
* [Terraform::HuaweiCloud::BlockstorageVolumeV2](BlockstorageVolumeV2.md)
* [Terraform::HuaweiCloud::CceClusterV3](CceClusterV3.md)
* [Terraform::HuaweiCloud::CceNodesV3](CceNodesV3.md)
* [Terraform::HuaweiCloud::CesAlarmrule](CesAlarmrule.md)
* [Terraform::HuaweiCloud::ComputeFloatingipAssociateV2](ComputeFloatingipAssociateV2.md)
* [Terraform::HuaweiCloud::ComputeFloatingipV2](ComputeFloatingipV2.md)
* [Terraform::HuaweiCloud::ComputeInstanceV2](ComputeInstanceV2.md)
* [Terraform::HuaweiCloud::ComputeKeypairV2](ComputeKeypairV2.md)
* [Terraform::HuaweiCloud::ComputeSecgroupV2](ComputeSecgroupV2.md)
* [Terraform::HuaweiCloud::ComputeServergroupV2](ComputeServergroupV2.md)
* [Terraform::HuaweiCloud::ComputeVolumeAttachV2](ComputeVolumeAttachV2.md)
* [Terraform::HuaweiCloud::CsbsBackupPolicyV1](CsbsBackupPolicyV1.md)
* [Terraform::HuaweiCloud::CsbsBackupV1](CsbsBackupV1.md)
* [Terraform::HuaweiCloud::CtsTrackerV1](CtsTrackerV1.md)
* [Terraform::HuaweiCloud::DcsInstanceV1](DcsInstanceV1.md)
* [Terraform::HuaweiCloud::DmsGroupV1](DmsGroupV1.md)
* [Terraform::HuaweiCloud::DmsInstanceV1](DmsInstanceV1.md)
* [Terraform::HuaweiCloud::DmsQueueV1](DmsQueueV1.md)
* [Terraform::HuaweiCloud::DnsRecordsetV2](DnsRecordsetV2.md)
* [Terraform::HuaweiCloud::DnsZoneV2](DnsZoneV2.md)
* [Terraform::HuaweiCloud::DwsCluster](DwsCluster.md)
* [Terraform::HuaweiCloud::ElbBackendecs](ElbBackendecs.md)
* [Terraform::HuaweiCloud::ElbHealthcheck](ElbHealthcheck.md)
* [Terraform::HuaweiCloud::ElbListener](ElbListener.md)
* [Terraform::HuaweiCloud::ElbLoadbalancer](ElbLoadbalancer.md)
* [Terraform::HuaweiCloud::FwFirewallGroupV2](FwFirewallGroupV2.md)
* [Terraform::HuaweiCloud::FwPolicyV2](FwPolicyV2.md)
* [Terraform::HuaweiCloud::FwRuleV2](FwRuleV2.md)
* [Terraform::HuaweiCloud::IamAgencyV3](IamAgencyV3.md)
* [Terraform::HuaweiCloud::ImagesImageV2](ImagesImageV2.md)
* [Terraform::HuaweiCloud::KmsKeyV1](KmsKeyV1.md)
* [Terraform::HuaweiCloud::LbListenerV2](LbListenerV2.md)
* [Terraform::HuaweiCloud::LbLoadbalancerV2](LbLoadbalancerV2.md)
* [Terraform::HuaweiCloud::LbMemberV2](LbMemberV2.md)
* [Terraform::HuaweiCloud::LbMonitorV2](LbMonitorV2.md)
* [Terraform::HuaweiCloud::LbPoolV2](LbPoolV2.md)
* [Terraform::HuaweiCloud::MaasTaskV1](MaasTaskV1.md)
* [Terraform::HuaweiCloud::MlsInstance](MlsInstance.md)
* [Terraform::HuaweiCloud::MrsClusterV1](MrsClusterV1.md)
* [Terraform::HuaweiCloud::MrsJobV1](MrsJobV1.md)
* [Terraform::HuaweiCloud::NatGatewayV2](NatGatewayV2.md)
* [Terraform::HuaweiCloud::NatSnatRuleV2](NatSnatRuleV2.md)
* [Terraform::HuaweiCloud::NetworkingFloatingipAssociateV2](NetworkingFloatingipAssociateV2.md)
* [Terraform::HuaweiCloud::NetworkingFloatingipV2](NetworkingFloatingipV2.md)
* [Terraform::HuaweiCloud::NetworkingNetworkV2](NetworkingNetworkV2.md)
* [Terraform::HuaweiCloud::NetworkingPortV2](NetworkingPortV2.md)
* [Terraform::HuaweiCloud::NetworkingRouterInterfaceV2](NetworkingRouterInterfaceV2.md)
* [Terraform::HuaweiCloud::NetworkingRouterRouteV2](NetworkingRouterRouteV2.md)
* [Terraform::HuaweiCloud::NetworkingRouterV2](NetworkingRouterV2.md)
* [Terraform::HuaweiCloud::NetworkingSecgroupRuleV2](NetworkingSecgroupRuleV2.md)
* [Terraform::HuaweiCloud::NetworkingSecgroupV2](NetworkingSecgroupV2.md)
* [Terraform::HuaweiCloud::NetworkingSubnetV2](NetworkingSubnetV2.md)
* [Terraform::HuaweiCloud::RdsInstanceV1](RdsInstanceV1.md)
* [Terraform::HuaweiCloud::RtsSoftwareConfigV1](RtsSoftwareConfigV1.md)
* [Terraform::HuaweiCloud::RtsStackV1_](RtsStackV1_.md)
* [Terraform::HuaweiCloud::S3BucketObject](S3BucketObject.md)
* [Terraform::HuaweiCloud::S3BucketPolicy](S3BucketPolicy.md)
* [Terraform::HuaweiCloud::S3Bucket](S3Bucket.md)
* [Terraform::HuaweiCloud::SfsFileSystemV2](SfsFileSystemV2.md)
* [Terraform::HuaweiCloud::SmnSubscriptionV2](SmnSubscriptionV2.md)
* [Terraform::HuaweiCloud::SmnTopicV2](SmnTopicV2.md)
* [Terraform::HuaweiCloud::VbsBackupPolicyV2](VbsBackupPolicyV2.md)
* [Terraform::HuaweiCloud::VbsBackupV2](VbsBackupV2.md)
* [Terraform::HuaweiCloud::VpcEipV1](VpcEipV1.md)
* [Terraform::HuaweiCloud::VpcPeeringConnectionAccepterV2](VpcPeeringConnectionAccepterV2.md)
* [Terraform::HuaweiCloud::VpcPeeringConnectionV2](VpcPeeringConnectionV2.md)
* [Terraform::HuaweiCloud::VpcRouteV2](VpcRouteV2.md)
* [Terraform::HuaweiCloud::VpcSubnetV1](VpcSubnetV1.md)
* [Terraform::HuaweiCloud::VpcV1](VpcV1.md)