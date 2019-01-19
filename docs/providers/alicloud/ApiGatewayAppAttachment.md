# Terraform::Alicloud::ApiGatewayAppAttachment

Provides an app attachment resource.It is used for authorizing a specific api to an app accessing. 

For information about Api Gateway App attachment and how to use it, see [Add specified API access authorities](https://www.alibabacloud.com/help/doc-detail/43673.htm)

~> **NOTE:** Terraform will auto build app attachment while it uses `Terraform::Alicloud::ApiGatewayAppAttachment` to build.

## Properties

`ApiId` - (Required，ForceNew) The api_id that app apply to access.

`GroupId` - (Required，ForceNew) The group that the api belongs to.

`AppId` - (Required，ForceNew) The app that apply to the authorization.

`StageName` - (Required，ForceNew) Stage that the app apply to access.


## Return Values

### Fn::GetAtt

`Id` - The ID of the app attachment of api gateway., formatted as `<group_id>:<api_id>:<app_id>:<stage_name>`.

## See Also

* [alicloud_api_gateway_app_attachment](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_app_attachment.html) in the _Terraform Provider Documentation_