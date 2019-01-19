# Terraform::Tfe::Organization

Manages organizations.

## Properties

`Name` - (Required) Name of the organization.

`Email` - (Required) Admin email address.

`SessionTimeoutMinutes` - (Optional) Session timeout after inactivity. Defaults to `20160`.

`SessionRememberMinutes` - (Optional) Session expiration. Defaults to `20160`.

`CollaboratorAuthPolicy` - (Optional) Authentication policy (`password` or `two_factor_mandatory`). Defaults to `password`.


## Return Values

### Fn::GetAtt

`Id` - The name of the organization.

## See Also

* [tfe_organization](https://www.terraform.io/docs/providers/tfe/r/organization.html) in the _Terraform Provider Documentation_