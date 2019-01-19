# Terraform::Skytap::Network

Provides a Skytap Network resource. Networks are not top-level elements of the Skytap API.
Rather, they are elements properly contained within an environment.
Operations on them are implicitly on the containing environment.

## Properties

`EnvironmentId` - (Required, Force New) ID of the environment you want to attach the network to. If updating with a new one then the network will be recreated.

`Name` - (Required) User-defined name of the network. Limited to 255 characters. UTF-8 character type.

`Domain` - (Required) Domain name for the Skytap network. Limited to 64 characters.

`Subnet` - (Required) Defines the subnet address and subnet mask size in CIDR format (for example, 10.0.0.0/24). IP addresses for the VMs are assigned from this subnet and standard network services (DNS resolution, CIFS share, routes to Internet) are defined appropriately for it.

`Gateway` - (Optional, Computed) Gateway IP address.

`Tunnelable` - (Optional) If true, this network can be connected to other networks.


## See Also

* [skytap_network](https://www.terraform.io/docs/providers/skytap/r/network.html) in the _Terraform Provider Documentation_