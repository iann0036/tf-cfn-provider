# Terraform::OVH::PubliccloudPrivateNetwork

__DEPRECATED__ use `ovh_cloud_network_private` instead.
Creates a private network in a public cloud project.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ProjectId` - See Argument Reference above.

`Name` - See Argument Reference above.

`VlanId` - See Argument Reference above.

`Regions` - See Argument Reference above.

`RegionsStatus` - A map representing the status of the network per region.

`RegionsStatus/region` - The id of the region.

`RegionsStatus/status` - The status of the network in the region.

`Status` - the status of the network. should be normally set to 'ACTIVE'.

`Type` - the type of the network. Either 'private' or 'public'.

## See Also

* [ovh_publiccloud_private_network](https://www.terraform.io/docs/providers/ovh/r/publiccloud_private_network.html) in the _Terraform Provider Documentation_