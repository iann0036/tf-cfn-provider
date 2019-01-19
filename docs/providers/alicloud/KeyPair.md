# Terraform::Alicloud::KeyPair

Provides a key pair resource.

## Properties

`KeyName` - (Force new resource) The key pair's name. It is the only in one Alicloud account.

`KeyNamePrefix` - (Force new resource) The key pair name's prefix. It is conflict with `KeyName`. If it is specified, terraform will using it to build the only key name.

`PublicKey` - (Force new resource) You can import an existing public key and using Alicloud key pair to manage it.

`KeyFile` - (Force new resource) The name of file to save your new key pair's private key. Strongly suggest you to specified it when you creating key pair, otherwise, you wouldn't get its private key ever.


## Return Values

### Fn::GetAtt

`KeyName` - The name of the key pair.

## See Also

* [alicloud_key_pair](https://www.terraform.io/docs/providers/alicloud/r/key_pair.html) in the _Terraform Provider Documentation_