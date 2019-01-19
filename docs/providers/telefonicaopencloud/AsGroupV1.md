# Terraform::TelefonicaOpenCloud::AsGroupV1

Manages a V1 Autoscaling Group resource within TelefonicaOpenCloud.

## Properties

`Region` - (Optional) The region in which to create the AS group. If omitted, the `Region` argument of the provider is used. Changing this creates a new AS group.

`ScalingGroupName` - (Required) The name of the scaling group. The name can contain letters, digits, underscores(_), and hyphens(-),and cannot exceed 64 characters.

`ScalingConfigurationId` - (Optional) The configuration ID which defines configurations of instances in the AS group.

`DesireInstanceNumber` - (Optional) The expected number of instances. The default value is the minimum number of instances. The value ranges from the minimum number of instances to the maximum number of instances.

`MinInstanceNumber` - (Optional) The minimum number of instances. The default value is 0.

`MaxInstanceNumber` - (Optional) The maximum number of instances. The default value is 0.

`CoolDownTime` - (Optional) The cooling duration (in seconds). The value ranges from 0 to 86400, and is 900 by default.

`LbListenerId` - (Optional) The ELB listener IDs. The system supports up to three ELB listeners, the IDs of which are separated using a comma (,).

`AvailableZones` - (Optional) The availability zones in which to create the instances in the autoscaling group.

`Networks` - (Required) An array of one or more network IDs. The system supports up to five networks. The networks object structure is documented below.

`SecurityGroups` - (Required) An array of one or more security group IDs to associate with the group. The security_groups object structure is documented below.

`VpcId` - (Required) The VPC ID. Changing this creates a new group.

`HealthPeriodicAuditMethod` - (Optional) The health check method for instances in the AS group. The health check methods include `ELB_AUDIT` and `NOVA_AUDIT`. If load balancing is configured, the default value of this parameter is `ELB_AUDIT`. Otherwise, the default value is `NOVA_AUDIT`.

`HealthPeriodicAuditTime` - (Optional) The health check period for instances. The period has four options: 5 minutes (default), 15 minutes, 60 minutes, and 180 minutes.

`InstanceTerminatePolicy` - (Optional) The instance removal policy. The policy has four options: `OLD_CONFIG_OLD_INSTANCE` (default), `OLD_CONFIG_NEW_INSTANCE`, `OLD_INSTANCE`, and `NEW_INSTANCE`.

`Notifications` - (Optional) The notification mode. The system only supports `EMAIL` mode which refers to notification by email.

`DeletePublicip` - (Optional) Whether to delete the elastic IP address bound to the instances of AS group when deleting the instances. The options are `true` and `false`.

`DeleteInstances` - (Optional) Whether to delete the instances in the AS group when deleting the AS group. The options are `yes` and `no`.

### Networks Properties

`Id` - (Required) The network UUID.

### SecurityGroups Properties

`Id` - (Required) The UUID of the security group.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`ScalingGroupName` - See Properties above.

`DesireInstanceNumber` - See Properties above.

`MinInstanceNumber` - See Properties above.

`MaxInstanceNumber` - See Properties above.

`CoolDownTime` - See Properties above.

`LbListenerId` - See Properties above.

`HealthPeriodicAuditMethod` - See Properties above.

`HealthPeriodicAuditTime` - See Properties above.

`InstanceTerminatePolicy` - See Properties above.

`ScalingConfigurationId` - See Properties above.

`DeletePublicip` - See Properties above.

`Notifications` - See Properties above.

`Instances` - The instances IDs of the AS group.

## See Also

* [telefonicaopencloud_as_group_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/as_group_v1.html) in the _Terraform Provider Documentation_