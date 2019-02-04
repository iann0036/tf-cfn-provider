# Terraform::OVH::PubliccloudPrivateNetwork

__DEPRECATED__ use `Terraform::OVH::CloudNetworkPrivate` instead.
Creates a private network in a public cloud project.

## Properties

`ProjectId` - (Required) The id of the public cloud project. If omitted,
the `OVH_PROJECT_ID` environment variable is used.

`Name` - (Required) The name of the network.

`VlanId` - a vlan id to associate with the network.
Changing this value recreates the resource. Defaults to 0.

`Regions` - an array of valid OVH public cloud region ID in which the network
will be available. Ex.: "GRA1". Defaults to all public cloud regions.


## Return Values

### Fn::GetAtt

`ProjectId` - See Properties above.

`Name` - See Properties above.

`VlanId` - See Properties above.

`Regions` - See Properties above.

`RegionsStatus` - A map representing the status of the network per region.

`RegionsStatus/region` - The id of the region.

`RegionsStatus/status` - The status of the network in the region.

`Status` - the status of the network. should be normally set to 'ACTIVE'.

`Type` - the type of the network. Either 'private' or 'public'.

## See Also

* [ovh_publiccloud_private_network](https://www.terraform.io/docs/providers/ovh/r/publiccloud_private_network.html) in the _Terraform Provider Documentation_