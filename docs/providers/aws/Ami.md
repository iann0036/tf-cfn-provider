# Terraform::AWS::Ami

The AMI resource allows the creation and management of a completely-custom
*Amazon Machine Image* (AMI).

If you just want to duplicate an existing AMI, possibly copying it to another
region, it's better to use `aws_ami_copy` instead.

If you just want to share an existing AMI with another AWS account,
it's better to use `aws_ami_launch_permission` instead.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the created AMI.

`RootSnapshotId` - The Snapshot ID for the root volume (for EBS-backed AMIs).

## See Also

* [aws_ami](https://www.terraform.io/docs/providers/aws/r/ami.html) in the _Terraform Provider Documentation_