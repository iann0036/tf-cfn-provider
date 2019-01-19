# Terraform::Rancher::Registry

Provides a Rancher Registy resource. This can be used to create registries for rancher environments and retrieve their information

## Properties

`Name` - (Required) The name of the registry.

`Description` - (Optional) A registry description.

`EnvironmentId` - (Required) The ID of the environment to create the registry for.

`ServerAddress` - (Required) The server address for the registry.


## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

## See Also

* [rancher_registry](https://www.terraform.io/docs/providers/rancher/r/registry.html) in the _Terraform Provider Documentation_