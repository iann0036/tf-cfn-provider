# Terraform::Packet::Volume

Provides a Packet Block Storage Volume resource to allow you to
manage block volumes on your account.
Once created by Terraform, they must then be attached and mounted
using the api and `packet_block_attach` and `packet_block_detach`
scripts.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The unique ID of the volume.

`Name` - The name of the volume.

`Description` - The description of the volume.

`Size` - The size in GB of the volume.

`Plan` - Performance plan the volume is on.

`BillingCycle` - The billing cycle, defaults to hourly.

`Facility` - The facility slug the volume resides in.

`State` - The state of the volume.

`Locked` - Whether the volume is locked or not.

`ProjectId ` - The project id the volume is in.

`Attachments` - A list of attachments, each with it's own `href` attribute.

`Created` - The timestamp for when the volume was created.

`Updated` - The timestamp for the last time the volume was updated.

## See Also

* [packet_volume](https://www.terraform.io/docs/providers/packet/r/volume.html) in the _Terraform Provider Documentation_