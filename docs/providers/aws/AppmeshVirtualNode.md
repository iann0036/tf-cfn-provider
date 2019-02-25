# Terraform::AWS::AppmeshVirtualNode

Provides an AWS App Mesh virtual node resource.

~> **Note:** Backward incompatible API changes have been announced for AWS App Mesh which will affect this resource. Read more about the changes [here](https://github.com/awslabs/aws-app-mesh-examples/issues/92).

## Properties

`Name` - (Required) The name to use for the virtual node.

`MeshName` - (Required) The name of the service mesh in which to create the virtual node.

`Spec` - (Required) The virtual node specification to apply.

### Spec Properties

`Backends` - (Optional) The backends to which the virtual node is expected to send outbound traffic.

`Listener` - (Optional) The listeners from which the virtual node is expected to receive inbound traffic.

`ServiceDiscovery` - (Optional) The service discovery information for the virtual node.

### Listener Properties

`PortMapping` - (Required) The port mapping information for the listener.

`HealthCheck` - (Optional) The health check information for the listener.

### ServiceDiscovery Properties

`Dns` - (Required) Specifies the DNS service name for the virtual node.

### Dns Properties

`ServiceName` - (Required) The DNS service name for your virtual node.

### PortMapping Properties

`Port` - (Required) The port used for the port mapping.

`Protocol` - (Required) The protocol used for the port mapping. Valid values are `http` and `tcp`.

### HealthCheck Properties

`HealthyThreshold` - (Required) The number of consecutive successful health checks that must occur before declaring listener healthy.

`IntervalMillis` - (Required) The time period in milliseconds between each health check execution.

`Protocol` - (Required) The protocol for the health check request. Valid values are `http` and `tcp`.

`TimeoutMillis` - (Required) The amount of time to wait when receiving a response from the health check, in milliseconds.

`UnhealthyThreshold` - (Required) The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.

`Path` - (Optional) The destination path for the health check request. This is only required if the specified protocol is `http`.

`Port` - (Optional) The destination port for the health check request. This port must match the port defined in the `PortMapping` for the listener.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual node.

`Arn` - The ARN of the virtual node.

`CreatedDate` - The creation date of the virtual node.

`LastUpdatedDate` - The last update date of the virtual node.

## See Also

* [aws_appmesh_virtual_node](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node.html) in the _Terraform Provider Documentation_