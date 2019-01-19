# Terraform::AWS::OpsworksMysqlLayer

Provides an OpsWorks MySQL layer resource.

~> **Note:** All arguments including the root password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`StackId` - (Required) The id of the stack the layer will belong to.

`Name` - (Optional) A human-readable name for the layer.

`AutoAssignElasticIps` - (Optional) Whether to automatically assign an elastic IP address to the layer's instances.

`AutoAssignPublicIps` - (Optional) For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

`CustomInstanceProfileArn` - (Optional) The ARN of an IAM profile that will be used for the layer's instances.

`CustomSecurityGroupIds` - (Optional) Ids for a set of security groups to apply to the layer's instances.

`AutoHealing` - (Optional) Whether to enable auto-healing for the layer.

`InstallUpdatesOnBoot` - (Optional) Whether to install OS and package updates on each instance when it boots.

`InstanceShutdownTimeout` - (Optional) The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

`ElasticLoadBalancer` - (Optional) Name of an Elastic Load Balancer to attach to this layer.

`DrainElbOnShutdown` - (Optional) Whether to enable Elastic Load Balancing connection draining.

`RootPassword` - (Optional) Root password to use for MySQL.

`RootPasswordOnAllInstances` - (Optional) Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

`SystemPackages` - (Optional) Names of a set of system packages to install on the layer's instances.

`UseEbsOptimizedInstances` - (Optional) Whether to use EBS-optimized instances.

`EbsVolume` - (Optional) `EbsVolume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

`CustomJson` - (Optional) Custom JSON attributes to apply to the layer.

### EbsVolume Properties

`MountPoint` - (Required) The path to mount the EBS volume on the layer's instances.

`Size` - (Required) The size of the volume in gigabytes.

`NumberOfDisks` - (Required) The number of disks to use for the EBS volume.

`RaidLevel` - (Required) The RAID level to use for the volume.

`Type` - (Optional) The type of volume to create. This may be `standard` (the default), `io1` or `gp2`.

`Iops` - (Optional) For PIOPS volumes, the IOPS per disk.


## Return Values

### Fn::GetAtt

`Id` - The id of the layer.

## See Also

* [aws_opsworks_mysql_layer](https://www.terraform.io/docs/providers/aws/r/opsworks_mysql_layer.html) in the _Terraform Provider Documentation_