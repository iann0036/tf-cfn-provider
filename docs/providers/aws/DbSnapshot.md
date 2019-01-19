# Terraform::AWS::DbSnapshot

Manages a RDS database instance snapshot. For managing RDS database cluster snapshots, see the [`aws_db_cluster_snapshot` resource](/docs/providers/aws/r/db_cluster_snapshot.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AllocatedStorage` - Specifies the allocated storage size in gigabytes (GB).

`AvailabilityZone` - Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

`DbSnapshotArn` - The Amazon Resource Name (ARN) for the DB snapshot.

`Encrypted` - Specifies whether the DB snapshot is encrypted.

`Engine` - Specifies the name of the database engine.

`EngineVersion` - Specifies the version of the database engine.

`Iops` - Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

`KmsKeyId` - The ARN for the KMS encryption key.

`LicenseModel` - License model information for the restored DB instance.

`OptionGroupName` - Provides the option group name for the DB snapshot.

`SourceDbSnapshotIdentifier` - The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.

`SourceRegion` - The region that the DB snapshot was created in or copied from.

`Status` - Specifies the status of this DB snapshot.

`StorageType` - Specifies the storage type associated with DB snapshot.

`VpcId` - Specifies the storage type associated with DB snapshot.

## See Also

* [aws_db_snapshot](https://www.terraform.io/docs/providers/aws/r/db_snapshot.html) in the _Terraform Provider Documentation_