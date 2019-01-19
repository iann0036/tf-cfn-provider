# Terraform::Docker::Network

Manages a Docker Network. This can be used alongside
[docker\_container](/docs/providers/docker/r/container.html)
to create virtual networks within the docker environment.

## Properties

`Name` - (Required, string) The name of the Docker network.

`Labels` - (Optional, map of string/string key/value pairs) User-defined key/value metadata.

`CheckDuplicate` - (Optional, boolean) Requests daemon to check for networks with same name.

`Driver` - (Optional, string) Name of the network driver to use. Defaults to `bridge` driver.

`Options` - (Optional, map of strings) Network specific options to be used by the drivers.

`Internal` - (Optional, boolean) Restrict external access to the network. Defaults to `false`.

`Attachable` - (Optional, boolean) Enable manual container attachment to the network. Defaults to `false`.

`Ingress` - (Optional, boolean) Create swarm routing-mesh network. Defaults to `false`.

`Ipv6` - (Optional, boolean) Enable IPv6 networking. Defaults to `false`.

`IpamDriver` - (Optional, string) Driver used by the custom IP scheme of the network.

`IpamConfig` - (Optional, block) See [IPAM config](#ipam_config) below for details.


## See Also

* [docker_network](https://www.terraform.io/docs/providers/docker/r/network.html) in the _Terraform Provider Documentation_