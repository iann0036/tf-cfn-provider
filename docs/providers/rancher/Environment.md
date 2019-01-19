# Terraform::Rancher::Environment

Provides a Rancher Environment resource. This can be used to create and manage environments on rancher.

## Properties

`Name` - (Required) The name of the environment.

`Description` - (Optional) An environment description.

`Orchestration` - (Optional) Must be one of **cattle**, **swarm**, **mesos**, **windows** or **kubernetes**. This is a helper for setting the project_template_ids for the included Rancher templates. This will conflict with project_template_id setting. Changing this forces a new resource to be created.

`ProjectTemplateId` - (Optional) This can be any valid project template ID. If this is set, then orchestration can not be. Changing this forces a new resource to be created.

`Member` - (Optional) Members to add to the environment.


## Return Values

### Fn::GetAtt

`Id` - The ID of the environment (ie `1a11`) that can be used in other Terraform resources such as Rancher Stack definitions.

## See Also

* [rancher_environment](https://www.terraform.io/docs/providers/rancher/r/environment.html) in the _Terraform Provider Documentation_