# Terraform::Rancher::Host

Provides a Rancher Host resource. This can be used to manage and delete hosts on Rancher.

## Properties

`Id` - (Computed) The ID of the resource.

`Name` - (Required) The name of the host.

`Description` - (Optional) A host description.

`EnvironmentId` - (Required) The ID of the environment the host is associated to.

`Hostname` - (Required) The host name. Used as the primary key to detect the host ID.

`Labels` - (Optional) A dictionary of labels to apply to the host. Computed internal labels are excluded from that list.


## See Also

* [rancher_host](https://www.terraform.io/docs/providers/rancher/r/host.html) in the _Terraform Provider Documentation_