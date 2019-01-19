# Terraform::Alicloud::OtsInstanceAttachment

This resource will help you to bind a VPC to an OTS instance.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The resource ID. The value is same as "instance_name".

`InstanceName` - The instance name.

`VpcName` - The name of attaching VPC to instance.

`VswitchId` - The ID of attaching VSwitch to instance.

`VpcId` - The ID of attaching VPC to instance.

## See Also

* [alicloud_ots_instance_attachment](https://www.terraform.io/docs/providers/alicloud/r/ots_instance_attachment.html) in the _Terraform Provider Documentation_