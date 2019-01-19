# Terraform::Alicloud::FcService

Provides a Alicloud Function Compute Service resource. The resource is the base of launching Function and Trigger configuration.
 For information about Service and how to use it, see [What is Function Compute](https://www.alibabacloud.com/help/doc-detail/52895.htm).

-> **NOTE:** The resource requires a provider field 'account_id'. [See account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

-> **NOTE:** If you happen the error "Argument 'internetAccess' is not supported", you need to log on web console and click button "Apply VPC Function"
which is in the upper of [Function Service Web Console](https://fc.console.aliyun.com/) page.

-> **NOTE:** Currently not all regions support Function Compute Service.
For more details supported regions, see [Service endpoints](https://www.alibabacloud.com/help/doc-detail/52984.htm)

## Properties

`Name` - (ForceNew) The Function Compute service name. It is the only in one Alicloud account and is conflict with "name_prefix".

`NamePrefix` - (ForceNew) Setting a prefix to get a only name. It is conflict with "name".

`Description` - (Optional) The function compute service description.

`InternetAccess` - (Optional) Whether to allow the service to access Internet. Default to "true".

`Role` - (Optional) RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See [User Permissions](https://www.alibabacloud.com/help/doc-detail/52885.htm) for more details.

`LogConfig` - (Optional) Provide this to store your FC service logs. Fields documented below. See [Create a Service](https://www.alibabacloud.com/help/doc-detail/51924.htm).

`VpcConfig` - (Optional) Provide this to allow your FC service to access your VPC. Fields documented below. See [Function Compute Service in VPC](https://www.alibabacloud.com/help/faq-detail/72959.htm).

`Project` - (Required) The project name of Logs service.

`Logstore` - (Required) The log store name of Logs service.

`VswitchIds` - (Required) A list of vswitch IDs associated with the FC service.

`SecurityGroupId` - (Required) A security group ID associated with the FC service.


## Return Values

### Fn::GetAtt

`Id` - The ID of the FC service. The value is same as name.

`LastModified` - The date this resource was last modified.

## See Also

* [alicloud_fc_service](https://www.terraform.io/docs/providers/alicloud/r/fc_service.html) in the _Terraform Provider Documentation_