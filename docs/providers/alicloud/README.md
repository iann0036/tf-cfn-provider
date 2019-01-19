# Alicloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/alicloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - This is the Alicloud access key.

* `secret_key` - This is the Alicloud secret key.

* `region` - This is the Alicloud region.

* `security_token` - Alicloud [Security Token Service](https://www.alibabacloud.com/help/doc-detail/66222.html).

* `account_id` - (Optional) Alibaba Cloud Account ID. It is used by the Function Compute service and to connect router interfaces.
  If not provided, the provider will attempt to retrieve it automatically with [STS GetCallerIdentity](https://www.alibabacloud.com/help/doc-detail/43767.htm).

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

* [Terraform::Alicloud::ApiGatewayApi](ApiGatewayApi.md)
* [Terraform::Alicloud::ApiGatewayAppAttachment](ApiGatewayAppAttachment.md)
* [Terraform::Alicloud::ApiGatewayApp](ApiGatewayApp.md)
* [Terraform::Alicloud::ApiGatewayGroup](ApiGatewayGroup.md)
* [Terraform::Alicloud::CdnDomain](CdnDomain.md)
* [Terraform::Alicloud::CenBandwidthLimit](CenBandwidthLimit.md)
* [Terraform::Alicloud::CenBandwidthPackageAttachment](CenBandwidthPackageAttachment.md)
* [Terraform::Alicloud::CenBandwidthPackage](CenBandwidthPackage.md)
* [Terraform::Alicloud::CenInstanceAttachment](CenInstanceAttachment.md)
* [Terraform::Alicloud::CenInstance](CenInstance.md)
* [Terraform::Alicloud::CenRouteEntry](CenRouteEntry.md)
* [Terraform::Alicloud::CmsAlarm](CmsAlarm.md)
* [Terraform::Alicloud::CommonBandwidthPackageAttachment](CommonBandwidthPackageAttachment.md)
* [Terraform::Alicloud::CommonBandwidthPackage](CommonBandwidthPackage.md)
* [Terraform::Alicloud::ContainerCluster](ContainerCluster.md)
* [Terraform::Alicloud::CsApplication](CsApplication.md)
* [Terraform::Alicloud::CsKubernetes](CsKubernetes.md)
* [Terraform::Alicloud::CsManagedKubernetes](CsManagedKubernetes.md)
* [Terraform::Alicloud::CsSwarm](CsSwarm.md)
* [Terraform::Alicloud::DatahubProject](DatahubProject.md)
* [Terraform::Alicloud::DatahubSubscription](DatahubSubscription.md)
* [Terraform::Alicloud::DatahubTopic](DatahubTopic.md)
* [Terraform::Alicloud::DbAccountPrivilege](DbAccountPrivilege.md)
* [Terraform::Alicloud::DbAccount](DbAccount.md)
* [Terraform::Alicloud::DbBackupPolicy](DbBackupPolicy.md)
* [Terraform::Alicloud::DbConnection](DbConnection.md)
* [Terraform::Alicloud::DbDatabase](DbDatabase.md)
* [Terraform::Alicloud::DbInstance](DbInstance.md)
* [Terraform::Alicloud::DiskAttachment](DiskAttachment.md)
* [Terraform::Alicloud::Disk](Disk.md)
* [Terraform::Alicloud::DnsGroup](DnsGroup.md)
* [Terraform::Alicloud::Dns](Dns.md)
* [Terraform::Alicloud::DrdsInstance](DrdsInstance.md)
* [Terraform::Alicloud::EipAssociation](EipAssociation.md)
* [Terraform::Alicloud::Eip](Eip.md)
* [Terraform::Alicloud::EssAlarm](EssAlarm.md)
* [Terraform::Alicloud::EssAttachment](EssAttachment.md)
* [Terraform::Alicloud::EssLifecycleHook](EssLifecycleHook.md)
* [Terraform::Alicloud::EssScalingConfiguration](EssScalingConfiguration.md)
* [Terraform::Alicloud::EssScalingGroup](EssScalingGroup.md)
* [Terraform::Alicloud::EssScalingRule](EssScalingRule.md)
* [Terraform::Alicloud::EssSchedule](EssSchedule.md)
* [Terraform::Alicloud::FcFunction](FcFunction.md)
* [Terraform::Alicloud::FcService](FcService.md)
* [Terraform::Alicloud::Forward](Forward.md)
* [Terraform::Alicloud::HavipAttachment](HavipAttachment.md)
* [Terraform::Alicloud::Havip](Havip.md)
* [Terraform::Alicloud::Instance](Instance.md)
* [Terraform::Alicloud::KeyPairAttachment](KeyPairAttachment.md)
* [Terraform::Alicloud::KeyPair](KeyPair.md)
* [Terraform::Alicloud::KmsKey](KmsKey.md)
* [Terraform::Alicloud::KvstoreBackupPolicy](KvstoreBackupPolicy.md)
* [Terraform::Alicloud::KvstoreInstance](KvstoreInstance.md)
* [Terraform::Alicloud::LogMachineGroup](LogMachineGroup.md)
* [Terraform::Alicloud::LogProject](LogProject.md)
* [Terraform::Alicloud::LogStoreIndex](LogStoreIndex.md)
* [Terraform::Alicloud::LogStore](LogStore.md)
* [Terraform::Alicloud::MnsQueue](MnsQueue.md)
* [Terraform::Alicloud::MnsTopicSubscription](MnsTopicSubscription.md)
* [Terraform::Alicloud::MnsTopic](MnsTopic.md)
* [Terraform::Alicloud::NatGateway](NatGateway.md)
* [Terraform::Alicloud::NetworkInterfaceAttachment](NetworkInterfaceAttachment.md)
* [Terraform::Alicloud::NetworkInterface](NetworkInterface.md)
* [Terraform::Alicloud::OssBucketObject](OssBucketObject.md)
* [Terraform::Alicloud::OssBucket](OssBucket.md)
* [Terraform::Alicloud::OtsInstanceAttachment](OtsInstanceAttachment.md)
* [Terraform::Alicloud::OtsInstance](OtsInstance.md)
* [Terraform::Alicloud::OtsTable](OtsTable.md)
* [Terraform::Alicloud::PvtzZoneAttachment](PvtzZoneAttachment.md)
* [Terraform::Alicloud::PvtzZoneRecord](PvtzZoneRecord.md)
* [Terraform::Alicloud::PvtzZone](PvtzZone.md)
* [Terraform::Alicloud::RamAccessKey](RamAccessKey.md)
* [Terraform::Alicloud::RamAccountAlias](RamAccountAlias.md)
* [Terraform::Alicloud::RamAlias](RamAlias.md)
* [Terraform::Alicloud::RamGroupMembership](RamGroupMembership.md)
* [Terraform::Alicloud::RamGroupPolicyAttachment](RamGroupPolicyAttachment.md)
* [Terraform::Alicloud::RamGroup](RamGroup.md)
* [Terraform::Alicloud::RamLoginProfile](RamLoginProfile.md)
* [Terraform::Alicloud::RamPolicy](RamPolicy.md)
* [Terraform::Alicloud::RamRoleAttachment](RamRoleAttachment.md)
* [Terraform::Alicloud::RamRolePolicyAttachment](RamRolePolicyAttachment.md)
* [Terraform::Alicloud::RamRole](RamRole.md)
* [Terraform::Alicloud::RamUserPolicyAttachment](RamUserPolicyAttachment.md)
* [Terraform::Alicloud::RamUser](RamUser.md)
* [Terraform::Alicloud::RouteEntry](RouteEntry.md)
* [Terraform::Alicloud::RouteTableAttachment](RouteTableAttachment.md)
* [Terraform::Alicloud::RouteTable](RouteTable.md)
* [Terraform::Alicloud::RouterInterfaceConnection](RouterInterfaceConnection.md)
* [Terraform::Alicloud::RouterInterface](RouterInterface.md)
* [Terraform::Alicloud::SecurityGroupRule](SecurityGroupRule.md)
* [Terraform::Alicloud::SecurityGroup](SecurityGroup.md)
* [Terraform::Alicloud::SlbAcl](SlbAcl.md)
* [Terraform::Alicloud::SlbAttachment](SlbAttachment.md)
* [Terraform::Alicloud::SlbCaCertificate](SlbCaCertificate.md)
* [Terraform::Alicloud::SlbListener](SlbListener.md)
* [Terraform::Alicloud::SlbRule](SlbRule.md)
* [Terraform::Alicloud::SlbServerCertificate](SlbServerCertificate.md)
* [Terraform::Alicloud::SlbServerGroup](SlbServerGroup.md)
* [Terraform::Alicloud::Slb](Slb.md)
* [Terraform::Alicloud::Snat](Snat.md)
* [Terraform::Alicloud::SslVpnClientCert](SslVpnClientCert.md)
* [Terraform::Alicloud::SslVpnServer](SslVpnServer.md)
* [Terraform::Alicloud::Vpc](Vpc.md)
* [Terraform::Alicloud::VpnConnection](VpnConnection.md)
* [Terraform::Alicloud::VpnCustomerGateway](VpnCustomerGateway.md)
* [Terraform::Alicloud::VpnGateway](VpnGateway.md)
* [Terraform::Alicloud::Vswitch](Vswitch.md)