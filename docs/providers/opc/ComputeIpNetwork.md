# Terraform::OPC::ComputeIpNetwork

The ``opc_compute_ip_network`` resource creates and manages an IP Network in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Name` - The name of the IP Network.

`IpAddressPrefix` - The IPv4 address prefix, in CIDR format.

`Description` - The description of the IP Network.

`IpNetworkExchange` - The IP Network Exchange for the IP Network.

`PublicNaptEnabled` - Whether public internet access using NAPT for VNICs without any public IP Reservation or not.

`Uri` - Uniform Resource Identifier for the IP Network.

## See Also

* [opc_compute_ip_network](https://www.terraform.io/docs/providers/opc/r/compute_ip_network.html) in the _Terraform Provider Documentation_