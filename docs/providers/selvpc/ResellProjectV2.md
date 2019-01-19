# Terraform::SelVPC::ResellProjectV2

Manages a V2 project resource within Resell Selectel VPC.

## Properties

`Name` - (Required) The name of the project.

`CustomUrl` - (Optional) The custom url for the project. Needs to be the 3rd-level domain for the `selvpc.ru`. Example: `terraform-project-001.selvpc.ru`.

`Theme` - (Optional) An additional theme settings for this project. The structure is described below.

`AutoQuotas` - (Optional) A boolean parameter that specifies if project should get automatically calculated quotas.

`Quotas` - (Optional) An array of desired quotas for this project. The structure is described below.

`Color` - (Optional) A background color in hex format.

`Logo` - (Optional) An url of the project header logo.

`ResourceName` - (Required) A name of the billing resource to set quotas for.

`ResourceQuotas` - (Required) An array of desired billing quotas for this particular resource. The structure is described below.

`Region` - (Optional) A Selectel VPC region for the resource quota.

`Zone` - (Optional) A Selectel VPC zone for the resource quota.

`Value` - (Required) A value of the resource quota.


## Return Values

### Fn::GetAtt

`Url` - An url of the Selectel VP project. It is set by the Selectel and can't.

`Enabled` - Shows if project is active or it was disabled by the Selectel.

`AllQuotas` - Contains all quotas. They can differ from the configurable `quota`.

## See Also

* [selvpc_resell_project_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_project_v2.html) in the _Terraform Provider Documentation_