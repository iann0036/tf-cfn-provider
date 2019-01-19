# Terraform::AWS::AppmeshRoute

Provides an AWS App Mesh route resource.

## Properties

`Name` - (Required) The name to use for the route.

`MeshName` - (Required) The name of the service mesh in which to create the route.

`VirtualRouteName` - (Required) The name of the virtual router in which to create the route.

`Spec` - (Required) The route specification to apply.

### HttpRoute Properties

`Action` - (Required) The action to take if a match is determined.

`Match` - (Required) The criteria for determining an HTTP request match.

### Match Properties

`Prefix` - (Required) Specifies the path with which to match requests. This parameter must always start with /, which by itself matches all requests to the virtual router service name.

### Spec Properties

`HttpRoute` - (Optional) The HTTP routing information for the route.

### Action Properties

`WeightedTarget` - (Required) The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.

### WeightedTarget Properties

`VirtualNode` - (Required) The virtual node to associate with the weighted target.

`Weight` - (Required) The relative weight of the weighted target. An integer between 0 and 100.


## Return Values

### Fn::GetAtt

`Id` - The ID of the route.

`Arn` - The ARN of the route.

`CreatedDate` - The creation date of the route.

`LastUpdatedDate` - The last update date of the route.

## See Also

* [aws_appmesh_route](https://www.terraform.io/docs/providers/aws/r/appmesh_route.html) in the _Terraform Provider Documentation_