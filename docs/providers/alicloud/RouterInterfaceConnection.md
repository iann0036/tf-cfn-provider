# Terraform::Alicloud::RouterInterfaceConnection

Provides a VPC router interface connection resource to connect two router interfaces which are in two different VPCs.
After that, all of the two router interfaces will be active.

-> **NOTE:** At present, Router interface does not support changing opposite router interface, the connection delete action is only deactivating it to inactive, not modifying the connection to empty.

-> **NOTE:** If you want to changing opposite router interface, you can delete router interface and re-build them.

-> **NOTE:** A integrated router interface connection tunnel requires both InitiatingSide and AcceptingSide configuring opposite router interface.

-> **NOTE:** Please remember to add a `depends_on` clause in the router interface connection from the InitiatingSide to the AcceptingSide, because the connection from the AcceptingSide to the InitiatingSide must be done first.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Router interface ID. The value is equal to "interface_id".

## See Also

* [alicloud_router_interface_connection](https://www.terraform.io/docs/providers/alicloud/r/router_interface_connection.html) in the _Terraform Provider Documentation_