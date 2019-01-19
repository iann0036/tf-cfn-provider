# Terraform::CloudStack::StaticRoute

Creates a static route for the given private gateway or VPC.

## Properties

`Cidr` - (Required) The CIDR for the static route. Changing this forces a new resource to be created.

`GatewayId` - (Required) The ID of the Private gateway. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the static route.

## See Also

* [cloudstack_static_route](https://www.terraform.io/docs/providers/cloudstack/r/static_route.html) in the _Terraform Provider Documentation_