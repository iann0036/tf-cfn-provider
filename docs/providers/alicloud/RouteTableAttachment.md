# Terraform::Alicloud::RouteTableAttachment

Provides an Alicloud Route Table Attachment resource for associating Route Table to VSwitch Instance.

~> **NOTE:** Terraform will auto build route table attachment while it uses `alicloud_route_table_attachment` to build a route table attachment resource.

For information about route table and how to use it, see [What is Route Table](https://www.alibabacloud.com/help/doc-detail/87057.htm).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the route table attachment id and formates as `<route_table_id>:<vswitch_id>`.

## See Also

* [alicloud_route_table_attachment](https://www.terraform.io/docs/providers/alicloud/r/route_table_attachment.html) in the _Terraform Provider Documentation_