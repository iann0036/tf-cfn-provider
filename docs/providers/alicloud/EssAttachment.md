# Terraform::Alicloud::EssAttachment

Attaches several ECS instances to a specified scaling group or remove them from it.

~> **NOTE:** ECS instances can be attached or remove only when the scaling group is active and it has no scaling activity in progress.

~> **NOTE:** There are two types ECS instances in a scaling group: "AutoCreated" and "Attached". The total number of them can not larger than the scaling group "MaxSize".

## Properties

`ScalingGroupId` - (Required) ID of the scaling group of a scaling configuration.

`InstanceIds` - (Required) ID of the ECS instance to be attached to the scaling group. You can input up to 20 IDs.

`Force` - (Optional) Whether to remove forcibly "AutoCreated" ECS instances in order to release scaling group capacity "MaxSize" for attaching ECS instances. Default to false.


## Return Values

### Fn::GetAtt

`Id` - The ESS attachment resource ID.

`InstanceIds` - ID of list "Attached" ECS instance.

`Force` - Whether to delete "AutoCreated" ECS instances.

## See Also

* [alicloud_ess_attachment](https://www.terraform.io/docs/providers/alicloud/r/ess_attachment.html) in the _Terraform Provider Documentation_