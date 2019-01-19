# Terraform::AWS::RedshiftSnapshotCopyGrant

Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.

Note that the grant must exist in the destination region, and not in the region of the cluster.

## Properties

`SnapshotCopyGrantName` - (Required, Forces new resource) A friendly name for identifying the grant.

`KmsKeyId` - (Optional, Forces new resource) The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## See Also

* [aws_redshift_snapshot_copy_grant](https://www.terraform.io/docs/providers/aws/r/redshift_snapshot_copy_grant.html) in the _Terraform Provider Documentation_