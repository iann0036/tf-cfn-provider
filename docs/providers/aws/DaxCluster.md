# Terraform::AWS::DaxCluster

Provides a DAX Cluster resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The ARN of the DAX cluster.

`Nodes` - List of node objects including `id`, `address`, `port` and.

`ConfigurationEndpoint` - The configuration endpoint for this DAX cluster,.

`ClusterAddress` - The DNS name of the DAX cluster without the port appended.

`Port` - The port used by the configuration endpoint.

## See Also

* [aws_dax_cluster](https://www.terraform.io/docs/providers/aws/r/dax_cluster.html) in the _Terraform Provider Documentation_