# FlexibleEngine Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/flexibleengine**. The below arguments may be included as the key/value or JSON properties in the secret:

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

* [Terraform::FlexibleEngine::AntiddosV1](docs/providers/flexibleengine/AntiddosV1.md)
* [Terraform::FlexibleEngine::AsConfigurationV1](docs/providers/flexibleengine/AsConfigurationV1.md)
* [Terraform::FlexibleEngine::AsGroupV1](docs/providers/flexibleengine/AsGroupV1.md)
* [Terraform::FlexibleEngine::AsPolicyV1](docs/providers/flexibleengine/AsPolicyV1.md)
* [Terraform::FlexibleEngine::BlockstorageVolumeV2](docs/providers/flexibleengine/BlockstorageVolumeV2.md)
* [Terraform::FlexibleEngine::CceClusterV3](docs/providers/flexibleengine/CceClusterV3.md)
* [Terraform::FlexibleEngine::CceNodesV3](docs/providers/flexibleengine/CceNodesV3.md)
* [Terraform::FlexibleEngine::CesAlarmrule](docs/providers/flexibleengine/CesAlarmrule.md)
* [Terraform::FlexibleEngine::ComputeBmsServerV2](docs/providers/flexibleengine/ComputeBmsServerV2.md)
* [Terraform::FlexibleEngine::ComputeFloatingipAssociateV2](docs/providers/flexibleengine/ComputeFloatingipAssociateV2.md)
* [Terraform::FlexibleEngine::ComputeFloatingipV2](docs/providers/flexibleengine/ComputeFloatingipV2.md)
* [Terraform::FlexibleEngine::ComputeInstanceV2](docs/providers/flexibleengine/ComputeInstanceV2.md)
* [Terraform::FlexibleEngine::ComputeKeypairV2](docs/providers/flexibleengine/ComputeKeypairV2.md)
* [Terraform::FlexibleEngine::ComputeServergroupV2](docs/providers/flexibleengine/ComputeServergroupV2.md)
* [Terraform::FlexibleEngine::ComputeVolumeAttachV2](docs/providers/flexibleengine/ComputeVolumeAttachV2.md)
* [Terraform::FlexibleEngine::CsbsBackupPolicyV1](docs/providers/flexibleengine/CsbsBackupPolicyV1.md)
* [Terraform::FlexibleEngine::CsbsBackupV1](docs/providers/flexibleengine/CsbsBackupV1.md)
* [Terraform::FlexibleEngine::CtsTrackerV1](docs/providers/flexibleengine/CtsTrackerV1.md)
* [Terraform::FlexibleEngine::DcsInstanceV1](docs/providers/flexibleengine/DcsInstanceV1.md)
* [Terraform::FlexibleEngine::DnsRecordsetV2](docs/providers/flexibleengine/DnsRecordsetV2.md)
* [Terraform::FlexibleEngine::DnsZoneV2](docs/providers/flexibleengine/DnsZoneV2.md)
* [Terraform::FlexibleEngine::DrsReplicationV2](docs/providers/flexibleengine/DrsReplicationV2.md)
* [Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2](docs/providers/flexibleengine/DrsReplicationconsistencygroupV2.md)
* [Terraform::FlexibleEngine::DwsClusterV1](docs/providers/flexibleengine/DwsClusterV1.md)
* [Terraform::FlexibleEngine::ElbBackend](docs/providers/flexibleengine/ElbBackend.md)
* [Terraform::FlexibleEngine::ElbHealth](docs/providers/flexibleengine/ElbHealth.md)
* [Terraform::FlexibleEngine::ElbListener](docs/providers/flexibleengine/ElbListener.md)
* [Terraform::FlexibleEngine::ElbLoadbalancer](docs/providers/flexibleengine/ElbLoadbalancer.md)
* [Terraform::FlexibleEngine::FwFirewallGroupV2](docs/providers/flexibleengine/FwFirewallGroupV2.md)
* [Terraform::FlexibleEngine::FwPolicyV2](docs/providers/flexibleengine/FwPolicyV2.md)
* [Terraform::FlexibleEngine::FwRuleV2](docs/providers/flexibleengine/FwRuleV2.md)
* [Terraform::FlexibleEngine::ImagesImageV2](docs/providers/flexibleengine/ImagesImageV2.md)
* [Terraform::FlexibleEngine::LbCertificateV2](docs/providers/flexibleengine/LbCertificateV2.md)
* [Terraform::FlexibleEngine::LbListenerV2](docs/providers/flexibleengine/LbListenerV2.md)
* [Terraform::FlexibleEngine::LbLoadbalancerV2](docs/providers/flexibleengine/LbLoadbalancerV2.md)
* [Terraform::FlexibleEngine::LbMemberV2](docs/providers/flexibleengine/LbMemberV2.md)
* [Terraform::FlexibleEngine::LbMonitorV2](docs/providers/flexibleengine/LbMonitorV2.md)
* [Terraform::FlexibleEngine::LbPoolV2](docs/providers/flexibleengine/LbPoolV2.md)
* [Terraform::FlexibleEngine::MlsInstanceV1](docs/providers/flexibleengine/MlsInstanceV1.md)
* [Terraform::FlexibleEngine::MrsClusterV1](docs/providers/flexibleengine/MrsClusterV1.md)
* [Terraform::FlexibleEngine::MrsJobV1](docs/providers/flexibleengine/MrsJobV1.md)
* [Terraform::FlexibleEngine::NatGatewayV2](docs/providers/flexibleengine/NatGatewayV2.md)
* [Terraform::FlexibleEngine::NatSnatRuleV2](docs/providers/flexibleengine/NatSnatRuleV2.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipAssociateV2](docs/providers/flexibleengine/NetworkingFloatingipAssociateV2.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipV2](docs/providers/flexibleengine/NetworkingFloatingipV2.md)
* [Terraform::FlexibleEngine::NetworkingNetworkV2](docs/providers/flexibleengine/NetworkingNetworkV2.md)
* [Terraform::FlexibleEngine::NetworkingPortV2](docs/providers/flexibleengine/NetworkingPortV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterInterfaceV2](docs/providers/flexibleengine/NetworkingRouterInterfaceV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterRouteV2](docs/providers/flexibleengine/NetworkingRouterRouteV2.md)
* [Terraform::FlexibleEngine::NetworkingRouterV2](docs/providers/flexibleengine/NetworkingRouterV2.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupRuleV2](docs/providers/flexibleengine/NetworkingSecgroupRuleV2.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupV2](docs/providers/flexibleengine/NetworkingSecgroupV2.md)
* [Terraform::FlexibleEngine::NetworkingSubnetV2](docs/providers/flexibleengine/NetworkingSubnetV2.md)
* [Terraform::FlexibleEngine::NetworkingVipAssociateV2](docs/providers/flexibleengine/NetworkingVipAssociateV2.md)
* [Terraform::FlexibleEngine::NetworkingVipV2](docs/providers/flexibleengine/NetworkingVipV2.md)
* [Terraform::FlexibleEngine::RdsInstanceV1](docs/providers/flexibleengine/RdsInstanceV1.md)
* [Terraform::FlexibleEngine::RtsSoftwareConfigV1](docs/providers/flexibleengine/RtsSoftwareConfigV1.md)
* [Terraform::FlexibleEngine::RtsStackV1](docs/providers/flexibleengine/RtsStackV1.md)
* [Terraform::FlexibleEngine::S3BucketObject](docs/providers/flexibleengine/S3BucketObject.md)
* [Terraform::FlexibleEngine::S3BucketPolicy](docs/providers/flexibleengine/S3BucketPolicy.md)
* [Terraform::FlexibleEngine::S3Bucket](docs/providers/flexibleengine/S3Bucket.md)
* [Terraform::FlexibleEngine::SfsFileSystemV2](docs/providers/flexibleengine/SfsFileSystemV2.md)
* [Terraform::FlexibleEngine::SmnSubscriptionV2](docs/providers/flexibleengine/SmnSubscriptionV2.md)
* [Terraform::FlexibleEngine::SmnTopicV2](docs/providers/flexibleengine/SmnTopicV2.md)
* [Terraform::FlexibleEngine::VbsBackupPolicyV2](docs/providers/flexibleengine/VbsBackupPolicyV2.md)
* [Terraform::FlexibleEngine::VbsBackupV2](docs/providers/flexibleengine/VbsBackupV2.md)
* [Terraform::FlexibleEngine::VpcEipV1](docs/providers/flexibleengine/VpcEipV1.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionAccepterV2](docs/providers/flexibleengine/VpcPeeringConnectionAccepterV2.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionV2](docs/providers/flexibleengine/VpcPeeringConnectionV2.md)
* [Terraform::FlexibleEngine::VpcRouteV2](docs/providers/flexibleengine/VpcRouteV2.md)
* [Terraform::FlexibleEngine::VpcSubnetV1](docs/providers/flexibleengine/VpcSubnetV1.md)
* [Terraform::FlexibleEngine::VpcV1](docs/providers/flexibleengine/VpcV1.md)