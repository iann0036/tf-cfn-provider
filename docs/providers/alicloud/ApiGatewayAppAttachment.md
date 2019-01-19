# Terraform::Alicloud::ApiGatewayAppAttachment

Provides an app attachment resource.It is used for authorizing a specific api to an app accessing. 

For information about Api Gateway App attachment and how to use it, see [Add specified API access authorities](https://www.alibabacloud.com/help/doc-detail/43673.htm)

~> **NOTE:** Terraform will auto build app attachment while it uses `alicloud_api_gateway_app_attachment` to build.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the app attachment of api gateway., formatted as `<group_id>:<api_id>:<app_id>:<stage_name>`.

## See Also

* [alicloud_api_gateway_app_attachment](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_app_attachment.html) in the _Terraform Provider Documentation_