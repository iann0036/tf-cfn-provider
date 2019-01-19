# Terraform::AWS::EbsVolume

Manages a single EBS volume.

## Properties

`AvailabilityZone` - (Required) The AZ where the EBS volume will exist.

`Encrypted` - (Optional) If true, the disk will be encrypted.

`Iops` - (Optional) The amount of IOPS to provision for the disk.

`Size` - (Optional) The size of the drive in GiBs.

`Type` - (Optional) The type of EBS volume. Can be "standard", "gp2", "io1", "sc1" or "st1" (Default: "standard").

`KmsKeyId` - (Optional) The ARN for the KMS encryption key. When specifying `KmsKeyId`, `Encrypted` needs to be set to true.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The volume ID (e.g. vol-59fcb34e).

`Arn` - The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).

## See Also

* [aws_ebs_volume](https://www.terraform.io/docs/providers/aws/r/ebs_volume.html) in the _Terraform Provider Documentation_