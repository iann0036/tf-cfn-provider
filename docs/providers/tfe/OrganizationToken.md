# Terraform::Tfe::OrganizationToken

Generates a new organization token, replacing any existing token. This token
can be used to act as the organization service account.

## Properties

`Organization` - (Required) Name of the organization.

`ForceRegenerate` - (Optional) If set to `true`, a new token will be
generated even if a token already exists. This will invalidate the existing
token!.


## Return Values

### Fn::GetAtt

`Id` - The ID of the token.

`Token` - The generated token.

## See Also

* [tfe_organization_token](https://www.terraform.io/docs/providers/tfe/r/organization_token.html) in the _Terraform Provider Documentation_