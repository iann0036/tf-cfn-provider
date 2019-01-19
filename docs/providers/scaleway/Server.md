# Terraform::Scaleway::Server

Provides servers. This allows servers to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#servers).

## Properties

`Name` - (Required) name of server.

`Image` - (Required) base image of server.

`Type` - (Required) type of server.

`Bootscript` - (Optional) server bootscript.

`BootType` - (Optional) the boot mechanism for this server. Possible values include `local` and `Bootscript`.

`Tags` - (Optional) list of tags for server.

`EnableIpv6` - (Optional) enable ipv6.

`DynamicIpRequired` - (Optional) make server publicly available.

`PublicIp` - (Optional) set a public ip previously created (a real ip is expected here, not its resource id).

`SecurityGroup` - (Optional) assign security group to server.

`Volume` - (Optional) attach additional volumes to your instance (see below).

`PublicIpv6` - (Read Only) if `EnableIpv6` is set this contains the ipv6 address of your instance.

`State` - (Optional) allows you to define the desired state of your server. Valid values include (`stopped`, `running`).

`Cloudinit` - (Optional) allows you to define cloudinit script for this server.

`StateDetail` - (Read Only) contains details from the scaleway API the state of your instance.


## Return Values

### Fn::GetAtt

`Id` - id of the new resource.

`PrivateIp` - private ip of the new resource.

`PublicIp` - public ip of the new resource.

## See Also

* [scaleway_server](https://www.terraform.io/docs/providers/scaleway/r/server.html) in the _Terraform Provider Documentation_