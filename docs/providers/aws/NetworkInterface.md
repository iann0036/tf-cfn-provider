# Terraform::AWS::NetworkInterface

Provides an Elastic network interface (ENI) resource.

## Properties

`SubnetId` - (Required) Subnet ID to create the ENI in.

`Description` - (Optional) A description for the network interface.

`PrivateIps` - (Optional) List of private IPs to assign to the ENI.

`PrivateIpsCount` - (Optional) Number of private IPs to assign to the ENI.

`SecurityGroups` - (Optional) List of security group IDs to assign to the ENI.

`Attachment` - (Optional) Block to define the attachment of the ENI. Documented below.

`SourceDestCheck` - (Optional) Whether to enable source destination checking for the ENI. Default true.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Instance` - (Required) ID of the instance to attach to.

`DeviceIndex` - (Required) Integer to define the devices index.


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