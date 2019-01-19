# Terraform::Alicloud::FcFunction

Provides a Alicloud Function Compute Trigger resource. Based on trigger, execute your code in response to events in Alibaba Cloud.
 For information about Service and how to use it, see [What is Function Compute](https://www.alibabacloud.com/help/doc-detail/52895.htm).

-> **NOTE:** The resource requires a provider field 'account_id'. [See account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

## Properties

`Service` - (Required, ForceNew) The Function Compute service name.

`Function` - (Required, ForceNew) The Function Compute function name.

`Name` - (ForceNew) The Function Compute trigger name. It is the only in one service and is conflict with "name_prefix".

`NamePrefix` - (ForceNew) Setting a prefix to get a only trigger name. It is conflict with "name".

`Role` - (Optional) RAM role arn attached to the Function Compute trigger. Role used by the event source to call the function. The value format is "acs:ram::$account-id:role/$role-name". See [Create a trigger](https://www.alibabacloud.com/help/doc-detail/53102.htm) for more details.

`SourceArn` - (Optional, ForceNew) Event source resource address. See [Create a trigger](https://www.alibabacloud.com/help/doc-detail/53102.htm) for more details.

`Config` - (Optional) The config of Function Compute trigger. See [Configure triggers and events](https://www.alibabacloud.com/help/doc-detail/70140.htm) for more details.

`Type` - (Required, ForceNew) The Type of the trigger. Valid values: ["oss", "log", "timer", "http"].


## Return Values

### Fn::GetAtt

`Id` - The ID of the function. The value is formate as `<service>:<function>:<name>`.

`LastModified` - The date this resource was last modified.

## See Also

* [alicloud_fc_function](https://www.terraform.io/docs/providers/alicloud/r/fc_function.html) in the _Terraform Provider Documentation_