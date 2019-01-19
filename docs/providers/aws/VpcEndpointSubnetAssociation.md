# Terraform::AWS::VpcEndpointSubnetAssociation

Provides a resource to create an association between a VPC endpoint and a subnet.

~> **NOTE on VPC Endpoints and VPC Endpoint Subnet Associations:** Terraform provides
both a standalone VPC Endpoint Subnet Association (an association between a VPC endpoint
and a single `SubnetId`) and a [VPC Endpoint](vpc_endpoint.html) resource with a `subnet_ids`
attribute. Do not use the same subnet ID in both a VPC Endpoint resource and a VPC Endpoint Subnet
Association resource. Doing so will cause a conflict of associations and will overwrite the association.

## Properties

`VpcEndpointId` - (Required) The ID of the VPC endpoint with which the subnet will be associated.

`SubnetId` - (Required) The ID of the subnet to be associated with the VPC endpoint.


## Return Values

### Fn::GetAtt

`Id` - The ID of the association.

## See Also

* [aws_vpc_endpoint_subnet_association](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_subnet_association.html) in the _Terraform Provider Documentation_