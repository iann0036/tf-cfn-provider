# Terraform::Docker::Image

Pulls a Docker image to a given Docker host from a Docker Registry.

This resource will *not* pull new layers of the image automatically unless used in
conjunction with [`docker_registry_image`](/docs/providers/docker/d/registry_image.html)
data source to update the `pull_triggers` field.

## Properties

TBC

## See Also

* [docker_image](https://www.terraform.io/docs/providers/docker/r/image.html) in the _Terraform Provider Documentation_