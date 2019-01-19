# Terraform::Scaleway::Token

Provides Tokens for scaleway API access. For additional details please refer to [API documentation](https://developer.scaleway.com/#tokens-tokens-post).

## Properties

`Expires` - (Optional) Define if the token should automatically expire or not.

`Email` - (Optional) Scaleway account email. Defaults to registered account.

`Password` - (Optional) Scaleway account password. Required for cross-account token management.

`Description` - (Optional) Token description.


## Return Values

### Fn::GetAtt

`Id` - Token ID - can be used to access scaleway API.

`AccessKey` - Token Access Key.

`SecretKey` - Token Secret Key.

`CreationIp` - IP used to create the token.

`ExpirationDate` - Expiration date of token, if expiration is requested.

## See Also

* [scaleway_token](https://www.terraform.io/docs/providers/scaleway/r/token.html) in the _Terraform Provider Documentation_