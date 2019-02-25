# Terraform::Linode::Token

Provides a Linode Token resource.  This can be used to create, modify, and delete Linode API Personal Access Tokens.  Personal Access Tokens proxy user credentials for Linode API access.  This is necessary for tools, such as Terraform, to interact with Linode services on a user's behalf.

It is common for Terraform itself to be configured with broadly scoped Personal Access Tokens.  Provisioning scripts or tools configured within a Linode Instance should follow the principle of least privilege to afford only the required roles for tools to perform their necessary tasks.  The `Terraform::Linode::Token` resource allows for the management of Personal Access Tokens with scopes mirroring or narrowing the scope of the parent token.

For more information, see the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/getTokens).

## Properties

`Label` - A label for the Token.

`Scopes` - The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to *. Tokens with more restrictive scopes are generally more secure.

`Expiry` - When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with 'null' as their expiry and will never expire unless revoked.


## See Also

* [linode_token](https://www.terraform.io/docs/providers/linode/r/token.html) in the _Terraform Provider Documentation_