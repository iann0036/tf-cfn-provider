# Terraform::Triton::Vlan

The `Terraform::Triton::Vlan` resource represents an Triton VLAN. A VLAN provides a low level way to segregate and subdivide the network. Traffic on one VLAN cannot, _on its own_, reach another VLAN.

## Properties

`VlanId` - (int, Required, Change forces new resource)
Number between 0-4095 indicating VLAN ID.

`Name` - (string, Required)
Unique name to identify VLAN.

`Description` - (string, Optional)
Description of the VLAN.


## See Also

* [triton_vlan](https://www.terraform.io/docs/providers/triton/r/vlan.html) in the _Terraform Provider Documentation_