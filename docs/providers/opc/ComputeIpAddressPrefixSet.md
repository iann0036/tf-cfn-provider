# Terraform::OPC::ComputeIpAddressPrefixSet

The ``Terraform::OPC::ComputeIpAddressPrefixSet`` resource creates and manages an IP address prefix set in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The name of the ip address prefix set.

`Prefixes` - (Optional) List of CIDR IPv4 prefixes assigned in the virtual network.

`Description` - (Optional) A description of the ip address prefix set.

`Tags` - (Optional) List of tags that may be applied to the ip address prefix set.

`Uri` - (Computed) The Uniform Resource Identifier of the ip address prefix set.


## See Also

* [opc_compute_ip_address_prefix_set](https://www.terraform.io/docs/providers/opc/r/compute_ip_address_prefix_set.html) in the _Terraform Provider Documentation_