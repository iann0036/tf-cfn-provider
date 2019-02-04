# Azure Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/azurerm**. The below arguments may be included as the key/value or JSON properties in the secret:

* `client_id` - (Optional) The Client ID which should be used. This can also be sourced from the `ARM_CLIENT_ID` Environment Variable.

* `environment` - (Optional) The Cloud Environment which should be used. Possible values are `public`, `usgovernment`, `german` and `china`. Defaults to `public`.

* `subscription_id` - (Optional) The Subscription ID which should be used. This can also be sourced from the `ARM_SUBSCRIPTION_ID` Environment Variable.

* `tenant_id` - (Optional) The Tenant ID which should be used. This can also be sourced from the `ARM_TENANT_ID` Environment Variable.

---

When authenticating as a Service Principal using a Client Certificate, the following fields can be set:

* `client_certificate_password` - (Optional) The password associated with the Client Certificate. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PASSWORD` Environment Variable.

* `client_certificate_path` - (Optional) The path to the Client Certificate associated with the Service Principal which should be used. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PATH` Environment Variable.

More information on [how to configure a Service Principal using a Client Certificate can be found in this guide](auth/service_principal_client_certificate.html).

---

When authenticating as a Service Principal using a Client Secret, the following fields can be set:

* `client_secret` - (Optional) The Client Secret which should be used. This can also be sourced from the `ARM_CLIENT_SECRET` Environment Variable.

More information on [how to configure a Service Principal using a Client Secret can be found in this guide](auth/service_principal_client_secret.html).

---

When authenticating using Managed Service Identity, the following fields can be set:

* `msi_endpoint` - (Optional) The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. This can also be sourced from the `ARM_MSI_ENDPOINT` Environment Variable.

* `use_msi` - (Optional) Should Managed Service Identity be used for Authentication? This can also be sourced from the `ARM_USE_MSI` Environment Variable. Defaults to `false`.

More information on [how to configure a Service Principal using Managed Service Identity can be found in this guide](auth/managed_service_identity.html).

---

For some advanced scenarios, such as where more granular permissions are necessary - the following properties can be set:

* `partner_id` - (Optional) A GUID/UUID that is [registered](https://docs.microsoft.com/azure/marketplace/azure-partner-customer-usage-attribution#register-guids-and-offers) with Microsoft to facilitate partner resource usage attribution. This can also be sourced from the `ARM_PARTNER_ID` Environment Variable.

* `skip_credentials_validation` - (Optional) Should the AzureRM Provider skip verifying the credentials being used are valid? This can also be sourced from the `ARM_SKIP_CREDENTIALS_VALIDATION` Environment Variable. Defaults to `false`.

* `skip_provider_registration` - (Optional) Should the AzureRM Provider skip registering any required Resource Providers? This can also be sourced from the `ARM_SKIP_PROVIDER_REGISTRATION` Environment Variable. Defaults to `false`.

It's also possible to use multiple Provider blocks within a single Terraform configuration, for example to work with resources across multiple Subscriptions - more information can be found [in the documentation for Providers](https://www.terraform.io/docs/configuration/providers.html#multiple-provider-instances).


## Supported Resources

* [Terraform::AzureRM::ApiManagement](ApiManagement.md)
* [Terraform::AzureRM::AppServiceActiveSlot](AppServiceActiveSlot.md)
* [Terraform::AzureRM::AppServiceCustomHostnameBinding](AppServiceCustomHostnameBinding.md)
* [Terraform::AzureRM::AppServicePlan](AppServicePlan.md)
* [Terraform::AzureRM::AppServiceSlot](AppServiceSlot.md)
* [Terraform::AzureRM::AppService](AppService.md)
* [Terraform::AzureRM::ApplicationGateway](ApplicationGateway.md)
* [Terraform::AzureRM::ApplicationInsightsApiKey](ApplicationInsightsApiKey.md)
* [Terraform::AzureRM::ApplicationInsights](ApplicationInsights.md)
* [Terraform::AzureRM::ApplicationSecurityGroup](ApplicationSecurityGroup.md)
* [Terraform::AzureRM::AutomationAccount](AutomationAccount.md)
* [Terraform::AzureRM::AutomationCredential](AutomationCredential.md)
* [Terraform::AzureRM::AutomationDscConfiguration](AutomationDscConfiguration.md)
* [Terraform::AzureRM::AutomationDscNodeconfiguration](AutomationDscNodeconfiguration.md)
* [Terraform::AzureRM::AutomationModule](AutomationModule.md)
* [Terraform::AzureRM::AutomationRunbook](AutomationRunbook.md)
* [Terraform::AzureRM::AutomationSchedule](AutomationSchedule.md)
* [Terraform::AzureRM::AutoscaleSetting](AutoscaleSetting.md)
* [Terraform::AzureRM::AvailabilitySet](AvailabilitySet.md)
* [Terraform::AzureRM::AzureadApplication](AzureadApplication.md)
* [Terraform::AzureRM::AzureadServicePrincipalPassword](AzureadServicePrincipalPassword.md)
* [Terraform::AzureRM::AzureadServicePrincipal](AzureadServicePrincipal.md)
* [Terraform::AzureRM::BatchAccount](BatchAccount.md)
* [Terraform::AzureRM::BatchPool](BatchPool.md)
* [Terraform::AzureRM::CdnEndpoint](CdnEndpoint.md)
* [Terraform::AzureRM::CdnProfile](CdnProfile.md)
* [Terraform::AzureRM::CognitiveAccount](CognitiveAccount.md)
* [Terraform::AzureRM::ContainerGroup](ContainerGroup.md)
* [Terraform::AzureRM::ContainerRegistry](ContainerRegistry.md)
* [Terraform::AzureRM::ContainerService](ContainerService.md)
* [Terraform::AzureRM::CosmosdbAccount](CosmosdbAccount.md)
* [Terraform::AzureRM::DataLakeAnalyticsAccount](DataLakeAnalyticsAccount.md)
* [Terraform::AzureRM::DataLakeAnalyticsFirewallRule](DataLakeAnalyticsFirewallRule.md)
* [Terraform::AzureRM::DataLakeStoreFile](DataLakeStoreFile.md)
* [Terraform::AzureRM::DataLakeStoreFirewallRule](DataLakeStoreFirewallRule.md)
* [Terraform::AzureRM::DataLakeStore](DataLakeStore.md)
* [Terraform::AzureRM::DatabricksWorkspace](DatabricksWorkspace.md)
* [Terraform::AzureRM::DdosProtectionPlan](DdosProtectionPlan.md)
* [Terraform::AzureRM::DevTestLab](DevTestLab.md)
* [Terraform::AzureRM::DevTestLinuxVirtualMachine](DevTestLinuxVirtualMachine.md)
* [Terraform::AzureRM::DevTestPolicy](DevTestPolicy.md)
* [Terraform::AzureRM::DevTestVirtualNetwork](DevTestVirtualNetwork.md)
* [Terraform::AzureRM::DevTestWindowsVirtualMachine](DevTestWindowsVirtualMachine.md)
* [Terraform::AzureRM::DevspaceController](DevspaceController.md)
* [Terraform::AzureRM::DnsARecord](DnsARecord.md)
* [Terraform::AzureRM::DnsAaaaRecord](DnsAaaaRecord.md)
* [Terraform::AzureRM::DnsCaaRecord](DnsCaaRecord.md)
* [Terraform::AzureRM::DnsCnameRecord](DnsCnameRecord.md)
* [Terraform::AzureRM::DnsMxRecord](DnsMxRecord.md)
* [Terraform::AzureRM::DnsNsRecord](DnsNsRecord.md)
* [Terraform::AzureRM::DnsPtrRecord](DnsPtrRecord.md)
* [Terraform::AzureRM::DnsSrvRecord](DnsSrvRecord.md)
* [Terraform::AzureRM::DnsTxtRecord](DnsTxtRecord.md)
* [Terraform::AzureRM::DnsZone](DnsZone.md)
* [Terraform::AzureRM::EventgridTopic](EventgridTopic.md)
* [Terraform::AzureRM::EventhubAuthorizationRule](EventhubAuthorizationRule.md)
* [Terraform::AzureRM::EventhubConsumerGroup](EventhubConsumerGroup.md)
* [Terraform::AzureRM::EventhubNamespaceAuthorizationRule](EventhubNamespaceAuthorizationRule.md)
* [Terraform::AzureRM::EventhubNamespace](EventhubNamespace.md)
* [Terraform::AzureRM::Eventhub](Eventhub.md)
* [Terraform::AzureRM::ExpressRouteCircuitAuthorization](ExpressRouteCircuitAuthorization.md)
* [Terraform::AzureRM::ExpressRouteCircuitPeering](ExpressRouteCircuitPeering.md)
* [Terraform::AzureRM::ExpressRouteCircuit](ExpressRouteCircuit.md)
* [Terraform::AzureRM::FirewallApplicationRuleCollection](FirewallApplicationRuleCollection.md)
* [Terraform::AzureRM::FirewallNetworkRuleCollection](FirewallNetworkRuleCollection.md)
* [Terraform::AzureRM::Firewall](Firewall.md)
* [Terraform::AzureRM::FunctionApp](FunctionApp.md)
* [Terraform::AzureRM::Image](Image.md)
* [Terraform::AzureRM::IothubConsumerGroup](IothubConsumerGroup.md)
* [Terraform::AzureRM::Iothub](Iothub.md)
* [Terraform::AzureRM::KeyVaultAccessPolicy](KeyVaultAccessPolicy.md)
* [Terraform::AzureRM::KeyVaultCertificate](KeyVaultCertificate.md)
* [Terraform::AzureRM::KeyVaultKey](KeyVaultKey.md)
* [Terraform::AzureRM::KeyVaultSecret](KeyVaultSecret.md)
* [Terraform::AzureRM::KeyVault](KeyVault.md)
* [Terraform::AzureRM::KubernetesCluster](KubernetesCluster.md)
* [Terraform::AzureRM::LbBackendAddressPool](LbBackendAddressPool.md)
* [Terraform::AzureRM::LbNatPool](LbNatPool.md)
* [Terraform::AzureRM::LbNatRule](LbNatRule.md)
* [Terraform::AzureRM::LbProbe](LbProbe.md)
* [Terraform::AzureRM::LbRule](LbRule.md)
* [Terraform::AzureRM::Lb](Lb.md)
* [Terraform::AzureRM::LocalNetworkGateway](LocalNetworkGateway.md)
* [Terraform::AzureRM::LogAnalyticsLinkedService](LogAnalyticsLinkedService.md)
* [Terraform::AzureRM::LogAnalyticsSolution](LogAnalyticsSolution.md)
* [Terraform::AzureRM::LogAnalyticsWorkspaceLinkedService](LogAnalyticsWorkspaceLinkedService.md)
* [Terraform::AzureRM::LogAnalyticsWorkspace](LogAnalyticsWorkspace.md)
* [Terraform::AzureRM::LogicAppActionCustom](LogicAppActionCustom.md)
* [Terraform::AzureRM::LogicAppActionHttp](LogicAppActionHttp.md)
* [Terraform::AzureRM::LogicAppTriggerCustom](LogicAppTriggerCustom.md)
* [Terraform::AzureRM::LogicAppTriggerHttpRequest](LogicAppTriggerHttpRequest.md)
* [Terraform::AzureRM::LogicAppTriggerRecurrence](LogicAppTriggerRecurrence.md)
* [Terraform::AzureRM::LogicAppWorkflow](LogicAppWorkflow.md)
* [Terraform::AzureRM::ManagedDisk](ManagedDisk.md)
* [Terraform::AzureRM::ManagementGroup](ManagementGroup.md)
* [Terraform::AzureRM::ManagementLock](ManagementLock.md)
* [Terraform::AzureRM::MariadbDatabase](MariadbDatabase.md)
* [Terraform::AzureRM::MariadbServer](MariadbServer.md)
* [Terraform::AzureRM::MetricAlertrule](MetricAlertrule.md)
* [Terraform::AzureRM::MonitorActionGroup](MonitorActionGroup.md)
* [Terraform::AzureRM::MonitorActivityLogAlert](MonitorActivityLogAlert.md)
* [Terraform::AzureRM::MonitorAutoscaleSetting](MonitorAutoscaleSetting.md)
* [Terraform::AzureRM::MonitorDiagnosticSetting](MonitorDiagnosticSetting.md)
* [Terraform::AzureRM::MonitorLogProfile](MonitorLogProfile.md)
* [Terraform::AzureRM::MonitorMetricAlert](MonitorMetricAlert.md)
* [Terraform::AzureRM::MonitorMetricAlertrule](MonitorMetricAlertrule.md)
* [Terraform::AzureRM::MssqlElasticpool](MssqlElasticpool.md)
* [Terraform::AzureRM::MysqlConfiguration](MysqlConfiguration.md)
* [Terraform::AzureRM::MysqlDatabase](MysqlDatabase.md)
* [Terraform::AzureRM::MysqlFirewallRule](MysqlFirewallRule.md)
* [Terraform::AzureRM::MysqlServer](MysqlServer.md)
* [Terraform::AzureRM::MysqlVirtualNetworkRule](MysqlVirtualNetworkRule.md)
* [Terraform::AzureRM::NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation](NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.md)
* [Terraform::AzureRM::NetworkInterfaceApplicationSecurityGroupAssociation](NetworkInterfaceApplicationSecurityGroupAssociation.md)
* [Terraform::AzureRM::NetworkInterfaceBackendAddressPoolAssociation](NetworkInterfaceBackendAddressPoolAssociation.md)
* [Terraform::AzureRM::NetworkInterfaceNatRuleAssociation](NetworkInterfaceNatRuleAssociation.md)
* [Terraform::AzureRM::NetworkInterface](NetworkInterface.md)
* [Terraform::AzureRM::NetworkSecurityGroup](NetworkSecurityGroup.md)
* [Terraform::AzureRM::NetworkSecurityRule](NetworkSecurityRule.md)
* [Terraform::AzureRM::NetworkWatcher](NetworkWatcher.md)
* [Terraform::AzureRM::NotificationHubAuthorizationRule](NotificationHubAuthorizationRule.md)
* [Terraform::AzureRM::NotificationHubNamespace](NotificationHubNamespace.md)
* [Terraform::AzureRM::NotificationHub](NotificationHub.md)
* [Terraform::AzureRM::PacketCapture](PacketCapture.md)
* [Terraform::AzureRM::PolicyAssignment](PolicyAssignment.md)
* [Terraform::AzureRM::PolicyDefinition](PolicyDefinition.md)
* [Terraform::AzureRM::PolicySetDefinition](PolicySetDefinition.md)
* [Terraform::AzureRM::PostgresqlConfiguration](PostgresqlConfiguration.md)
* [Terraform::AzureRM::PostgresqlDatabase](PostgresqlDatabase.md)
* [Terraform::AzureRM::PostgresqlFirewallRule](PostgresqlFirewallRule.md)
* [Terraform::AzureRM::PostgresqlServer](PostgresqlServer.md)
* [Terraform::AzureRM::PostgresqlVirtualNetworkRule](PostgresqlVirtualNetworkRule.md)
* [Terraform::AzureRM::PublicIp](PublicIp.md)
* [Terraform::AzureRM::RecoveryServicesProtectedVm](RecoveryServicesProtectedVm.md)
* [Terraform::AzureRM::RecoveryServicesProtectionPolicyVm](RecoveryServicesProtectionPolicyVm.md)
* [Terraform::AzureRM::RecoveryServicesVault](RecoveryServicesVault.md)
* [Terraform::AzureRM::RedisCache](RedisCache.md)
* [Terraform::AzureRM::RedisFirewallRule](RedisFirewallRule.md)
* [Terraform::AzureRM::RelayNamespace](RelayNamespace.md)
* [Terraform::AzureRM::ResourceGroup](ResourceGroup.md)
* [Terraform::AzureRM::RoleAssignment](RoleAssignment.md)
* [Terraform::AzureRM::RoleDefinition](RoleDefinition.md)
* [Terraform::AzureRM::RouteTable](RouteTable.md)
* [Terraform::AzureRM::Route](Route.md)
* [Terraform::AzureRM::SchedulerJobCollection](SchedulerJobCollection.md)
* [Terraform::AzureRM::SchedulerJob](SchedulerJob.md)
* [Terraform::AzureRM::SearchService](SearchService.md)
* [Terraform::AzureRM::SecurityCenterContact](SecurityCenterContact.md)
* [Terraform::AzureRM::SecurityCenterSubscriptionPricing](SecurityCenterSubscriptionPricing.md)
* [Terraform::AzureRM::SecurityCenterWorkspace](SecurityCenterWorkspace.md)
* [Terraform::AzureRM::ServiceFabricCluster](ServiceFabricCluster.md)
* [Terraform::AzureRM::ServicebusNamespaceAuthorizationRule](ServicebusNamespaceAuthorizationRule.md)
* [Terraform::AzureRM::ServicebusNamespace](ServicebusNamespace.md)
* [Terraform::AzureRM::ServicebusQueueAuthorizationRule](ServicebusQueueAuthorizationRule.md)
* [Terraform::AzureRM::ServicebusQueue](ServicebusQueue.md)
* [Terraform::AzureRM::ServicebusSubscriptionRule](ServicebusSubscriptionRule.md)
* [Terraform::AzureRM::ServicebusSubscription](ServicebusSubscription.md)
* [Terraform::AzureRM::ServicebusTopicAuthorizationRule](ServicebusTopicAuthorizationRule.md)
* [Terraform::AzureRM::ServicebusTopic](ServicebusTopic.md)
* [Terraform::AzureRM::SharedImageGallery](SharedImageGallery.md)
* [Terraform::AzureRM::SharedImageVersion](SharedImageVersion.md)
* [Terraform::AzureRM::SharedImage](SharedImage.md)
* [Terraform::AzureRM::SignalrService](SignalrService.md)
* [Terraform::AzureRM::Snapshot](Snapshot.md)
* [Terraform::AzureRM::SqlActiveDirectoryAdministrator](SqlActiveDirectoryAdministrator.md)
* [Terraform::AzureRM::SqlDatabase](SqlDatabase.md)
* [Terraform::AzureRM::SqlElasticpool](SqlElasticpool.md)
* [Terraform::AzureRM::SqlFirewallRule](SqlFirewallRule.md)
* [Terraform::AzureRM::SqlServer](SqlServer.md)
* [Terraform::AzureRM::SqlVirtualNetworkRule](SqlVirtualNetworkRule.md)
* [Terraform::AzureRM::StorageAccount](StorageAccount.md)
* [Terraform::AzureRM::StorageBlob](StorageBlob.md)
* [Terraform::AzureRM::StorageContainer](StorageContainer.md)
* [Terraform::AzureRM::StorageQueue](StorageQueue.md)
* [Terraform::AzureRM::StorageShare](StorageShare.md)
* [Terraform::AzureRM::StorageTable](StorageTable.md)
* [Terraform::AzureRM::SubnetNetworkSecurityGroupAssociation](SubnetNetworkSecurityGroupAssociation.md)
* [Terraform::AzureRM::SubnetRouteTableAssociation](SubnetRouteTableAssociation.md)
* [Terraform::AzureRM::Subnet](Subnet.md)
* [Terraform::AzureRM::TemplateDeployment](TemplateDeployment.md)
* [Terraform::AzureRM::TrafficManagerEndpoint](TrafficManagerEndpoint.md)
* [Terraform::AzureRM::TrafficManagerProfile](TrafficManagerProfile.md)
* [Terraform::AzureRM::UserAssignedIdentity](UserAssignedIdentity.md)
* [Terraform::AzureRM::VirtualMachineDataDiskAttachment](VirtualMachineDataDiskAttachment.md)
* [Terraform::AzureRM::VirtualMachineExtension](VirtualMachineExtension.md)
* [Terraform::AzureRM::VirtualMachineScaleSet](VirtualMachineScaleSet.md)
* [Terraform::AzureRM::VirtualMachine](VirtualMachine.md)
* [Terraform::AzureRM::VirtualNetworkGatewayConnection](VirtualNetworkGatewayConnection.md)
* [Terraform::AzureRM::VirtualNetworkGateway](VirtualNetworkGateway.md)
* [Terraform::AzureRM::VirtualNetworkPeering](VirtualNetworkPeering.md)
* [Terraform::AzureRM::VirtualNetwork](VirtualNetwork.md)