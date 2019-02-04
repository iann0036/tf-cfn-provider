# Terraform::Alicloud::KmsKey

A kms key can help user to protect data security in the transmission process.

## Properties

`Description` - (Optional) The description of the key as viewed in Alicloud console. Default to "From Terraform".

`KeyUsage` - (Optional) Specifies the usage of CMK. Currently, default to 'ENCRYPT/DECRYPT', indicating that CMK is used for encryption and decryption.

`DeletionWindowInDays` - (Optional) Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

`IsEnabled` - (Optional) Specifies whether the key is enabled. Defaults to true.


## Return Values

### Fn::GetAtt

`Id` - The ID of the key.

`Arn` - The Alicloud Resource Name (ARN) of the key.

`Description` - The description of the key.

`KeyUsage` - Specifies the usage of CMK.

`DeletionWindowInDays` - During pre-deletion days.

`IsEnabled` - Whether the key is enabled.

## See Also

* [alicloud_kms_key](https://www.terraform.io/docs/providers/alicloud/r/kms_key.html) in the _Terraform Provider Documentation_