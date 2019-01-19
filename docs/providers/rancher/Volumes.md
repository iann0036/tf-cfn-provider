# Terraform::Rancher::Volumes

Provides a Rancher Volume resource. This can be used to create volumes for rancher environments and retrieve their information.

## Properties

`Name` - (Required) The name of the volume.

`Description` - (Optional) A description of the volume.

`EnvironmentId` - (Required) The ID of the environment to create the volume for.

`Driver` - (Required) The volume driver.


## See Also

* [rancher_volumes](https://www.terraform.io/docs/providers/rancher/r/volumes.html) in the _Terraform Provider Documentation_