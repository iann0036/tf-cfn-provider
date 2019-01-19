# Terraform::Alicloud::KeyPairAttachment

Provides a key pair attachment resource to bind key pair for several ECS instances.

-> **NOTE:** After the key pair is attached with sone instances, there instances must be rebooted to make the key pair affect.

## Properties

`KeyName` - (Required, Force new resource) The name of key pair used to bind.

`InstanceIds` - (Required, Force new resource) The list of ECS instance's IDs.

`Force` - (Required, Force new resource) Set it to true and it will reboot instances which attached with the key pair to make key pair affect immediately.


## Return Values

### Fn::GetAtt

`KeyName` - The name of the key pair.

## See Also

* [alicloud_key_pair_attachment](https://www.terraform.io/docs/providers/alicloud/r/key_pair_attachment.html) in the _Terraform Provider Documentation_