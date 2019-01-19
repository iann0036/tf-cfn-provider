# Terraform::AWS::AppmeshVirtualNode

Provides an AWS App Mesh virtual node resource.

## Properties

`Name` - (Required) The name to use for the virtual node.

`MeshName` - (Required) The name of the service mesh in which to create the virtual node.

`Spec` - (Required) The virtual node specification to apply.

### Listener Properties

`PortMapping` - (Required) The port mapping information for the listener.

### Dns Properties

`ServiceName` - (Required) The DNS service name for your virtual node.

### Spec Properties

`Backends` - (Optional) The backends to which the virtual node is expected to send outbound traffic.

`Listener` - (Optional) The listeners from which the virtual node is expected to receive inbound traffic.

`ServiceDiscovery` - (Optional) The service discovery information for the virtual node.

### PortMapping Properties

`Port` - (Required) The port used for the port mapping.

`Protocol` - (Required) The protocol used for the port mapping. Valid values are `http` and `tcp`.

### ServiceDiscovery Properties

`Dns` - (Required) Specifies the DNS service name for the virtual node.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual node.

`Arn` - The ARN of the virtual node.

`CreatedDate` - The creation date of the virtual node.

`LastUpdatedDate` - The last update date of the virtual node.

## See Also

* [aws_appmesh_virtual_node](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node.html) in the _Terraform Provider Documentation_