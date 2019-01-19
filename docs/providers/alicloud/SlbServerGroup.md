# Terraform::Alicloud::SlbServerGroup

A virtual server group contains several ECS instances. The virtual server group can help you to define multiple listening dimension,
and to meet the personalized requirements of domain name and URL forwarding.

~> **NOTE:** One ECS instance can be added into multiple virtual server groups.

~> **NOTE:** One virtual server group can be attached with multiple listeners in one load balancer.

~> **NOTE:** One Classic and Internet load balancer, its virtual server group can add Classic and VPC ECS instances.

~> **NOTE:** One Classic and Intranet load balancer, its virtual server group can only add Classic ECS instances.

~> **NOTE:** One VPC load balancer, its virtual server group can only add the same VPC ECS instances.

## Properties

`LoadBalancerId` - (Required, ForceNew) The Load Balancer ID which is used to launch a new virtual server group.

`Name` - (Optional) Name of the virtual server group. Our plugin provides a default name: "tf-server-group".

`Servers` - (Required) A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual server group.

`LoadBalancerId` - The Load Balancer ID which is used to launch a new virtual server group.

`Name` - The name of the virtual server group.

`Servers` - A list of ECS instances that have be added.

## See Also

* [alicloud_slb_server_group](https://www.terraform.io/docs/providers/alicloud/r/slb_server_group.html) in the _Terraform Provider Documentation_