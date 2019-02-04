# Terraform::Docker::Volume

Creates and destroys a volume in Docker. This can be used alongside
[docker\_container](/docs/providers/docker/r/container.html)
to prepare volumes that can be shared across containers.

## Properties

`Name` - (Optional, string) The name of the Docker volume (generated if not
provided).

`Labels` - (Optional, map of string/string key/value pairs) User-defined key/value metadata.

`Driver` - (Optional, string) Driver type for the volume (defaults to local).

`DriverOpts` - (Optional, map of strings) Options specific to the driver.


## See Also

* [docker_volume](https://www.terraform.io/docs/providers/docker/r/volume.html) in the _Terraform Provider Documentation_