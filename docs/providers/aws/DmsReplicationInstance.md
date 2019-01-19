# Terraform::AWS::DmsReplicationInstance

Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.

## Properties

`AllocatedStorage` - (Optional, Default: 50, Min: 5, Max: 6144) The amount of storage (in gigabytes) to be initially allocated for the replication instance.

`ApplyImmediately` - (Optional, Default: false) Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.

`AutoMinorVersionUpgrade` - (Optional, Default: false) Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.

`AvailabilityZone` - (Optional) The EC2 Availability Zone that the replication instance will be created in.

`EngineVersion` - (Optional) The engine version number of the replication instance.

`KmsKeyArn` - (Optional) The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `KmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.

`MultiAz` - (Optional) Specifies if the replication instance is a multi-az deployment. You cannot set the `AvailabilityZone` parameter if the `MultiAz` parameter is set to `true`.

`PreferredMaintenanceWindow` - (Optional) The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

`PubliclyAccessible` - (Optional, Default: false) Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.

`ReplicationInstanceClass` - (Required) The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge`.

`ReplicationInstanceId` - (Required) The replication instance identifier. This parameter is stored as a lowercase string.

`ReplicationSubnetGroupId` - (Optional) A subnet group to associate with the replication instance.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`VpcSecurityGroupIds` - (Optional) A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.


## Return Values

### Fn::GetAtt

`ReplicationInstanceArn` - The Amazon Resource Name (ARN) of the replication instance.

`ReplicationInstancePrivateIps` -  A list of the private IP addresses of the replication instance.

`ReplicationInstancePublicIps` - A list of the public IP addresses of the replication instance.

## See Also

* [aws_dms_replication_instance](https://www.terraform.io/docs/providers/aws/r/dms_replication_instance.html) in the _Terraform Provider Documentation_