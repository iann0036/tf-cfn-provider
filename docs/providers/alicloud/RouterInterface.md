# Terraform::Alicloud::RouterInterface

Provides a VPC router interface resource aim to build a connection between two VPCs.

-> **NOTE:** Only one pair of connected router interfaces can exist between two routers. Up to 5 router interfaces can be created for each router and each account.

-> **NOTE:** The router interface is not connected when it is created. It can be connected by means of resource [alicloud_router_interface_connection](https://www.terraform.io/docs/providers/alicloud/r/router_interface_connection.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - Router interface ID.

`RouterId` - Router ID.

`RouterType` - Router type.

`Role` - Router interface role.

`Name` - Router interface name.

`Description` - Router interface description.

`Specification` - Router nterface specification.

`AccessPointId` - Access point of the router interface.

`OppositeAccessPointId` - (Deprecated) It has been deprecated from version 1.11.0.

`OppositeRouterType` - Peer router type.

`OppositeRouterId` - Peer router ID.

`OppositeInterfaceId` - Peer router interface ID.

`OppositeInterfaceOwnerId` - Peer account ID.

`HealthCheckSourceIp` - Source IP of Packet of Line HealthCheck.

`HealthCheckTargetIp` - Target IP of Packet of Line HealthCheck.

## See Also

* [alicloud_router_interface](https://www.terraform.io/docs/providers/alicloud/r/router_interface.html) in the _Terraform Provider Documentation_