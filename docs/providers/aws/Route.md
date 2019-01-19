# Terraform::AWS::Route

Provides a resource to create a routing table entry (a route) in a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a [Route Table](route_table.html) resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Route Table identifier and destination.

## See Also

* [aws_route](https://www.terraform.io/docs/providers/aws/r/route.html) in the _Terraform Provider Documentation_