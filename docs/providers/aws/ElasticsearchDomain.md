# Terraform::AWS::ElasticsearchDomain

Manages an AWS Elasticsearch Domain.

## Properties

`DomainName` - (Required) Name of the domain.

`AccessPolicies` - (Optional) IAM policy document specifying the access policies for the domain.

`AdvancedOptions` - (Optional) Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing Terraform to want to recreate your Elasticsearch
domain on every apply.

`EbsOptions` - (Optional) EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.

`EncryptAtRest` - (Optional) Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.

`NodeToNodeEncryption` - (Optional) Node-to-node encryption options. See below.

`ClusterConfig` - (Optional) Cluster configuration of the domain, see below.

`SnapshotOptions` - (Optional) Snapshot related options, see below.

`VpcOptions` - (Optional) VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).

`LogPublishingOptions` - (Optional) Options for publishing slow logs to CloudWatch Logs.

`ElasticsearchVersion` - (Optional) The version of Elasticsearch to deploy. Defaults to `1.5`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`EbsEnabled` - (Required) Whether EBS volumes are attached to data nodes in the domain.

`VolumeType` - (Optional) The type of EBS volumes attached to data nodes.

`VolumeSize` - The size of EBS volumes attached to data nodes (in GB).
**Required** if `EbsEnabled` is set to `true`.

`Iops` - (Optional) The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.

`Enabled` - (Required) Whether to enable encryption at rest. If the `EncryptAtRest` block is not provided then this defaults to `false`.

`KmsKeyId` - (Optional) The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.

`InstanceType` - (Optional) Instance type of data nodes in the cluster.

`InstanceCount` - (Optional) Number of instances in the cluster.

`DedicatedMasterEnabled` - (Optional) Indicates whether dedicated master nodes are enabled for the cluster.

`DedicatedMasterType` - (Optional) Instance type of the dedicated master nodes in the cluster.

`DedicatedMasterCount` - (Optional) Number of dedicated master nodes in the cluster.

`ZoneAwarenessEnabled` - (Optional) Indicates whether zone awareness is enabled.

`Enabled` - (Required) Whether to enable node-to-node encryption. If the `NodeToNodeEncryption` block is not provided then this defaults to `false`.

`SecurityGroupIds` - (Optional) List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.

`SubnetIds` - (Required) List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.

`AutomatedSnapshotStartHour` - (Required) Hour during which the service takes an automated daily
snapshot of the indices in the domain.

`LogType` - (Required) A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS.

`CloudwatchLogGroupArn` - (Required) ARN of the Cloudwatch log group to which log needs to be published.

`Enabled` - (Optional, Default: true) Specifies whether given log publishing option is enabled or not.

`Enabled` - (Optional, Default: false) Specifies whether Amazon Cognito authentication with Kibana is enabled or not.

`UserPoolId` - (Required) ID of the Cognito User Pool to use.

`IdentityPoolId` - (Required) ID of the Cognito Identity Pool to use.

`RoleArn` - (Required) ARN of the IAM role that has the AmazonESCognitoAccess policy attached.


## Return Values

### Fn::GetAtt

`Endpoint` - Domain-specific endpoint used to submit index, search, and data upload requests.

`VpcOptions.0.availabilityZones` - If the domain was created inside a VPC, the names of the availability zones the configured `SubnetIds` were created inside.

`DomainName` - The name of the Elasticsearch domain.

`VpcOptions.0.vpcId` - If the domain was created inside a VPC, the ID of the VPC.

`KibanaEndpoint` - Domain-specific endpoint for kibana without https scheme.

`DomainId` - Unique identifier for the domain.

`Arn` - Amazon Resource Name (ARN) of the domain.

## See Also

* [aws_elasticsearch_domain](https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain.html) in the _Terraform Provider Documentation_