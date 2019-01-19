# Terraform::CloudStack::Vpc

Creates a VPC.

## Properties

`Name` - (Required) The name of the VPC.

`DisplayText` - (Optional) The display text of the VPC.

`Cidr` - (Required) The CIDR block for the VPC. Changing this forces a new resource to be created.

`VpcOffering` - (Required) The name or ID of the VPC offering to use for this VPC. Changing this forces a new resource to be created.

`NetworkDomain` - (Optional) The default DNS domain for networks created in this VPC. Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to deploy this instance to. Changing this forces a new resource to be created.

`Zone` - (Required) The name or ID of the zone where this disk volume will be available. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC.

`DisplayText` - The display text of the VPC.

`SourceNatIp` - The source NAT IP assigned to the VPC.

## See Also

* [cloudstack_vpc](https://www.terraform.io/docs/providers/cloudstack/r/vpc.html) in the _Terraform Provider Documentation_