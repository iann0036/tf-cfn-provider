# Terraform::Rancher::Stack

Provides a Rancher Stack resource. This can be used to create and manage stacks on rancher.

## Properties

`Name` - (Required) The name of the stack.

`Description` - (Optional) A stack description.

`EnvironmentId` - (Required) The ID of the environment to create the stack for.

`DockerCompose` - (Optional) The `docker-compose.yml` content to apply for the stack.

`RancherCompose` - (Optional) The `rancher-compose.yml` content to apply for the stack.

`Environment` - (Optional) The environment to apply to interpret the docker-compose and rancher-compose files.

`CatalogId` - (Optional) The catalog ID to link this stack to. When provided, `DockerCompose` and `RancherCompose` will be retrieved from the catalog unless they are overridden.

`Scope` - (Optional) The scope to attach the stack to. Must be one of **user** or **system**. Defaults to **user**.

`StartOnCreate` - (Optional) Whether to start the stack automatically.

`FinishUpgrade` - (Optional) Whether to automatically finish upgrades to this stack.


## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

`RenderedDockerCompose` - The interpolated `DockerCompose` applied to the stack.

`RenderedRancherCompose` - The interpolated `RancherCompose` applied to the stack.

## See Also

* [rancher_stack](https://www.terraform.io/docs/providers/rancher/r/stack.html) in the _Terraform Provider Documentation_