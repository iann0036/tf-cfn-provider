# AWS Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/aws**. The below arguments may be included as the key/value or JSON properties in the secret:

* `access_key` - (Optional) This is the AWS access key. It must be provided, but
  it can also be sourced from the `AWS_ACCESS_KEY_ID` environment variable, or via
  a shared credentials file if `profile` is specified.

* `secret_key` - (Optional) This is the AWS secret key. It must be provided, but
  it can also be sourced from the `AWS_SECRET_ACCESS_KEY` environment variable, or
  via a shared credentials file if `profile` is specified.

* `region` - (Required) This is the AWS region. It must be provided, but
  it can also be sourced from the `AWS_DEFAULT_REGION` environment variables, or
  via a shared credentials file if `profile` is specified.

* `profile` - (Optional) This is the AWS profile name as set in the shared credentials
  file.

* `assume_role` - (Optional) An `assume_role` block (documented below). Only one
  `assume_role` block may be in the configuration.

* `shared_credentials_file` = (Optional) This is the path to the shared credentials file.
  If this is not set and a profile is specified, `~/.aws/credentials` will be used.

* `token` - (Optional) Use this to set an MFA token. It can also be sourced
  from the `AWS_SESSION_TOKEN` environment variable.

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
  - [`aws_api_gateway_deployment` resource](/docs/providers/aws/r/api_gateway_deployment.html)
  - [`aws_api_gateway_rest_api` resource](/docs/providers/aws/r/api_gateway_rest_api.html)
  - [`aws_api_gateway_stage` resource](/docs/providers/aws/r/api_gateway_stage.html)
  - [`aws_budgets_budget` resource](/docs/providers/aws/r/budgets_budget.html)
  - [`aws_cognito_identity_pool` resource](/docs/providers/aws/r/cognito_identity_pool.html)
  - [`aws_cognito_user_pool` resource](/docs/providers/aws/r/cognito_user_pool.html)
  - [`aws_cognito_user_pools` data source](/docs/providers/aws/d/cognito_user_pools.html)
  - [`aws_dms_replication_subnet_group` resource](/docs/providers/aws/r/dms_replication_subnet_group.html)
  - [`aws_dx_connection` resource](/docs/providers/aws/r/dx_connection.html)
  - [`aws_dx_hosted_private_virtual_interface_accepter` resource](/docs/providers/aws/r/dx_hosted_private_virtual_interface_accepter.html)
  - [`aws_dx_hosted_private_virtual_interface` resource](/docs/providers/aws/r/dx_hosted_private_virtual_interface.html)
  - [`aws_dx_hosted_public_virtual_interface_accepter` resource](/docs/providers/aws/r/dx_hosted_public_virtual_interface_accepter.html)
  - [`aws_dx_hosted_public_virtual_interface` resource](/docs/providers/aws/r/dx_hosted_public_virtual_interface.html)
  - [`aws_dx_lag` resource](/docs/providers/aws/r/dx_lag.html)
  - [`aws_dx_private_virtual_interface` resource](/docs/providers/aws/r/dx_private_virtual_interface.html)
  - [`aws_dx_public_virtual_interface` resource](/docs/providers/aws/r/dx_public_virtual_interface.html)
  - [`aws_ebs_volume` data source](/docs/providers/aws/d/ebs_volume.html)
  - [`aws_ecs_cluster` resource (import)](/docs/providers/aws/r/ecs_cluster.html)
  - [`aws_ecs_service` resource (import)](/docs/providers/aws/r/ecs_service.html)
  - [`aws_efs_file_system` data source](/docs/providers/aws/d/efs_file_system.html)
  - [`aws_efs_file_system` resource](/docs/providers/aws/r/efs_file_system.html)
  - [`aws_efs_mount_target` data source](/docs/providers/aws/d/efs_mount_target.html)
  - [`aws_efs_mount_target` resource](/docs/providers/aws/r/efs_mount_target.html)
  - [`aws_elasticache_cluster` data source](/docs/providers/aws/d/elasticache_cluster.html)
  - [`aws_elasticache_cluster` resource](/docs/providers/aws/r/elasticache_cluster.html)
  - [`aws_elb` resource](/docs/providers/aws/r/elb.html)
  - [`aws_instance` data source](/docs/providers/aws/d/instance.html)
  - [`aws_instance` resource](/docs/providers/aws/r/instance.html)
  - [`aws_launch_template` resource](/docs/providers/aws/r/launch_template.html)
  - [`aws_redshift_cluster` resource](/docs/providers/aws/r/redshift_cluster.html)
  - [`aws_redshift_subnet_group` resource](/docs/providers/aws/r/redshift_subnet_group.html)
  - [`aws_s3_account_public_access_block` resource](/docs/providers/aws/r/s3_account_public_access_block.html)
  - [`aws_ses_domain_identity_verification` resource](/docs/providers/aws/r/ses_domain_identity_verification.html)
  - [`aws_ses_domain_identity` resource](/docs/providers/aws/r/ses_domain_identity.html)
  - [`aws_ssm_document` resource](/docs/providers/aws/r/ssm_document.html)
  - [`aws_ssm_parameter` resource](/docs/providers/aws/r/ssm_parameter.html)
  - [`aws_vpc` data source](/docs/providers/aws/d/vpc.html)
  - [`aws_vpc` resource](/docs/providers/aws/r/vpc.html)
  - [`aws_waf_ipset` resource](/docs/providers/aws/r/waf_ipset.html)
  - [`aws_wafregional_ipset` resource](/docs/providers/aws/r/wafregional_ipset.html)

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

* [Terraform::AWS::AcmCertificateValidation](docs/providers/aws/AcmCertificateValidation.md)
* [Terraform::AWS::AcmCertificate](docs/providers/aws/AcmCertificate.md)
* [Terraform::AWS::AcmpcaCertificateAuthority](docs/providers/aws/AcmpcaCertificateAuthority.md)
* [Terraform::AWS::AmiCopy](docs/providers/aws/AmiCopy.md)
* [Terraform::AWS::AmiFromInstance](docs/providers/aws/AmiFromInstance.md)
* [Terraform::AWS::AmiLaunchPermission](docs/providers/aws/AmiLaunchPermission.md)
* [Terraform::AWS::Ami](docs/providers/aws/Ami.md)
* [Terraform::AWS::ApiGatewayAccount](docs/providers/aws/ApiGatewayAccount.md)
* [Terraform::AWS::ApiGatewayApiKey](docs/providers/aws/ApiGatewayApiKey.md)
* [Terraform::AWS::ApiGatewayAuthorizer](docs/providers/aws/ApiGatewayAuthorizer.md)
* [Terraform::AWS::ApiGatewayBasePathMapping](docs/providers/aws/ApiGatewayBasePathMapping.md)
* [Terraform::AWS::ApiGatewayClientCertificate](docs/providers/aws/ApiGatewayClientCertificate.md)
* [Terraform::AWS::ApiGatewayDeployment](docs/providers/aws/ApiGatewayDeployment.md)
* [Terraform::AWS::ApiGatewayDocumentationPart](docs/providers/aws/ApiGatewayDocumentationPart.md)
* [Terraform::AWS::ApiGatewayDocumentationVersion](docs/providers/aws/ApiGatewayDocumentationVersion.md)
* [Terraform::AWS::ApiGatewayDomainName](docs/providers/aws/ApiGatewayDomainName.md)
* [Terraform::AWS::ApiGatewayGatewayResponse](docs/providers/aws/ApiGatewayGatewayResponse.md)
* [Terraform::AWS::ApiGatewayIntegrationResponse](docs/providers/aws/ApiGatewayIntegrationResponse.md)
* [Terraform::AWS::ApiGatewayIntegration](docs/providers/aws/ApiGatewayIntegration.md)
* [Terraform::AWS::ApiGatewayMethodResponse](docs/providers/aws/ApiGatewayMethodResponse.md)
* [Terraform::AWS::ApiGatewayMethodSettings](docs/providers/aws/ApiGatewayMethodSettings.md)
* [Terraform::AWS::ApiGatewayMethod](docs/providers/aws/ApiGatewayMethod.md)
* [Terraform::AWS::ApiGatewayModel](docs/providers/aws/ApiGatewayModel.md)
* [Terraform::AWS::ApiGatewayRequestValidator](docs/providers/aws/ApiGatewayRequestValidator.md)
* [Terraform::AWS::ApiGatewayResource](docs/providers/aws/ApiGatewayResource.md)
* [Terraform::AWS::ApiGatewayRestApi](docs/providers/aws/ApiGatewayRestApi.md)
* [Terraform::AWS::ApiGatewayStage](docs/providers/aws/ApiGatewayStage.md)
* [Terraform::AWS::ApiGatewayUsagePlanKey](docs/providers/aws/ApiGatewayUsagePlanKey.md)
* [Terraform::AWS::ApiGatewayUsagePlan](docs/providers/aws/ApiGatewayUsagePlan.md)
* [Terraform::AWS::ApiGatewayVpcLink](docs/providers/aws/ApiGatewayVpcLink.md)
* [Terraform::AWS::AppCookieStickinessPolicy](docs/providers/aws/AppCookieStickinessPolicy.md)
* [Terraform::AWS::AppautoscalingPolicy](docs/providers/aws/AppautoscalingPolicy.md)
* [Terraform::AWS::AppautoscalingScheduledAction](docs/providers/aws/AppautoscalingScheduledAction.md)
* [Terraform::AWS::AppautoscalingTarget](docs/providers/aws/AppautoscalingTarget.md)
* [Terraform::AWS::AppmeshMesh](docs/providers/aws/AppmeshMesh.md)
* [Terraform::AWS::AppmeshRoute](docs/providers/aws/AppmeshRoute.md)
* [Terraform::AWS::AppmeshVirtualNode](docs/providers/aws/AppmeshVirtualNode.md)
* [Terraform::AWS::AppmeshVirtualRouter](docs/providers/aws/AppmeshVirtualRouter.md)
* [Terraform::AWS::AppsyncApiKey](docs/providers/aws/AppsyncApiKey.md)
* [Terraform::AWS::AppsyncDatasource](docs/providers/aws/AppsyncDatasource.md)
* [Terraform::AWS::AppsyncGraphqlApi](docs/providers/aws/AppsyncGraphqlApi.md)
* [Terraform::AWS::AthenaDatabase](docs/providers/aws/AthenaDatabase.md)
* [Terraform::AWS::AthenaNamedQuery](docs/providers/aws/AthenaNamedQuery.md)
* [Terraform::AWS::AutoscalingAttachment](docs/providers/aws/AutoscalingAttachment.md)
* [Terraform::AWS::AutoscalingGroup](docs/providers/aws/AutoscalingGroup.md)
* [Terraform::AWS::AutoscalingLifecycleHook](docs/providers/aws/AutoscalingLifecycleHook.md)
* [Terraform::AWS::AutoscalingNotification](docs/providers/aws/AutoscalingNotification.md)
* [Terraform::AWS::AutoscalingPolicy](docs/providers/aws/AutoscalingPolicy.md)
* [Terraform::AWS::AutoscalingSchedule](docs/providers/aws/AutoscalingSchedule.md)
* [Terraform::AWS::BatchComputeEnvironment](docs/providers/aws/BatchComputeEnvironment.md)
* [Terraform::AWS::BatchJobDefinition](docs/providers/aws/BatchJobDefinition.md)
* [Terraform::AWS::BatchJobQueue](docs/providers/aws/BatchJobQueue.md)
* [Terraform::AWS::BudgetsBudget](docs/providers/aws/BudgetsBudget.md)
* [Terraform::AWS::Cloud9EnvironmentEc2](docs/providers/aws/Cloud9EnvironmentEc2.md)
* [Terraform::AWS::CloudformationStack](docs/providers/aws/CloudformationStack.md)
* [Terraform::AWS::CloudfrontDistribution](docs/providers/aws/CloudfrontDistribution.md)
* [Terraform::AWS::CloudfrontOriginAccessIdentity](docs/providers/aws/CloudfrontOriginAccessIdentity.md)
* [Terraform::AWS::CloudfrontPublicKey](docs/providers/aws/CloudfrontPublicKey.md)
* [Terraform::AWS::CloudhsmV2Cluster](docs/providers/aws/CloudhsmV2Cluster.md)
* [Terraform::AWS::CloudhsmV2Hsm](docs/providers/aws/CloudhsmV2Hsm.md)
* [Terraform::AWS::Cloudtrail](docs/providers/aws/Cloudtrail.md)
* [Terraform::AWS::CloudwatchDashboard](docs/providers/aws/CloudwatchDashboard.md)
* [Terraform::AWS::CloudwatchEventPermission](docs/providers/aws/CloudwatchEventPermission.md)
* [Terraform::AWS::CloudwatchEventRule](docs/providers/aws/CloudwatchEventRule.md)
* [Terraform::AWS::CloudwatchEventTarget](docs/providers/aws/CloudwatchEventTarget.md)
* [Terraform::AWS::CloudwatchLogDestinationPolicy](docs/providers/aws/CloudwatchLogDestinationPolicy.md)
* [Terraform::AWS::CloudwatchLogDestination](docs/providers/aws/CloudwatchLogDestination.md)
* [Terraform::AWS::CloudwatchLogGroup](docs/providers/aws/CloudwatchLogGroup.md)
* [Terraform::AWS::CloudwatchLogMetricFilter](docs/providers/aws/CloudwatchLogMetricFilter.md)
* [Terraform::AWS::CloudwatchLogResourcePolicy](docs/providers/aws/CloudwatchLogResourcePolicy.md)
* [Terraform::AWS::CloudwatchLogStream](docs/providers/aws/CloudwatchLogStream.md)
* [Terraform::AWS::CloudwatchLogSubscriptionFilter](docs/providers/aws/CloudwatchLogSubscriptionFilter.md)
* [Terraform::AWS::CloudwatchMetricAlarm](docs/providers/aws/CloudwatchMetricAlarm.md)
* [Terraform::AWS::CodebuildProject](docs/providers/aws/CodebuildProject.md)
* [Terraform::AWS::CodebuildWebhook](docs/providers/aws/CodebuildWebhook.md)
* [Terraform::AWS::CodecommitRepository](docs/providers/aws/CodecommitRepository.md)
* [Terraform::AWS::CodecommitTrigger](docs/providers/aws/CodecommitTrigger.md)
* [Terraform::AWS::CodedeployApp](docs/providers/aws/CodedeployApp.md)
* [Terraform::AWS::CodedeployDeploymentConfig](docs/providers/aws/CodedeployDeploymentConfig.md)
* [Terraform::AWS::CodedeployDeploymentGroup](docs/providers/aws/CodedeployDeploymentGroup.md)
* [Terraform::AWS::CodepipelineWebhook](docs/providers/aws/CodepipelineWebhook.md)
* [Terraform::AWS::Codepipeline](docs/providers/aws/Codepipeline.md)
* [Terraform::AWS::CognitoIdentityPoolRolesAttachment](docs/providers/aws/CognitoIdentityPoolRolesAttachment.md)
* [Terraform::AWS::CognitoIdentityPool](docs/providers/aws/CognitoIdentityPool.md)
* [Terraform::AWS::CognitoIdentityProvider](docs/providers/aws/CognitoIdentityProvider.md)
* [Terraform::AWS::CognitoResourceServer](docs/providers/aws/CognitoResourceServer.md)
* [Terraform::AWS::CognitoUserGroup](docs/providers/aws/CognitoUserGroup.md)
* [Terraform::AWS::CognitoUserPoolClient](docs/providers/aws/CognitoUserPoolClient.md)
* [Terraform::AWS::CognitoUserPoolDomain](docs/providers/aws/CognitoUserPoolDomain.md)
* [Terraform::AWS::CognitoUserPool](docs/providers/aws/CognitoUserPool.md)
* [Terraform::AWS::ConfigAggregateAuthorization](docs/providers/aws/ConfigAggregateAuthorization.md)
* [Terraform::AWS::ConfigConfigRule](docs/providers/aws/ConfigConfigRule.md)
* [Terraform::AWS::ConfigConfigurationAggregator](docs/providers/aws/ConfigConfigurationAggregator.md)
* [Terraform::AWS::ConfigConfigurationRecorderStatus](docs/providers/aws/ConfigConfigurationRecorderStatus.md)
* [Terraform::AWS::ConfigConfigurationRecorder](docs/providers/aws/ConfigConfigurationRecorder.md)
* [Terraform::AWS::ConfigDeliveryChannel](docs/providers/aws/ConfigDeliveryChannel.md)
* [Terraform::AWS::CustomerGateway](docs/providers/aws/CustomerGateway.md)
* [Terraform::AWS::DatasyncAgent](docs/providers/aws/DatasyncAgent.md)
* [Terraform::AWS::DatasyncLocationEfs](docs/providers/aws/DatasyncLocationEfs.md)
* [Terraform::AWS::DatasyncLocationNfs](docs/providers/aws/DatasyncLocationNfs.md)
* [Terraform::AWS::DatasyncLocationS3](docs/providers/aws/DatasyncLocationS3.md)
* [Terraform::AWS::DatasyncTask](docs/providers/aws/DatasyncTask.md)
* [Terraform::AWS::DaxCluster](docs/providers/aws/DaxCluster.md)
* [Terraform::AWS::DaxParameterGroup](docs/providers/aws/DaxParameterGroup.md)
* [Terraform::AWS::DaxSubnetGroup](docs/providers/aws/DaxSubnetGroup.md)
* [Terraform::AWS::DbClusterSnapshot](docs/providers/aws/DbClusterSnapshot.md)
* [Terraform::AWS::DbEventSubscription](docs/providers/aws/DbEventSubscription.md)
* [Terraform::AWS::DbInstance](docs/providers/aws/DbInstance.md)
* [Terraform::AWS::DbOptionGroup](docs/providers/aws/DbOptionGroup.md)
* [Terraform::AWS::DbParameterGroup](docs/providers/aws/DbParameterGroup.md)
* [Terraform::AWS::DbSecurityGroup](docs/providers/aws/DbSecurityGroup.md)
* [Terraform::AWS::DbSnapshot](docs/providers/aws/DbSnapshot.md)
* [Terraform::AWS::DbSubnetGroup](docs/providers/aws/DbSubnetGroup.md)
* [Terraform::AWS::DefaultNetworkAcl](docs/providers/aws/DefaultNetworkAcl.md)
* [Terraform::AWS::DefaultRouteTable](docs/providers/aws/DefaultRouteTable.md)
* [Terraform::AWS::DefaultSecurityGroup](docs/providers/aws/DefaultSecurityGroup.md)
* [Terraform::AWS::DefaultSubnet](docs/providers/aws/DefaultSubnet.md)
* [Terraform::AWS::DefaultVpc](docs/providers/aws/DefaultVpc.md)
* [Terraform::AWS::DevicefarmProject](docs/providers/aws/DevicefarmProject.md)
* [Terraform::AWS::DirectoryServiceConditionalForwarder](docs/providers/aws/DirectoryServiceConditionalForwarder.md)
* [Terraform::AWS::DirectoryServiceDirectory](docs/providers/aws/DirectoryServiceDirectory.md)
* [Terraform::AWS::DlmLifecyclePolicy](docs/providers/aws/DlmLifecyclePolicy.md)
* [Terraform::AWS::DmsCertificate](docs/providers/aws/DmsCertificate.md)
* [Terraform::AWS::DmsEndpoint](docs/providers/aws/DmsEndpoint.md)
* [Terraform::AWS::DmsReplicationInstance](docs/providers/aws/DmsReplicationInstance.md)
* [Terraform::AWS::DmsReplicationSubnetGroup](docs/providers/aws/DmsReplicationSubnetGroup.md)
* [Terraform::AWS::DmsReplicationTask](docs/providers/aws/DmsReplicationTask.md)
* [Terraform::AWS::DocdbClusterParameterGroup](docs/providers/aws/DocdbClusterParameterGroup.md)
* [Terraform::AWS::DocdbSubnetGroup](docs/providers/aws/DocdbSubnetGroup.md)
* [Terraform::AWS::DxBgpPeer](docs/providers/aws/DxBgpPeer.md)
* [Terraform::AWS::DxConnectionAssociation](docs/providers/aws/DxConnectionAssociation.md)
* [Terraform::AWS::DxConnection](docs/providers/aws/DxConnection.md)
* [Terraform::AWS::DxGatewayAssociation](docs/providers/aws/DxGatewayAssociation.md)
* [Terraform::AWS::DxGateway](docs/providers/aws/DxGateway.md)
* [Terraform::AWS::DxHostedPrivateVirtualInterfaceAccepter](docs/providers/aws/DxHostedPrivateVirtualInterfaceAccepter.md)
* [Terraform::AWS::DxHostedPrivateVirtualInterface](docs/providers/aws/DxHostedPrivateVirtualInterface.md)
* [Terraform::AWS::DxHostedPublicVirtualInterfaceAccepter](docs/providers/aws/DxHostedPublicVirtualInterfaceAccepter.md)
* [Terraform::AWS::DxHostedPublicVirtualInterface](docs/providers/aws/DxHostedPublicVirtualInterface.md)
* [Terraform::AWS::DxLag](docs/providers/aws/DxLag.md)
* [Terraform::AWS::DxPrivateVirtualInterface](docs/providers/aws/DxPrivateVirtualInterface.md)
* [Terraform::AWS::DxPublicVirtualInterface](docs/providers/aws/DxPublicVirtualInterface.md)
* [Terraform::AWS::DynamodbGlobalTable](docs/providers/aws/DynamodbGlobalTable.md)
* [Terraform::AWS::DynamodbTableItem](docs/providers/aws/DynamodbTableItem.md)
* [Terraform::AWS::DynamodbTable](docs/providers/aws/DynamodbTable.md)
* [Terraform::AWS::EbsSnapshotCopy](docs/providers/aws/EbsSnapshotCopy.md)
* [Terraform::AWS::EbsSnapshot](docs/providers/aws/EbsSnapshot.md)
* [Terraform::AWS::EbsVolume](docs/providers/aws/EbsVolume.md)
* [Terraform::AWS::Ec2CapacityReservation](docs/providers/aws/Ec2CapacityReservation.md)
* [Terraform::AWS::Ec2Fleet](docs/providers/aws/Ec2Fleet.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTableAssociation](docs/providers/aws/Ec2TransitGatewayRouteTableAssociation.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTablePropagation](docs/providers/aws/Ec2TransitGatewayRouteTablePropagation.md)
* [Terraform::AWS::Ec2TransitGatewayRouteTable](docs/providers/aws/Ec2TransitGatewayRouteTable.md)
* [Terraform::AWS::Ec2TransitGatewayRoute](docs/providers/aws/Ec2TransitGatewayRoute.md)
* [Terraform::AWS::Ec2TransitGatewayVpcAttachment](docs/providers/aws/Ec2TransitGatewayVpcAttachment.md)
* [Terraform::AWS::Ec2TransitGateway](docs/providers/aws/Ec2TransitGateway.md)
* [Terraform::AWS::EcrLifecyclePolicy](docs/providers/aws/EcrLifecyclePolicy.md)
* [Terraform::AWS::EcrRepositoryPolicy](docs/providers/aws/EcrRepositoryPolicy.md)
* [Terraform::AWS::EcrRepository](docs/providers/aws/EcrRepository.md)
* [Terraform::AWS::EcsCluster](docs/providers/aws/EcsCluster.md)
* [Terraform::AWS::EcsService](docs/providers/aws/EcsService.md)
* [Terraform::AWS::EcsTaskDefinition](docs/providers/aws/EcsTaskDefinition.md)
* [Terraform::AWS::EfsFileSystem](docs/providers/aws/EfsFileSystem.md)
* [Terraform::AWS::EfsMountTarget](docs/providers/aws/EfsMountTarget.md)
* [Terraform::AWS::EgressOnlyInternetGateway](docs/providers/aws/EgressOnlyInternetGateway.md)
* [Terraform::AWS::EipAssociation](docs/providers/aws/EipAssociation.md)
* [Terraform::AWS::Eip](docs/providers/aws/Eip.md)
* [Terraform::AWS::EksCluster](docs/providers/aws/EksCluster.md)
* [Terraform::AWS::ElasticBeanstalkApplicationVersion](docs/providers/aws/ElasticBeanstalkApplicationVersion.md)
* [Terraform::AWS::ElasticBeanstalkApplication](docs/providers/aws/ElasticBeanstalkApplication.md)
* [Terraform::AWS::ElasticBeanstalkConfigurationTemplate](docs/providers/aws/ElasticBeanstalkConfigurationTemplate.md)
* [Terraform::AWS::ElasticBeanstalkEnvironment](docs/providers/aws/ElasticBeanstalkEnvironment.md)
* [Terraform::AWS::ElasticacheCluster](docs/providers/aws/ElasticacheCluster.md)
* [Terraform::AWS::ElasticacheParameterGroup](docs/providers/aws/ElasticacheParameterGroup.md)
* [Terraform::AWS::ElasticacheReplicationGroup](docs/providers/aws/ElasticacheReplicationGroup.md)
* [Terraform::AWS::ElasticacheSecurityGroup](docs/providers/aws/ElasticacheSecurityGroup.md)
* [Terraform::AWS::ElasticacheSubnetGroup](docs/providers/aws/ElasticacheSubnetGroup.md)
* [Terraform::AWS::ElasticsearchDomainPolicy](docs/providers/aws/ElasticsearchDomainPolicy.md)
* [Terraform::AWS::ElasticsearchDomain](docs/providers/aws/ElasticsearchDomain.md)
* [Terraform::AWS::ElastictranscoderPipeline](docs/providers/aws/ElastictranscoderPipeline.md)
* [Terraform::AWS::ElastictranscoderPreset](docs/providers/aws/ElastictranscoderPreset.md)
* [Terraform::AWS::ElbAttachment](docs/providers/aws/ElbAttachment.md)
* [Terraform::AWS::Elb](docs/providers/aws/Elb.md)
* [Terraform::AWS::EmrCluster](docs/providers/aws/EmrCluster.md)
* [Terraform::AWS::EmrInstanceGroup](docs/providers/aws/EmrInstanceGroup.md)
* [Terraform::AWS::EmrSecurityConfiguration](docs/providers/aws/EmrSecurityConfiguration.md)
* [Terraform::AWS::FlowLog](docs/providers/aws/FlowLog.md)
* [Terraform::AWS::GameliftAlias](docs/providers/aws/GameliftAlias.md)
* [Terraform::AWS::GameliftBuild](docs/providers/aws/GameliftBuild.md)
* [Terraform::AWS::GameliftFleet](docs/providers/aws/GameliftFleet.md)
* [Terraform::AWS::GameliftGameSessionQueue](docs/providers/aws/GameliftGameSessionQueue.md)
* [Terraform::AWS::GlacierVaultLock](docs/providers/aws/GlacierVaultLock.md)
* [Terraform::AWS::GlacierVault](docs/providers/aws/GlacierVault.md)
* [Terraform::AWS::GlobalacceleratorAccelerator](docs/providers/aws/GlobalacceleratorAccelerator.md)
* [Terraform::AWS::GlueCatalogDatabase](docs/providers/aws/GlueCatalogDatabase.md)
* [Terraform::AWS::GlueCatalogTable](docs/providers/aws/GlueCatalogTable.md)
* [Terraform::AWS::GlueClassifier](docs/providers/aws/GlueClassifier.md)
* [Terraform::AWS::GlueConnection](docs/providers/aws/GlueConnection.md)
* [Terraform::AWS::GlueCrawler](docs/providers/aws/GlueCrawler.md)
* [Terraform::AWS::GlueJob](docs/providers/aws/GlueJob.md)
* [Terraform::AWS::GlueSecurityConfiguration](docs/providers/aws/GlueSecurityConfiguration.md)
* [Terraform::AWS::GlueTrigger](docs/providers/aws/GlueTrigger.md)
* [Terraform::AWS::GuarddutyDetector](docs/providers/aws/GuarddutyDetector.md)
* [Terraform::AWS::GuarddutyIpset](docs/providers/aws/GuarddutyIpset.md)
* [Terraform::AWS::GuarddutyMember](docs/providers/aws/GuarddutyMember.md)
* [Terraform::AWS::GuarddutyThreatintelset](docs/providers/aws/GuarddutyThreatintelset.md)
* [Terraform::AWS::IamAccessKey](docs/providers/aws/IamAccessKey.md)
* [Terraform::AWS::IamAccountAlias](docs/providers/aws/IamAccountAlias.md)
* [Terraform::AWS::IamAccountPasswordPolicy](docs/providers/aws/IamAccountPasswordPolicy.md)
* [Terraform::AWS::IamGroupMembership](docs/providers/aws/IamGroupMembership.md)
* [Terraform::AWS::IamGroupPolicyAttachment](docs/providers/aws/IamGroupPolicyAttachment.md)
* [Terraform::AWS::IamGroupPolicy](docs/providers/aws/IamGroupPolicy.md)
* [Terraform::AWS::IamGroup](docs/providers/aws/IamGroup.md)
* [Terraform::AWS::IamInstanceProfile](docs/providers/aws/IamInstanceProfile.md)
* [Terraform::AWS::IamOpenidConnectProvider](docs/providers/aws/IamOpenidConnectProvider.md)
* [Terraform::AWS::IamPolicyAttachment](docs/providers/aws/IamPolicyAttachment.md)
* [Terraform::AWS::IamPolicy](docs/providers/aws/IamPolicy.md)
* [Terraform::AWS::IamRolePolicyAttachment](docs/providers/aws/IamRolePolicyAttachment.md)
* [Terraform::AWS::IamRolePolicy](docs/providers/aws/IamRolePolicy.md)
* [Terraform::AWS::IamRole](docs/providers/aws/IamRole.md)
* [Terraform::AWS::IamSamlProvider](docs/providers/aws/IamSamlProvider.md)
* [Terraform::AWS::IamServerCertificate](docs/providers/aws/IamServerCertificate.md)
* [Terraform::AWS::IamServiceLinkedRole](docs/providers/aws/IamServiceLinkedRole.md)
* [Terraform::AWS::IamUserGroupMembership](docs/providers/aws/IamUserGroupMembership.md)
* [Terraform::AWS::IamUserLoginProfile](docs/providers/aws/IamUserLoginProfile.md)
* [Terraform::AWS::IamUserPolicyAttachment](docs/providers/aws/IamUserPolicyAttachment.md)
* [Terraform::AWS::IamUserPolicy](docs/providers/aws/IamUserPolicy.md)
* [Terraform::AWS::IamUserSshKey](docs/providers/aws/IamUserSshKey.md)
* [Terraform::AWS::IamUser](docs/providers/aws/IamUser.md)
* [Terraform::AWS::InspectorAssessmentTarget](docs/providers/aws/InspectorAssessmentTarget.md)
* [Terraform::AWS::InspectorAssessmentTemplate](docs/providers/aws/InspectorAssessmentTemplate.md)
* [Terraform::AWS::InspectorResourceGroup](docs/providers/aws/InspectorResourceGroup.md)
* [Terraform::AWS::Instance](docs/providers/aws/Instance.md)
* [Terraform::AWS::InternetGateway](docs/providers/aws/InternetGateway.md)
* [Terraform::AWS::IotCertificate](docs/providers/aws/IotCertificate.md)
* [Terraform::AWS::IotPolicyAttachment](docs/providers/aws/IotPolicyAttachment.md)
* [Terraform::AWS::IotPolicy](docs/providers/aws/IotPolicy.md)
* [Terraform::AWS::IotThingPrincipalAttachment](docs/providers/aws/IotThingPrincipalAttachment.md)
* [Terraform::AWS::IotThingType](docs/providers/aws/IotThingType.md)
* [Terraform::AWS::IotThing](docs/providers/aws/IotThing.md)
* [Terraform::AWS::IotTopicRule](docs/providers/aws/IotTopicRule.md)
* [Terraform::AWS::KeyPair](docs/providers/aws/KeyPair.md)
* [Terraform::AWS::KinesisAnalyticsApplication](docs/providers/aws/KinesisAnalyticsApplication.md)
* [Terraform::AWS::KinesisFirehoseDeliveryStream](docs/providers/aws/KinesisFirehoseDeliveryStream.md)
* [Terraform::AWS::KinesisStream](docs/providers/aws/KinesisStream.md)
* [Terraform::AWS::KmsAlias](docs/providers/aws/KmsAlias.md)
* [Terraform::AWS::KmsGrant](docs/providers/aws/KmsGrant.md)
* [Terraform::AWS::KmsKey](docs/providers/aws/KmsKey.md)
* [Terraform::AWS::LambdaAlias](docs/providers/aws/LambdaAlias.md)
* [Terraform::AWS::LambdaEventSourceMapping](docs/providers/aws/LambdaEventSourceMapping.md)
* [Terraform::AWS::LambdaFunction](docs/providers/aws/LambdaFunction.md)
* [Terraform::AWS::LambdaLayerVersion](docs/providers/aws/LambdaLayerVersion.md)
* [Terraform::AWS::LambdaPermission](docs/providers/aws/LambdaPermission.md)
* [Terraform::AWS::LaunchConfiguration](docs/providers/aws/LaunchConfiguration.md)
* [Terraform::AWS::LaunchTemplate](docs/providers/aws/LaunchTemplate.md)
* [Terraform::AWS::LbCookieStickinessPolicy](docs/providers/aws/LbCookieStickinessPolicy.md)
* [Terraform::AWS::LbListenerCertificate](docs/providers/aws/LbListenerCertificate.md)
* [Terraform::AWS::LbListenerRule](docs/providers/aws/LbListenerRule.md)
* [Terraform::AWS::LbListener](docs/providers/aws/LbListener.md)
* [Terraform::AWS::LbSslNegotiationPolicy](docs/providers/aws/LbSslNegotiationPolicy.md)
* [Terraform::AWS::LbTargetGroupAttachment](docs/providers/aws/LbTargetGroupAttachment.md)
* [Terraform::AWS::LbTargetGroup](docs/providers/aws/LbTargetGroup.md)
* [Terraform::AWS::Lb](docs/providers/aws/Lb.md)
* [Terraform::AWS::LicensemanagerAssociation](docs/providers/aws/LicensemanagerAssociation.md)
* [Terraform::AWS::LicensemanagerLicenseConfiguration](docs/providers/aws/LicensemanagerLicenseConfiguration.md)
* [Terraform::AWS::LightsailDomain](docs/providers/aws/LightsailDomain.md)
* [Terraform::AWS::LightsailInstance](docs/providers/aws/LightsailInstance.md)
* [Terraform::AWS::LightsailKeyPair](docs/providers/aws/LightsailKeyPair.md)
* [Terraform::AWS::LightsailStaticIpAttachment](docs/providers/aws/LightsailStaticIpAttachment.md)
* [Terraform::AWS::LightsailStaticIp](docs/providers/aws/LightsailStaticIp.md)
* [Terraform::AWS::LoadBalancerBackendServerPolicy](docs/providers/aws/LoadBalancerBackendServerPolicy.md)
* [Terraform::AWS::LoadBalancerListenerPolicy](docs/providers/aws/LoadBalancerListenerPolicy.md)
* [Terraform::AWS::LoadBalancerPolicy](docs/providers/aws/LoadBalancerPolicy.md)
* [Terraform::AWS::MacieMemberAccountAssociation](docs/providers/aws/MacieMemberAccountAssociation.md)
* [Terraform::AWS::MacieS3BucketAssociation](docs/providers/aws/MacieS3BucketAssociation.md)
* [Terraform::AWS::MainRouteTableAssociation](docs/providers/aws/MainRouteTableAssociation.md)
* [Terraform::AWS::MediaPackageChannel](docs/providers/aws/MediaPackageChannel.md)
* [Terraform::AWS::MediaStoreContainerPolicy](docs/providers/aws/MediaStoreContainerPolicy.md)
* [Terraform::AWS::MediaStoreContainer](docs/providers/aws/MediaStoreContainer.md)
* [Terraform::AWS::MqBroker](docs/providers/aws/MqBroker.md)
* [Terraform::AWS::MqConfiguration](docs/providers/aws/MqConfiguration.md)
* [Terraform::AWS::NatGateway](docs/providers/aws/NatGateway.md)
* [Terraform::AWS::NeptuneClusterInstance](docs/providers/aws/NeptuneClusterInstance.md)
* [Terraform::AWS::NeptuneClusterParameterGroup](docs/providers/aws/NeptuneClusterParameterGroup.md)
* [Terraform::AWS::NeptuneClusterSnapshot](docs/providers/aws/NeptuneClusterSnapshot.md)
* [Terraform::AWS::NeptuneCluster](docs/providers/aws/NeptuneCluster.md)
* [Terraform::AWS::NeptuneEventSubscription](docs/providers/aws/NeptuneEventSubscription.md)
* [Terraform::AWS::NeptuneParameterGroup](docs/providers/aws/NeptuneParameterGroup.md)
* [Terraform::AWS::NeptuneSubnetGroup](docs/providers/aws/NeptuneSubnetGroup.md)
* [Terraform::AWS::NetworkAclRule](docs/providers/aws/NetworkAclRule.md)
* [Terraform::AWS::NetworkAcl](docs/providers/aws/NetworkAcl.md)
* [Terraform::AWS::NetworkInterfaceAttachment](docs/providers/aws/NetworkInterfaceAttachment.md)
* [Terraform::AWS::NetworkInterfaceSgAttachment](docs/providers/aws/NetworkInterfaceSgAttachment.md)
* [Terraform::AWS::NetworkInterface](docs/providers/aws/NetworkInterface.md)
* [Terraform::AWS::OpsworksApplication](docs/providers/aws/OpsworksApplication.md)
* [Terraform::AWS::OpsworksCustomLayer](docs/providers/aws/OpsworksCustomLayer.md)
* [Terraform::AWS::OpsworksGangliaLayer](docs/providers/aws/OpsworksGangliaLayer.md)
* [Terraform::AWS::OpsworksHaproxyLayer](docs/providers/aws/OpsworksHaproxyLayer.md)
* [Terraform::AWS::OpsworksInstance](docs/providers/aws/OpsworksInstance.md)
* [Terraform::AWS::OpsworksJavaAppLayer](docs/providers/aws/OpsworksJavaAppLayer.md)
* [Terraform::AWS::OpsworksMemcachedLayer](docs/providers/aws/OpsworksMemcachedLayer.md)
* [Terraform::AWS::OpsworksMysqlLayer](docs/providers/aws/OpsworksMysqlLayer.md)
* [Terraform::AWS::OpsworksNodejsAppLayer](docs/providers/aws/OpsworksNodejsAppLayer.md)
* [Terraform::AWS::OpsworksPermission](docs/providers/aws/OpsworksPermission.md)
* [Terraform::AWS::OpsworksPhpAppLayer](docs/providers/aws/OpsworksPhpAppLayer.md)
* [Terraform::AWS::OpsworksRailsAppLayer](docs/providers/aws/OpsworksRailsAppLayer.md)
* [Terraform::AWS::OpsworksRdsDbInstance](docs/providers/aws/OpsworksRdsDbInstance.md)
* [Terraform::AWS::OpsworksStack](docs/providers/aws/OpsworksStack.md)
* [Terraform::AWS::OpsworksStaticWebLayer](docs/providers/aws/OpsworksStaticWebLayer.md)
* [Terraform::AWS::OpsworksUserProfile](docs/providers/aws/OpsworksUserProfile.md)
* [Terraform::AWS::OrganizationsAccount](docs/providers/aws/OrganizationsAccount.md)
* [Terraform::AWS::OrganizationsOrganization](docs/providers/aws/OrganizationsOrganization.md)
* [Terraform::AWS::OrganizationsPolicyAttachment](docs/providers/aws/OrganizationsPolicyAttachment.md)
* [Terraform::AWS::OrganizationsPolicy](docs/providers/aws/OrganizationsPolicy.md)
* [Terraform::AWS::PinpointAdmChannel](docs/providers/aws/PinpointAdmChannel.md)
* [Terraform::AWS::PinpointApnsChannel](docs/providers/aws/PinpointApnsChannel.md)
* [Terraform::AWS::PinpointApnsSandboxChannel](docs/providers/aws/PinpointApnsSandboxChannel.md)
* [Terraform::AWS::PinpointApnsVoipChannel](docs/providers/aws/PinpointApnsVoipChannel.md)
* [Terraform::AWS::PinpointApnsVoipSandboxChannel](docs/providers/aws/PinpointApnsVoipSandboxChannel.md)
* [Terraform::AWS::PinpointApp](docs/providers/aws/PinpointApp.md)
* [Terraform::AWS::PinpointBaiduChannel](docs/providers/aws/PinpointBaiduChannel.md)
* [Terraform::AWS::PinpointEmailChannel](docs/providers/aws/PinpointEmailChannel.md)
* [Terraform::AWS::PinpointEventStream](docs/providers/aws/PinpointEventStream.md)
* [Terraform::AWS::PinpointGcmChannel](docs/providers/aws/PinpointGcmChannel.md)
* [Terraform::AWS::PinpointSmsChannel](docs/providers/aws/PinpointSmsChannel.md)
* [Terraform::AWS::PlacementGroup](docs/providers/aws/PlacementGroup.md)
* [Terraform::AWS::ProxyProtocolPolicy](docs/providers/aws/ProxyProtocolPolicy.md)
* [Terraform::AWS::RamResourceShare](docs/providers/aws/RamResourceShare.md)
* [Terraform::AWS::RdsClusterEndpoint](docs/providers/aws/RdsClusterEndpoint.md)
* [Terraform::AWS::RdsClusterInstance](docs/providers/aws/RdsClusterInstance.md)
* [Terraform::AWS::RdsClusterParameterGroup](docs/providers/aws/RdsClusterParameterGroup.md)
* [Terraform::AWS::RdsCluster](docs/providers/aws/RdsCluster.md)
* [Terraform::AWS::RdsGlobalCluster](docs/providers/aws/RdsGlobalCluster.md)
* [Terraform::AWS::RedshiftCluster](docs/providers/aws/RedshiftCluster.md)
* [Terraform::AWS::RedshiftEventSubscription](docs/providers/aws/RedshiftEventSubscription.md)
* [Terraform::AWS::RedshiftParameterGroup](docs/providers/aws/RedshiftParameterGroup.md)
* [Terraform::AWS::RedshiftSecurityGroup](docs/providers/aws/RedshiftSecurityGroup.md)
* [Terraform::AWS::RedshiftSnapshotCopyGrant](docs/providers/aws/RedshiftSnapshotCopyGrant.md)
* [Terraform::AWS::RedshiftSubnetGroup](docs/providers/aws/RedshiftSubnetGroup.md)
* [Terraform::AWS::ResourcegroupsGroup](docs/providers/aws/ResourcegroupsGroup.md)
* [Terraform::AWS::Route53DelegationSet](docs/providers/aws/Route53DelegationSet.md)
* [Terraform::AWS::Route53HealthCheck](docs/providers/aws/Route53HealthCheck.md)
* [Terraform::AWS::Route53QueryLog](docs/providers/aws/Route53QueryLog.md)
* [Terraform::AWS::Route53Record](docs/providers/aws/Route53Record.md)
* [Terraform::AWS::Route53ZoneAssociation](docs/providers/aws/Route53ZoneAssociation.md)
* [Terraform::AWS::Route53Zone](docs/providers/aws/Route53Zone.md)
* [Terraform::AWS::RouteTableAssociation](docs/providers/aws/RouteTableAssociation.md)
* [Terraform::AWS::RouteTable](docs/providers/aws/RouteTable.md)
* [Terraform::AWS::Route](docs/providers/aws/Route.md)
* [Terraform::AWS::S3AccountPublicAccessBlock](docs/providers/aws/S3AccountPublicAccessBlock.md)
* [Terraform::AWS::S3BucketInventory](docs/providers/aws/S3BucketInventory.md)
* [Terraform::AWS::S3BucketMetric](docs/providers/aws/S3BucketMetric.md)
* [Terraform::AWS::S3BucketNotification](docs/providers/aws/S3BucketNotification.md)
* [Terraform::AWS::S3BucketObject](docs/providers/aws/S3BucketObject.md)
* [Terraform::AWS::S3BucketPolicy](docs/providers/aws/S3BucketPolicy.md)
* [Terraform::AWS::S3BucketPublicAccessBlock](docs/providers/aws/S3BucketPublicAccessBlock.md)
* [Terraform::AWS::S3Bucket](docs/providers/aws/S3Bucket.md)
* [Terraform::AWS::SagemakerNotebookInstance](docs/providers/aws/SagemakerNotebookInstance.md)
* [Terraform::AWS::SecretsmanagerSecretVersion](docs/providers/aws/SecretsmanagerSecretVersion.md)
* [Terraform::AWS::SecretsmanagerSecret](docs/providers/aws/SecretsmanagerSecret.md)
* [Terraform::AWS::SecurityGroupRule](docs/providers/aws/SecurityGroupRule.md)
* [Terraform::AWS::SecurityGroup](docs/providers/aws/SecurityGroup.md)
* [Terraform::AWS::SecurityhubAccount](docs/providers/aws/SecurityhubAccount.md)
* [Terraform::AWS::SecurityhubProductSubscription](docs/providers/aws/SecurityhubProductSubscription.md)
* [Terraform::AWS::SecurityhubStandardsSubscription](docs/providers/aws/SecurityhubStandardsSubscription.md)
* [Terraform::AWS::ServiceDiscoveryHttpNamespace](docs/providers/aws/ServiceDiscoveryHttpNamespace.md)
* [Terraform::AWS::ServiceDiscoveryPrivateDnsNamespace](docs/providers/aws/ServiceDiscoveryPrivateDnsNamespace.md)
* [Terraform::AWS::ServiceDiscoveryPublicDnsNamespace](docs/providers/aws/ServiceDiscoveryPublicDnsNamespace.md)
* [Terraform::AWS::ServiceDiscoveryService](docs/providers/aws/ServiceDiscoveryService.md)
* [Terraform::AWS::ServicecatalogPortfolio](docs/providers/aws/ServicecatalogPortfolio.md)
* [Terraform::AWS::SesActiveReceiptRuleSet](docs/providers/aws/SesActiveReceiptRuleSet.md)
* [Terraform::AWS::SesConfigurationSet](docs/providers/aws/SesConfigurationSet.md)
* [Terraform::AWS::SesDomainDkim](docs/providers/aws/SesDomainDkim.md)
* [Terraform::AWS::SesDomainIdentityVerification](docs/providers/aws/SesDomainIdentityVerification.md)
* [Terraform::AWS::SesDomainIdentity](docs/providers/aws/SesDomainIdentity.md)
* [Terraform::AWS::SesDomainMailFrom](docs/providers/aws/SesDomainMailFrom.md)
* [Terraform::AWS::SesEventDestination](docs/providers/aws/SesEventDestination.md)
* [Terraform::AWS::SesReceiptFilter](docs/providers/aws/SesReceiptFilter.md)
* [Terraform::AWS::SesReceiptRuleSet](docs/providers/aws/SesReceiptRuleSet.md)
* [Terraform::AWS::SesReceiptRule](docs/providers/aws/SesReceiptRule.md)
* [Terraform::AWS::SesTemplate](docs/providers/aws/SesTemplate.md)
* [Terraform::AWS::SimpledbDomain](docs/providers/aws/SimpledbDomain.md)
* [Terraform::AWS::SnapshotCreateVolumePermission](docs/providers/aws/SnapshotCreateVolumePermission.md)
* [Terraform::AWS::SnsPlatformApplication](docs/providers/aws/SnsPlatformApplication.md)
* [Terraform::AWS::SnsSmsPreferences](docs/providers/aws/SnsSmsPreferences.md)
* [Terraform::AWS::SnsTopicPolicy](docs/providers/aws/SnsTopicPolicy.md)
* [Terraform::AWS::SnsTopicSubscription](docs/providers/aws/SnsTopicSubscription.md)
* [Terraform::AWS::SnsTopic](docs/providers/aws/SnsTopic.md)
* [Terraform::AWS::SpotDatafeedSubscription](docs/providers/aws/SpotDatafeedSubscription.md)
* [Terraform::AWS::SpotFleetRequest](docs/providers/aws/SpotFleetRequest.md)
* [Terraform::AWS::SpotInstanceRequest](docs/providers/aws/SpotInstanceRequest.md)
* [Terraform::AWS::SqsQueuePolicy](docs/providers/aws/SqsQueuePolicy.md)
* [Terraform::AWS::SqsQueue](docs/providers/aws/SqsQueue.md)
* [Terraform::AWS::SsmActivation](docs/providers/aws/SsmActivation.md)
* [Terraform::AWS::SsmAssociation](docs/providers/aws/SsmAssociation.md)
* [Terraform::AWS::SsmDocument](docs/providers/aws/SsmDocument.md)
* [Terraform::AWS::SsmMaintenanceWindowTarget](docs/providers/aws/SsmMaintenanceWindowTarget.md)
* [Terraform::AWS::SsmMaintenanceWindowTask](docs/providers/aws/SsmMaintenanceWindowTask.md)
* [Terraform::AWS::SsmMaintenanceWindow](docs/providers/aws/SsmMaintenanceWindow.md)
* [Terraform::AWS::SsmParameter](docs/providers/aws/SsmParameter.md)
* [Terraform::AWS::SsmPatchBaseline](docs/providers/aws/SsmPatchBaseline.md)
* [Terraform::AWS::SsmPatchGroup](docs/providers/aws/SsmPatchGroup.md)
* [Terraform::AWS::SsmResourceDataSync](docs/providers/aws/SsmResourceDataSync.md)
* [Terraform::AWS::StoragegatewayCache](docs/providers/aws/StoragegatewayCache.md)
* [Terraform::AWS::StoragegatewayCachedIscsiVolume](docs/providers/aws/StoragegatewayCachedIscsiVolume.md)
* [Terraform::AWS::StoragegatewayGateway](docs/providers/aws/StoragegatewayGateway.md)
* [Terraform::AWS::StoragegatewayNfsFileShare](docs/providers/aws/StoragegatewayNfsFileShare.md)
* [Terraform::AWS::StoragegatewaySmbFileShare](docs/providers/aws/StoragegatewaySmbFileShare.md)
* [Terraform::AWS::StoragegatewayUploadBuffer](docs/providers/aws/StoragegatewayUploadBuffer.md)
* [Terraform::AWS::StoragegatewayWorkingStorage](docs/providers/aws/StoragegatewayWorkingStorage.md)
* [Terraform::AWS::Subnet](docs/providers/aws/Subnet.md)
* [Terraform::AWS::SwfDomain](docs/providers/aws/SwfDomain.md)
* [Terraform::AWS::TransferServer](docs/providers/aws/TransferServer.md)
* [Terraform::AWS::TransferSshKey](docs/providers/aws/TransferSshKey.md)
* [Terraform::AWS::TransferUser](docs/providers/aws/TransferUser.md)
* [Terraform::AWS::VolumeAttachment](docs/providers/aws/VolumeAttachment.md)
* [Terraform::AWS::VpcDhcpOptionsAssociation](docs/providers/aws/VpcDhcpOptionsAssociation.md)
* [Terraform::AWS::VpcDhcpOptions](docs/providers/aws/VpcDhcpOptions.md)
* [Terraform::AWS::VpcEndpointConnectionNotification](docs/providers/aws/VpcEndpointConnectionNotification.md)
* [Terraform::AWS::VpcEndpointRouteTableAssociation](docs/providers/aws/VpcEndpointRouteTableAssociation.md)
* [Terraform::AWS::VpcEndpointServiceAllowedPrincipal](docs/providers/aws/VpcEndpointServiceAllowedPrincipal.md)
* [Terraform::AWS::VpcEndpointService](docs/providers/aws/VpcEndpointService.md)
* [Terraform::AWS::VpcEndpointSubnetAssociation](docs/providers/aws/VpcEndpointSubnetAssociation.md)
* [Terraform::AWS::VpcEndpoint](docs/providers/aws/VpcEndpoint.md)
* [Terraform::AWS::VpcIpv4CidrBlockAssociation](docs/providers/aws/VpcIpv4CidrBlockAssociation.md)
* [Terraform::AWS::VpcPeeringConnectionAccepter](docs/providers/aws/VpcPeeringConnectionAccepter.md)
* [Terraform::AWS::VpcPeeringConnectionOptions](docs/providers/aws/VpcPeeringConnectionOptions.md)
* [Terraform::AWS::VpcPeeringConnection](docs/providers/aws/VpcPeeringConnection.md)
* [Terraform::AWS::Vpc](docs/providers/aws/Vpc.md)
* [Terraform::AWS::VpnConnectionRoute](docs/providers/aws/VpnConnectionRoute.md)
* [Terraform::AWS::VpnConnection](docs/providers/aws/VpnConnection.md)
* [Terraform::AWS::VpnGatewayAttachment](docs/providers/aws/VpnGatewayAttachment.md)
* [Terraform::AWS::VpnGatewayRoutePropagation](docs/providers/aws/VpnGatewayRoutePropagation.md)
* [Terraform::AWS::VpnGateway](docs/providers/aws/VpnGateway.md)
* [Terraform::AWS::WafByteMatchSet](docs/providers/aws/WafByteMatchSet.md)
* [Terraform::AWS::WafGeoMatchSet](docs/providers/aws/WafGeoMatchSet.md)
* [Terraform::AWS::WafIpset](docs/providers/aws/WafIpset.md)
* [Terraform::AWS::WafRateBasedRule](docs/providers/aws/WafRateBasedRule.md)
* [Terraform::AWS::WafRegexMatchSet](docs/providers/aws/WafRegexMatchSet.md)
* [Terraform::AWS::WafRegexPatternSet](docs/providers/aws/WafRegexPatternSet.md)
* [Terraform::AWS::WafRuleGroup](docs/providers/aws/WafRuleGroup.md)
* [Terraform::AWS::WafRule](docs/providers/aws/WafRule.md)
* [Terraform::AWS::WafSizeConstraintSet](docs/providers/aws/WafSizeConstraintSet.md)
* [Terraform::AWS::WafSqlInjectionMatchSet](docs/providers/aws/WafSqlInjectionMatchSet.md)
* [Terraform::AWS::WafWebAcl](docs/providers/aws/WafWebAcl.md)
* [Terraform::AWS::WafXssMatchSet](docs/providers/aws/WafXssMatchSet.md)
* [Terraform::AWS::WafregionalByteMatchSet](docs/providers/aws/WafregionalByteMatchSet.md)
* [Terraform::AWS::WafregionalGeoMatchSet](docs/providers/aws/WafregionalGeoMatchSet.md)
* [Terraform::AWS::WafregionalIpset](docs/providers/aws/WafregionalIpset.md)
* [Terraform::AWS::WafregionalRateBasedRule](docs/providers/aws/WafregionalRateBasedRule.md)
* [Terraform::AWS::WafregionalRegexMatchSet](docs/providers/aws/WafregionalRegexMatchSet.md)
* [Terraform::AWS::WafregionalRegexPatternSet](docs/providers/aws/WafregionalRegexPatternSet.md)
* [Terraform::AWS::WafregionalRuleGroup](docs/providers/aws/WafregionalRuleGroup.md)
* [Terraform::AWS::WafregionalRule](docs/providers/aws/WafregionalRule.md)
* [Terraform::AWS::WafregionalSizeConstraintSet](docs/providers/aws/WafregionalSizeConstraintSet.md)
* [Terraform::AWS::WafregionalSqlInjectionMatchSet](docs/providers/aws/WafregionalSqlInjectionMatchSet.md)
* [Terraform::AWS::WafregionalWebAclAssociation](docs/providers/aws/WafregionalWebAclAssociation.md)
* [Terraform::AWS::WafregionalWebAcl](docs/providers/aws/WafregionalWebAcl.md)
* [Terraform::AWS::WafregionalXssMatchSet](docs/providers/aws/WafregionalXssMatchSet.md)