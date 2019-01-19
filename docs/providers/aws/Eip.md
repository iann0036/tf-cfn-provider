# Terraform::AWS::Eip

Provides an Elastic IP resource.

~> **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.

~> **Note:** Do not use `network_interface` to associate the EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Contains the EIP allocation ID.

`PrivateIp` - Contains the private IP address (if in VPC).

`AssociateWithPrivateIp` - Contains the user specified private IP address.

`PublicIp` - Contains the public IP address.

`Instance` - Contains the ID of the attached instance.

`NetworkInterface` - Contains the ID of the attached network interface.

`PublicIpv4Pool` - EC2 IPv4 address pool identifier (if in VPC).

## See Also

* [aws_eip](https://www.terraform.io/docs/providers/aws/r/eip.html) in the _Terraform Provider Documentation_