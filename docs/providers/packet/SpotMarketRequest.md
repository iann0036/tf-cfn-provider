# Terraform::Packet::SpotMarketRequest

Provides a Packet Spot Market Request resource to allow you to
manage spot market requests on your account. https://help.packet.net/en-us/article/20-spot-market

## Properties

`DevicesMax` - (Required) Maximum number devices to be created.

`DevicesMin` - (Required) Miniumum number devices to be created.

`MaxBidPrice` - (Required) Maximum price user is willing to pay per hour per device.

`Facilities` - (Required) Facility IDs where devices should be created.

`InstanceParameters` - (Required) Device parameters. See device resource for details.

`ProjectId` - (Required) Project ID.

`WaitForDevices` - (Optional) On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Spot Market Request.

## See Also

* [packet_spot_market_request](https://www.terraform.io/docs/providers/packet/r/spot_market_request.html) in the _Terraform Provider Documentation_