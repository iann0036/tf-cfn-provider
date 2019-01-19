# Terraform::Docker::Container

Manages the lifecycle of a Docker container.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ExitCode` - The exit code of the container if its execution is done (`must_run` must be disabled).

`ContainerLogs` - The logs of the container if its execution is done (`attach` must be disabled).

`NetworkData` - (Map of a block) The IP addresses of the container on each.

`IpAddress` - *Deprecated:* Use `network_data` instead. The IP address of the container's first network it.

`IpPrefixLength` - *Deprecated:* Use `network_data` instead. The IP prefix length of the container as read from its.

`Gateway` - *Deprecated:* Use `network_data` instead. The network gateway of the container as read from its.

`Bridge` - The network bridge of the container as read from its NetworkSettings.

## See Also

* [docker_container](https://www.terraform.io/docs/providers/docker/r/container.html) in the _Terraform Provider Documentation_