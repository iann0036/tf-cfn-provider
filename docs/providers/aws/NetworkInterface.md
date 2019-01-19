# Terraform::AWS::NetworkInterface

Provides an Elastic network interface (ENI) resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the network interface.

`SubnetId` - Subnet ID the ENI is in.

`Description` - A description for the network interface.

`PrivateIps` - List of private IPs assigned to the ENI.

`SecurityGroups` - List of security groups attached to the ENI.

`Attachment` - Block defining the attachment of the ENI.

`SourceDestCheck` - Whether source destination checking is enabled.

`Tags` - Tags assigned to the ENI.

## See Also

* [aws_network_interface](https://www.terraform.io/docs/providers/aws/r/network_interface.html) in the _Terraform Provider Documentation_