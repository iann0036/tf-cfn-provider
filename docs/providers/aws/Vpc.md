# Terraform::AWS::Vpc

Provides an VPC resource.

## Properties

`CidrBlock` - (Required) The CIDR block for the VPC.

`InstanceTenancy` - (Optional) A tenancy option for instances launched into the VPC.

`EnableDnsSupport` - (Optional) A boolean flag to enable/disable DNS support in the VPC. Defaults true.

`EnableDnsHostnames` - (Optional) A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.

`EnableClassiclink` - (Optional) A boolean flag to enable/disable ClassicLink for the VPC. Only valid in regions and accounts that support EC2 Classic. See the [ClassicLink documentation][1] for more information. Defaults false.

`EnableClassiclinkDnsSupport` - (Optional) A boolean flag to enable/disable ClassicLink DNS Support for the VPC. Only valid in regions and accounts that support EC2 Classic.

`AssignGeneratedIpv6CidrBlock` - (Optional) Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block. Default is `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

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