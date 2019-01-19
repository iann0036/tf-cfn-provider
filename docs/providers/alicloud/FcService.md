# Terraform::Alicloud::FcService

Provides a Alicloud Function Compute Service resource. The resource is the base of launching Function and Trigger configuration.
 For information about Service and how to use it, see [What is Function Compute](https://www.alibabacloud.com/help/doc-detail/52895.htm).

-> **NOTE:** The resource requires a provider field 'account_id'. [See account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

-> **NOTE:** If you happen the error "Argument 'internetAccess' is not supported", you need to log on web console and click button "Apply VPC Function"
which is in the upper of [Function Service Web Console](https://fc.console.aliyun.com/) page.

-> **NOTE:** Currently not all regions support Function Compute Service.
For more details supported regions, see [Service endpoints](https://www.alibabacloud.com/help/doc-detail/52984.htm)

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the FC service. The value is same as name.

`LastModified` - The date this resource was last modified.

## See Also

* [alicloud_fc_service](https://www.terraform.io/docs/providers/alicloud/r/fc_service.html) in the _Terraform Provider Documentation_