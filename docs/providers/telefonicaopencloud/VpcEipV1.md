# Terraform::TelefonicaOpenCloud::VpcEipV1

Manages a V1 EIP resource within Telefonica Open Cloud VPC.

## Properties

`Region` - (Optional) The region in which to create the eip. If omitted, the `Region` argument of the provider is used. Changing this creates a new eip.

`Publicip` - (Required) The elastic IP address object.

`Bandwidth` - (Required) The bandwidth object.

`Type` - (Required) The value must be a type supported by the system. Only `5_bgp` supported now. Changing this creates a new eip.

`IpAddress` - (Optional) The value must be a valid IP address in the available IP address segment. Changing this creates a new eip.

`PortId` - (Optional) The port id which this eip will associate with. If the value is "" or this not specified, the eip will be in unbind state.

`Name` - (Required) The bandwidth name, which is a string of 1 to 64 characters that contain letters, digits, underscores (_), and hyphens (-).

`Size` - (Required) The bandwidth size. The value ranges from 1 to 300 Mbit/s.

`ChargeType` - (Required) Whether the bandwidth is shared or exclusive. Changing this creates a new eip.

`ChargeMode` - (Optional) This is a reserved field. If the system supports charging by traffic and this field is specified, then you are charged by traffic for elastic IP addresses. Changing this creates a new eip.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Publicip/type` - See Properties above.

`Publicip/ipAddress` - See Properties above.

`Publicip/portId` - See Properties above.

`Bandwidth/name` - See Properties above.

`Bandwidth/size` - See Properties above.

`Bandwidth/chargeType` - See Properties above.

`Bandwidth/chargeMode` - See Properties above.

## See Also

* [telefonicaopencloud_vpc_eip_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/vpc_eip_v1.html) in the _Terraform Provider Documentation_