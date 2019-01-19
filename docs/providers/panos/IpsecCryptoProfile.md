# Terraform::Panos::IpsecCryptoProfile

This resource allows you to add/update/delete IPSec crypto profiles.

## Properties

`Name` - (Required) The object's name.

`Protocol` - (Optional) The protocol.  Valid values are `esp` (the default) or `ah`.

`Authentications` - (Required, list) - List of authentication types.

`Encryptions` - (Required, list) - List of encryption types.  Valid values are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, `aes-256-cbc`, `aes-128-gcm`, `aes-256-gcm`, and `null`.  Note that the "gcm" values are only available in PAN-OS 7.0+.

`DhGroup` - (Optional) The DH group value.  Valid values should start with the string `group`.

`LifetimeType` - (Optional) The lifetime type.  Valid values are `seconds`, `minutes`, `hours` (the default), or `days`.

`LifetimeValue` - (Optional, int) The lifetime value.

`LifesizeType` - (Optional) The lifesize type.  Valid values are `kb`, `mb`, `gb`, or `tb`.

`LifesizeValue` - (Optional, int) the lifesize value.


## See Also

* [panos_ipsec_crypto_profile](https://www.terraform.io/docs/providers/panos/r/ipsec_crypto_profile.html) in the _Terraform Provider Documentation_