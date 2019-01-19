# Terraform::Alicloud::OtsInstanceAttachment

This resource will help you to bind a VPC to an OTS instance.

## Properties

`InstanceName` - (Required, ForceNew) The name of the OTS instance.

`VpcName` - (Required, ForceNew) The name of attaching VPC to instance.

`VswitchId` - (Required, ForceNew) The ID of attaching VSwitch to instance.


## Return Values

### Fn::GetAtt

`Id` - The resource ID. The value is same as "instance_name".

`InstanceName` - The instance name.

`VpcName` - The name of attaching VPC to instance.

`VswitchId` - The ID of attaching VSwitch to instance.

`VpcId` - The ID of attaching VPC to instance.

## See Also

* [alicloud_ots_instance_attachment](https://www.terraform.io/docs/providers/alicloud/r/ots_instance_attachment.html) in the _Terraform Provider Documentation_