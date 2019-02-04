# Terraform::OCI::ContainerengineNodePool

This resource provides the Node Pool resource in Oracle Cloud Infrastructure Container Engine service.

Create a new node pool.

## Properties

`ClusterId` - (Required) The OCID of the cluster to which this node pool is attached.

`CompartmentId` - (Required) The OCID of the compartment in which the node pool exists.

`InitialNodeLabels` - (Optional) (Updatable) A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`Key` - (Optional) (Updatable) The key of the pair.

`Value` - (Optional) (Updatable) The value of the pair.

`KubernetesVersion` - (Required) (Updatable) The version of Kubernetes to install on the nodes in the node pool.

`Name` - (Required) (Updatable) The name of the node pool. Avoid entering confidential information.

`NodeImageName` - (Required) The name of the image running on the nodes in the node pool.

`NodeShape` - (Required) The name of the node shape of the nodes in the node pool.

`QuantityPerSubnet` - (Optional) (Updatable) The number of nodes to create in each subnet.

`SshPublicKey` - (Optional) The SSH public key to add to each node in the node pool.

`SubnetIds` - (Required) (Updatable) The OCIDs of the subnets in which to place nodes for this node pool.


## Return Values

### Fn::GetAtt

`ClusterId` - The OCID of the cluster to which this node pool is attached.

`CompartmentId` - The OCID of the compartment in which the node pool exists.

`Id` - The OCID of the compute instance backing this node.

`InitialNodeLabels` - A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`Key` - The key of the pair.

`Value` - The value of the pair.

`KubernetesVersion` - The version of Kubernetes running on the nodes in the node pool.

`Name` - The name of the node.

`NodeImageId` - The OCID of the image running on the nodes in the node pool.

`NodeImageName` - The name of the image running on the nodes in the node pool.

`NodeShape` - The name of the node shape of the nodes in the node pool.

`Nodes` - The nodes in the node pool.

`AvailabilityDomain` - The name of the availability domain in which this node is placed.

`Error` - An error that may be associated with the node.

`Code` - A short error code that defines the upstream error, meant for programmatic parsing. See [API Errors](https://docs.cloud.oracle.com/iaas/Content/API/References/apierrors.htm).

`Message` - A human-readable error string of the upstream error.

`LifecycleDetails` - Details about the state of the node.

`NodePoolId` - The OCID of the node pool to which this node belongs.

`PublicIp` - The public IP address of this node.

`State` - The state of the node.

`SubnetId` - The OCID of the subnet in which this node is placed.

`QuantityPerSubnet` - The number of nodes in each subnet.

`SshPublicKey` - The SSH public key on each node in the node pool.

`SubnetIds` - The OCIDs of the subnets in which to place nodes for this node pool.

## See Also

* [oci_containerengine_node_pool](https://www.terraform.io/docs/providers/oci/r/containerengine_node_pool.html) in the _Terraform Provider Documentation_