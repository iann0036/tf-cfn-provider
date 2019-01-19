# Terraform::FlexibleEngine::CceNodesV3

Add a node to a container cluster.

## Properties

`ClusterId` - (Required) ID of the cluster. Changing this parameter will create a new resource.

`BillingMode` - (Optional) Node's billing mode: The value is 0 (on demand). Changing this parameter will create a new resource.

`Name` - (Optional) Node Name.

`Labels` - (Optional) Node tag, key/value pair format. Changing this parameter will create a new resource.

`Annotations` - (Optional) Node annotation, key/value pair format. Changing this parameter will create a new resource.

`FlavorId` - (Required) Specifies the flavor id. Changing this parameter will create a new resource.

`AvailabilityZone` - (Required) specify the name of the available partition (AZ). Changing this parameter will create a new resource.

`KeyPair` - (Required) Key pair name when logging in to select the key pair mode. Changing this parameter will create a new resource.

`EipIds` - (Optional) List of existing elastic IP IDs. Changing this parameter will create a new resource.

`EipCount` - (Optional) Number of elastic IPs to be dynamically created. Changing this parameter will create a new resource.

`Iptype` - (Required) Elastic IP type.

`BandwidthChargeMode` - (Optional) Bandwidth billing type. Changing this parameter will create a new resource.

`Sharetype` - (Required) Bandwidth sharing type. Changing this parameter will create a new resource.

`BandwidthSize` - (Required) Bandwidth size. Changing this parameter will create a new resource.

`ExtendParamChargingMode` - (Optional) Node charging mode, 0 is on-demand charging. Changing this parameter will create a new cluster resource.

`EcsPerformanceType` - (Optional) Classification of cloud server specifications. Changing this parameter will create a new cluster resource.

`OrderId` - (Optional) Order ID, mandatory when the node payment type is the automatic payment package period type. Changing this parameter will create a new cluster resource.

`ProductId` - (Optional) The Product ID. Changing this parameter will create a new cluster resource.

`MaxPods` - (Optional) The maximum number of instances a node is allowed to create. Changing this parameter will create a new cluster resource.

`PublicKey` - (Optional) The Public key. Changing this parameter will create a new cluster resource.

`Size` - (Required) Disk size in GB.

`Volumetype` - (Required) Disk type.

`ExtendParam` - (Optional) Disk expansion parameters.

`Size` - (Required) Disk size in GB.

`Volumetype` - (Required) Disk type.

`ExtendParam` - (Optional) Disk expansion parameters.


## Return Values

### Fn::GetAtt

`Status` -  Node status information.

## See Also

* [flexibleengine_cce_nodes_v3](https://www.terraform.io/docs/providers/flexibleengine/r/cce_nodes_v3.html) in the _Terraform Provider Documentation_