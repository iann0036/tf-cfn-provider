# Terraform::Alicloud::SlbAttachment

Add a group of backend servers (ECS instance) to the Server Load Balancer or remove them from it.

## Properties

`LoadBalancerId` - (Required) ID of the load balancer.

`InstanceIds` - (Required) A list of instance ids to added backend server in the SLB.

`Weight` - (Optional) Weight of the instances. Valid value range: [0-100]. Default to 100.

`SlbId` - (Deprecated) It has been deprecated from provider version 1.6.0. New field 'load_balancer_id' replaces it.

`Instances` - (Deprecated) It has been deprecated from provider version 1.6.0. New field 'instance_ids' replaces it.


## Return Values

### Fn::GetAtt

`Id` - ID of the resource.

`LoadBalancerId` - ID of the load balancer.

`InstanceIds` - A list of instance ids that have been added in the SLB.

`Weight` - (Optional) Weight of the instances.

`BackendServers` - The backend servers of the load balancer.

## See Also

* [alicloud_slb_attachment](https://www.terraform.io/docs/providers/alicloud/r/slb_attachment.html) in the _Terraform Provider Documentation_