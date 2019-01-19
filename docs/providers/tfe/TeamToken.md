# Terraform::Tfe::TeamToken

Generates a new team token and overrides existing token if one exists.

## Properties

`TeamId` - (Required) ID of the team.

`ForceRegenerate` - (Optional) If set to `true`, a new token will be generated even if a token already exists. This will invalidate the existing token!.


## Return Values

### Fn::GetAtt

`Id` - The ID of the token.

`Token` - The generated token.

## See Also

* [tfe_team_token](https://www.terraform.io/docs/providers/tfe/r/team_token.html) in the _Terraform Provider Documentation_