# Alicloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/alicloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - This is the Alicloud access key. It must be provided, but
  it can also be sourced from the `ALICLOUD_ACCESS_KEY` environment variable.

* `secret_key` - This is the Alicloud secret key. It must be provided, but
  it can also be sourced from the `ALICLOUD_SECRET_KEY` environment variable.

* `region` - This is the Alicloud region. It must be provided, but
  it can also be sourced from the `ALICLOUD_REGION` environment variables.

* `security_token` - Alicloud [Security Token Service](https://www.alibabacloud.com/help/doc-detail/66222.html).
  It can be sourced from the `ALICLOUD_SECURITY_TOKEN` environment variable.

* `account_id` - (Optional) Alibaba Cloud Account ID. It is used by the Function Compute service and to connect router interfaces.
  If not provided, the provider will attempt to retrieve it automatically with [STS GetCallerIdentity](https://www.alibabacloud.com/help/doc-detail/43767.htm).
  It can be sourced from the `ALICLOUD_ACCOUNT_ID` environment variable.

Nested `endpoints` block supports the following:

* `ecs` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom ECS endpoints.

* `rds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom RDS endpoints.

* `slb` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom SLB endpoints.

* `vpc` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom VPC and VPN endpoints.

* `cen` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom CEN endpoints.

* `ess` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Autoscaling endpoints.

* `oss` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom OSS endpoints.

* `dns` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom DNS endpoints.

* `ram` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom RAM endpoints.

* `cs` - (Optional) Use this to override the default  endpoint URL constructed from the `region`. It's typically used to connect to custom Container Service endpoints.

* `cdn` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom CDN endpoints.

* `kms` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom KMS endpoints.

* `ots` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Table Store endpoints.

* `cms` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Cloud Monitor endpoints.

* `pvtz` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Private Zone endpoints.

* `sts` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom STS endpoints.

* `log` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Log Service endpoints.

* `drds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom DRDS endpoints.

* `dds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom MongoDB endpoints.

* `kvstore` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom R-KVStore endpoints.

* `fc` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Function Computing endpoints.

* `apigateway` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Api Gateway endpoints.

* `datahub` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Datahub endpoints.

* `mns` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom MNS endpoints.

* `location` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Location Service endpoints.",


## Supported Resources

* [Terraform::Alicloud::ApiGatewayApi](docs/providers/alicloud/ApiGatewayApi.md)
* [Terraform::Alicloud::ApiGatewayAppAttachment](docs/providers/alicloud/ApiGatewayAppAttachment.md)
* [Terraform::Alicloud::ApiGatewayApp](docs/providers/alicloud/ApiGatewayApp.md)
* [Terraform::Alicloud::ApiGatewayGroup](docs/providers/alicloud/ApiGatewayGroup.md)
* [Terraform::Alicloud::CdnDomain](docs/providers/alicloud/CdnDomain.md)
* [Terraform::Alicloud::CenBandwidthLimit](docs/providers/alicloud/CenBandwidthLimit.md)
* [Terraform::Alicloud::CenBandwidthPackageAttachment](docs/providers/alicloud/CenBandwidthPackageAttachment.md)
* [Terraform::Alicloud::CenBandwidthPackage](docs/providers/alicloud/CenBandwidthPackage.md)
* [Terraform::Alicloud::CenInstanceAttachment](docs/providers/alicloud/CenInstanceAttachment.md)
* [Terraform::Alicloud::CenInstance](docs/providers/alicloud/CenInstance.md)
* [Terraform::Alicloud::CenRouteEntry](docs/providers/alicloud/CenRouteEntry.md)
* [Terraform::Alicloud::CmsAlarm](docs/providers/alicloud/CmsAlarm.md)
* [Terraform::Alicloud::CommonBandwidthPackageAttachment](docs/providers/alicloud/CommonBandwidthPackageAttachment.md)
* [Terraform::Alicloud::CommonBandwidthPackage](docs/providers/alicloud/CommonBandwidthPackage.md)
* [Terraform::Alicloud::ContainerCluster](docs/providers/alicloud/ContainerCluster.md)
* [Terraform::Alicloud::CsApplication](docs/providers/alicloud/CsApplication.md)
* [Terraform::Alicloud::CsKubernetes](docs/providers/alicloud/CsKubernetes.md)
* [Terraform::Alicloud::CsManagedKubernetes](docs/providers/alicloud/CsManagedKubernetes.md)
* [Terraform::Alicloud::CsSwarm](docs/providers/alicloud/CsSwarm.md)
* [Terraform::Alicloud::DatahubProject](docs/providers/alicloud/DatahubProject.md)
* [Terraform::Alicloud::DatahubSubscription](docs/providers/alicloud/DatahubSubscription.md)
* [Terraform::Alicloud::DatahubTopic](docs/providers/alicloud/DatahubTopic.md)
* [Terraform::Alicloud::DbAccountPrivilege](docs/providers/alicloud/DbAccountPrivilege.md)
* [Terraform::Alicloud::DbAccount](docs/providers/alicloud/DbAccount.md)
* [Terraform::Alicloud::DbBackupPolicy](docs/providers/alicloud/DbBackupPolicy.md)
* [Terraform::Alicloud::DbConnection](docs/providers/alicloud/DbConnection.md)
* [Terraform::Alicloud::DbDatabase](docs/providers/alicloud/DbDatabase.md)
* [Terraform::Alicloud::DbInstance](docs/providers/alicloud/DbInstance.md)
* [Terraform::Alicloud::DiskAttachment](docs/providers/alicloud/DiskAttachment.md)
* [Terraform::Alicloud::Disk](docs/providers/alicloud/Disk.md)
* [Terraform::Alicloud::DnsGroup](docs/providers/alicloud/DnsGroup.md)
* [Terraform::Alicloud::Dns](docs/providers/alicloud/Dns.md)
* [Terraform::Alicloud::DrdsInstance](docs/providers/alicloud/DrdsInstance.md)
* [Terraform::Alicloud::EipAssociation](docs/providers/alicloud/EipAssociation.md)
* [Terraform::Alicloud::Eip](docs/providers/alicloud/Eip.md)
* [Terraform::Alicloud::EssAlarm](docs/providers/alicloud/EssAlarm.md)
* [Terraform::Alicloud::EssAttachment](docs/providers/alicloud/EssAttachment.md)
* [Terraform::Alicloud::EssLifecycleHook](docs/providers/alicloud/EssLifecycleHook.md)
* [Terraform::Alicloud::EssScalingConfiguration](docs/providers/alicloud/EssScalingConfiguration.md)
* [Terraform::Alicloud::EssScalingGroup](docs/providers/alicloud/EssScalingGroup.md)
* [Terraform::Alicloud::EssScalingRule](docs/providers/alicloud/EssScalingRule.md)
* [Terraform::Alicloud::EssSchedule](docs/providers/alicloud/EssSchedule.md)
* [Terraform::Alicloud::FcFunction](docs/providers/alicloud/FcFunction.md)
* [Terraform::Alicloud::FcService](docs/providers/alicloud/FcService.md)
* [Terraform::Alicloud::Forward](docs/providers/alicloud/Forward.md)
* [Terraform::Alicloud::HavipAttachment](docs/providers/alicloud/HavipAttachment.md)
* [Terraform::Alicloud::Havip](docs/providers/alicloud/Havip.md)
* [Terraform::Alicloud::Instance](docs/providers/alicloud/Instance.md)
* [Terraform::Alicloud::KeyPairAttachment](docs/providers/alicloud/KeyPairAttachment.md)
* [Terraform::Alicloud::KeyPair](docs/providers/alicloud/KeyPair.md)
* [Terraform::Alicloud::KmsKey](docs/providers/alicloud/KmsKey.md)
* [Terraform::Alicloud::KvstoreBackupPolicy](docs/providers/alicloud/KvstoreBackupPolicy.md)
* [Terraform::Alicloud::KvstoreInstance](docs/providers/alicloud/KvstoreInstance.md)
* [Terraform::Alicloud::LogMachineGroup](docs/providers/alicloud/LogMachineGroup.md)
* [Terraform::Alicloud::LogProject](docs/providers/alicloud/LogProject.md)
* [Terraform::Alicloud::LogStoreIndex](docs/providers/alicloud/LogStoreIndex.md)
* [Terraform::Alicloud::LogStore](docs/providers/alicloud/LogStore.md)
* [Terraform::Alicloud::MnsQueue](docs/providers/alicloud/MnsQueue.md)
* [Terraform::Alicloud::MnsTopicSubscription](docs/providers/alicloud/MnsTopicSubscription.md)
* [Terraform::Alicloud::MnsTopic](docs/providers/alicloud/MnsTopic.md)
* [Terraform::Alicloud::NatGateway](docs/providers/alicloud/NatGateway.md)
* [Terraform::Alicloud::NetworkInterfaceAttachment](docs/providers/alicloud/NetworkInterfaceAttachment.md)
* [Terraform::Alicloud::NetworkInterface](docs/providers/alicloud/NetworkInterface.md)
* [Terraform::Alicloud::OssBucketObject](docs/providers/alicloud/OssBucketObject.md)
* [Terraform::Alicloud::OssBucket](docs/providers/alicloud/OssBucket.md)
* [Terraform::Alicloud::OtsInstanceAttachment](docs/providers/alicloud/OtsInstanceAttachment.md)
* [Terraform::Alicloud::OtsInstance](docs/providers/alicloud/OtsInstance.md)
* [Terraform::Alicloud::OtsTable](docs/providers/alicloud/OtsTable.md)
* [Terraform::Alicloud::PvtzZoneAttachment](docs/providers/alicloud/PvtzZoneAttachment.md)
* [Terraform::Alicloud::PvtzZoneRecord](docs/providers/alicloud/PvtzZoneRecord.md)
* [Terraform::Alicloud::PvtzZone](docs/providers/alicloud/PvtzZone.md)
* [Terraform::Alicloud::RamAccessKey](docs/providers/alicloud/RamAccessKey.md)
* [Terraform::Alicloud::RamAccountAlias](docs/providers/alicloud/RamAccountAlias.md)
* [Terraform::Alicloud::RamAlias](docs/providers/alicloud/RamAlias.md)
* [Terraform::Alicloud::RamGroupMembership](docs/providers/alicloud/RamGroupMembership.md)
* [Terraform::Alicloud::RamGroupPolicyAttachment](docs/providers/alicloud/RamGroupPolicyAttachment.md)
* [Terraform::Alicloud::RamGroup](docs/providers/alicloud/RamGroup.md)
* [Terraform::Alicloud::RamLoginProfile](docs/providers/alicloud/RamLoginProfile.md)
* [Terraform::Alicloud::RamPolicy](docs/providers/alicloud/RamPolicy.md)
* [Terraform::Alicloud::RamRoleAttachment](docs/providers/alicloud/RamRoleAttachment.md)
* [Terraform::Alicloud::RamRolePolicyAttachment](docs/providers/alicloud/RamRolePolicyAttachment.md)
* [Terraform::Alicloud::RamRole](docs/providers/alicloud/RamRole.md)
* [Terraform::Alicloud::RamUserPolicyAttachment](docs/providers/alicloud/RamUserPolicyAttachment.md)
* [Terraform::Alicloud::RamUser](docs/providers/alicloud/RamUser.md)
* [Terraform::Alicloud::RouteEntry](docs/providers/alicloud/RouteEntry.md)
* [Terraform::Alicloud::RouteTableAttachment](docs/providers/alicloud/RouteTableAttachment.md)
* [Terraform::Alicloud::RouteTable](docs/providers/alicloud/RouteTable.md)
* [Terraform::Alicloud::RouterInterfaceConnection](docs/providers/alicloud/RouterInterfaceConnection.md)
* [Terraform::Alicloud::RouterInterface](docs/providers/alicloud/RouterInterface.md)
* [Terraform::Alicloud::SecurityGroupRule](docs/providers/alicloud/SecurityGroupRule.md)
* [Terraform::Alicloud::SecurityGroup](docs/providers/alicloud/SecurityGroup.md)
* [Terraform::Alicloud::SlbAcl](docs/providers/alicloud/SlbAcl.md)
* [Terraform::Alicloud::SlbAttachment](docs/providers/alicloud/SlbAttachment.md)
* [Terraform::Alicloud::SlbCaCertificate](docs/providers/alicloud/SlbCaCertificate.md)
* [Terraform::Alicloud::SlbListener](docs/providers/alicloud/SlbListener.md)
* [Terraform::Alicloud::SlbRule](docs/providers/alicloud/SlbRule.md)
* [Terraform::Alicloud::SlbServerCertificate](docs/providers/alicloud/SlbServerCertificate.md)
* [Terraform::Alicloud::SlbServerGroup](docs/providers/alicloud/SlbServerGroup.md)
* [Terraform::Alicloud::Slb](docs/providers/alicloud/Slb.md)
* [Terraform::Alicloud::Snat](docs/providers/alicloud/Snat.md)
* [Terraform::Alicloud::SslVpnClientCert](docs/providers/alicloud/SslVpnClientCert.md)
* [Terraform::Alicloud::SslVpnServer](docs/providers/alicloud/SslVpnServer.md)
* [Terraform::Alicloud::Vpc](docs/providers/alicloud/Vpc.md)
* [Terraform::Alicloud::VpnConnection](docs/providers/alicloud/VpnConnection.md)
* [Terraform::Alicloud::VpnCustomerGateway](docs/providers/alicloud/VpnCustomerGateway.md)
* [Terraform::Alicloud::VpnGateway](docs/providers/alicloud/VpnGateway.md)
* [Terraform::Alicloud::Vswitch](docs/providers/alicloud/Vswitch.md)