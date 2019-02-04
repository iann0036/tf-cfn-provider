# Terraform::Docker::Container

Manages the lifecycle of a Docker container.

## Properties

`Name` - (Required, string) The name of the Docker container.

`Image` - (Required, string) The ID of the image to back this container.
The easiest way to get this value is to use the `Terraform::Docker::Image` resource
as is shown in the example above.

`Command` - (Optional, list of strings) The command to use to start the
container. For example, to run `/usr/bin/myprogram -f baz.conf` set the
command to be `["/usr/bin/myprogram", "-f", "baz.conf"]`.

`Entrypoint` - (Optional, list of strings) The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run `/usr/bin/myprogram`
when starting a container, set the entrypoint to be
`["/usr/bin/myprogram"]`.

`User` - (Optional, string) User used for run the first process. Format is
`User` or `user:group` which user and group can be passed literraly or
by name.

`Dns` - (Optional, set of strings) Set of DNS servers.

`DnsOpts` - (Optional, set of strings) Set of DNS options used by the DNS provider(s), see `resolv.conf` documentation for valid list of options.

`DnsSearch` - (Optional, set of strings) Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.

`Env` - (Optional, set of strings) Environment variables to set.

`Labels` - (Optional, map of strings) Key/value pairs to set as labels on the
container.

`Links` - (Optional, set of strings) Set of links for link based
connectivity between containers that are running on the same host.

`Hostname` - (Optional, string) Hostname of the container.

`Domainname` - (Optional, string) Domain name of the container.

`Restart` - (Optional, string) The restart policy for the container. Must be
one of "no", "on-failure", "always", "unless-stopped".

`MaxRetryCount` - (Optional, int) The maximum amount of times to an attempt
a restart when `Restart` is set to "on-failure".

`Rm` - (Optional, bool) If true, then the container will be automatically removed after his execution. Terraform
won't check this container after creation.

`Start` - (Optional, bool) If true, then the Docker container will be
started after creation. If false, then the container is only created.

`Attach` - (Optional, bool) If true attach to the container after its creation and waits the end of his execution.

`Logs` - (Optional, bool) Save the container logs (`Attach` must be enabled).

`MustRun` - (Optional, bool) If true, then the Docker container will be
kept running. If false, then as long as the container exists, Terraform
assumes it is successful.

`Capabilities` - (Optional, block) See [Capabilities](#capabilities) below for details.

`Ports` - (Optional, block) See [Ports](#ports) below for details.

`Host` - (Optional, block) See [Extra Hosts](#extra_hosts) below for
details.

`Privileged` - (Optional, bool) Run container in privileged mode.

`Devices` - (Optional, bool) See [Devices](#devices) below for details.

`PublishAllPorts` - (Optional, bool) Publish all ports of the container.

`Volumes` - (Optional, block) See [Volumes](#volumes) below for details.

`Memory` - (Optional, int) The memory limit for the container in MBs.

`MemorySwap` - (Optional, int) The total memory limit (memory + swap) for the
container in MBs. This setting may compute to `-1` after `terraform apply` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

`CpuShares` - (Optional, int) CPU shares (relative weight) for the container.

`CpuSet` - (Optional, string) A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. `0-1`.

`LogDriver` - (Optional, string) The logging driver to use for the container.
Defaults to "json-file".

`LogOpts` - (Optional, map of strings) Key/value pairs to use as options for
the logging driver.

`NetworkAlias` - (Optional, set of strings) Network aliases of the container for user-defined networks only. *Deprecated:* use `NetworksAdvanced` instead.

`NetworkMode` - (Optional, string) Network mode of the container.

`Networks` - (Optional, set of strings) Id of the networks in which the
container is. *Deprecated:* use `NetworksAdvanced` instead.

`NetworksAdvanced` - (Optional, block) See [Networks Advanced](#networks_advanced) below for details. If this block has priority to the deprecated `NetworkAlias` and `network` properties.

`DestroyGraceSeconds` - (Optional, int) If defined will attempt to stop the container before destroying. Container will be destroyed after `n` seconds or on successful stop.

`Upload` - (Optional, block) See [File Upload](#upload) below for details.

`Ulimit` - (Optional, block) See [Ulimits](#ulimits) below for
details.

`PidMode` - (Optional, string) The PID (Process) Namespace mode for the container. Either `container:<name|id>` or `Host`.

`UsernsMode` - (Optional, string) Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

`Healthcheck` - (Optional, block) See [Healthcheck](#healthcheck) below for details.


## Return Values

### Fn::GetAtt

`ExitCode` - The exit code of the container if its execution is done (`MustRun` must be disabled).

`ContainerLogs` - The logs of the container if its execution is done (`Attach` must be disabled).

`NetworkData` - (Map of a block) The IP addresses of the container on each.

`IpAddress` - *Deprecated:* Use `network_data` instead. The IP address of the container's first network it.

`IpPrefixLength` - *Deprecated:* Use `network_data` instead. The IP prefix length of the container as read from its.

`Gateway` - *Deprecated:* Use `network_data` instead. The network gateway of the container as read from its.

`Bridge` - The network bridge of the container as read from its NetworkSettings.

## See Also

* [docker_container](https://www.terraform.io/docs/providers/docker/r/container.html) in the _Terraform Provider Documentation_