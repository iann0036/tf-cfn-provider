# Terraform::AWS::VpcEndpoint

Provides a VPC Endpoint resource.

~> **NOTE on VPC Endpoints and VPC Endpoint Associations:** Terraform provides both standalone VPC Endpoint Associations for
[Route Tables](vpc_endpoint_route_table_association.html) - (an association between a VPC endpoint and a single `route_table_id`) and
[Subnets](vpc_endpoint_subnet_association.html) - (an association between a VPC endpoint and a single `subnet_id`) and
a VPC Endpoint resource with `route_table_ids` and `subnet_ids` attributes.
Do not use the same resource ID in both a VPC Endpoint resource and a VPC Endpoint Association resource.
Doing so will cause a conflict of associations and will overwrite the association.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC endpoint.

`State` - The state of the VPC endpoint.

`PrefixListId` - The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.

`CidrBlocks` - The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.

`NetworkInterfaceIds` - One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.

`DnsEntry` - The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.

`DnsName` - The DNS name.

`HostedZoneId` - The ID of the private hosted zone.

## See Also

* [aws_vpc_endpoint](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint.html) in the _Terraform Provider Documentation_