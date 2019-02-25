# Terraform::AWS::DefaultSubnet

Provides a resource to manage a [default AWS VPC subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html#default-vpc-basics)
in the current region.

The `Terraform::AWS::DefaultSubnet` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management.

## Properties

`MapPublicIpOnLaunch` -  (Optional) Specify true to indicate
that instances launched into the subnet should be assigned
a public IP address.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the subnet.

`AvailabilityZone` - The AZ for the subnet.

`AvailabilityZoneId` - The AZ ID of the subnet.

`CidrBlock` - The CIDR block for the subnet.

`VpcId` - The VPC ID.

`Ipv6AssociationId` - The association ID for the IPv6 CIDR block.

`Ipv6CidrBlock` - The IPv6 CIDR block.

`OwnerId` - The ID of the AWS account that owns the subnet.

## See Also

* [aws_default_subnet](https://www.terraform.io/docs/providers/aws/r/default_subnet.html) in the _Terraform Provider Documentation_