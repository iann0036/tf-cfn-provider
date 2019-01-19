# Terraform::AWS::RedshiftSnapshotCopyGrant

Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.

Note that the grant must exist in the destination region, and not in the region of the cluster.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_redshift_snapshot_copy_grant](https://www.terraform.io/docs/providers/aws/r/redshift_snapshot_copy_grant.html) in the _Terraform Provider Documentation_