# Terraform::CloudStack::PrivateGateway

Creates a private gateway for the given VPC.

*NOTE: private gateway can only be created using a ROOT account!*

## Properties

`Gateway` - (Required) the gateway of the Private gateway. Changing this forces a new resource to be created.

`IpAddress` - (Required) the IP address of the Private gateway. Changing this forces a new resource to be created.

`Netmask` - (Required) The netmask of the Private gateway. Changing this forces a new resource to be created.

`Vlan` - (Required) The VLAN number (1-4095) the network will use.

`PhysicalNetworkId` - (Optional) The ID of the physical network this private gateway belongs to.

`NetworkOffering` - (Optional) The name or ID of the network offering to use for the private gateways network connection.

`AclId` - (Required) The ACL ID that should be attached to the network.

`VpcId` - (Required) The VPC ID in which to create this Private gateway. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the private gateway.

## See Also

* [cloudstack_private_gateway](https://www.terraform.io/docs/providers/cloudstack/r/private_gateway.html) in the _Terraform Provider Documentation_