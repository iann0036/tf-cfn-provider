# Terraform::AWS::VolumeAttachment

Provides an AWS EBS Volume Attachment as a top level resource, to attach and
detach volumes from AWS Instances.

~> **NOTE on EBS block devices:** If you use `ebs_block_device` on an `Terraform::AWS::Instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebsBlockDevice` cannot be mixed with external `awsEbsVolume` + `awsEbsVolumeAttachment` resources for a given instance.

## Properties

`DeviceName` - (Required) The device name to expose to the instance (for example, `/dev/sdh` or `xvdh`).

`InstanceId` - (Required) ID of the Instance to attach to.

`VolumeId` - (Required) ID of the Volume to be attached.

`ForceDetach` - (Optional, Boolean) Set to `true` if you want to force the volume to detach. Useful if previous attempts failed, but use this option only as a last resort, as this can result in **data loss**. See [Detaching an Amazon EBS Volume from an Instance][1] for more information.

`SkipDestroy` - (Optional, Boolean) Set this to true if you do not wish to detach the volume from the instance to which it is attached at destroy time, and instead just remove the attachment from Terraform state. This is useful when destroying an instance which has volumes created by some other means attached.


## Return Values

### Fn::GetAtt

`DeviceName` - The device name exposed to the instance.

`InstanceId` - ID of the Instance.

`VolumeId` - ID of the Volume.

## See Also

* [aws_volume_attachment](https://www.terraform.io/docs/providers/aws/r/volume_attachment.html) in the _Terraform Provider Documentation_