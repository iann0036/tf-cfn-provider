# Terraform::AWS::Vpc

Provides an VPC resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - Amazon Resource Name (ARN) of VPC.

`Id` - The ID of the VPC.

`CidrBlock` - The CIDR block of the VPC.

`InstanceTenancy` - Tenancy of instances spin up within VPC.

`EnableDnsSupport` - Whether or not the VPC has DNS support.

`EnableDnsHostnames` - Whether or not the VPC has DNS hostname support.

`EnableClassiclink` - Whether or not the VPC has Classiclink enabled.

`MainRouteTableId` - The ID of the main route table associated with.

`DefaultNetworkAclId` - The ID of the network ACL created by default on VPC creation.

`DefaultSecurityGroupId` - The ID of the security group created by default on VPC creation.

`DefaultRouteTableId` - The ID of the route table created by default on VPC creation.

`Ipv6AssociationId` - The association ID for the IPv6 CIDR block.

`Ipv6CidrBlock` - The IPv6 CIDR block.

`OwnerId` - The ID of the AWS account that owns the VPC.

## See Also

* [aws_vpc](https://www.terraform.io/docs/providers/aws/r/vpc.html) in the _Terraform Provider Documentation_