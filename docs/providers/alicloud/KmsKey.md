# Terraform::Alicloud::KmsKey

A kms key can help user to protect data security in the transmission process.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the key.

`Arn` - The Alicloud Resource Name (ARN) of the key.

`Description` - The description of the key.

`KeyUsage` - Specifies the usage of CMK.

`DeletionWindowInDays` - During pre-deletion days.

`IsEnabled` - Whether the key is enabled.

## See Also

* [alicloud_kms_key](https://www.terraform.io/docs/providers/alicloud/r/kms_key.html) in the _Terraform Provider Documentation_