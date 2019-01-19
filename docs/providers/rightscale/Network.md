# Terraform::RightScale::Network

Use this resource to create, update or destroy RightScale [networks](http://reference.rightscale.com/api1.5/resources/ResourceNetworks.html) in cloud management.

## Properties

`CloudHref` - (Required) Cloud you want to create the network in.

`CidrBlock` - (Optional*) Cloud-specific.  Some clouds require this field, others do not.

`Name` - (Optional) Network name.

`Description` - (Optional) Network description.

`InstanceTenancy` - (Optional) Launch policy for AWS instances in the network. Specify 'dedicated' to force all instances to be launched as 'dedicated'.  Defaults to 'default.'.

`RouteTableHref` - (Optional) Sets the default route table for this network, useful if you create the route table with a different resource.

`DeploymentHref` - (Optional) Href of the deployment that owns the network.  If you wish to use a deployment object as top level ownership construct, perhaps allocating the new network to a single deployment, then provide this href.


## Return Values

### Fn::GetAtt

`Href` - Href of the network.

`ResourceUid` - Cloud resource_uid as reported by cm platform.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_network](https://www.terraform.io/docs/providers/rightscale/r/network.html) in the _Terraform Provider Documentation_