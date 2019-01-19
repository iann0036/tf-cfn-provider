# Terraform::OPC::ComputeIpAddressAssociation

The ``Terraform::OPC::ComputeIpAddressAssociation`` resource creates and manages an IP address association between an IP address reservation and a virtual NIC in an Oracle Cloud Infrastructure Compute Classic identity domain, for an IP Network.

## Properties

`Name` - (Required) The name of the ip address association.

`IpAddressReservation` - (Optional) The name of the NAT IP address reservation.

`Vnic` - (Optional) The name of the virtual NIC associated with this NAT IP reservation.

`Description` - (Optional) A description of the ip address association.

`Tags` - (Optional) List of tags that may be applied to the ip address association.

`Uri` - (Computed) The Uniform Resource Identifier of the ip address association.


## See Also

* [opc_compute_ip_address_association](https://www.terraform.io/docs/providers/opc/r/compute_ip_address_association.html) in the _Terraform Provider Documentation_