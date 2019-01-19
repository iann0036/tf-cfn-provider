# Terraform::UCloud::LbRule

Provides a Load Balancer Rule resource to add content forwarding policies for Load Balancer backend resource.

## Properties

`LoadBalancerId` - (Required) The ID of the load balancer which requires the rule.

`ListenerId` - (Required) The ID of the listener which requires the rule.

`BackendIds` - (Required) The IDs of the backend servers where rule applies, this argument is populated base on the `backend_id` responed from `lb_attachment create`.

`Path` - (Optional) The path of Content forward matching fields. `Path` and `Domain` cannot coexist. `Path` and `Domain` must be filled in one.

`Domain` - (Optional) The domain of content forward matching fields. `Path` and `Domain` cannot coexist. `Path` and `Domain` must be filled in one.


## See Also

* [ucloud_lb_rule](https://www.terraform.io/docs/providers/ucloud/r/lb_rule.html) in the _Terraform Provider Documentation_