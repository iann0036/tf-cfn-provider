# Terraform::AWS::DbClusterSnapshot

Manages a RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the [`aws_db_snapshot` resource](/docs/providers/aws/r/db_snapshot.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AllocatedStorage` - Specifies the allocated storage size in gigabytes (GB).

`AvailabilityZones` - List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

`DbClusterSnapshotArn` - The Amazon Resource Name (ARN) for the DB Cluster Snapshot.

`Engine` - Specifies the name of the database engine.

`EngineVersion` - Version of the database engine for this DB cluster snapshot.

`KmsKeyId` - If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

`LicenseModel` - License model information for the restored DB cluster.

`Port` - Port that the DB cluster was listening on at the time of the snapshot.

`SourceDbClusterSnapshotIdentifier` - The DB Cluster Snapshot Arn that the DB Cluster Snapshot was copied from. It only has value in case of cross customer or cross region copy.

`StorageEncrypted` - Specifies whether the DB cluster snapshot is encrypted.

`Status` - The status of this DB Cluster Snapshot.

`VpcId` - The VPC ID associated with the DB cluster snapshot.

## See Also

* [aws_db_cluster_snapshot](https://www.terraform.io/docs/providers/aws/r/db_cluster_snapshot.html) in the _Terraform Provider Documentation_