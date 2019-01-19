# Terraform::Alicloud::RamAccessKey

Provides a RAM User access key resource.

~> **NOTE:**  You should set the `SecretFile` if you want to get the access key.

## Properties

`UserName` - (Required, Forces new resource) Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.

`SecretFile` - (Optional, Forces new resource) The name of file that can save access key id and access key secret. Strongly suggest you to specified it when you creating access key, otherwise, you wouldn't get its secret ever.

`Status` - (Optional) Status of access key. It must be `Active` or `Inactive`. Default value is `Active`.


## Return Values

### Fn::GetAtt

`Id` - The access key ID.

`Status` - The access key status.

## See Also

* [alicloud_ram_access_key](https://www.terraform.io/docs/providers/alicloud/r/ram_access_key.html) in the _Terraform Provider Documentation_