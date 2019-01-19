# Terraform::AWS::Ami

The AMI resource allows the creation and management of a completely-custom
*Amazon Machine Image* (AMI).

If you just want to duplicate an existing AMI, possibly copying it to another
region, it's better to use `Terraform::AWS::AmiCopy` instead.

If you just want to share an existing AMI with another AWS account,
it's better to use `Terraform::AWS::AmiLaunchPermission` instead.

## Properties

`Name` - (Required) A region-unique name for the AMI.

`Description` - (Optional) A longer, human-readable description for the AMI.

`EnaSupport` - (Optional) Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.

`RootDeviceName` - (Optional) The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).

`VirtualizationType` - (Optional) Keyword to choose what virtualization mode created instances will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type changes the set of further arguments that are required, as described below.

`Architecture` - (Optional) Machine architecture for created instances. Defaults to "x86_64".

`EbsBlockDevice` - (Optional) Nested block describing an EBS block device that should be attached to created instances. The structure of this block is described below.

`EphemeralBlockDevice` - (Optional) Nested block describing an ephemeral block device that should be attached to created instances. The structure of this block is described below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`ImageLocation` - (Required) Path to an S3 object containing an image manifest, e.g. created by the `ec2-upload-bundle` command in the EC2 command line tools.

`KernelId` - (Required) The id of the kernel image (AKI) that will be used as the paravirtual kernel in created instances.

`RamdiskId` - (Optional) The id of an initrd image (ARI) that will be used when booting the created instances.

`SriovNetSupport` - (Optional) When set to "simple" (the default), enables enhanced networking for created instances. No other value is supported at this time.

`DeviceName` - (Required) The path at which the device is exposed to created instances.

`DeleteOnTermination` - (Optional) Boolean controlling whether the EBS volumes created to support each created instance will be deleted once that instance is terminated.

`Encrypted` - (Optional) Boolean controlling whether the created EBS volumes will be encrypted. Can't be used with `SnapshotId`.

`Iops` - (Required only when `VolumeType` is "io1") Number of I/O operations per second the created volumes will support.

`SnapshotId` - (Optional) The id of an EBS snapshot that will be used to initialize the created EBS volumes. If set, the `VolumeSize` attribute must be at least as large as the referenced snapshot.

`VolumeSize` - (Required unless `SnapshotId` is set) The size of created volumes in GiB. If `SnapshotId` is set and `VolumeSize` is omitted then the volume will have the same size as the selected snapshot.

`VolumeType` - (Optional) The type of EBS volume to create. Can be one of "standard" (the default), "io1" or "gp2".

`KmsKeyId` - (Optional) The full ARN of the AWS Key Management Service (AWS KMS) CMK to use when encrypting the snapshots of an image during a copy operation. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used.

`VirtualName` - (Required) A name for the ephemeral device, of the form "ephemeralN" where *N* is a volume number starting from zero.


## Return Values

### Fn::GetAtt

`Id` - The ID of the created AMI.

`RootSnapshotId` - The Snapshot ID for the root volume (for EBS-backed AMIs).

## See Also

* [aws_ami](https://www.terraform.io/docs/providers/aws/r/ami.html) in the _Terraform Provider Documentation_