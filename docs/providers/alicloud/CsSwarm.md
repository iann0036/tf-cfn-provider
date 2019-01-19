# Terraform::Alicloud::CsSwarm

This resource will help you to manager a Swarm Cluster.

-> **NOTE:** Swarm cluster only supports VPC network and you can specify a VPC network by filed `vswitch_id`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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