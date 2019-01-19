# Terraform::Triton::Fabric

The `Terraform::Triton::Fabric` resource represents an fabric for a Triton account. The fabric is a logical set of interconnected switches.

## Properties

`Name` - (String, Required, Change forces new resource) Network name.

`Description` - (String, Optional, Change forces new resource) Optional description of network.

`Subnet` - (String, Required, Change forces new resource) CIDR formatted string describing network.

`ProvisionStartIp` - (String, Required, Change forces new resource) First IP on the network that can be assigned.

`ProvisionEndIp` - (String, Required, Change forces new resource) Last assignable IP on the network.

`Gateway` - (String, Optional, Change forces new resource) Optional gateway IP.

`Resolvers` - (List, Optional) Array of IP addresses for resolvers.

`Routes` - (Map, Optional, Change forces new resource) Map of CIDR block to Gateway IP address.

`InternetNat` - (Bool, Optional, Change forces new resource) If a NAT zone is provisioned at Gateway IP address. Default is `true`.

`VlanId` - (Int, Required, Change forces new resource) VLAN id the network is on. Number between 0-4095 indicating VLAN ID.


## See Also

* [triton_fabric](https://www.terraform.io/docs/providers/triton/r/fabric.html) in the _Terraform Provider Documentation_