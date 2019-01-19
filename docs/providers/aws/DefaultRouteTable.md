# Terraform::AWS::DefaultRouteTable

Provides a resource to manage a Default VPC Routing Table.

Each VPC created in AWS comes with a Default Route Table that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource. It is recommended you **do not** use both `Terraform::AWS::DefaultRouteTable` to
manage the default route table **and** use the `Terraform::AWS::MainRouteTableAssociation`,
due to possible conflict in routes.

The `Terraform::AWS::DefaultRouteTable` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Route
Table that cannot be destroyed, and is created with a single route.

When Terraform first adopts the Default Route Table, it **immediately removes all
defined routes**. It then proceeds to create any routes specified in the
configuration. This step is required so that only the routes specified in the
configuration present in the Default Route Table.

For more information about Route Tables, see the AWS Documentation on
[Route Tables][aws-route-tables].

For more information about managing normal Route Tables in Terraform, see our
documentation on [aws_route_table][tf-route-tables].

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone [Route resource](route.html) and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite routes.

## Properties

`DefaultRouteTableId` - (Required) The ID of the Default Routing Table.

`Route` - (Optional) A list of route objects. Their keys are documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`PropagatingVgws` - (Optional) A list of virtual gateways for propagation.


## Return Values

### Fn::GetAtt

`Id` - The ID of the routing table.

`OwnerId` - The ID of the AWS account that owns the route table.

## See Also

* [aws_default_route_table](https://www.terraform.io/docs/providers/aws/r/default_route_table.html) in the _Terraform Provider Documentation_