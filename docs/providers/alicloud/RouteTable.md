# Terraform::Alicloud::RouteTable

Provides a route table resource to add customized route tables.

~> **NOTE:** Terraform will auto build route table instance while it uses `alicloud_route_table` to build a route table resource.

Currently, customized route tables are available in most regions apart from China (Beijing), China (Hangzhou), and China (Shenzhen) regions.
For information about route table and how to use it, see [What is Route Table](https://www.alibabacloud.com/help/doc-detail/87057.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the route table instance id.

## See Also

* [alicloud_route_table](https://www.terraform.io/docs/providers/alicloud/r/route_table.html) in the _Terraform Provider Documentation_