# Terraform::AWS::VpcPeeringConnection

Provides a resource to manage a VPC peering connection.

~> **NOTE on VPC Peering Connections and VPC Peering Connection Options:** Terraform provides
both a standalone [VPC Peering Connection Options](vpc_peering_options.html) and a VPC Peering Connection
resource with `accepter` and `requester` attributes. Do not manage options for the same VPC peering
connection in both a VPC Peering Connection resource and a VPC Peering Connection Options resource.
Doing so will cause a conflict of options and will overwrite the options.
Using a VPC Peering Connection Options resource decouples management of the connection options from
management of the VPC Peering Connection and allows options to be set correctly in cross-account scenarios.

-> **Note:** For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region
VPC Peering Connections use the `aws_vpc_peering_connection` resource to manage the requester's side of the
connection and use the `aws_vpc_peering_connection_accepter` resource to manage the accepter's side of the connection.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC Peering Connection.

`AcceptStatus` - The status of the VPC Peering Connection request.

## See Also

* [aws_vpc_peering_connection](https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection.html) in the _Terraform Provider Documentation_