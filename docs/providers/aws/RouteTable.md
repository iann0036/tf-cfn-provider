# Terraform::AWS::RouteTable

Provides a resource to create a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone [Route resource](route.html) and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE on `gateway_id` and `nat_gateway_id`:** The AWS API is very forgiving with these two
attributes and the `Terraform::AWS::RouteTable` resource can be created with a NAT ID specified as a Gateway ID attribute.
This _will_ lead to a permanent diff between your configuration and statefile, as the API returns the correct
parameters in the returned route table. If you're experiencing constant diffs in your `Terraform::AWS::RouteTable` resources,
the first thing to check is whether or not you're specifying a NAT ID instead of a Gateway ID, or vice-versa.

~> **NOTE on `PropagatingVgws` and the `Terraform::AWS::VpnGatewayRoutePropagation` resource:**
If the `PropagatingVgws` argument is present, it's not supported to _also_
define route propagations using `Terraform::AWS::VpnGatewayRoutePropagation`, since
this resource will delete any propagating gateways not explicitly listed in
`PropagatingVgws`. Omit this argument when defining route propagation using
the separate resource.

## Properties

`VpcId` - (Required) The VPC ID.

`Route` - (Optional) A list of route objects. Their keys are documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`PropagatingVgws` - (Optional) A list of virtual gateways for propagation.


## Return Values

### Fn::GetAtt

`Id` - The ID of the routing table.

`OwnerId` - The ID of the AWS account that owns the route table.

## See Also

* [aws_route_table](https://www.terraform.io/docs/providers/aws/r/route_table.html) in the _Terraform Provider Documentation_