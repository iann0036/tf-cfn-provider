# Terraform::Alicloud::ApiGatewayApi

Provides an api resource.When you create an API, you must enter the basic information about the API, and define the API request information, the API backend service and response information.

For information about Api Gateway Api and how to use it, see [Create an API](https://www.alibabacloud.com/help/doc-detail/29478.htm)

~> **NOTE:** Terraform will auto build api while it uses `alicloud_api_gateway_api` to build api.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the api resource of api gateway.

`ApiId` - The ID of the api of api gateway.

## See Also

* [alicloud_api_gateway_api](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_api.html) in the _Terraform Provider Documentation_