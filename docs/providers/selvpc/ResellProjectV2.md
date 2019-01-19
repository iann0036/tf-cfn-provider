# Terraform::SelVPC::ResellProjectV2

Manages a V2 project resource within Resell Selectel VPC.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Url` - An url of the Selectel VP project. It is set by the Selectel and can't.

`Enabled` - Shows if project is active or it was disabled by the Selectel.

`AllQuotas` - Contains all quotas. They can differ from the configurable `quota`.

## See Also

* [selvpc_resell_project_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_project_v2.html) in the _Terraform Provider Documentation_