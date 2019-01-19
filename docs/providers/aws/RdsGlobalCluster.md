# Terraform::AWS::RdsGlobalCluster

Manages a RDS Global Cluster, which is an Aurora global database spread across multiple regions. The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.

More information about Aurora global databases can be found in the [Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database-creating).

~> **NOTE:** RDS only supports the `aurora` engine (MySQL 5.6 compatible) for Global Clusters at this time.

## Properties

`DatabaseName` - (Optional) Name for an automatically created database on cluster creation.

`DeletionProtection` - (Optional) If the Global Cluster should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

`Engine` - (Optional) Name of the database engine to be used for this DB cluster. Valid values: `aurora`. Defaults to `aurora`.

`EngineVersion` - (Optional) Engine version of the Aurora global database.

`StorageEncrypted` - (Optional) Specifies whether the DB cluster is encrypted. The default is `false`.


## See Also

* [aws_rds_global_cluster](https://www.terraform.io/docs/providers/aws/r/rds_global_cluster.html) in the _Terraform Provider Documentation_