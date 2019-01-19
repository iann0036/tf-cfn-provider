# Terraform::Alicloud::ApiGatewayApp

Provides an app resource.It must create an app before calling a third-party API because the app is the identity used to call the third-party API.

For information about Api Gateway App and how to use it, see [Create An APP](https://www.alibabacloud.com/help/doc-detail/43663.html)

~> **NOTE:** Terraform will auto build api app while it uses `alicloud_api_gateway_app` to build api app.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the app of api gateway.

## See Also

* [alicloud_api_gateway_app](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_app.html) in the _Terraform Provider Documentation_