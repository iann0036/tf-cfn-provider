# Terraform::AWS::Eip

Provides an Elastic IP resource.

~> **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.

~> **Note:** Do not use `NetworkInterface` to associate the EIP to `Terraform::AWS::Lb` or `awsNatGateway` resources. Instead use the `allocationId` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

## Properties

`Vpc` - (Optional) Boolean if the EIP is in a VPC or not.

`Instance` - (Optional) EC2 instance ID.

`NetworkInterface` - (Optional) Network interface ID to associate with.

`AssociateWithPrivateIp` - (Optional) A user specified primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`PublicIpv4Pool` - (Optional) EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.


## Return Values

### Fn::GetAtt

`Id` - Contains the EIP allocation ID.

`PrivateIp` - Contains the private IP address (if in VPC).

`AssociateWithPrivateIp` - Contains the user specified private IP address.

`PublicIp` - Contains the public IP address.

`Instance` - Contains the ID of the attached instance.

`NetworkInterface` - Contains the ID of the attached network interface.

`PublicIpv4Pool` - EC2 IPv4 address pool identifier (if in VPC).

## See Also

* [aws_eip](https://www.terraform.io/docs/providers/aws/r/eip.html) in the _Terraform Provider Documentation_