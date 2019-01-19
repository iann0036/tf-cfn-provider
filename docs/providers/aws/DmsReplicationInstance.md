# Terraform::AWS::DmsReplicationInstance

Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ReplicationInstanceArn` - The Amazon Resource Name (ARN) of the replication instance.

`ReplicationInstancePrivateIps` -  A list of the private IP addresses of the replication instance.

`ReplicationInstancePublicIps` - A list of the public IP addresses of the replication instance.

## See Also

* [aws_dms_replication_instance](https://www.terraform.io/docs/providers/aws/r/dms_replication_instance.html) in the _Terraform Provider Documentation_