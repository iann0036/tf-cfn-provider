# Terraform::AWS::VolumeAttachment

Provides an AWS EBS Volume Attachment as a top level resource, to attach and
detach volumes from AWS Instances.

~> **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.

## Properties

TBC

## Return Values

### Fn::GetAtt

`DeviceName` - The device name exposed to the instance.

`InstanceId` - ID of the Instance.

`VolumeId` - ID of the Volume.

## See Also

* [aws_volume_attachment](https://www.terraform.io/docs/providers/aws/r/volume_attachment.html) in the _Terraform Provider Documentation_