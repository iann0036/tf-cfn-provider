# Terraform::Panos::IkeCryptoProfile

This resource allows you to add/update/delete IKE crypto profiles.

## Properties

`Name` - (Required) The object's name.

`DhGroups` - (Required, list) List of DH Group entries.  Values should have a prefix if `group`.

`Authentications` - (Required, list) List of authentication types.  This c.

`Encryptions` - (Required, list) List of encryption types.  Valid values are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, and `aes-256-cbc`.

`LifetimeType` - (Optional) The lifetime type.  Valid values are `seconds`, `minutes`, `hours` (the default), and `days`.

`LifetimeValue` - (Optional, int) The lifetime value.

`AuthenticationMultiple` - (Optional, PAN-OS 7.0+, int) IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication is disabled.


## See Also

* [panos_ike_crypto_profile](https://www.terraform.io/docs/providers/panos/r/ike_crypto_profile.html) in the _Terraform Provider Documentation_