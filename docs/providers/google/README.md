# Google Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/google** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

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

* `scopes` - (Optional) The list of OAuth 2.0 [scopes] used to generate access token for Google APIs.
  Default list of scopes:
    * https://www.googleapis.com/auth/compute
    * https://www.googleapis.com/auth/cloud-platform
    * https://www.googleapis.com/auth/ndev.clouddns.readwrite
    * https://www.googleapis.com/auth/devstorage.full_control

[Google Cloud service account file]: https://console.cloud.google.com/apis/credentials/serviceaccountkey
[adc]: https://cloud.google.com/docs/authentication/production
[gce-service-account]: https://cloud.google.com/compute/docs/authentication
[gcloud adc]: https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login
[service accounts]: https://cloud.google.com/docs/authentication/getting-started
[GCE metadata]: https://cloud.google.com/docs/authentication/production#obtaining_credentials_on_compute_engine_kubernetes_engine_app_engine_flexible_environment_and_cloud_functions
[scopes]: https://developers.google.com/identity/protocols/googlescopes


## Supported Resources

* [Terraform::Google::AppEngineApplication](AppEngineApplication.md)
* [Terraform::Google::AppEngineFirewallRule](AppEngineFirewallRule.md)
* [Terraform::Google::BigqueryDataset](BigqueryDataset.md)
* [Terraform::Google::BigqueryTable](BigqueryTable.md)
* [Terraform::Google::BigtableInstance](BigtableInstance.md)
* [Terraform::Google::BigtableTable](BigtableTable.md)
* [Terraform::Google::BillingAccountIamMember](BillingAccountIamMember.md)
* [Terraform::Google::BillingAccountIamPolicy](BillingAccountIamPolicy.md)
* [Terraform::Google::BillingAccount_iamBinding](BillingAccount_iamBinding.md)
* [Terraform::Google::CloudbuildTrigger](CloudbuildTrigger.md)
* [Terraform::Google::CloudfunctionsFunction](CloudfunctionsFunction.md)
* [Terraform::Google::CloudiotRegistry](CloudiotRegistry.md)
* [Terraform::Google::ComposerEnvironment](ComposerEnvironment.md)
* [Terraform::Google::ComputeAddress](ComputeAddress.md)
* [Terraform::Google::ComputeAttachedDisk](ComputeAttachedDisk.md)
* [Terraform::Google::ComputeAutoscaler](ComputeAutoscaler.md)
* [Terraform::Google::ComputeBackendBucket](ComputeBackendBucket.md)
* [Terraform::Google::ComputeBackendService](ComputeBackendService.md)
* [Terraform::Google::ComputeDisk](ComputeDisk.md)
* [Terraform::Google::ComputeFirewall](ComputeFirewall.md)
* [Terraform::Google::ComputeForwardingRule](ComputeForwardingRule.md)
* [Terraform::Google::ComputeGlobalAddress](ComputeGlobalAddress.md)
* [Terraform::Google::ComputeGlobalForwardingRule](ComputeGlobalForwardingRule.md)
* [Terraform::Google::ComputeHealthCheck](ComputeHealthCheck.md)
* [Terraform::Google::ComputeHttpHealthCheck](ComputeHttpHealthCheck.md)
* [Terraform::Google::ComputeHttpsHealthCheck](ComputeHttpsHealthCheck.md)
* [Terraform::Google::ComputeImage](ComputeImage.md)
* [Terraform::Google::ComputeInstanceFromTemplate](ComputeInstanceFromTemplate.md)
* [Terraform::Google::ComputeInstanceGroupManager](ComputeInstanceGroupManager.md)
* [Terraform::Google::ComputeInstanceGroup](ComputeInstanceGroup.md)
* [Terraform::Google::ComputeInstanceTemplate](ComputeInstanceTemplate.md)
* [Terraform::Google::ComputeInstance](ComputeInstance.md)
* [Terraform::Google::ComputeInterconnectAttachment](ComputeInterconnectAttachment.md)
* [Terraform::Google::ComputeNetworkPeering](ComputeNetworkPeering.md)
* [Terraform::Google::ComputeNetwork](ComputeNetwork.md)
* [Terraform::Google::ComputeProjectMetadataItem](ComputeProjectMetadataItem.md)
* [Terraform::Google::ComputeProjectMetadata](ComputeProjectMetadata.md)
* [Terraform::Google::ComputeRegionAutoscaler](ComputeRegionAutoscaler.md)
* [Terraform::Google::ComputeRegionBackendService](ComputeRegionBackendService.md)
* [Terraform::Google::ComputeRegionDisk](ComputeRegionDisk.md)
* [Terraform::Google::ComputeRegionInstanceGroupManager](ComputeRegionInstanceGroupManager.md)
* [Terraform::Google::ComputeRoute](ComputeRoute.md)
* [Terraform::Google::ComputeRouterInterface](ComputeRouterInterface.md)
* [Terraform::Google::ComputeRouterNat](ComputeRouterNat.md)
* [Terraform::Google::ComputeRouterPeer](ComputeRouterPeer.md)
* [Terraform::Google::ComputeRouter](ComputeRouter.md)
* [Terraform::Google::ComputeSecurityPolicy](ComputeSecurityPolicy.md)
* [Terraform::Google::ComputeSharedVpcHostProject](ComputeSharedVpcHostProject.md)
* [Terraform::Google::ComputeSharedVpcServiceProject](ComputeSharedVpcServiceProject.md)
* [Terraform::Google::ComputeSnapshot](ComputeSnapshot.md)
* [Terraform::Google::ComputeSslCertificate](ComputeSslCertificate.md)
* [Terraform::Google::ComputeSslPolicy](ComputeSslPolicy.md)
* [Terraform::Google::ComputeSubnetwork](ComputeSubnetwork.md)
* [Terraform::Google::ComputeTargetHttpProxy](ComputeTargetHttpProxy.md)
* [Terraform::Google::ComputeTargetHttpsProxy](ComputeTargetHttpsProxy.md)
* [Terraform::Google::ComputeTargetPool](ComputeTargetPool.md)
* [Terraform::Google::ComputeTargetSslProxy](ComputeTargetSslProxy.md)
* [Terraform::Google::ComputeTargetTcpProxy](ComputeTargetTcpProxy.md)
* [Terraform::Google::ComputeUrlMap](ComputeUrlMap.md)
* [Terraform::Google::ComputeVpnGateway](ComputeVpnGateway.md)
* [Terraform::Google::ComputeVpnTunnel](ComputeVpnTunnel.md)
* [Terraform::Google::ContainerCluster](ContainerCluster.md)
* [Terraform::Google::ContainerNodePool](ContainerNodePool.md)
* [Terraform::Google::DataflowJob](DataflowJob.md)
* [Terraform::Google::DataprocCluster](DataprocCluster.md)
* [Terraform::Google::DataprocJob](DataprocJob.md)
* [Terraform::Google::DnsManagedZone](DnsManagedZone.md)
* [Terraform::Google::DnsRecordSet](DnsRecordSet.md)
* [Terraform::Google::EndpointsService](EndpointsService.md)
* [Terraform::Google::FolderIamBinding](FolderIamBinding.md)
* [Terraform::Google::FolderIamMember](FolderIamMember.md)
* [Terraform::Google::FolderIamPolicy](FolderIamPolicy.md)
* [Terraform::Google::FolderOrganizationPolicy](FolderOrganizationPolicy.md)
* [Terraform::Google::Folder](Folder.md)
* [Terraform::Google::KmsCryptoKeyIamBinding](KmsCryptoKeyIamBinding.md)
* [Terraform::Google::KmsCryptoKeyIamMember](KmsCryptoKeyIamMember.md)
* [Terraform::Google::KmsCryptoKey](KmsCryptoKey.md)
* [Terraform::Google::KmsKeyRing](KmsKeyRing.md)
* [Terraform::Google::LoggingBillingAccountExclusion](LoggingBillingAccountExclusion.md)
* [Terraform::Google::LoggingBillingAccountSink](LoggingBillingAccountSink.md)
* [Terraform::Google::LoggingFolderExclusion](LoggingFolderExclusion.md)
* [Terraform::Google::LoggingFolderSink](LoggingFolderSink.md)
* [Terraform::Google::LoggingOrganizationExclusion](LoggingOrganizationExclusion.md)
* [Terraform::Google::LoggingOrganizationSink](LoggingOrganizationSink.md)
* [Terraform::Google::LoggingProjectExclusion](LoggingProjectExclusion.md)
* [Terraform::Google::LoggingProjectSink](LoggingProjectSink.md)
* [Terraform::Google::MonitoringAlertPolicy](MonitoringAlertPolicy.md)
* [Terraform::Google::MonitoringGroup](MonitoringGroup.md)
* [Terraform::Google::MonitoringNotificationChannel](MonitoringNotificationChannel.md)
* [Terraform::Google::MonitoringUptimeCheckConfig](MonitoringUptimeCheckConfig.md)
* [Terraform::Google::OrganizationIamBinding](OrganizationIamBinding.md)
* [Terraform::Google::OrganizationIamCustomRole](OrganizationIamCustomRole.md)
* [Terraform::Google::OrganizationIamMember](OrganizationIamMember.md)
* [Terraform::Google::OrganizationIamPolicy](OrganizationIamPolicy.md)
* [Terraform::Google::OrganizationPolicy](OrganizationPolicy.md)
* [Terraform::Google::ProjectIamCustomRole](ProjectIamCustomRole.md)
* [Terraform::Google::ProjectOrganizationPolicy](ProjectOrganizationPolicy.md)
* [Terraform::Google::ProjectService](ProjectService.md)
* [Terraform::Google::ProjectServices](ProjectServices.md)
* [Terraform::Google::ProjectUsageExportBucket](ProjectUsageExportBucket.md)
* [Terraform::Google::Project](Project.md)
* [Terraform::Google::PubsubSubscription](PubsubSubscription.md)
* [Terraform::Google::PubsubTopic](PubsubTopic.md)
* [Terraform::Google::RedisInstance](RedisInstance.md)
* [Terraform::Google::ResourceManagerLien](ResourceManagerLien.md)
* [Terraform::Google::RuntimeconfigConfig](RuntimeconfigConfig.md)
* [Terraform::Google::RuntimeconfigVariable](RuntimeconfigVariable.md)
* [Terraform::Google::ServiceAccountKey](ServiceAccountKey.md)
* [Terraform::Google::ServiceAccount](ServiceAccount.md)
* [Terraform::Google::ServiceNetworkingConnection](ServiceNetworkingConnection.md)
* [Terraform::Google::SourcerepoRepository](SourcerepoRepository.md)
* [Terraform::Google::SpannerDatabase](SpannerDatabase.md)
* [Terraform::Google::SpannerInstance](SpannerInstance.md)
* [Terraform::Google::SqlDatabaseInstance](SqlDatabaseInstance.md)
* [Terraform::Google::SqlDatabase](SqlDatabase.md)
* [Terraform::Google::SqlSslCert](SqlSslCert.md)
* [Terraform::Google::SqlUser](SqlUser.md)
* [Terraform::Google::StorageBucketAcl](StorageBucketAcl.md)
* [Terraform::Google::StorageBucketObject](StorageBucketObject.md)
* [Terraform::Google::StorageBucket](StorageBucket.md)
* [Terraform::Google::StorageDefaultObjectAccessControl](StorageDefaultObjectAccessControl.md)
* [Terraform::Google::StorageDefaultObjectAcl](StorageDefaultObjectAcl.md)
* [Terraform::Google::StorageNotification](StorageNotification.md)
* [Terraform::Google::StorageObjectAccessControl](StorageObjectAccessControl.md)
* [Terraform::Google::StorageObjectAcl](StorageObjectAcl.md)
* [Terraform::Google::StorageTransferJob](StorageTransferJob.md)