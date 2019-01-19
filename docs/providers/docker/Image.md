# Terraform::Docker::Image

Pulls a Docker image to a given Docker host from a Docker Registry.

This resource will *not* pull new layers of the image automatically unless used in
conjunction with [`Terraform::Docker::RegistryImage`](/docs/providers/docker/d/registry_image.html)
data source to update the `PullTriggers` field.

## Properties

`Name` - (Required, string) The name of the Docker image, including any tags or SHA256 repo digests.

`KeepLocally` - (Optional, boolean) If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker local storage on destroy operation.

`PullTriggers` - (Optional, list of strings) List of values which cause an image pull when changed. This is used to store the image digest from the registry when using the `Terraform::Docker::RegistryImage` [data source](/docs/providers/docker/d/registry_image.html) to trigger an image update.

`PullTrigger` - **Deprecated**, use `PullTriggers` instead.


## See Also

* [docker_image](https://www.terraform.io/docs/providers/docker/r/image.html) in the _Terraform Provider Documentation_