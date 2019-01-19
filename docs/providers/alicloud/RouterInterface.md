# Terraform::Alicloud::RouterInterface

Provides a VPC router interface resource aim to build a connection between two VPCs.

-> **NOTE:** Only one pair of connected router interfaces can exist between two routers. Up to 5 router interfaces can be created for each router and each account.

-> **NOTE:** The router interface is not connected when it is created. It can be connected by means of resource [alicloud_router_interface_connection](https://www.terraform.io/docs/providers/alicloud/r/router_interface_connection.html).

## Properties

`OppositeRegion` - (Required, Force New) The Region of peer side.

`RouterType` - (Required, Forces New) Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.

`OppositeRouterType` - (Deprecated) It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.

`RouterId` - (Required, Force New) The Router ID.

`OppositeRouterId` - (Deprecated) It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.

`Role` - (Required, Force New) The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.

`Specification` - (Optional) Specification of router interfaces. It is valid when `Role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).

`AccessPointId` - (Deprecated) It has been deprecated from version 1.11.0.

`OppositeAccessPointId` - (Deprecated) It has been deprecated from version 1.11.0.

`OppositeInterfaceId` - (Deprecated) It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.

`OppositeInterfaceOwnerId` - (Deprecated) It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.

`Name` - (Optional) Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted. If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.

`Description` - (Optional) Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.

`HealthCheckSourceIp` - (Optional) Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `RouterType` is `VBR`. The IP must be an unused IP in the local VPC. It and `HealthCheckTargetIp` must be specified at the same time.

`HealthCheckTargetIp` - (Optional) Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `RouterType` is `VBR`. The IP must be an unused IP in the local VPC. It and `HealthCheckSourceIp` must be specified at the same time.

`InstanceChargeType` - (Optional, ForceNew) The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.

`Period` - (Optional, ForceNew) The duration that you will buy the resource, in month. It is valid when `InstanceChargeType` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.


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