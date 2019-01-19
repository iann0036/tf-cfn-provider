# Google Cloud Provider

##Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/google**. The below arguments may be included as the key/value or JSON properties in the secret:

* `credentials` - (Optional) The path or contents of a file that contains your
  service account private key in JSON format. You can download your existing
  [Google Cloud service account file] from the Google Cloud Console, or you can
  create a new one from the same page.

  Credentials can also be specified using any of the following environment
  variables (listed in order of precedence):

    * `GOOGLE_CREDENTIALS`
    * `GOOGLE_CLOUD_KEYFILE_JSON`
    * `GCLOUD_KEYFILE_JSON`

  The [`GOOGLE_APPLICATION_CREDENTIALS`][adc]
  environment variable can also contain the path of a file to obtain credentials
  from.

  If no credentials are specified, the provider will fall back to using the
  [Google Application Default Credentials][adc].
  If you are running Terraform from a GCE instance, see [Creating and Enabling
  Service Accounts for Instances][gce-service-account] for details.

  On your computer, if you have made your identity available as the
  Application Default Credentials by running [`gcloud auth application-default
  login`][gcloud adc], the provider will use your identity.

  -> [Service accounts][service accounts] are the recommended way
  to manage GCP credentials. [GCE metadata] is also acceptable, although it can
  only be used when running Terraform from within [certain GCP resources](https://cloud.google.com/docs/authentication/production#obtaining_credentials_on_compute_engine_kubernetes_engine_app_engine_flexible_environment_and_cloud_functions).
  Credentials obtained through `gcloud` are not guaranteed to work for all APIs.

* `access_token` - (Optional) An temporary [OAuth 2.0 access token](https://developers.google.com/identity/protocols/OAuth2)
  obtained from the Google Authorization server, i.e. the
  `Authorization: Bearer` token used to authenticate Google API HTTP requests.

  Access tokens can also be specified using any of the following environment
  variables (listed in order of precedence):

    * `GOOGLE_OAUTH_ACCESS_TOKEN`

  -> These access tokens cannot be renewed by Terraform and thus will only work for at most 1 hour. If you anticipate Terraform needing access for more than one hour per run, please use `credentials` instead. Credentials are used to complete a two-legged OAuth 2.0 flow on your behalf to obtain access tokens and can be used renew or reauthenticate for tokens as needed.

* `project` - (Optional) The ID of the project to apply any resources to.  This
  can also be specified using any of the following environment variables (listed
  in order of precedence):

    * `GOOGLE_PROJECT`
    * `GOOGLE_CLOUD_PROJECT`
    * `GCLOUD_PROJECT`
    * `CLOUDSDK_CORE_PROJECT`

    -> `GOOGLE_PROJECT` is the recommended environment variable to use if
    you choose to add your project using environment variables.

* `region` - (Optional) The region to operate under, if not specified by a given resource.
  This can also be specified using any of the following environment variables (listed in order of
  precedence):

    * `GOOGLE_REGION`
    * `GCLOUD_REGION`
    * `CLOUDSDK_COMPUTE_REGION`

* `zone` - (Optional) The zone to operate under, if not specified by a given resource.
  This can also be specified using any of the following environment variables (listed in order of
  precedence):

    * `GOOGLE_ZONE`
    * `GCLOUD_ZONE`
    * `CLOUDSDK_COMPUTE_ZONE`

[Google Cloud service account file]: https://console.cloud.google.com/apis/credentials/serviceaccountkey
[adc]: https://cloud.google.com/docs/authentication/production
[gce-service-account]: https://cloud.google.com/compute/docs/authentication
[gcloud adc]: https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login
[service accounts]: https://cloud.google.com/docs/authentication/getting-started
[GCE metadata]: https://cloud.google.com/docs/authentication/production#obtaining_credentials_on_compute_engine_kubernetes_engine_app_engine_flexible_environment_and_cloud_functions


## Supported Resources

* [Terraform::Google::AppEngineApplication](docs/providers/google/AppEngineApplication.md)
* [Terraform::Google::AppEngineFirewallRule](docs/providers/google/AppEngineFirewallRule.md)
* [Terraform::Google::BigqueryDataset](docs/providers/google/BigqueryDataset.md)
* [Terraform::Google::BigqueryTable](docs/providers/google/BigqueryTable.md)
* [Terraform::Google::BigtableInstance](docs/providers/google/BigtableInstance.md)
* [Terraform::Google::BigtableTable](docs/providers/google/BigtableTable.md)
* [Terraform::Google::BillingAccountIamMember](docs/providers/google/BillingAccountIamMember.md)
* [Terraform::Google::BillingAccountIamPolicy](docs/providers/google/BillingAccountIamPolicy.md)
* [Terraform::Google::BillingAccount_iamBinding](docs/providers/google/BillingAccount_iamBinding.md)
* [Terraform::Google::CloudbuildTrigger](docs/providers/google/CloudbuildTrigger.md)
* [Terraform::Google::CloudfunctionsFunction](docs/providers/google/CloudfunctionsFunction.md)
* [Terraform::Google::CloudiotRegistry](docs/providers/google/CloudiotRegistry.md)
* [Terraform::Google::ComposerEnvironment](docs/providers/google/ComposerEnvironment.md)
* [Terraform::Google::ComputeAddress](docs/providers/google/ComputeAddress.md)
* [Terraform::Google::ComputeAttachedDisk](docs/providers/google/ComputeAttachedDisk.md)
* [Terraform::Google::ComputeAutoscaler](docs/providers/google/ComputeAutoscaler.md)
* [Terraform::Google::ComputeBackendBucket](docs/providers/google/ComputeBackendBucket.md)
* [Terraform::Google::ComputeBackendService](docs/providers/google/ComputeBackendService.md)
* [Terraform::Google::ComputeDisk](docs/providers/google/ComputeDisk.md)
* [Terraform::Google::ComputeFirewall](docs/providers/google/ComputeFirewall.md)
* [Terraform::Google::ComputeForwardingRule](docs/providers/google/ComputeForwardingRule.md)
* [Terraform::Google::ComputeGlobalAddress](docs/providers/google/ComputeGlobalAddress.md)
* [Terraform::Google::ComputeGlobalForwardingRule](docs/providers/google/ComputeGlobalForwardingRule.md)
* [Terraform::Google::ComputeHealthCheck](docs/providers/google/ComputeHealthCheck.md)
* [Terraform::Google::ComputeHttpHealthCheck](docs/providers/google/ComputeHttpHealthCheck.md)
* [Terraform::Google::ComputeHttpsHealthCheck](docs/providers/google/ComputeHttpsHealthCheck.md)
* [Terraform::Google::ComputeImage](docs/providers/google/ComputeImage.md)
* [Terraform::Google::ComputeInstanceFromTemplate](docs/providers/google/ComputeInstanceFromTemplate.md)
* [Terraform::Google::ComputeInstanceGroupManager](docs/providers/google/ComputeInstanceGroupManager.md)
* [Terraform::Google::ComputeInstanceGroup](docs/providers/google/ComputeInstanceGroup.md)
* [Terraform::Google::ComputeInstanceTemplate](docs/providers/google/ComputeInstanceTemplate.md)
* [Terraform::Google::ComputeInstance](docs/providers/google/ComputeInstance.md)
* [Terraform::Google::ComputeInterconnectAttachment](docs/providers/google/ComputeInterconnectAttachment.md)
* [Terraform::Google::ComputeNetworkPeering](docs/providers/google/ComputeNetworkPeering.md)
* [Terraform::Google::ComputeNetwork](docs/providers/google/ComputeNetwork.md)
* [Terraform::Google::ComputeProjectMetadataItem](docs/providers/google/ComputeProjectMetadataItem.md)
* [Terraform::Google::ComputeProjectMetadata](docs/providers/google/ComputeProjectMetadata.md)
* [Terraform::Google::ComputeRegionAutoscaler](docs/providers/google/ComputeRegionAutoscaler.md)
* [Terraform::Google::ComputeRegionBackendService](docs/providers/google/ComputeRegionBackendService.md)
* [Terraform::Google::ComputeRegionDisk](docs/providers/google/ComputeRegionDisk.md)
* [Terraform::Google::ComputeRegionInstanceGroupManager](docs/providers/google/ComputeRegionInstanceGroupManager.md)
* [Terraform::Google::ComputeRoute](docs/providers/google/ComputeRoute.md)
* [Terraform::Google::ComputeRouterInterface](docs/providers/google/ComputeRouterInterface.md)
* [Terraform::Google::ComputeRouterNat](docs/providers/google/ComputeRouterNat.md)
* [Terraform::Google::ComputeRouterPeer](docs/providers/google/ComputeRouterPeer.md)
* [Terraform::Google::ComputeRouter](docs/providers/google/ComputeRouter.md)
* [Terraform::Google::ComputeSecurityPolicy](docs/providers/google/ComputeSecurityPolicy.md)
* [Terraform::Google::ComputeSharedVpcHostProject](docs/providers/google/ComputeSharedVpcHostProject.md)
* [Terraform::Google::ComputeSharedVpcServiceProject](docs/providers/google/ComputeSharedVpcServiceProject.md)
* [Terraform::Google::ComputeSnapshot](docs/providers/google/ComputeSnapshot.md)
* [Terraform::Google::ComputeSslCertificate](docs/providers/google/ComputeSslCertificate.md)
* [Terraform::Google::ComputeSslPolicy](docs/providers/google/ComputeSslPolicy.md)
* [Terraform::Google::ComputeSubnetwork](docs/providers/google/ComputeSubnetwork.md)
* [Terraform::Google::ComputeTargetHttpProxy](docs/providers/google/ComputeTargetHttpProxy.md)
* [Terraform::Google::ComputeTargetHttpsProxy](docs/providers/google/ComputeTargetHttpsProxy.md)
* [Terraform::Google::ComputeTargetPool](docs/providers/google/ComputeTargetPool.md)
* [Terraform::Google::ComputeTargetSslProxy](docs/providers/google/ComputeTargetSslProxy.md)
* [Terraform::Google::ComputeTargetTcpProxy](docs/providers/google/ComputeTargetTcpProxy.md)
* [Terraform::Google::ComputeUrlMap](docs/providers/google/ComputeUrlMap.md)
* [Terraform::Google::ComputeVpnGateway](docs/providers/google/ComputeVpnGateway.md)
* [Terraform::Google::ComputeVpnTunnel](docs/providers/google/ComputeVpnTunnel.md)
* [Terraform::Google::ContainerCluster](docs/providers/google/ContainerCluster.md)
* [Terraform::Google::ContainerNodePool](docs/providers/google/ContainerNodePool.md)
* [Terraform::Google::DataflowJob](docs/providers/google/DataflowJob.md)
* [Terraform::Google::DataprocCluster](docs/providers/google/DataprocCluster.md)
* [Terraform::Google::DataprocJob](docs/providers/google/DataprocJob.md)
* [Terraform::Google::DnsManagedZone](docs/providers/google/DnsManagedZone.md)
* [Terraform::Google::DnsRecordSet](docs/providers/google/DnsRecordSet.md)
* [Terraform::Google::EndpointsService](docs/providers/google/EndpointsService.md)
* [Terraform::Google::FolderIamBinding](docs/providers/google/FolderIamBinding.md)
* [Terraform::Google::FolderIamMember](docs/providers/google/FolderIamMember.md)
* [Terraform::Google::FolderIamPolicy](docs/providers/google/FolderIamPolicy.md)
* [Terraform::Google::FolderOrganizationPolicy](docs/providers/google/FolderOrganizationPolicy.md)
* [Terraform::Google::Folder](docs/providers/google/Folder.md)
* [Terraform::Google::KmsCryptoKeyIamBinding](docs/providers/google/KmsCryptoKeyIamBinding.md)
* [Terraform::Google::KmsCryptoKeyIamMember](docs/providers/google/KmsCryptoKeyIamMember.md)
* [Terraform::Google::KmsCryptoKey](docs/providers/google/KmsCryptoKey.md)
* [Terraform::Google::KmsKeyRing](docs/providers/google/KmsKeyRing.md)
* [Terraform::Google::LoggingBillingAccountExclusion](docs/providers/google/LoggingBillingAccountExclusion.md)
* [Terraform::Google::LoggingBillingAccountSink](docs/providers/google/LoggingBillingAccountSink.md)
* [Terraform::Google::LoggingFolderExclusion](docs/providers/google/LoggingFolderExclusion.md)
* [Terraform::Google::LoggingFolderSink](docs/providers/google/LoggingFolderSink.md)
* [Terraform::Google::LoggingOrganizationExclusion](docs/providers/google/LoggingOrganizationExclusion.md)
* [Terraform::Google::LoggingOrganizationSink](docs/providers/google/LoggingOrganizationSink.md)
* [Terraform::Google::LoggingProjectExclusion](docs/providers/google/LoggingProjectExclusion.md)
* [Terraform::Google::LoggingProjectSink](docs/providers/google/LoggingProjectSink.md)
* [Terraform::Google::MonitoringAlertPolicy](docs/providers/google/MonitoringAlertPolicy.md)
* [Terraform::Google::MonitoringGroup](docs/providers/google/MonitoringGroup.md)
* [Terraform::Google::MonitoringNotificationChannel](docs/providers/google/MonitoringNotificationChannel.md)
* [Terraform::Google::MonitoringUptimeCheckConfig](docs/providers/google/MonitoringUptimeCheckConfig.md)
* [Terraform::Google::OrganizationIamBinding](docs/providers/google/OrganizationIamBinding.md)
* [Terraform::Google::OrganizationIamCustomRole](docs/providers/google/OrganizationIamCustomRole.md)
* [Terraform::Google::OrganizationIamMember](docs/providers/google/OrganizationIamMember.md)
* [Terraform::Google::OrganizationIamPolicy](docs/providers/google/OrganizationIamPolicy.md)
* [Terraform::Google::OrganizationPolicy](docs/providers/google/OrganizationPolicy.md)
* [Terraform::Google::ProjectIamCustomRole](docs/providers/google/ProjectIamCustomRole.md)
* [Terraform::Google::ProjectOrganizationPolicy](docs/providers/google/ProjectOrganizationPolicy.md)
* [Terraform::Google::ProjectService](docs/providers/google/ProjectService.md)
* [Terraform::Google::ProjectServices](docs/providers/google/ProjectServices.md)
* [Terraform::Google::ProjectUsageExportBucket](docs/providers/google/ProjectUsageExportBucket.md)
* [Terraform::Google::Project](docs/providers/google/Project.md)
* [Terraform::Google::PubsubSubscription](docs/providers/google/PubsubSubscription.md)
* [Terraform::Google::PubsubTopic](docs/providers/google/PubsubTopic.md)
* [Terraform::Google::RedisInstance](docs/providers/google/RedisInstance.md)
* [Terraform::Google::ResourceManagerLien](docs/providers/google/ResourceManagerLien.md)
* [Terraform::Google::RuntimeconfigConfig](docs/providers/google/RuntimeconfigConfig.md)
* [Terraform::Google::RuntimeconfigVariable](docs/providers/google/RuntimeconfigVariable.md)
* [Terraform::Google::ServiceAccountKey](docs/providers/google/ServiceAccountKey.md)
* [Terraform::Google::ServiceAccount](docs/providers/google/ServiceAccount.md)
* [Terraform::Google::ServiceNetworkingConnection](docs/providers/google/ServiceNetworkingConnection.md)
* [Terraform::Google::SourcerepoRepository](docs/providers/google/SourcerepoRepository.md)
* [Terraform::Google::SpannerDatabase](docs/providers/google/SpannerDatabase.md)
* [Terraform::Google::SpannerInstance](docs/providers/google/SpannerInstance.md)
* [Terraform::Google::SqlDatabaseInstance](docs/providers/google/SqlDatabaseInstance.md)
* [Terraform::Google::SqlDatabase](docs/providers/google/SqlDatabase.md)
* [Terraform::Google::SqlSslCert](docs/providers/google/SqlSslCert.md)
* [Terraform::Google::SqlUser](docs/providers/google/SqlUser.md)
* [Terraform::Google::StorageBucketAcl](docs/providers/google/StorageBucketAcl.md)
* [Terraform::Google::StorageBucketObject](docs/providers/google/StorageBucketObject.md)
* [Terraform::Google::StorageBucket](docs/providers/google/StorageBucket.md)
* [Terraform::Google::StorageDefaultObjectAccessControl](docs/providers/google/StorageDefaultObjectAccessControl.md)
* [Terraform::Google::StorageDefaultObjectAcl](docs/providers/google/StorageDefaultObjectAcl.md)
* [Terraform::Google::StorageNotification](docs/providers/google/StorageNotification.md)
* [Terraform::Google::StorageObjectAccessControl](docs/providers/google/StorageObjectAccessControl.md)
* [Terraform::Google::StorageObjectAcl](docs/providers/google/StorageObjectAcl.md)
* [Terraform::Google::StorageTransferJob](docs/providers/google/StorageTransferJob.md)