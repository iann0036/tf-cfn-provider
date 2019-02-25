# AWS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/aws** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - (Optional) This is the AWS access key.

* `secret_key` - (Optional) This is the AWS secret key.

* `region` - (Required) This is the AWS region.

* `profile` - (Optional) This is the AWS profile name as set in the shared credentials
  file.

* `assume_role` - (Optional) An `assume_role` block (documented below). Only one
  `assume_role` block may be in the configuration.

* `shared_credentials_file` = (Optional) This is the path to the shared credentials file.
  If this is not set and a profile is specified, `~/.aws/credentials` will be used.

* `token` - (Optional) Use this to set an MFA token.

* `max_retries` - (Optional) This is the maximum number of times an API
  call is retried, in the case where requests are being throttled or
  experiencing transient failures. The delay between the subsequent API
  calls increases exponentially.

* `allowed_account_ids` - (Optional) List of allowed, white listed, AWS
  account IDs to prevent you from mistakenly using an incorrect one (and
  potentially end up destroying a live environment). Conflicts with
  `forbidden_account_ids`.

* `forbidden_account_ids` - (Optional) List of forbidden, blacklisted,
  AWS account IDs to prevent you mistakenly using a wrong one (and
  potentially end up destroying a live environment). Conflicts with
  `allowed_account_ids`.

* `insecure` - (Optional) Explicitly allow the provider to
  perform "insecure" SSL requests. If omitted, default value is `false`.

* `skip_credentials_validation` - (Optional) Skip the credentials
  validation via the STS API. Useful for AWS API implementations that do
  not have STS available or implemented.

* `skip_get_ec2_platforms` - (Optional) Skip getting the supported EC2
  platforms. Used by users that don't have ec2:DescribeAccountAttributes
  permissions.

* `skip_region_validation` - (Optional) Skip validation of provided region name.
  Useful for AWS-like implementations that use their own region names
  or to bypass the validation for regions that aren't publicly available yet.

* `skip_requesting_account_id` - (Optional) Skip requesting the account
  ID.  Useful for AWS API implementations that do not have the IAM, STS
  API, or metadata API.  When set to `true` and not determined previously,
  returns an empty account ID when manually constructing ARN attributes with
  the following:
  - [`Terraform::AWS::ApiGatewayDeployment` resource](/docs/providers/aws/r/api_gateway_deployment.html)
  - [`Terraform::AWS::ApiGatewayRestApi` resource](/docs/providers/aws/r/api_gateway_rest_api.html)
  - [`Terraform::AWS::ApiGatewayStage` resource](/docs/providers/aws/r/api_gateway_stage.html)
  - [`Terraform::AWS::BudgetsBudget` resource](/docs/providers/aws/r/budgets_budget.html)
  - [`Terraform::AWS::CognitoIdentityPool` resource](/docs/providers/aws/r/cognito_identity_pool.html)
  - [`Terraform::AWS::CognitoUserPool` resource](/docs/providers/aws/r/cognito_user_pool.html)
  - [`Terraform::AWS::CognitoUserPools` data source](/docs/providers/aws/d/cognito_user_pools.html)
  - [`Terraform::AWS::DmsReplicationSubnetGroup` resource](/docs/providers/aws/r/dms_replication_subnet_group.html)
  - [`Terraform::AWS::DxConnection` resource](/docs/providers/aws/r/dx_connection.html)
  - [`Terraform::AWS::DxHostedPrivateVirtualInterfaceAccepter` resource](/docs/providers/aws/r/dx_hosted_private_virtual_interface_accepter.html)
  - [`Terraform::AWS::DxHostedPrivateVirtualInterface` resource](/docs/providers/aws/r/dx_hosted_private_virtual_interface.html)
  - [`Terraform::AWS::DxHostedPublicVirtualInterfaceAccepter` resource](/docs/providers/aws/r/dx_hosted_public_virtual_interface_accepter.html)
  - [`Terraform::AWS::DxHostedPublicVirtualInterface` resource](/docs/providers/aws/r/dx_hosted_public_virtual_interface.html)
  - [`Terraform::AWS::DxLag` resource](/docs/providers/aws/r/dx_lag.html)
  - [`Terraform::AWS::DxPrivateVirtualInterface` resource](/docs/providers/aws/r/dx_private_virtual_interface.html)
  - [`Terraform::AWS::DxPublicVirtualInterface` resource](/docs/providers/aws/r/dx_public_virtual_interface.html)
  - [`Terraform::AWS::EbsVolume` data source](/docs/providers/aws/d/ebs_volume.html)
  - [`Terraform::AWS::EcsCluster` resource (import)](/docs/providers/aws/r/ecs_cluster.html)
  - [`Terraform::AWS::EcsService` resource (import)](/docs/providers/aws/r/ecs_service.html)
  - [`Terraform::AWS::EfsFileSystem` data source](/docs/providers/aws/d/efs_file_system.html)
  - [`Terraform::AWS::EfsFileSystem` resource](/docs/providers/aws/r/efs_file_system.html)
  - [`Terraform::AWS::EfsMountTarget` data source](/docs/providers/aws/d/efs_mount_target.html)
  - [`Terraform::AWS::EfsMountTarget` resource](/docs/providers/aws/r/efs_mount_target.html)
  - [`Terraform::AWS::ElasticacheCluster` data source](/docs/providers/aws/d/elasticache_cluster.html)
  - [`Terraform::AWS::ElasticacheCluster` resource](/docs/providers/aws/r/elasticache_cluster.html)
  - [`Terraform::AWS::Elb` resource](/docs/providers/aws/r/elb.html)
  - [`Terraform::AWS::Instance` data source](/docs/providers/aws/d/instance.html)
  - [`Terraform::AWS::Instance` resource](/docs/providers/aws/r/instance.html)
  - [`Terraform::AWS::LaunchTemplate` resource](/docs/providers/aws/r/launch_template.html)
  - [`Terraform::AWS::RedshiftCluster` resource](/docs/providers/aws/r/redshift_cluster.html)
  - [`Terraform::AWS::RedshiftSubnetGroup` resource](/docs/providers/aws/r/redshift_subnet_group.html)
  - [`Terraform::AWS::S3AccountPublicAccessBlock` resource](/docs/providers/aws/r/s3_account_public_access_block.html)
  - [`Terraform::AWS::SesDomainIdentityVerification` resource](/docs/providers/aws/r/ses_domain_identity_verification.html)
  - [`Terraform::AWS::SesDomainIdentity` resource](/docs/providers/aws/r/ses_domain_identity.html)
  - [`Terraform::AWS::SsmDocument` resource](/docs/providers/aws/r/ssm_document.html)
  - [`Terraform::AWS::SsmParameter` resource](/docs/providers/aws/r/ssm_parameter.html)
  - [`Terraform::AWS::Vpc` data source](/docs/providers/aws/d/vpc.html)
  - [`Terraform::AWS::Vpc` resource](/docs/providers/aws/r/vpc.html)
  - [`Terraform::AWS::WafIpset` resource](/docs/providers/aws/r/waf_ipset.html)
  - [`Terraform::AWS::WafregionalIpset` resource](/docs/providers/aws/r/wafregional_ipset.html)

* `skip_metadata_api_check` - (Optional) Skip the AWS Metadata API
  check.  Useful for AWS API implementations that do not have a metadata
  API endpoint.  Setting to `true` prevents Terraform from authenticating
  via the Metadata API. You may need to use other authentication methods
  like static credentials, configuration variables, or environment
  variables.

* `s3_force_path_style` - (Optional) Set this to `true` to force the
  request to use path-style addressing, i.e.,
  `http://s3.amazonaws.com/BUCKET/KEY`. By default, the S3 client will use
  virtual hosted bucket addressing, `http://BUCKET.s3.amazonaws.com/KEY`,
  when possible. Specific to the Amazon S3 service.

The nested `assume_role` block supports the following:

* `role_arn` - (Required) The ARN of the role to assume.

* `session_name` - (Optional) The session name to use when making the
  AssumeRole call.

* `external_id` - (Optional) The external ID to use when making the
  AssumeRole call.

* `policy` - (Optional) A more restrictive policy to apply to the temporary credentials.
This gives you a way to further restrict the permissions for the resulting temporary
security credentials. You cannot use the passed policy to grant permissions that are
in excess of those allowed by the access policy of the role that is being assumed.

Nested `endpoints` block supports the following:

* `acm` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom ACM endpoints.

* `apigateway` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom API Gateway endpoints.

* `cloudformation` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom CloudFormation endpoints.

* `cloudwatch` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom CloudWatch endpoints.

* `cloudwatchevents` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom CloudWatchEvents endpoints.

* `cloudwatchlogs` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom CloudWatchLogs endpoints.

* `devicefarm` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom DeviceFarm endpoints.

* `dynamodb` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  `dynamodb-local`.

* `ec2` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom EC2 endpoints.

* `autoscaling` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom Autoscaling endpoints.

* `ecr` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom ECR endpoints.

* `ecs` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom ECS endpoints.

* `elb` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom ELB endpoints.

* `efs` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom EFS endpoints.

* `es` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`.  It's typically used to connect to
  custom Elasticsearch endpoints.

* `iam` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom IAM endpoints.

* `kinesis` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  `kinesalite`.

* `kms` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom KMS endpoints.

* `lambda` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom Lambda endpoints.

* `r53` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom Route53 endpoints.

* `rds` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom RDS endpoints.

* `s3` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom S3 endpoints.

* `s3control` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom S3 Control endpoints (e.g. account-level public access block).

* `sns` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom SNS endpoints.

* `sqs` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom SQS endpoints.

* `sts` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom STS endpoints.

* `ssm` - (Optional) Use this to override the default endpoint
  URL constructed from the `region`. It's typically used to connect to
  custom SSM endpoints.


## Supported Resources

* [Terraform::AWS::AcmCertificateValidation](AcmCertificateValidation.md)
* [Terraform::AWS::AcmCertificate](AcmCertificate.md)
* [Terraform::AWS::AcmpcaCertificateAuthority](AcmpcaCertificateAuthority.md)
* [Terraform::AWS::AmiCopy](AmiCopy.md)
* [Terraform::AWS::AmiFromInstance](AmiFromInstance.md)
* [Terraform::AWS::AmiLaunchPermission](AmiLaunchPermission.md)
* [Terraform::AWS::Ami](Ami.md)
* [Terraform::AWS::ApiGatewayAccount](ApiGatewayAccount.md)
* [Terraform::AWS::ApiGatewayApiKey](ApiGatewayApiKey.md)
* [Terraform::AWS::ApiGatewayAuthorizer](ApiGatewayAuthorizer.md)
* [Terraform::AWS::ApiGatewayBasePathMapping](ApiGatewayBasePathMapping.md)
* [Terraform::AWS::ApiGatewayClientCertificate](ApiGatewayClientCertificate.md)
* [Terraform::AWS::ApiGatewayDeployment](ApiGatewayDeployment.md)
* [Terraform::AWS::ApiGatewayDocumentationPart](ApiGatewayDocumentationPart.md)
* [Terraform::AWS::ApiGatewayDocumentationVersion](ApiGatewayDocumentationVersion.md)
* [Terraform::AWS::ApiGatewayDomainName](ApiGatewayDomainName.md)
* [Terraform::AWS::ApiGatewayGatewayResponse](ApiGatewayGatewayResponse.md)
* [Terraform::AWS::ApiGatewayIntegrationResponse](ApiGatewayIntegrationResponse.md)
* [Terraform::AWS::ApiGatewayIntegration](ApiGatewayIntegration.md)
* [Terraform::AWS::ApiGatewayMethodResponse](ApiGatewayMethodResponse.md)
* [Terraform::AWS::ApiGatewayMethodSettings](ApiGatewayMethodSettings.md)
* [Terraform::AWS::ApiGatewayMethod](ApiGatewayMethod.md)
* [Terraform::AWS::ApiGatewayModel](ApiGatewayModel.md)
* [Terraform::AWS::ApiGatewayRequestValidator](ApiGatewayRequestValidator.md)
* [Terraform::AWS::ApiGatewayResource](ApiGatewayResource.md)
* [Terraform::AWS::ApiGatewayRestApi](ApiGatewayRestApi.md)
* [Terraform::AWS::ApiGatewayStage](ApiGatewayStage.md)
* [Terraform::AWS::ApiGatewayUsagePlanKey](ApiGatewayUsagePlanKey.md)
* [Terraform::AWS::ApiGatewayUsagePlan](ApiGatewayUsagePlan.md)
* [Terraform::AWS::ApiGatewayVpcLink](ApiGatewayVpcLink.md)
* [Terraform::AWS::AppCookieStickinessPolicy](AppCookieStickinessPolicy.md)
* [Terraform::AWS::AppautoscalingPolicy](AppautoscalingPolicy.md)
* [Terraform::AWS::AppautoscalingScheduledAction](AppautoscalingScheduledAction.md)
* [Terraform::AWS::AppautoscalingTarget](AppautoscalingTarget.md)
* [Terraform::AWS::AppmeshMesh](AppmeshMesh.md)
* [Terraform::AWS::AppmeshRoute](AppmeshRoute.md)
* [Terraform::AWS::AppmeshVirtualNode](AppmeshVirtualNode.md)
* [Terraform::AWS::AppmeshVirtualRouter](AppmeshVirtualRouter.md)
* [Terraform::AWS::AppsyncApiKey](AppsyncApiKey.md)
* [Terraform::AWS::AppsyncDatasource](AppsyncDatasource.md)
* [Terraform::AWS::AppsyncGraphqlApi](AppsyncGraphqlApi.md)
* [Terraform::AWS::AthenaDatabase](AthenaDatabase.md)
* [Terraform::AWS::AthenaNamedQuery](AthenaNamedQuery.md)
* [Terraform::AWS::AutoscalingAttachment](AutoscalingAttachment.md)
* [Terraform::AWS::AutoscalingGroup](AutoscalingGroup.md)
* [Terraform::AWS::AutoscalingLifecycleHook](AutoscalingLifecycleHook.md)
* [Terraform::AWS::AutoscalingNotification](AutoscalingNotification.md)
* [Terraform::AWS::AutoscalingPolicy](AutoscalingPolicy.md)
* [Terraform::AWS::AutoscalingSchedule](AutoscalingSchedule.md)
* [Terraform::AWS::BackupVault](BackupVault.md)
* [Terraform::AWS::BatchComputeEnvironment](BatchComputeEnvironment.md)
* [Terraform::AWS::BatchJobDefinition](BatchJobDefinition.md)
* [Terraform::AWS::BatchJobQueue](BatchJobQueue.md)
* [Terraform::AWS::BudgetsBudget](BudgetsBudget.md)
* [Terraform::AWS::Cloud9EnvironmentEc2](Cloud9EnvironmentEc2.md)
* [Terraform::AWS::CloudformationStack](CloudformationStack.md)
* [Terraform::AWS::CloudfrontDistribution](CloudfrontDistribution.md)
* [Terraform::AWS::CloudfrontOriginAccessIdentity](CloudfrontOriginAccessIdentity.md)
* [Terraform::AWS::CloudfrontPublicKey](CloudfrontPublicKey.md)
* [Terraform::AWS::CloudhsmV2Cluster](CloudhsmV2Cluster.md)
* [Terraform::AWS::CloudhsmV2Hsm](CloudhsmV2Hsm.md)
* [Terraform::AWS::Cloudtrail](Cloudtrail.md)
* [Terraform::AWS::CloudwatchDashboard](CloudwatchDashboard.md)
* [Terraform::AWS::CloudwatchEventPermission](CloudwatchEventPermission.md)
* [Terraform::AWS::CloudwatchEventRule](CloudwatchEventRule.md)
* [Terraform::AWS::CloudwatchEventTarget](CloudwatchEventTarget.md)
* [Terraform::AWS::CloudwatchLogDestinationPolicy](CloudwatchLogDestinationPolicy.md)
* [Terraform::AWS::CloudwatchLogDestination](CloudwatchLogDestination.md)
* [Terraform::AWS::CloudwatchLogGroup](CloudwatchLogGroup.md)
* [Terraform::AWS::CloudwatchLogMetricFilter](CloudwatchLogMetricFilter.md)
* [Terraform::AWS::CloudwatchLogResourcePolicy](CloudwatchLogResourcePolicy.md)
* [Terraform::AWS::CloudwatchLogStream](CloudwatchLogStream.md)
* [Terraform::AWS::CloudwatchLogSubscriptionFilter](CloudwatchLogSubscriptionFilter.md)
* [Terraform::AWS::CloudwatchMetricAlarm](CloudwatchMetricAlarm.md)
* [Terraform::AWS::CodebuildProject](CodebuildProject.md)
* [Terraform::AWS::CodebuildWebhook](CodebuildWebhook.md)
* [Terraform::AWS::CodecommitRepository](CodecommitRepository.md)
* [Terraform::AWS::CodecommitTrigger](CodecommitTrigger.md)
* [Terraform::AWS::CodedeployApp](CodedeployApp.md)
* [Terraform::AWS::CodedeployDeploymentConfig](CodedeployDeploymentConfig.md)
* [Terraform::AWS::CodedeployDeploymentGroup](CodedeployDeploymentGroup.md)
* [Terraform::AWS::CodepipelineWebhook](CodepipelineWebhook.md)
* [Terraform::AWS::Codepipeline](Codepipeline.md)
* [Terraform::AWS::CognitoIdentityPoolRolesAttachment](CognitoIdentityPoolRolesAttachment.md)
* [Terraform::AWS::CognitoIdentityPool](CognitoIdentityPool.md)
* [Terraform::AWS::CognitoIdentityProvider](CognitoIdentityProvider.md)
* [Terraform::AWS::CognitoResourceServer](CognitoResourceServer.md)
* [Terraform::AWS::CognitoUserGroup](CognitoUserGroup.md)
* [Terraform::AWS::CognitoUserPoolClient](CognitoUserPoolClient.md)
* [Terraform::AWS::CognitoUserPoolDomain](CognitoUserPoolDomain.md)
* [Terraform::AWS::CognitoUserPool](CognitoUserPool.md)
* [Terraform::AWS::ConfigAggregateAuthorization](ConfigAggregateAuthorization.md)
* [Terraform::AWS::ConfigConfigRule](ConfigConfigRule.md)
* [Terraform::AWS::ConfigConfigurationAggregator](ConfigConfigurationAggregator.md)
* [Terraform::AWS::ConfigConfigurationRecorderStatus](ConfigConfigurationRecorderStatus.md)
* [Terraform::AWS::ConfigConfigurationRecorder](ConfigConfigurationRecorder.md)
* [Terraform::AWS::ConfigDeliveryChannel](ConfigDeliveryChannel.md)
* [Terraform::AWS::CurReportDefinition](CurReportDefinition.md)
* [Terraform::AWS::CustomerGateway](CustomerGateway.md)
* [Terraform::AWS::DatasyncAgent](DatasyncAgent.md)
* [Terraform::AWS::DatasyncLocationEfs](DatasyncLocationEfs.md)
* [Terraform::AWS::DatasyncLocationNfs](DatasyncLocationNfs.md)
* [Terraform::AWS::DatasyncLocationS3](DatasyncLocationS3.md)
* [Terraform::AWS::DatasyncTask](DatasyncTask.md)
* [Terraform::AWS::DaxCluster](DaxCluster.md)
* [Terraform::AWS::DaxParameterGroup](DaxParameterGroup.md)
* [Terraform::AWS::DaxSubnetGroup](DaxSubnetGroup.md)
* [Terraform::AWS::DbClusterSnapshot](DbClusterSnapshot.md)
* [Terraform::AWS::DbEventSubscription](DbEventSubscription.md)
* [Terraform::AWS::DbInstance](DbInstance.md)
* [Terraform::AWS::DbOptionGroup](DbOptionGroup.md)
* [Terraform::AWS::DbParameterGroup](DbParameterGroup.md)
* [Terraform::AWS::DbSecurityGroup](DbSecurityGroup.md)
* [Terraform::AWS::DbSnapshot](DbSnapshot.md)
* [Terraform::AWS::DbSubnetGroup](DbSubnetGroup.md)
* [Terraform::AWS::DefaultNetworkAcl](DefaultNetworkAcl.md)
* [Terraform::AWS::DefaultRouteTable](DefaultRouteTable.md)
* [Terraform::AWS::DefaultSecurityGroup](DefaultSecurityGroup.md)
* [Terraform::AWS::DefaultSubnet](DefaultSubnet.md)
* [Terraform::AWS::DefaultVpc](DefaultVpc.md)
* [Terraform::AWS::DevicefarmProject](DevicefarmProject.md)
* [Terraform::AWS::DirectoryServiceConditionalForwarder](DirectoryServiceConditionalForwarder.md)
* [Terraform::AWS::DirectoryServiceDirectory](DirectoryServiceDirectory.md)
* [Terraform::AWS::DlmLifecyclePolicy](DlmLifecyclePolicy.md)
* [Terraform::AWS::DmsCertificate](DmsCertificate.md)
* [Terraform::AWS::DmsEndpoint](DmsEndpoint.md)
* [Terraform::AWS::DmsReplicationInstance](DmsReplicationInstance.md)
* [Terraform::AWS::DmsReplicationSubnetGroup](DmsReplicationSubnetGroup.md)
* [Terraform::AWS::DmsReplicationTask](DmsReplicationTask.md)
* [Terraform::AWS::DocdbClusterInstance](DocdbClusterInstance.md)
* [Terraform::AWS::DocdbClusterParameterGroup](DocdbClusterParameterGroup.md)
* [Terraform::AWS::DocdbClusterSnapshot](DocdbClusterSnapshot.md)
* [Terraform::AWS::DocdbCluster](DocdbCluster.md)
* [Terraform::AWS::DocdbSubnetGroup](DocdbSubnetGroup.md)
* [Terraform::AWS::DxBgpPeer](DxBgpPeer.md)
* [Terraform::AWS::DxConnectionAssociation](DxConnectionAssociation.md)
* [Terraform::AWS::DxConnection](DxConnection.md)
* [Terraform::AWS::DxGatewayAssociation](DxGatewayAssociation.md)
* [Terraform::AWS::DxGateway](DxGateway.md)
* [Terraform::AWS::DxHostedPrivateVirtualInterfaceAccepter](DxHostedPrivateVirtualInterfaceAccepter.md)
* [Terraform::AWS::DxHostedPrivateVirtualInterface](DxHostedPrivateVirtualInterface.md)
* [Terraform::AWS::DxHostedPublicVirtualInterfaceAccepter](DxHostedPublicVirtualInterfaceAccepter.md)
* [Terraform::AWS::DxHostedPublicVirtualInterface](DxHostedPublicVirtualInterface.md)
* [Terraform::AWS::DxLag](DxLag.md)
* [Terraform::AWS::DxPrivateVirtualInterface](DxPrivateVirtualInterface.md)
* [Terraform::AWS::DxPublicVirtualInterface](DxPublicVirtualInterface.md)
* [Terraform::AWS::DynamodbGlobalTable](DynamodbGlobalTable.md)
* [Terraform::AWS::DynamodbTableItem](DynamodbTableItem.md)
* [Terraform::AWS::DynamodbTable](DynamodbTable.md)
* [Terraform::AWS::EbsSnapshotCopy](EbsSnapshotCopy.md)
* [Terraform::AWS::EbsSnapshot](EbsSnapshot.md)
* [Terraform::AWS::EbsVolume](EbsVolume.md)
* [Terraform::AWS::Ec2CapacityReservation](Ec2CapacityReservation.md)
* [Terraform::AWS::Ec2ClientVpnEndpoint](Ec2ClientVpnEndpoint.md)
* [Terraform::AWS::Ec2ClientVpnNetworkAssociation](Ec2ClientVpnNetworkAssociation.md)
* [Terraform::AWS::Ec2Fleet](Ec2Fleet.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTableAssociation](Ec2TransitGatewayRouteTableAssociation.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTablePropagation](Ec2TransitGatewayRouteTablePropagation.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTable](Ec2TransitGatewayRouteTable.md)
* [Terraform::AWS::Ec2TransitGatewayRoute](Ec2TransitGatewayRoute.md)
* [Terraform::AWS::Ec2TransitGatewayVpcAttachment](Ec2TransitGatewayVpcAttachment.md)
* [Terraform::AWS::Ec2TransitGateway](Ec2TransitGateway.md)
* [Terraform::AWS::EcrLifecyclePolicy](EcrLifecyclePolicy.md)
* [Terraform::AWS::EcrRepositoryPolicy](EcrRepositoryPolicy.md)
* [Terraform::AWS::EcrRepository](EcrRepository.md)
* [Terraform::AWS::EcsCluster](EcsCluster.md)
* [Terraform::AWS::EcsService](EcsService.md)
* [Terraform::AWS::EcsTaskDefinition](EcsTaskDefinition.md)
* [Terraform::AWS::EfsFileSystem](EfsFileSystem.md)
* [Terraform::AWS::EfsMountTarget](EfsMountTarget.md)
* [Terraform::AWS::EgressOnlyInternetGateway](EgressOnlyInternetGateway.md)
* [Terraform::AWS::EipAssociation](EipAssociation.md)
* [Terraform::AWS::Eip](Eip.md)
* [Terraform::AWS::EksCluster](EksCluster.md)
* [Terraform::AWS::ElasticBeanstalkApplicationVersion](ElasticBeanstalkApplicationVersion.md)
* [Terraform::AWS::ElasticBeanstalkApplication](ElasticBeanstalkApplication.md)
* [Terraform::AWS::ElasticBeanstalkConfigurationTemplate](ElasticBeanstalkConfigurationTemplate.md)
* [Terraform::AWS::ElasticBeanstalkEnvironment](ElasticBeanstalkEnvironment.md)
* [Terraform::AWS::ElasticacheCluster](ElasticacheCluster.md)
* [Terraform::AWS::ElasticacheParameterGroup](ElasticacheParameterGroup.md)
* [Terraform::AWS::ElasticacheReplicationGroup](ElasticacheReplicationGroup.md)
* [Terraform::AWS::ElasticacheSecurityGroup](ElasticacheSecurityGroup.md)
* [Terraform::AWS::ElasticacheSubnetGroup](ElasticacheSubnetGroup.md)
* [Terraform::AWS::ElasticsearchDomainPolicy](ElasticsearchDomainPolicy.md)
* [Terraform::AWS::ElasticsearchDomain](ElasticsearchDomain.md)
* [Terraform::AWS::ElastictranscoderPipeline](ElastictranscoderPipeline.md)
* [Terraform::AWS::ElastictranscoderPreset](ElastictranscoderPreset.md)
* [Terraform::AWS::ElbAttachment](ElbAttachment.md)
* [Terraform::AWS::Elb](Elb.md)
* [Terraform::AWS::EmrCluster](EmrCluster.md)
* [Terraform::AWS::EmrInstanceGroup](EmrInstanceGroup.md)
* [Terraform::AWS::EmrSecurityConfiguration](EmrSecurityConfiguration.md)
* [Terraform::AWS::FlowLog](FlowLog.md)
* [Terraform::AWS::GameliftAlias](GameliftAlias.md)
* [Terraform::AWS::GameliftBuild](GameliftBuild.md)
* [Terraform::AWS::GameliftFleet](GameliftFleet.md)
* [Terraform::AWS::GameliftGameSessionQueue](GameliftGameSessionQueue.md)
* [Terraform::AWS::GlacierVaultLock](GlacierVaultLock.md)
* [Terraform::AWS::GlacierVault](GlacierVault.md)
* [Terraform::AWS::GlobalacceleratorAccelerator](GlobalacceleratorAccelerator.md)
* [Terraform::AWS::GlueCatalogDatabase](GlueCatalogDatabase.md)
* [Terraform::AWS::GlueCatalogTable](GlueCatalogTable.md)
* [Terraform::AWS::GlueClassifier](GlueClassifier.md)
* [Terraform::AWS::GlueConnection](GlueConnection.md)
* [Terraform::AWS::GlueCrawler](GlueCrawler.md)
* [Terraform::AWS::GlueJob](GlueJob.md)
* [Terraform::AWS::GlueSecurityConfiguration](GlueSecurityConfiguration.md)
* [Terraform::AWS::GlueTrigger](GlueTrigger.md)
* [Terraform::AWS::GuarddutyDetector](GuarddutyDetector.md)
* [Terraform::AWS::GuarddutyIpset](GuarddutyIpset.md)
* [Terraform::AWS::GuarddutyMember](GuarddutyMember.md)
* [Terraform::AWS::GuarddutyThreatintelset](GuarddutyThreatintelset.md)
* [Terraform::AWS::IamAccessKey](IamAccessKey.md)
* [Terraform::AWS::IamAccountAlias](IamAccountAlias.md)
* [Terraform::AWS::IamAccountPasswordPolicy](IamAccountPasswordPolicy.md)
* [Terraform::AWS::IamGroupMembership](IamGroupMembership.md)
* [Terraform::AWS::IamGroupPolicyAttachment](IamGroupPolicyAttachment.md)
* [Terraform::AWS::IamGroupPolicy](IamGroupPolicy.md)
* [Terraform::AWS::IamGroup](IamGroup.md)
* [Terraform::AWS::IamInstanceProfile](IamInstanceProfile.md)
* [Terraform::AWS::IamOpenidConnectProvider](IamOpenidConnectProvider.md)
* [Terraform::AWS::IamPolicyAttachment](IamPolicyAttachment.md)
* [Terraform::AWS::IamPolicy](IamPolicy.md)
* [Terraform::AWS::IamRolePolicyAttachment](IamRolePolicyAttachment.md)
* [Terraform::AWS::IamRolePolicy](IamRolePolicy.md)
* [Terraform::AWS::IamRole](IamRole.md)
* [Terraform::AWS::IamSamlProvider](IamSamlProvider.md)
* [Terraform::AWS::IamServerCertificate](IamServerCertificate.md)
* [Terraform::AWS::IamServiceLinkedRole](IamServiceLinkedRole.md)
* [Terraform::AWS::IamUserGroupMembership](IamUserGroupMembership.md)
* [Terraform::AWS::IamUserLoginProfile](IamUserLoginProfile.md)
* [Terraform::AWS::IamUserPolicyAttachment](IamUserPolicyAttachment.md)
* [Terraform::AWS::IamUserPolicy](IamUserPolicy.md)
* [Terraform::AWS::IamUserSshKey](IamUserSshKey.md)
* [Terraform::AWS::IamUser](IamUser.md)
* [Terraform::AWS::InspectorAssessmentTarget](InspectorAssessmentTarget.md)
* [Terraform::AWS::InspectorAssessmentTemplate](InspectorAssessmentTemplate.md)
* [Terraform::AWS::InspectorResourceGroup](InspectorResourceGroup.md)
* [Terraform::AWS::Instance](Instance.md)
* [Terraform::AWS::InternetGateway](InternetGateway.md)
* [Terraform::AWS::IotCertificate](IotCertificate.md)
* [Terraform::AWS::IotPolicyAttachment](IotPolicyAttachment.md)
* [Terraform::AWS::IotPolicy](IotPolicy.md)
* [Terraform::AWS::IotRoleAlias](IotRoleAlias.md)
* [Terraform::AWS::IotThingPrincipalAttachment](IotThingPrincipalAttachment.md)
* [Terraform::AWS::IotThingType](IotThingType.md)
* [Terraform::AWS::IotThing](IotThing.md)
* [Terraform::AWS::IotTopicRule](IotTopicRule.md)
* [Terraform::AWS::KeyPair](KeyPair.md)
* [Terraform::AWS::KinesisAnalyticsApplication](KinesisAnalyticsApplication.md)
* [Terraform::AWS::KinesisFirehoseDeliveryStream](KinesisFirehoseDeliveryStream.md)
* [Terraform::AWS::KinesisStream](KinesisStream.md)
* [Terraform::AWS::KmsAlias](KmsAlias.md)
* [Terraform::AWS::KmsGrant](KmsGrant.md)
* [Terraform::AWS::KmsKey](KmsKey.md)
* [Terraform::AWS::LambdaAlias](LambdaAlias.md)
* [Terraform::AWS::LambdaEventSourceMapping](LambdaEventSourceMapping.md)
* [Terraform::AWS::LambdaFunction](LambdaFunction.md)
* [Terraform::AWS::LambdaLayerVersion](LambdaLayerVersion.md)
* [Terraform::AWS::LambdaPermission](LambdaPermission.md)
* [Terraform::AWS::LaunchConfiguration](LaunchConfiguration.md)
* [Terraform::AWS::LaunchTemplate](LaunchTemplate.md)
* [Terraform::AWS::LbCookieStickinessPolicy](LbCookieStickinessPolicy.md)
* [Terraform::AWS::LbListenerCertificate](LbListenerCertificate.md)
* [Terraform::AWS::LbListenerRule](LbListenerRule.md)
* [Terraform::AWS::LbListener](LbListener.md)
* [Terraform::AWS::LbSslNegotiationPolicy](LbSslNegotiationPolicy.md)
* [Terraform::AWS::LbTargetGroupAttachment](LbTargetGroupAttachment.md)
* [Terraform::AWS::LbTargetGroup](LbTargetGroup.md)
* [Terraform::AWS::Lb](Lb.md)
* [Terraform::AWS::LicensemanagerAssociation](LicensemanagerAssociation.md)
* [Terraform::AWS::LicensemanagerLicenseConfiguration](LicensemanagerLicenseConfiguration.md)
* [Terraform::AWS::LightsailDomain](LightsailDomain.md)
* [Terraform::AWS::LightsailInstance](LightsailInstance.md)
* [Terraform::AWS::LightsailKeyPair](LightsailKeyPair.md)
* [Terraform::AWS::LightsailStaticIpAttachment](LightsailStaticIpAttachment.md)
* [Terraform::AWS::LightsailStaticIp](LightsailStaticIp.md)
* [Terraform::AWS::LoadBalancerBackendServerPolicy](LoadBalancerBackendServerPolicy.md)
* [Terraform::AWS::LoadBalancerListenerPolicy](LoadBalancerListenerPolicy.md)
* [Terraform::AWS::LoadBalancerPolicy](LoadBalancerPolicy.md)
* [Terraform::AWS::MacieMemberAccountAssociation](MacieMemberAccountAssociation.md)
* [Terraform::AWS::MacieS3BucketAssociation](MacieS3BucketAssociation.md)
* [Terraform::AWS::MainRouteTableAssociation](MainRouteTableAssociation.md)
* [Terraform::AWS::MediaPackageChannel](MediaPackageChannel.md)
* [Terraform::AWS::MediaStoreContainerPolicy](MediaStoreContainerPolicy.md)
* [Terraform::AWS::MediaStoreContainer](MediaStoreContainer.md)
* [Terraform::AWS::MqBroker](MqBroker.md)
* [Terraform::AWS::MqConfiguration](MqConfiguration.md)
* [Terraform::AWS::NatGateway](NatGateway.md)
* [Terraform::AWS::NeptuneClusterInstance](NeptuneClusterInstance.md)
* [Terraform::AWS::NeptuneClusterParameterGroup](NeptuneClusterParameterGroup.md)
* [Terraform::AWS::NeptuneClusterSnapshot](NeptuneClusterSnapshot.md)
* [Terraform::AWS::NeptuneCluster](NeptuneCluster.md)
* [Terraform::AWS::NeptuneEventSubscription](NeptuneEventSubscription.md)
* [Terraform::AWS::NeptuneParameterGroup](NeptuneParameterGroup.md)
* [Terraform::AWS::NeptuneSubnetGroup](NeptuneSubnetGroup.md)
* [Terraform::AWS::NetworkAclRule](NetworkAclRule.md)
* [Terraform::AWS::NetworkAcl](NetworkAcl.md)
* [Terraform::AWS::NetworkInterfaceAttachment](NetworkInterfaceAttachment.md)
* [Terraform::AWS::NetworkInterfaceSgAttachment](NetworkInterfaceSgAttachment.md)
* [Terraform::AWS::NetworkInterface](NetworkInterface.md)
* [Terraform::AWS::OpsworksApplication](OpsworksApplication.md)
* [Terraform::AWS::OpsworksCustomLayer](OpsworksCustomLayer.md)
* [Terraform::AWS::OpsworksGangliaLayer](OpsworksGangliaLayer.md)
* [Terraform::AWS::OpsworksHaproxyLayer](OpsworksHaproxyLayer.md)
* [Terraform::AWS::OpsworksInstance](OpsworksInstance.md)
* [Terraform::AWS::OpsworksJavaAppLayer](OpsworksJavaAppLayer.md)
* [Terraform::AWS::OpsworksMemcachedLayer](OpsworksMemcachedLayer.md)
* [Terraform::AWS::OpsworksMysqlLayer](OpsworksMysqlLayer.md)
* [Terraform::AWS::OpsworksNodejsAppLayer](OpsworksNodejsAppLayer.md)
* [Terraform::AWS::OpsworksPermission](OpsworksPermission.md)
* [Terraform::AWS::OpsworksPhpAppLayer](OpsworksPhpAppLayer.md)
* [Terraform::AWS::OpsworksRailsAppLayer](OpsworksRailsAppLayer.md)
* [Terraform::AWS::OpsworksRdsDbInstance](OpsworksRdsDbInstance.md)
* [Terraform::AWS::OpsworksStack](OpsworksStack.md)
* [Terraform::AWS::OpsworksStaticWebLayer](OpsworksStaticWebLayer.md)
* [Terraform::AWS::OpsworksUserProfile](OpsworksUserProfile.md)
* [Terraform::AWS::OrganizationsAccount](OrganizationsAccount.md)
* [Terraform::AWS::OrganizationsOrganization](OrganizationsOrganization.md)
* [Terraform::AWS::OrganizationsPolicyAttachment](OrganizationsPolicyAttachment.md)
* [Terraform::AWS::OrganizationsPolicy](OrganizationsPolicy.md)
* [Terraform::AWS::PinpointAdmChannel](PinpointAdmChannel.md)
* [Terraform::AWS::PinpointApnsChannel](PinpointApnsChannel.md)
* [Terraform::AWS::PinpointApnsSandboxChannel](PinpointApnsSandboxChannel.md)
* [Terraform::AWS::PinpointApnsVoipChannel](PinpointApnsVoipChannel.md)
* [Terraform::AWS::PinpointApnsVoipSandboxChannel](PinpointApnsVoipSandboxChannel.md)
* [Terraform::AWS::PinpointApp](PinpointApp.md)
* [Terraform::AWS::PinpointBaiduChannel](PinpointBaiduChannel.md)
* [Terraform::AWS::PinpointEmailChannel](PinpointEmailChannel.md)
* [Terraform::AWS::PinpointEventStream](PinpointEventStream.md)
* [Terraform::AWS::PinpointGcmChannel](PinpointGcmChannel.md)
* [Terraform::AWS::PinpointSmsChannel](PinpointSmsChannel.md)
* [Terraform::AWS::PlacementGroup](PlacementGroup.md)
* [Terraform::AWS::ProxyProtocolPolicy](ProxyProtocolPolicy.md)
* [Terraform::AWS::RamPrincipalAssociation](RamPrincipalAssociation.md)
* [Terraform::AWS::RamResourceAssociation](RamResourceAssociation.md)
* [Terraform::AWS::RamResourceShare](RamResourceShare.md)
* [Terraform::AWS::RdsClusterEndpoint](RdsClusterEndpoint.md)
* [Terraform::AWS::RdsClusterInstance](RdsClusterInstance.md)
* [Terraform::AWS::RdsClusterParameterGroup](RdsClusterParameterGroup.md)
* [Terraform::AWS::RdsCluster](RdsCluster.md)
* [Terraform::AWS::RdsGlobalCluster](RdsGlobalCluster.md)
* [Terraform::AWS::RedshiftCluster](RedshiftCluster.md)
* [Terraform::AWS::RedshiftEventSubscription](RedshiftEventSubscription.md)
* [Terraform::AWS::RedshiftParameterGroup](RedshiftParameterGroup.md)
* [Terraform::AWS::RedshiftSecurityGroup](RedshiftSecurityGroup.md)
* [Terraform::AWS::RedshiftSnapshotCopyGrant](RedshiftSnapshotCopyGrant.md)
* [Terraform::AWS::RedshiftSubnetGroup](RedshiftSubnetGroup.md)
* [Terraform::AWS::ResourcegroupsGroup](ResourcegroupsGroup.md)
* [Terraform::AWS::Route53DelegationSet](Route53DelegationSet.md)
* [Terraform::AWS::Route53HealthCheck](Route53HealthCheck.md)
* [Terraform::AWS::Route53QueryLog](Route53QueryLog.md)
* [Terraform::AWS::Route53Record](Route53Record.md)
* [Terraform::AWS::Route53ZoneAssociation](Route53ZoneAssociation.md)
* [Terraform::AWS::Route53Zone](Route53Zone.md)
* [Terraform::AWS::RouteTableAssociation](RouteTableAssociation.md)
* [Terraform::AWS::RouteTable](RouteTable.md)
* [Terraform::AWS::Route](Route.md)
* [Terraform::AWS::S3AccountPublicAccessBlock](S3AccountPublicAccessBlock.md)
* [Terraform::AWS::S3BucketInventory](S3BucketInventory.md)
* [Terraform::AWS::S3BucketMetric](S3BucketMetric.md)
* [Terraform::AWS::S3BucketNotification](S3BucketNotification.md)
* [Terraform::AWS::S3BucketObject](S3BucketObject.md)
* [Terraform::AWS::S3BucketPolicy](S3BucketPolicy.md)
* [Terraform::AWS::S3BucketPublicAccessBlock](S3BucketPublicAccessBlock.md)
* [Terraform::AWS::S3Bucket](S3Bucket.md)
* [Terraform::AWS::SagemakerModel](SagemakerModel.md)
* [Terraform::AWS::SagemakerNotebookInstance](SagemakerNotebookInstance.md)
* [Terraform::AWS::SecretsmanagerSecretVersion](SecretsmanagerSecretVersion.md)
* [Terraform::AWS::SecretsmanagerSecret](SecretsmanagerSecret.md)
* [Terraform::AWS::SecurityGroupRule](SecurityGroupRule.md)
* [Terraform::AWS::SecurityGroup](SecurityGroup.md)
* [Terraform::AWS::SecurityhubAccount](SecurityhubAccount.md)
* [Terraform::AWS::SecurityhubProductSubscription](SecurityhubProductSubscription.md)
* [Terraform::AWS::SecurityhubStandardsSubscription](SecurityhubStandardsSubscription.md)
* [Terraform::AWS::ServiceDiscoveryHttpNamespace](ServiceDiscoveryHttpNamespace.md)
* [Terraform::AWS::ServiceDiscoveryPrivateDnsNamespace](ServiceDiscoveryPrivateDnsNamespace.md)
* [Terraform::AWS::ServiceDiscoveryPublicDnsNamespace](ServiceDiscoveryPublicDnsNamespace.md)
* [Terraform::AWS::ServiceDiscoveryService](ServiceDiscoveryService.md)
* [Terraform::AWS::ServicecatalogPortfolio](ServicecatalogPortfolio.md)
* [Terraform::AWS::SesActiveReceiptRuleSet](SesActiveReceiptRuleSet.md)
* [Terraform::AWS::SesConfigurationSet](SesConfigurationSet.md)
* [Terraform::AWS::SesDomainDkim](SesDomainDkim.md)
* [Terraform::AWS::SesDomainIdentityVerification](SesDomainIdentityVerification.md)
* [Terraform::AWS::SesDomainIdentity](SesDomainIdentity.md)
* [Terraform::AWS::SesDomainMailFrom](SesDomainMailFrom.md)
* [Terraform::AWS::SesEventDestination](SesEventDestination.md)
* [Terraform::AWS::SesReceiptFilter](SesReceiptFilter.md)
* [Terraform::AWS::SesReceiptRuleSet](SesReceiptRuleSet.md)
* [Terraform::AWS::SesReceiptRule](SesReceiptRule.md)
* [Terraform::AWS::SesTemplate](SesTemplate.md)
* [Terraform::AWS::SimpledbDomain](SimpledbDomain.md)
* [Terraform::AWS::SnapshotCreateVolumePermission](SnapshotCreateVolumePermission.md)
* [Terraform::AWS::SnsPlatformApplication](SnsPlatformApplication.md)
* [Terraform::AWS::SnsSmsPreferences](SnsSmsPreferences.md)
* [Terraform::AWS::SnsTopicPolicy](SnsTopicPolicy.md)
* [Terraform::AWS::SnsTopicSubscription](SnsTopicSubscription.md)
* [Terraform::AWS::SnsTopic](SnsTopic.md)
* [Terraform::AWS::SpotDatafeedSubscription](SpotDatafeedSubscription.md)
* [Terraform::AWS::SpotFleetRequest](SpotFleetRequest.md)
* [Terraform::AWS::SpotInstanceRequest](SpotInstanceRequest.md)
* [Terraform::AWS::SqsQueuePolicy](SqsQueuePolicy.md)
* [Terraform::AWS::SqsQueue](SqsQueue.md)
* [Terraform::AWS::SsmActivation](SsmActivation.md)
* [Terraform::AWS::SsmAssociation](SsmAssociation.md)
* [Terraform::AWS::SsmDocument](SsmDocument.md)
* [Terraform::AWS::SsmMaintenanceWindowTarget](SsmMaintenanceWindowTarget.md)
* [Terraform::AWS::SsmMaintenanceWindowTask](SsmMaintenanceWindowTask.md)
* [Terraform::AWS::SsmMaintenanceWindow](SsmMaintenanceWindow.md)
* [Terraform::AWS::SsmParameter](SsmParameter.md)
* [Terraform::AWS::SsmPatchBaseline](SsmPatchBaseline.md)
* [Terraform::AWS::SsmPatchGroup](SsmPatchGroup.md)
* [Terraform::AWS::SsmResourceDataSync](SsmResourceDataSync.md)
* [Terraform::AWS::StoragegatewayCache](StoragegatewayCache.md)
* [Terraform::AWS::StoragegatewayCachedIscsiVolume](StoragegatewayCachedIscsiVolume.md)
* [Terraform::AWS::StoragegatewayGateway](StoragegatewayGateway.md)
* [Terraform::AWS::StoragegatewayNfsFileShare](StoragegatewayNfsFileShare.md)
* [Terraform::AWS::StoragegatewaySmbFileShare](StoragegatewaySmbFileShare.md)
* [Terraform::AWS::StoragegatewayUploadBuffer](StoragegatewayUploadBuffer.md)
* [Terraform::AWS::StoragegatewayWorkingStorage](StoragegatewayWorkingStorage.md)
* [Terraform::AWS::Subnet](Subnet.md)
* [Terraform::AWS::SwfDomain](SwfDomain.md)
* [Terraform::AWS::TransferServer](TransferServer.md)
* [Terraform::AWS::TransferSshKey](TransferSshKey.md)
* [Terraform::AWS::TransferUser](TransferUser.md)
* [Terraform::AWS::VolumeAttachment](VolumeAttachment.md)
* [Terraform::AWS::VpcDhcpOptionsAssociation](VpcDhcpOptionsAssociation.md)
* [Terraform::AWS::VpcDhcpOptions](VpcDhcpOptions.md)
* [Terraform::AWS::VpcEndpointConnectionNotification](VpcEndpointConnectionNotification.md)
* [Terraform::AWS::VpcEndpointRouteTableAssociation](VpcEndpointRouteTableAssociation.md)
* [Terraform::AWS::VpcEndpointServiceAllowedPrincipal](VpcEndpointServiceAllowedPrincipal.md)
* [Terraform::AWS::VpcEndpointService](VpcEndpointService.md)
* [Terraform::AWS::VpcEndpointSubnetAssociation](VpcEndpointSubnetAssociation.md)
* [Terraform::AWS::VpcEndpoint](VpcEndpoint.md)
* [Terraform::AWS::VpcIpv4CidrBlockAssociation](VpcIpv4CidrBlockAssociation.md)
* [Terraform::AWS::VpcPeeringConnectionAccepter](VpcPeeringConnectionAccepter.md)
* [Terraform::AWS::VpcPeeringConnectionOptions](VpcPeeringConnectionOptions.md)
* [Terraform::AWS::VpcPeeringConnection](VpcPeeringConnection.md)
* [Terraform::AWS::Vpc](Vpc.md)
* [Terraform::AWS::VpnConnectionRoute](VpnConnectionRoute.md)
* [Terraform::AWS::VpnConnection](VpnConnection.md)
* [Terraform::AWS::VpnGatewayAttachment](VpnGatewayAttachment.md)
* [Terraform::AWS::VpnGatewayRoutePropagation](VpnGatewayRoutePropagation.md)
* [Terraform::AWS::VpnGateway](VpnGateway.md)
* [Terraform::AWS::WafByteMatchSet](WafByteMatchSet.md)
* [Terraform::AWS::WafGeoMatchSet](WafGeoMatchSet.md)
* [Terraform::AWS::WafIpset](WafIpset.md)
* [Terraform::AWS::WafRateBasedRule](WafRateBasedRule.md)
* [Terraform::AWS::WafRegexMatchSet](WafRegexMatchSet.md)
* [Terraform::AWS::WafRegexPatternSet](WafRegexPatternSet.md)
* [Terraform::AWS::WafRuleGroup](WafRuleGroup.md)
* [Terraform::AWS::WafRule](WafRule.md)
* [Terraform::AWS::WafSizeConstraintSet](WafSizeConstraintSet.md)
* [Terraform::AWS::WafSqlInjectionMatchSet](WafSqlInjectionMatchSet.md)
* [Terraform::AWS::WafWebAcl](WafWebAcl.md)
* [Terraform::AWS::WafXssMatchSet](WafXssMatchSet.md)
* [Terraform::AWS::WafregionalByteMatchSet](WafregionalByteMatchSet.md)
* [Terraform::AWS::WafregionalGeoMatchSet](WafregionalGeoMatchSet.md)
* [Terraform::AWS::WafregionalIpset](WafregionalIpset.md)
* [Terraform::AWS::WafregionalRateBasedRule](WafregionalRateBasedRule.md)
* [Terraform::AWS::WafregionalRegexMatchSet](WafregionalRegexMatchSet.md)
* [Terraform::AWS::WafregionalRegexPatternSet](WafregionalRegexPatternSet.md)
* [Terraform::AWS::WafregionalRuleGroup](WafregionalRuleGroup.md)
* [Terraform::AWS::WafregionalRule](WafregionalRule.md)
* [Terraform::AWS::WafregionalSizeConstraintSet](WafregionalSizeConstraintSet.md)
* [Terraform::AWS::WafregionalSqlInjectionMatchSet](WafregionalSqlInjectionMatchSet.md)
* [Terraform::AWS::WafregionalWebAclAssociation](WafregionalWebAclAssociation.md)
* [Terraform::AWS::WafregionalWebAcl](WafregionalWebAcl.md)
* [Terraform::AWS::WafregionalXssMatchSet](WafregionalXssMatchSet.md)
* [Terraform::AWS::WorklinkFleet](WorklinkFleet.md)