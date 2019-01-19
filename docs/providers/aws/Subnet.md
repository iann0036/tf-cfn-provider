# Terraform::AWS::Subnet

Provides an VPC subnet resource.

## Properties

`AvailabilityZone` - (Optional) The AZ for the subnet.

`AvailabilityZoneId` - (Optional) The AZ ID of the subnet.

`CidrBlock` - (Required) The CIDR block for the subnet.

`Ipv6CidrBlock` - (Optional) The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.

`MapPublicIpOnLaunch` -  (Optional) Specify true to indicate that instances launched into the subnet should be assigned a public IP address. Default is `false`.

`AssignIpv6AddressOnCreation` - (Optional) Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is `false`.

`VpcId` - (Required) The VPC ID.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the subnet.

`Arn` - The ARN of the subnet.

`Ipv6CidrBlockAssociationId` - The association ID for the IPv6 CIDR block.

`OwnerId` - The ID of the AWS account that owns the subnet.

## See Also

* [aws_subnet](https://www.terraform.io/docs/providers/aws/r/subnet.html) in the _Terraform Provider Documentation_