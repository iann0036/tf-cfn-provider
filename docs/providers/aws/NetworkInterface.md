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

### Attachment Properties

`Instance` - (Required) ID of the instance to attach to.

`DeviceIndex` - (Required) Integer to define the devices index.


## Return Values

### Fn::GetAtt

`PrivateIps` - List of private IPs assigned to the ENI.

`Tags` - Tags assigned to the ENI.

`SubnetId` - Subnet ID the ENI is in.

`SourceDestCheck` - Whether source destination checking is enabled.

`Attachment` - Block defining the attachment of the ENI.

`Id` - The ID of the network interface.

`SecurityGroups` - List of security groups attached to the ENI.

`Description` - A description for the network interface.

## See Also

* [aws_network_interface](https://www.terraform.io/docs/providers/aws/r/network_interface.html) in the _Terraform Provider Documentation_