# Terraform::Tfe::Variable

Creates, updates and destroys variables.

## Properties

`Key` - (Required) Name of the variable.

`Value` - (Required) Value of the variable.

`Category` - (Required) Whether this is a Terraform or environment variable. Valid values are `terraform` or `env`.

`Hcl` - (Optional) Whether to evaluate the value of the variable as a string of HCL code. Has no effect for environment variables. Defaults to `false`.

`Sensitive` - (Optional) Whether the value is sensitive. If true then the variable is written once and not visible thereafter. Defaults to `false`.

`WorkspaceId` - (Required) ID of the workspace that owns the variable.


## Return Values

### Fn::GetAtt

`Id` - The ID of the variable.

## See Also

* [tfe_variable](https://www.terraform.io/docs/providers/tfe/r/variable.html) in the _Terraform Provider Documentation_