# Terraform::AWS::DaxCluster

Provides a DAX Cluster resource.

## Properties

`IamRoleArn` - (Required) A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.

`AvailabilityZones` - (Optional) List of Availability Zones in which the nodes will be created.

`ServerSideEncryption` - (Optional) Encrypt at rest options.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Enabled` - (Optional) Whether to enable encryption at rest. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the DAX cluster.

`Nodes` - List of node objects including `id`, `address`, `port` and.

`ConfigurationEndpoint` - The configuration endpoint for this DAX cluster,.

`ClusterAddress` - The DNS name of the DAX cluster without the port appended.

`Port` - The port used by the configuration endpoint.

## See Also

* [aws_dax_cluster](https://www.terraform.io/docs/providers/aws/r/dax_cluster.html) in the _Terraform Provider Documentation_