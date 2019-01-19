# Terraform::Linode::Nodebalancer

Provides a Linode NodeBalancer resource.  This can be used to create, modify, and delete Linodes NodeBalancers.
For more information, see [Getting Started with NodeBalancers](https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createNodeBalancer).

## Properties

`Region` - (Required) The region where this NodeBalancer will be deployed.  Examples are `"us-east"`, `"us-west"`, `"ap-south"`, etc.  *Changing `Region` forces the creation of a new Linode NodeBalancer.*.

`Label` - (Optional) The label of the Linode NodeBalancer.

`ClientConnThrottle` - (Optional) Throttle connections per second (0-20). Set to 0 (default) to disable throttling.

`LinodeId` - (Optional) The ID of a Linode Instance where the the NodeBalancer should be attached.

`Tags` - (Optional) A list of tags applied to this object. Tags are for organizational purposes only.


## See Also

* [linode_nodebalancer](https://www.terraform.io/docs/providers/linode/r/nodebalancer.html) in the _Terraform Provider Documentation_