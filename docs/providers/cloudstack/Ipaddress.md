# Terraform::CloudStack::Ipaddress

Acquires and associates a public IP.

## Properties

`IsPortable` - (Optional) This determines if the IP address should be transferable across zones (defaults false).

`NetworkId` - (Optional) The ID of the network for which an IP address should be acquired and associated. Changing this forces a new resource to be created.

`VpcId` - (Optional) The ID of the VPC for which an IP address should be acquired and associated. Changing this forces a new resource to be created.

`Zone` - (Optional) The name or ID of the zone for which an IP address should be acquired and associated. Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to deploy this instance to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the acquired and associated IP address.

`IpAddress` - The IP address that was acquired and associated.

## See Also

* [cloudstack_ipaddress](https://www.terraform.io/docs/providers/cloudstack/r/ipaddress.html) in the _Terraform Provider Documentation_