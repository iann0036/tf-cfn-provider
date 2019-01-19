# Terraform::Alicloud::SlbAttachment

Add a group of backend servers (ECS instance) to the Server Load Balancer or remove them from it.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the resource.

`LoadBalancerId` - ID of the load balancer.

`InstanceIds` - A list of instance ids that have been added in the SLB.

`Weight` - (Optional) Weight of the instances.

`BackendServers` - The backend servers of the load balancer.

## See Also

* [alicloud_slb_attachment](https://www.terraform.io/docs/providers/alicloud/r/slb_attachment.html) in the _Terraform Provider Documentation_