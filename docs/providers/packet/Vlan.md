# Terraform::Packet::Vlan

Provides a resource to allow users to manage Virtual Networks in their projects. VLANs are used in [Layer 2 networking setup](https://packet.kayako.com/article/57-layer-2-overview).

## Properties

`ProjectId` - (Required) ID of parent project.

`Facility` - (Required) Facility where to create the VLAN.

`Description` - Description string.


## Return Values

### Fn::GetAtt

`Vxlan` - VXLAN segment ID.

## See Also

* [packet_vlan](https://www.terraform.io/docs/providers/packet/r/vlan.html) in the _Terraform Provider Documentation_