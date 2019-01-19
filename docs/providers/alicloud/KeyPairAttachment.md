# Terraform::Alicloud::KeyPairAttachment

Provides a key pair attachment resource to bind key pair for several ECS instances.

-> **NOTE:** After the key pair is attached with sone instances, there instances must be rebooted to make the key pair affect.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`KeyName` - The name of the key pair.

## See Also

* [alicloud_key_pair_attachment](https://www.terraform.io/docs/providers/alicloud/r/key_pair_attachment.html) in the _Terraform Provider Documentation_