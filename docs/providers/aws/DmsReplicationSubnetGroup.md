# Terraform::AWS::DmsReplicationSubnetGroup

Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.

## Properties

`ReplicationSubnetGroupDescription` - (Required) The description for the subnet group.

`ReplicationSubnetGroupId` - (Required) The name for the replication subnet group. This value is stored as a lowercase string.

`SubnetIds` - (Required) A list of the EC2 subnet IDs for the subnet group.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`VpcId` - The ID of the VPC the subnet group is in.

## See Also

* [aws_dms_replication_subnet_group](https://www.terraform.io/docs/providers/aws/r/dms_replication_subnet_group.html) in the _Terraform Provider Documentation_