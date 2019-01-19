# Terraform::AWS::EipAssociation

Provides an AWS EIP Association as a top level resource, to associate and
disassociate Elastic IPs from AWS Instances and Network Interfaces.

~> **NOTE:** Do not use this resource to associate an EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

~> **NOTE:** `aws_eip_association` is useful in scenarios where EIPs are either
pre-existing or distributed to customers or users and therefore cannot be changed.

## Properties

TBC

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