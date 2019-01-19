# Terraform::Vault::AuthBackend



## Properties

`Type` - (Required) The name of the auth method type.

`Path` - (Optional) The path to mount the auth method — this defaults to the name of the type.

`Description` - (Optional) A description of the auth method.

`DefaultLeaseTtlSeconds` - (Optional) The default lease duration in seconds.

`MaxLeaseTtlSeconds` - (Optional) The maximum lease duration in seconds.

`ListingVisibility` - (Optional) Speficies whether to show this mount in the UI-specific listing endpoint.

`Local` - (Optional) Specifies if the auth method is local only.


## Return Values

### Fn::GetAtt

`Accessor` - The accessor for this auth method.

## See Also

* [vault_auth_backend](https://www.terraform.io/docs/providers/vault/r/auth_backend.html) in the _Terraform Provider Documentation_