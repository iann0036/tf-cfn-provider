# Terraform::TencentCloud::KeyPair

Provides a key pair resource.

## Properties

`KeyName` - (Force new resource) The key pair's name. It is the only in one TencentCloud account.

`PublicKey` - (Force new resource) You can import an existing public key and using TencentCloud key pair to manage it.


## Return Values

### Fn::GetAtt

`Id` - The id of the key pair, something like `skey-xxxxxxx`, use this for instance creation and resetting.

## See Also

* [tencentcloud_key_pair](https://www.terraform.io/docs/providers/tencentcloud/r/key_pair.html) in the _Terraform Provider Documentation_