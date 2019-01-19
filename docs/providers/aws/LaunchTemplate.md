# Terraform::AWS::LaunchTemplate

Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.

## Properties

`Name` - The name of the launch template. If you leave this blank, Terraform will auto-generate a unique name.

`NamePrefix` - Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - Description of the launch template.

`BlockDeviceMappings` - Specify volumes to attach to the instance besides the volumes specified by the AMI. See [Block Devices](#block-devices) below for details.

`CapacityReservationSpecification` - Targeting for EC2 capacity reservations. See [Capacity Reservation Specification](#capacity-reservation-specification) below for more details.

`CreditSpecification` - Customize the credit specification of the instance. See [Credit Specification](#credit-specification) below for more details.

`DisableApiTermination` - If `true`, enables [EC2 Instance Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

`EbsOptimized` - If `true`, the launched EC2 instance will be EBS-optimized.

`ElasticGpuSpecifications` - The elastic GPU to attach to the instance. See [Elastic GPU](#elastic-gpu) below for more details.

`IamInstanceProfile` - The IAM Instance Profile to launch the instance with. See [Instance Profile](#instance-profile) below for more details.

`ImageId` - The AMI from which to launch the instance.

`InstanceInitiatedShutdownBehavior` - Shutdown behavior for the instance. Can be `stop` or `terminate`. (Default: `stop`).

`InstanceMarketOptions` - The market (purchasing) option for the instance. See [Market Options](#market-options) below for details.

`InstanceType` - The type of the instance.

`KernelId` - The kernel ID.

`KeyName` - The key name to use for the instance.

`LicenseSpecification` - A list of license specifications to associate with. See [License Specifications](#license-specificiations) below for more details.

`Monitoring` - The monitoring option for the instance. See [Monitoring](#monitoring) below for more details.

`NetworkInterfaces` - Customize network interfaces to be attached at instance boot time. See [Network Interfaces](#network-interfaces) below for more details.

`Placement` - The placement of the instance. See [Placement](#placement) below for more details.

`RamDiskId` - The ID of the RAM disk.

`SecurityGroupNames` - A list of security group names to associate with. If you are creating Instances in a VPC, use `VpcSecurityGroupIds` instead.

`VpcSecurityGroupIds` - A list of security group IDs to associate with.

`TagSpecifications` - The tags to apply to the resources during launch. See [Tags](#tags) below for more details.

`Tags` - (Optional) A mapping of tags to assign to the launch template.

`UserData` - The Base64-encoded user data to provide when launching the instance.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of the launch template.

`Id` - The ID of the launch template.

`DefaultVersion` - The default version of the launch template.

`LatestVersion` - The latest version of the launch template.

## See Also

* [aws_launch_template](https://www.terraform.io/docs/providers/aws/r/launch_template.html) in the _Terraform Provider Documentation_