# Terraform::Alicloud::CsSwarm

This resource will help you to manager a Swarm Cluster.

-> **NOTE:** Swarm cluster only supports VPC network and you can specify a VPC network by filed `VswitchId`.

## Properties

`Name` - The container cluster's name. It is the only in one Alicloud account.

`NamePrefix` - The container cluster name's prefix. It is conflict with `Name`. If it is specified, terraform will using it to build the only cluster name. Default to 'Terraform-Creation'.

`Size` - Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.

`NodeNumber` - The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.

`CidrBlock` - (Required, Force new resource) The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:
- 192.168.0.0/16
- 172.19-30.0.0/16
- 10.0.0.0/16.

`ImageId` - (Force new resource) The image ID of ECS instance node used. Default to System automate allocated.

`InstanceType` - (Required, Force new resource) The type of ECS instance node.

`IsOutdated` - (Optional) Whether to use outdated instance type. Default to false.

`Password` - (Required, Force new resource) The password of ECS instance node.

`DiskCategory` - (Force new resource) The data disk category of ECS instance node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.

`DiskSize` - (Force new resource) The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.

`VswitchId` - (Required, Force new resource) The password of ECS instance node. If it is not specified, the container cluster's network mode will be `Classic`.

`ReleaseEip` - Whether to release EIP after creating swarm cluster successfully. Default to false.

`NeedSlb` - Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.


## Return Values

### Fn::GetAtt

`Id` - The ID of the container cluster.

`Name` - The name of the container cluster.

`Size` - It has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.

`NodeNumber` - The node number.

`VpcId` - The ID of VPC where the current cluster is located.

`VswitchId` - The ID of VSwitch where the current cluster is located.

`SlbId` - The ID of load balancer where the current cluster worker node is located.

`SecurityGroupId` - The ID of security group where the current cluster worker node is located.

`AgentVersion` - The nodes agent version.

`InstanceType` - The instance type of nodes.

`DiskCategory` - The data disk category of nodes.

`DiskSize` - The data disk size of nodes.

`Nodes` - List of cluster nodes. It contains several attributes to `Block Nodes`.

## See Also

* [alicloud_cs_swarm](https://www.terraform.io/docs/providers/alicloud/r/cs_swarm.html) in the _Terraform Provider Documentation_