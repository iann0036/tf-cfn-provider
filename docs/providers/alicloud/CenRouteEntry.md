# Terraform::Alicloud::CenRouteEntry

Provides a CEN route entry resource. Cloud Enterprise Network (CEN) supports publishing and withdrawing route entries of attached networks. You can publish a route entry of an attached VPC or VBR to a CEN instance, then other attached networks can learn the route if there is no route conflict. You can withdraw a published route entry when CEN does not need it any more.

For information about CEN route entries publishment and how to use it, see [Manage network routes](https://www.alibabacloud.com/help/doc-detail/86980.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the resource, formatted as `<instance_id>:<route_table_id>:<cidr_block>`.

## See Also

* [alicloud_cen_route_entry](https://www.terraform.io/docs/providers/alicloud/r/cen_route_entry.html) in the _Terraform Provider Documentation_