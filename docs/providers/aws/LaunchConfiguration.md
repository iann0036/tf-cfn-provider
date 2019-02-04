# Terraform::AWS::LaunchConfiguration

Provides a resource to create a new launch configuration, used for autoscaling groups.

## Properties

`Name` - (Optional) The name of the launch configuration. If you leave
this blank, Terraform will auto-generate a unique name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified
prefix. Conflicts with `Name`.

`ImageId` - (Required) The EC2 image ID to launch.

`InstanceType` - (Required) The size of instance to launch.

`IamInstanceProfile` - (Optional) The name attribute of the IAM instance profile to associate
with launched instances.

`KeyName` - (Optional) The key name that should be used for the instance.

`SecurityGroups` - (Optional) A list of associated security group IDS.

`AssociatePublicIpAddress` - (Optional) Associate a public ip address with an instance in a VPC.

`VpcClassicLinkId` - (Optional) The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`).

`VpcClassicLinkSecurityGroups` - (Optional) The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).

`UserData` - (Optional) The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `UserDataBase64` instead.

`UserDataBase64` - (Optional) Can be used instead of `UserData` to pass base64-encoded binary data directly. Use this instead of `UserData` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

`EnableMonitoring` - (Optional) Enables/disables detailed monitoring. This is enabled by default.

`EbsOptimized` - (Optional) If true, the launched EC2 instance will be EBS-optimized.

`RootBlockDevice` - (Optional) Customize details about the root block
device of the instance. See [Block Devices](#block-devices) below for details.

`EbsBlockDevice` - (Optional) Additional EBS block devices to attach to the
instance.  See [Block Devices](#block-devices) below for details.

`EphemeralBlockDevice` - (Optional) Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.

`SpotPrice` - (Optional; Default: On-demand price) The maximum price to use for reserving spot instances.

`PlacementTenancy` - (Optional) The tenancy of the instance. Valid values are
`"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details.


## Return Values

### Fn::GetAtt

`Id` - The ID of the launch configuration.

`Name` - The name of the launch configuration.

## See Also

* [aws_launch_configuration](https://www.terraform.io/docs/providers/aws/r/launch_configuration.html) in the _Terraform Provider Documentation_