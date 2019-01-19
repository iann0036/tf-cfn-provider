# Terraform::AWS::DaxCluster

Provides a DAX Cluster resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - The ARN of the DAX cluster.

`Nodes` - List of node objects including `id`, `address`, `port` and.

`ConfigurationEndpoint` - The configuration endpoint for this DAX cluster,.

`ClusterAddress` - The DNS name of the DAX cluster without the port appended.

`Port` - The port used by the configuration endpoint.

## See Also

* [aws_dax_cluster](https://www.terraform.io/docs/providers/aws/r/dax_cluster.html) in the _Terraform Provider Documentation_