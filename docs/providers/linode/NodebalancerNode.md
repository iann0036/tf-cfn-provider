# Terraform::Linode::NodebalancerNode

Provides a Linode NodeBalancer Node resource.  This can be used to create, modify, and delete Linodes NodeBalancer Nodes.
For more information, see [Getting Started with NodeBalancers](https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createNodeBalancerNode).

## Properties

`Label` - (Required) The label of the Linode NodeBalancer Node. This is for display purposes only.

`NodebalancerId` - (Required) The ID of the NodeBalancer to access.

`ConfigId` - (Required) The ID of the NodeBalancerConfig to access.

`Address` - (Required) The private IP Address where this backend can be reached. This must be a private IP address.

`Mode` - (Optional) The mode this NodeBalancer should use when sending traffic to this backend. If set to `accept` this backend is accepting traffic. If set to `reject` this backend will not receive traffic. If set to `drain` this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it.

`Weight` - (Optional) Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).


## See Also

* [linode_nodebalancer_node](https://www.terraform.io/docs/providers/linode/r/nodebalancer_node.html) in the _Terraform Provider Documentation_