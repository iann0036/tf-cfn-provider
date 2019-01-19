# Terraform::Alicloud::RouterInterfaceConnection

Provides a VPC router interface connection resource to connect two router interfaces which are in two different VPCs.
After that, all of the two router interfaces will be active.

-> **NOTE:** At present, Router interface does not support changing opposite router interface, the connection delete action is only deactivating it to inactive, not modifying the connection to empty.

-> **NOTE:** If you want to changing opposite router interface, you can delete router interface and re-build them.

-> **NOTE:** A integrated router interface connection tunnel requires both InitiatingSide and AcceptingSide configuring opposite router interface.

-> **NOTE:** Please remember to add a `depends_on` clause in the router interface connection from the InitiatingSide to the AcceptingSide, because the connection from the AcceptingSide to the InitiatingSide must be done first.

## Properties

`InterfaceId` - (Required, ForceNew) One side router interface ID.

`OppositeInterfaceId` - (Required, ForceNew) Another side router interface ID. It must belong the specified "opposite_interface_owner_id" account.

`OppositeInterfaceOwnerId` - (Optional, ForceNew) Another side router interface account ID. Log on to the Alibaba Cloud console, select User Info > Account Management to check the account ID. Default to [Provider account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

`OppositeRouterId` - (Optional, ForceNew) Another side router ID. It must belong the specified "opposite_interface_owner_id" account. It is valid when field "opposite_interface_owner_id" is specified.

`OppositeRouterType` - (Optional, ForceNew) Another side router Type. Optional value: VRouter, VBR. It is valid when field "opposite_interface_owner_id" is specified.


## Return Values

### Fn::GetAtt

`Id` - Router interface ID. The value is equal to "interface_id".

## See Also

* [alicloud_router_interface_connection](https://www.terraform.io/docs/providers/alicloud/r/router_interface_connection.html) in the _Terraform Provider Documentation_