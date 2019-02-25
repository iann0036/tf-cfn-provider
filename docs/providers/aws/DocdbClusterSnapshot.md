# Terraform::AWS::DocdbClusterSnapshot

Manages a DocDB database cluster snapshot for DocDB clusters.

## Properties

`DbClusterIdentifier` - (Required) The DocDB Cluster Identifier from which to take the snapshot.

`DbClusterSnapshotIdentifier` - (Required) The Identifier for the snapshot.


## Return Values

### Fn::GetAtt

`AvailabilityZones` - List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.

`DbClusterSnapshotArn` - The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.

`Engine` - Specifies the name of the database engine.

`EngineVersion` - Version of the database engine for this DocDB cluster snapshot.

`KmsKeyId` - If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.

`Port` - Port that the DocDB cluster was listening on at the time of the snapshot.

`SourceDbClusterSnapshotIdentifier` - The DocDB Cluster Snapshot Arn that the DocDB Cluster Snapshot was copied from. It only has value in case of cross customer or cross region copy.

`StorageEncrypted` - Specifies whether the DocDB cluster snapshot is encrypted.

`Status` - The status of this DocDB Cluster Snapshot.

`VpcId` - The VPC ID associated with the DocDB cluster snapshot.

## See Also

* [aws_docdb_cluster_snapshot](https://www.terraform.io/docs/providers/aws/r/docdb_cluster_snapshot.html) in the _Terraform Provider Documentation_