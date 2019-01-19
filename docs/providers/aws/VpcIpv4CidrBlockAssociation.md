# Terraform::AWS::VpcIpv4CidrBlockAssociation

Provides a resource to associate additional IPv4 CIDR blocks with a VPC.

When a VPC is created, a primary IPv4 CIDR block for the VPC must be specified.
The `aws_vpc_ipv4_cidr_block_association` resource allows further IPv4 CIDR blocks to be added to the VPC.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPC CIDR association.

## See Also

* [aws_vpc_ipv4_cidr_block_association](https://www.terraform.io/docs/providers/aws/r/vpc_ipv4_cidr_block_association.html) in the _Terraform Provider Documentation_