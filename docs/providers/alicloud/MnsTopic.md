# Terraform::Alicloud::MnsTopic

Provides a MNS topic resource.

~> **NOTE:** Terraform will auto build a mns topic  while it uses `Terraform::Alicloud::MnsTopic` to build a mns topic resource.

## Properties

`Name` - (Required, Forces new resource)Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

`MaximumMessageSize` - (Optional)This indicates the maximum length, in bytes, of any message body sent to the topic. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.

`LoggingEnabled` - (Optional) Is logging enabled? true or false. Default value to false.


## Return Values

### Fn::GetAtt

`Id` - The ID of the topic is equal to name.

## See Also

* [alicloud_mns_topic](https://www.terraform.io/docs/providers/alicloud/r/mns_topic.html) in the _Terraform Provider Documentation_