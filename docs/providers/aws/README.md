# AWS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/aws**. The below arguments may be included as the key/value or JSON properties in the secret:

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

