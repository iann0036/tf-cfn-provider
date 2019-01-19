# Terraform::AWS::VpcDhcpOptionsAssociation

Provides a VPC DHCP Options Association resource.

## Properties

`VpcId` - (Required) The ID of the VPC to which we would like to associate a DHCP Options Set.

`DhcpOptionsId` - (Required) The ID of the DHCP Options Set to associate to the VPC.


## Return Values

### Fn::GetAtt

`Id` - The ID of the DHCP Options Set Association.

## See Also

* [aws_vpc_dhcp_options_association](https://www.terraform.io/docs/providers/aws/r/vpc_dhcp_options_association.html) in the _Terraform Provider Documentation_