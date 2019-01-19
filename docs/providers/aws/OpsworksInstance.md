# Terraform::AWS::OpsworksInstance

Provides an OpsWorks instance resource.

## Properties

`InstanceType` - (Required) The type of instance to start.

`StackId` - (Required) The id of the stack the instance will belong to.

`LayerIds` - (Required) The ids of the layers the instance will belong to.

`State` - (Optional) The desired state of the instance.  Can be either `"running"` or `"stopped"`.

`InstallUpdatesOnBoot` - (Optional) Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

`AutoScalingType` - (Optional) Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

`AvailabilityZone` - (Optional) Name of the availability zone where instances will be created by default.

`EbsOptimized` - (Optional) If true, the launched EC2 instance will be EBS-optimized.

`Hostname` - (Optional) The instance's host name.

`Architecture` - (Optional) Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`.

`AmiId` - (Optional) The AMI to use for the instance.  If an AMI is specified, `Os` must be `"Custom"`.

`Os` - (Optional) Name of operating system that will be installed.

`RootDeviceType` - (Optional) Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`.

`SshKeyName` - (Optional) Name of the SSH keypair that instances will have by default.

`AgentVersion` - (Optional) The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

`SubnetId` - (Optional) Subnet ID to attach to.

`Tenancy` - (Optional) Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`.

`VirtualizationType` - (Optional) Keyword to choose what virtualization mode created instances will use. Can be either `"paravirtual"` or `"hvm"`.

`RootBlockDevice` - (Optional) Customize details about the root block device of the instance. See [Block Devices](#block-devices) below for details.

`EbsBlockDevice` - (Optional) Additional EBS block devices to attach to the instance.  See [Block Devices](#block-devices) below for details.

`EphemeralBlockDevice` - (Optional) Customize Ephemeral (also known as "Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.


## Return Values

### Fn::GetAtt

`Id` - The id of the OpsWorks instance.

`AgentVersion` - The AWS OpsWorks agent version.

`AvailabilityZone` - The availability zone of the instance.

`Ec2InstanceId` - EC2 instance ID.

`SshKeyName` - The key name of the instance.

`PublicDns` - The public DNS name assigned to the instance. For EC2-VPC, this.

`PublicIp` - The public IP address assigned to the instance, if applicable.

`PrivateDns` - The private DNS name assigned to the instance. Can only be.

`PrivateIp` - The private IP address assigned to the instance.

`SubnetId` - The VPC subnet ID.

`Tenancy` - The Instance tenancy.

`SecurityGroupIds` - The associated security groups.

## See Also

* [aws_opsworks_instance](https://www.terraform.io/docs/providers/aws/r/opsworks_instance.html) in the _Terraform Provider Documentation_