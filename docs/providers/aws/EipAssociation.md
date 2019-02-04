# Terraform::AWS::EipAssociation

Provides an AWS EIP Association as a top level resource, to associate and
disassociate Elastic IPs from AWS Instances and Network Interfaces.

~> **NOTE:** Do not use this resource to associate an EIP to `Terraform::AWS::Lb` or `awsNatGateway` resources. Instead use the `AllocationId` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

~> **NOTE:** `Terraform::AWS::EipAssociation` is useful in scenarios where EIPs are either
pre-existing or distributed to customers or users and therefore cannot be changed.

## Properties

`AllocationId` - (Optional) The allocation ID. This is required for EC2-VPC.

`AllowReassociation` - (Optional, Boolean) Whether to allow an Elastic IP to
be re-associated. Defaults to `true` in VPC.

`InstanceId` - (Optional) The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.

`NetworkInterfaceId` - (Optional) The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.

`PrivateIpAddress` - (Optional) The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.

`PublicIp` - (Optional) The Elastic IP address. This is required for EC2-Classic.


## Return Values

### Fn::GetAtt

`AssociationId` - The ID that represents the association of the Elastic IP.

`AllocationId` - As above.

`InstanceId` - As above.

`NetworkInterfaceId` - As above.

`PrivateIpAddress` - As above.

`PublicIp` - As above.

## See Also

* [aws_eip_association](https://www.terraform.io/docs/providers/aws/r/eip_association.html) in the _Terraform Provider Documentation_