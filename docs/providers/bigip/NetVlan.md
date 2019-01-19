# Terraform::BIGIP::NetVlan

`Terraform::BIGIP::NetVlan` Manages a vlan configuration

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the vlan.

`Tag` - (Optional) Specifies a number that the system adds into the header of any frame passing through the VLAN.

`Interfaces` - (Optional) Specifies which interfaces you want this VLAN to use for traffic management.

`Vlanport` - Physical or virtual port used for traffic.

`Tagged` - Specifies a list of tagged interfaces or trunks associated with this VLAN. Note that you can associate tagged interfaces or trunks with any number of VLANs.


## See Also

* [bigip_net_vlan](https://www.terraform.io/docs/providers/bigip/r/net_vlan.html) in the _Terraform Provider Documentation_