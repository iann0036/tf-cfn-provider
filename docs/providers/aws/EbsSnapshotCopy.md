# Terraform::AWS::EbsSnapshotCopy

Creates a Snapshot of a snapshot.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The snapshot ID (e.g. snap-59fcb34e).

`OwnerId` - The AWS account ID of the snapshot owner.

`OwnerAlias` - Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.

`Encrypted` - Whether the snapshot is encrypted.

`VolumeSize` - The size of the drive in GiBs.

`KmsKeyId` - The ARN for the KMS encryption key.

`DataEncryptionKeyId` - The data encryption key identifier for the snapshot.

`Tags` - A mapping of tags for the snapshot.

## See Also

* [aws_ebs_snapshot_copy](https://www.terraform.io/docs/providers/aws/r/ebs_snapshot_copy.html) in the _Terraform Provider Documentation_