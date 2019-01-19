# Terraform::OCI::CoreRouteTableAttachment

This resource provides the ability to associate a route table for a subnet in Oracle Cloud Infrastructure Core service.

Attaches the specified `route table` to the specified `subnet`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SubnetId` - (Required) The OCID of the subnet.

`RouteTableId` - (Required) The OCID of the route table.

## See Also

* [oci_core_route_table_attachment](https://www.terraform.io/docs/providers/oci/r/core_route_table_attachment.html) in the _Terraform Provider Documentation_