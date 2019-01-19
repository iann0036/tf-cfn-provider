# TelefonicaOpenCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/telefonicaopencloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - (Optional) The access key of the TelefonicaOpenCloud to use.

* `secret_key` - (Optional) The secret key of the TelefonicaOpenCloud to use.

* `auth_url` - (Required) The Identity authentication URL.

* `region` - (Optional) The region of the TelefonicaOpenCloud cloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region TelefonicaOpenCloud environments, but this behavior may vary
  depending on the TelefonicaOpenCloud environment being used.

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
  will only work when used with the TelefonicaOpenCloud Object Storage resources.

* `use_octavia` - (Optional) If set to `true`, API requests will go the Load Balancer
  service (Octavia) instead of the Networking service (Neutron).


## Supported Resources

* [Terraform::TelefonicaOpenCloud::AntiddosV1](AntiddosV1.md)
* [Terraform::TelefonicaOpenCloud::AsConfigurationV1](AsConfigurationV1.md)
* [Terraform::TelefonicaOpenCloud::AsGroupV1](AsGroupV1.md)
* [Terraform::TelefonicaOpenCloud::AsPolicyV1](AsPolicyV1.md)
* [Terraform::TelefonicaOpenCloud::BlockstorageVolumeV2](BlockstorageVolumeV2.md)
* [Terraform::TelefonicaOpenCloud::CesAlarmrule](CesAlarmrule.md)
* [Terraform::TelefonicaOpenCloud::ComputeBmsServerV2](ComputeBmsServerV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeFloatingipAssociateV2](ComputeFloatingipAssociateV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeFloatingipV2](ComputeFloatingipV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeInstanceV2](ComputeInstanceV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeKeypairV2](ComputeKeypairV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeSecgroupV2](ComputeSecgroupV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeServergroupV2](ComputeServergroupV2.md)
* [Terraform::TelefonicaOpenCloud::ComputeVolumeAttachV2](ComputeVolumeAttachV2.md)
* [Terraform::TelefonicaOpenCloud::CsbsBackupPolicyV1](CsbsBackupPolicyV1.md)
* [Terraform::TelefonicaOpenCloud::CsbsBackupV1](CsbsBackupV1.md)
* [Terraform::TelefonicaOpenCloud::CtsTrackerV1](CtsTrackerV1.md)
* [Terraform::TelefonicaOpenCloud::DcsInstanceV1](DcsInstanceV1.md)
* [Terraform::TelefonicaOpenCloud::DmsGroupV2](DmsGroupV2.md)
* [Terraform::TelefonicaOpenCloud::DmsQueueV2](DmsQueueV2.md)
* [Terraform::TelefonicaOpenCloud::DnsRecordsetV2](DnsRecordsetV2.md)
* [Terraform::TelefonicaOpenCloud::DnsZoneV2](DnsZoneV2.md)
* [Terraform::TelefonicaOpenCloud::ElbBackendecs](ElbBackendecs.md)
* [Terraform::TelefonicaOpenCloud::ElbHealthcheck](ElbHealthcheck.md)
* [Terraform::TelefonicaOpenCloud::ElbListener](ElbListener.md)
* [Terraform::TelefonicaOpenCloud::ElbLoadbalancer](ElbLoadbalancer.md)
* [Terraform::TelefonicaOpenCloud::FwFirewallGroupV2](FwFirewallGroupV2.md)
* [Terraform::TelefonicaOpenCloud::FwPolicyV2](FwPolicyV2.md)
* [Terraform::TelefonicaOpenCloud::FwRuleV2](FwRuleV2.md)
* [Terraform::TelefonicaOpenCloud::MaasTaskV1](MaasTaskV1.md)
* [Terraform::TelefonicaOpenCloud::MrsClusterV1](MrsClusterV1.md)
* [Terraform::TelefonicaOpenCloud::MrsJobV1](MrsJobV1.md)
* [Terraform::TelefonicaOpenCloud::NetworkingFloatingipV2](NetworkingFloatingipV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingNetworkV2](NetworkingNetworkV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingPortV2](NetworkingPortV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingRouterInterfaceV2](NetworkingRouterInterfaceV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingRouterRouteV2](NetworkingRouterRouteV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingRouterV2](NetworkingRouterV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingSecgroupRuleV2](NetworkingSecgroupRuleV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingSecgroupV2](NetworkingSecgroupV2.md)
* [Terraform::TelefonicaOpenCloud::NetworkingSubnetV2](NetworkingSubnetV2.md)
* [Terraform::TelefonicaOpenCloud::RdsInstanceV1](RdsInstanceV1.md)
* [Terraform::TelefonicaOpenCloud::RtsSoftwareConfigV1](RtsSoftwareConfigV1.md)
* [Terraform::TelefonicaOpenCloud::RtsStackV1](RtsStackV1.md)
* [Terraform::TelefonicaOpenCloud::S3BucketObject](S3BucketObject.md)
* [Terraform::TelefonicaOpenCloud::S3BucketPolicy](S3BucketPolicy.md)
* [Terraform::TelefonicaOpenCloud::S3Bucket](S3Bucket.md)
* [Terraform::TelefonicaOpenCloud::SfsFileSystemV2](SfsFileSystemV2.md)
* [Terraform::TelefonicaOpenCloud::SmnSubscriptionV2](SmnSubscriptionV2.md)
* [Terraform::TelefonicaOpenCloud::SmnTopicV2](SmnTopicV2.md)
* [Terraform::TelefonicaOpenCloud::VbsBackupPolicyV2](VbsBackupPolicyV2.md)
* [Terraform::TelefonicaOpenCloud::VbsBackupV2](VbsBackupV2.md)
* [Terraform::TelefonicaOpenCloud::VpcEipV1](VpcEipV1.md)
* [Terraform::TelefonicaOpenCloud::VpcPeeringConnectionAccepterV2](VpcPeeringConnectionAccepterV2.md)
* [Terraform::TelefonicaOpenCloud::VpcPeeringConnectionV2](VpcPeeringConnectionV2.md)
* [Terraform::TelefonicaOpenCloud::VpcSubnetV1](VpcSubnetV1.md)
* [Terraform::TelefonicaOpenCloud::VpcV1](VpcV1.md)