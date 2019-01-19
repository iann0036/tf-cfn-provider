# Terraform::OPC::ComputeIpAddressReservation

The ``Terraform::OPC::ComputeIpAddressReservation`` resource creates and manages an IP address reservation in an Oracle Cloud Infrastructure Compute Classic identity domain, for an IP Network.

## Properties

`Name` - (Required) The name of the ip address reservation.

`IpAddressPool` - (Required) The IP address pool from which you want to reserve an IP address. Typically one of either `public-ippool` or `cloud-ippool`.

`Description` - (Optional) A description of the ip address reservation.

`Tags` - (Optional) List of tags that may be applied to the IP address reservation.

`IpAddress` - Reserved NAT IPv4 address from the IP address pool.

`Uri` - The Uniform Resource Identifier of the ip address reservation.


## See Also

* [opc_compute_ip_address_reservation](https://www.terraform.io/docs/providers/opc/r/compute_ip_address_reservation.html) in the _Terraform Provider Documentation_