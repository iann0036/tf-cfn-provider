# FlexibleEngine Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/flexibleengine** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - (Optional) The access key of the FlexibleEngine cloud to use.
  If omitted, the `OS_ACCESS_KEY` environment variable is used.

* `secret_key` - (Optional) The secret key of the FlexibleEngine cloud to use.
  If omitted, the `OS_SECRET_KEY` environment variable is used.

* `auth_url` - (Required) The Identity authentication URL. If omitted, the
  `OS_AUTH_URL` environment variable is used.

* `region` - (Optional) The region of the FlexibleEngine cloud to use. If omitted,
  the `OS_REGION_NAME` environment variable is used. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region FlexibleEngine environments, but this behavior may vary
  depending on the FlexibleEngine environment being used.

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
  will only work when used with the FlexibleEngine Object Storage resources.


## Supported Resources

* [Terraform::FlexibleEngine::AntiddosV1](AntiddosV1.md)
* [Terraform::FlexibleEngine::AsConfigurationV1](AsConfigurationV1.md)
* [Terraform::FlexibleEngine::AsGroupV1](AsGroupV1.md)
* [Terraform::FlexibleEngine::AsPolicyV1](AsPolicyV1.md)
* [Terraform::FlexibleEngine::BlockstorageVolumeV2](BlockstorageVolumeV2.md)
* [Terraform::FlexibleEngine::CceClusterV3](CceClusterV3.md)
* [Terraform::FlexibleEngine::CceNodesV3](CceNodesV3.md)
* [Terraform::FlexibleEngine::CesAlarmrule](CesAlarmrule.md)
* [Terraform::FlexibleEngine::ComputeBmsServerV2](ComputeBmsServerV2.md)
* [Terraform::FlexibleEngine::ComputeFloatingipAssociateV2](ComputeFloatingipAssociateV2.md)
* [Terraform::FlexibleEngine::ComputeFloatingipV2](ComputeFloatingipV2.md)
* [Terraform::FlexibleEngine::ComputeInstanceV2](ComputeInstanceV2.md)
* [Terraform::FlexibleEngine::ComputeKeypairV2](ComputeKeypairV2.md)
* [Terraform::FlexibleEngine::ComputeServergroupV2](ComputeServergroupV2.md)
* [Terraform::FlexibleEngine::ComputeVolumeAttachV2](ComputeVolumeAttachV2.md)
* [Terraform::FlexibleEngine::CsbsBackupPolicyV1](CsbsBackupPolicyV1.md)
* [Terraform::FlexibleEngine::CsbsBackupV1](CsbsBackupV1.md)
* [Terraform::FlexibleEngine::CtsTrackerV1](CtsTrackerV1.md)
* [Terraform::FlexibleEngine::DcsInstanceV1](DcsInstanceV1.md)
* [Terraform::FlexibleEngine::DnsRecordsetV2](DnsRecordsetV2.md)
* [Terraform::FlexibleEngine::DnsZoneV2](DnsZoneV2.md)
* [Terraform::FlexibleEngine::DrsReplicationV2](DrsReplicationV2.md)
* [Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2](DrsReplicationconsistencygroupV2.md)
* [Terraform::FlexibleEngine::DwsClusterV1](DwsClusterV1.md)
* [Terraform::FlexibleEngine::ElbBackend](ElbBackend.md)
* [Terraform::FlexibleEngine::ElbHealth](ElbHealth.md)
* [Terraform::FlexibleEngine::ElbListener](ElbListener.md)
* [Terraform::FlexibleEngine::ElbLoadbalancer](ElbLoadbalancer.md)
* [Terraform::FlexibleEngine::FwFirewallGroupV2](FwFirewallGroupV2.md)
* [Terraform::FlexibleEngine::FwPolicyV2](FwPolicyV2.md)
* [Terraform::FlexibleEngine::FwRuleV2](FwRuleV2.md)
* [Terraform::FlexibleEngine::ImagesImageV2](ImagesImageV2.md)
* [Terraform::FlexibleEngine::LbCertificateV2](LbCertificateV2.md)
* [Terraform::FlexibleEngine::LbL7policyV2](LbL7policyV2.md)
* [Terraform::FlexibleEngine::LbL7ruleV2](LbL7ruleV2.md)
* [Terraform::FlexibleEngine::LbListenerV2](LbListenerV2.md)
* [Terraform::FlexibleEngine::LbLoadbalancerV2](LbLoadbalancerV2.md)
* [Terraform::FlexibleEngine::LbMemberV2](LbMemberV2.md)
* [Terraform::FlexibleEngine::LbMonitorV2](LbMonitorV2.md)
* [Terraform::FlexibleEngine::LbPoolV2](LbPoolV2.md)
* [Terraform::FlexibleEngine::MlsInstanceV1](MlsInstanceV1.md)
* [Terraform::FlexibleEngine::MrsClusterV1](MrsClusterV1.md)
* [Terraform::FlexibleEngine::MrsJobV1](MrsJobV1.md)
* [Terraform::FlexibleEngine::NatGatewayV2](NatGatewayV2.md)
* [Terraform::FlexibleEngine::NatSnatRuleV2](NatSnatRuleV2.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipAssociateV2](NetworkingFloatingipAssociateV2.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipV2](NetworkingFloatingipV2.md)
* [Terraform::FlexibleEngine::NetworkingNetworkV2](NetworkingNetworkV2.md)
* [Terraform::FlexibleEngine::NetworkingPortV2](NetworkingPortV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterInterfaceV2](NetworkingRouterInterfaceV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterRouteV2](NetworkingRouterRouteV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterV2](NetworkingRouterV2.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupRuleV2](NetworkingSecgroupRuleV2.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupV2](NetworkingSecgroupV2.md)
* [Terraform::FlexibleEngine::NetworkingSubnetV2](NetworkingSubnetV2.md)
* [Terraform::FlexibleEngine::NetworkingVipAssociateV2](NetworkingVipAssociateV2.md)
* [Terraform::FlexibleEngine::NetworkingVipV2](NetworkingVipV2.md)
* [Terraform::FlexibleEngine::RdsInstanceV1](RdsInstanceV1.md)
* [Terraform::FlexibleEngine::RtsSoftwareConfigV1](RtsSoftwareConfigV1.md)
* [Terraform::FlexibleEngine::RtsStackV1](RtsStackV1.md)
* [Terraform::FlexibleEngine::S3BucketObject](S3BucketObject.md)
* [Terraform::FlexibleEngine::S3BucketPolicy](S3BucketPolicy.md)
* [Terraform::FlexibleEngine::S3Bucket](S3Bucket.md)
* [Terraform::FlexibleEngine::SfsFileSystemV2](SfsFileSystemV2.md)
* [Terraform::FlexibleEngine::SmnSubscriptionV2](SmnSubscriptionV2.md)
* [Terraform::FlexibleEngine::SmnTopicV2](SmnTopicV2.md)
* [Terraform::FlexibleEngine::VbsBackupPolicyV2](VbsBackupPolicyV2.md)
* [Terraform::FlexibleEngine::VbsBackupV2](VbsBackupV2.md)
* [Terraform::FlexibleEngine::VpcEipV1](VpcEipV1.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionAccepterV2](VpcPeeringConnectionAccepterV2.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionV2](VpcPeeringConnectionV2.md)
* [Terraform::FlexibleEngine::VpcRouteV2](VpcRouteV2.md)
* [Terraform::FlexibleEngine::VpcSubnetV1](VpcSubnetV1.md)
* [Terraform::FlexibleEngine::VpcV1](VpcV1.md)