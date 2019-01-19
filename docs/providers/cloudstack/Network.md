# Terraform::CloudStack::Network

Creates a network.

## Properties

`Name` - (Required) The name of the network.

`DisplayText` - (Optional) The display text of the network.

`Cidr` - (Required) The CIDR block for the network. Changing this forces a new resource to be created.

`Gateway` - (Optional) Gateway that will be provided to the instances in this network. Defaults to the first usable IP in the range.

`Startip` - (Optional) Start of the IP block that will be available on the network. Defaults to the second available IP in the range.

`Endip` - (Optional) End of the IP block that will be available on the network. Defaults to the last available IP in the range.

`NetworkDomain` - (Optional) DNS domain for the network.

`NetworkOffering` - (Required) The name or ID of the network offering to use for this network.

`Vlan` - (Optional) The VLAN number (1-4095) the network will use. This might be required by the Network Offering if specifyVlan=true is set. Only the ROOT admin can set this value.

`VpcId` - (Optional) The VPC ID in which to create this network. Changing this forces a new resource to be created.

`AclId` - (Optional) The ACL ID that should be attached to the network or `none` if you do not want to attach an ACL. You can dynamically attach and swap ACL's, but if you want to detach an attached ACL and revert to using `none`, this will force a new resource to be created. (defaults `none`).

`Project` - (Optional) The name or ID of the project to deploy this instance to. Changing this forces a new resource to be created.

`SourceNatIp` - (Optional) If set to `true` a public IP will be associated with the network. This is mainly used when the network supports the source NAT service which claims the first associated IP address. This prevents the ability to manage the IP address as an independent entity.

`Zone` - (Required) The name or ID of the zone where this network will be available. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the network.

`DisplayText` - The display text of the network.

`NetworkDomain` - DNS domain for the network.

`SourceNatIpId` - The ID of the associated source NAT IP.

## See Also

* [cloudstack_network](https://www.terraform.io/docs/providers/cloudstack/r/network.html) in the _Terraform Provider Documentation_