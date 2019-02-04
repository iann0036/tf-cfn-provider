# Terraform::AWS::VpcEndpoint

Provides a VPC Endpoint resource.

~> **NOTE on VPC Endpoints and VPC Endpoint Associations:** Terraform provides both standalone VPC Endpoint Associations for
[Route Tables](vpc_endpoint_route_table_association.html) - (an association between a VPC endpoint and a single `route_table_id`) and
[Subnets](vpc_endpoint_subnet_association.html) - (an association between a VPC endpoint and a single `subnet_id`) and
a VPC Endpoint resource with `RouteTableIds` and `SubnetIds` attributes.
Do not use the same resource ID in both a VPC Endpoint resource and a VPC Endpoint Association resource.
Doing so will cause a conflict of associations and will overwrite the association.

## Properties

`VpcId` - (Required) The ID of the VPC in which the endpoint will be used.

`VpcEndpointType` - (Optional) The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.

`ServiceName` - (Required) The service name, in the form `com.amazonaws.region.service` for AWS services.

`AutoAccept` - (Optional) Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).

`Policy` - (Optional) A policy to attach to the endpoint that controls access to the service. Applicable for endpoints of type `Gateway`. Defaults to full access. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`RouteTableIds` - (Optional) One or more route table IDs. Applicable for endpoints of type `Gateway`.

`SubnetIds` - (Optional) The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.

`SecurityGroupIds` - (Optional) The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.

`PrivateDnsEnabled` - (Optional; AWS services and AWS Marketplace partner services only) Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
Defaults to `false`.


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