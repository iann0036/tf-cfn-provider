# Terraform::AWS::NeptuneClusterInstance

A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.

You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `instance_class` sizes.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Address` - The hostname of the instance. See also `endpoint` and `port`.

`Arn` - Amazon Resource Name (ARN) of neptune instance.

`DbiResourceId` - The region-unique, immutable identifier for the neptune instance.

`Endpoint` - The connection endpoint in `address:port` format.

`Id` - The Instance identifier.

`KmsKeyArn` - The ARN for the KMS encryption key if one is set to the neptune cluster.

`StorageEncrypted` - Specifies whether the neptune cluster is encrypted.

## See Also

* [aws_neptune_cluster_instance](https://www.terraform.io/docs/providers/aws/r/neptune_cluster_instance.html) in the _Terraform Provider Documentation_