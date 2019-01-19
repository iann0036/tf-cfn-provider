# Terraform::AWS::Instance

Provides an EC2 instance resource. This allows instances to be created, updated,
and deleted. Instances also support [provisioning](/docs/provisioners/index.html).

## Properties

`Ami` - (Required) The AMI to use for the instance.

`AvailabilityZone` - (Optional) The AZ to start the instance in.

`PlacementGroup` - (Optional) The Placement Group to start the instance in.

`Tenancy` - (Optional) The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the import-instance command.

`HostId` - (optional) The Id of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host.

`CpuCoreCount` - (Optional) Sets the number of CPU cores for an instance. This option is only supported on creation of instance type that support CPU Options [CPU Cores and Threads Per CPU Core Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html#cpu-options-supported-instances-values) - specifying this option for unsupported instance types will return an error from the EC2 API.

`CpuThreadsPerCore` - (Optional - has no effect unless `CpuCoreCount` is also set)  If set to to 1, hyperthreading is disabled on the launched instance. Defaults to 2 if not set. See [Optimizing CPU Options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for more information.

`EbsOptimized` - (Optional) If true, the launched EC2 instance will be EBS-optimized. Note that if this is not set on an instance type that is optimized by default then this will show as disabled but if the instance type is optimized by default then there is no need to set this and there is no effect to disabling it. See the [EBS Optimized section](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) of the AWS User Guide for more information.

`DisableApiTermination` - (Optional) If true, enables [EC2 Instance Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

`InstanceInitiatedShutdownBehavior` - (Optional) Shutdown behavior for the instance. Amazon defaults this to `stop` for EBS-backed instances and `terminate` for instance-store instances. Cannot be set on instance-store instances. See [Shutdown Behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior) for more information.

`InstanceType` - (Required) The type of instance to start. Updates to this field will trigger a stop/start of the EC2 instance.

`KeyName` - (Optional) The key name of the Key Pair to use for the instance; which can be managed using [the `Terraform::AWS::KeyPair` resource](key_pair.html).

`GetPasswordData` - (Optional) If true, wait for password data to become available and retrieve it. Useful for getting the administrator password for instances running Microsoft Windows. The password data is exported to the `password_data` attribute. See [GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) for more information.

`Monitoring` - (Optional) If true, the launched EC2 instance will have detailed monitoring enabled. (Available since v0.6.0).

`SecurityGroups` - (Optional, EC2-Classic and default VPC only) A list of security group names (EC2-Classic) or IDs (default VPC) to associate with.

`VpcSecurityGroupIds` - (Optional, VPC only) A list of security group IDs to associate with.

`SubnetId` - (Optional) The VPC Subnet ID to launch in.

`AssociatePublicIpAddress` - (Optional) Associate a public ip address with an instance in a VPC.  Boolean value.

`PrivateIp` - (Optional) Private IP address to associate with the instance in a VPC.

`SourceDestCheck` - (Optional) Controls if traffic is routed to the instance when the destination address does not match the instance. Used for NAT or VPNs. Defaults true.

`UserData` - (Optional) The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `UserDataBase64` instead.

`UserDataBase64` - (Optional) Can be used instead of `UserData` to pass base64-encoded binary data directly. Use this instead of `UserData` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.

`IamInstanceProfile` - (Optional) The IAM Instance Profile to launch the instance with. Specified as the name of the Instance Profile. Ensure your credentials have the correct permission to assign the instance profile according to the [EC2 documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-permissions), notably `iam:PassRole`.

`Ipv6AddressCount` - (Optional) A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.

`Ipv6Addresses` - (Optional) Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`VolumeTags` - (Optional) A mapping of tags to assign to the devices created by the instance at launch time.

`RootBlockDevice` - (Optional) Customize details about the root block device of the instance. See [Block Devices](#block-devices) below for details.

`EbsBlockDevice` - (Optional) Additional EBS block devices to attach to the instance.  See [Block Devices](#block-devices) below for details.

`EphemeralBlockDevice` - (Optional) Customize Ephemeral (also known as "Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.

`NetworkInterface` - (Optional) Customize network interfaces to be attached at instance boot time. See [Network Interfaces](#network-interfaces) below for more details.

`CreditSpecification` - (Optional) Customize the credit specification of the instance. See [Credit Specification](#credit-specification) below for more details.


## Return Values

### Fn::GetAtt

`Id` - The instance ID.

`Arn` - The ARN of the instance.

`AvailabilityZone` - The availability zone of the instance.

`PlacementGroup` - The placement group of the instance.

`KeyName` - The key name of the instance.

`PasswordData` - Base-64 encoded encrypted password data for the instance.

`PublicDns` - The public DNS name assigned to the instance. For EC2-VPC, this.

`PublicIp` - The public IP address assigned to the instance, if applicable. **NOTE**: If you are using an [`Terraform::AWS::Eip`](/docs/providers/aws/r/eip.html) with your instance, you should refer to the EIP's address directly and not use `publicIp`, as this field will change after the EIP is attached.

`Ipv6Addresses` - A list of assigned IPv6 addresses, if any.

`NetworkInterfaceId` - The ID of the network interface that was created with the instance.

`PrimaryNetworkInterfaceId` - The ID of the instance's primary network interface.

`PrivateDns` - The private DNS name assigned to the instance. Can only be.

`PrivateIp` - The private IP address assigned to the instance.

`SecurityGroups` - The associated security groups.

`VpcSecurityGroupIds` - The associated security groups in non-default VPC.

`SubnetId` - The VPC subnet ID.

`CreditSpecification` - Credit specification of instance.

## See Also

* [aws_instance](https://www.terraform.io/docs/providers/aws/r/instance.html) in the _Terraform Provider Documentation_