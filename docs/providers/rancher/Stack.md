# Terraform::Rancher::Stack

Provides a Rancher Stack resource. This can be used to create and manage stacks on rancher.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

`RenderedDockerCompose` - The interpolated `docker_compose` applied to the stack.

`RenderedRancherCompose` - The interpolated `rancher_compose` applied to the stack.

## See Also

* [rancher_stack](https://www.terraform.io/docs/providers/rancher/r/stack.html) in the _Terraform Provider Documentation_