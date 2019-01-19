# Terraform::Docker::Secret

Manages the secrets of a Docker service in a swarm.

## Properties

`Name` - (Required, string) The name of the Docker secret.

`Data` - (Required, string) The base64 encoded data of the secret.

`Labels` - (Optional, map of string/string key/value pairs) User-defined key/value metadata.


## See Also

* [docker_secret](https://www.terraform.io/docs/providers/docker/r/secret.html) in the _Terraform Provider Documentation_