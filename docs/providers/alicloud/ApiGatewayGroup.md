# Terraform::Alicloud::ApiGatewayGroup

Provides an api group resource.To create an API, you must firstly create a group which is a basic attribute of the API.

For information about Api Gateway Group and how to use it, see [Create An Api Group](https://www.alibabacloud.com/help/doc-detail/43611.html)

~> **NOTE:** Terraform will auto build api group while it uses `alicloud_api_gateway_group` to build api group.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the api group of api gateway.

## See Also

* [alicloud_api_gateway_group](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_group.html) in the _Terraform Provider Documentation_