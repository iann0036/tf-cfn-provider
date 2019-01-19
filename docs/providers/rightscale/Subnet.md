# Terraform::RightScale::Subnet

Use this resource to create, update or destroy RightScale [subnets](http://reference.rightscale.com/api1.5/resources/ResourceSubnets.html).

## Properties

`CloudHref` - (Required) Href of cloud you want to create the subnet in.

`NetworkHref` - (Required) Href of network to create subnet in.

`CidrBlock` - (Required) Subnet allocation range in CIDR notation.

`Name` - (Optional) Subnet name.

`Description` - (Optional) Subnet description.

`DatacenterHref` - (Optional) Href of cloud datacenter to assign subnet to.

`RouteTableHref` - (Optional) Sets the default route table for this subnet, useful if you create the route table with a different resource.


## Return Values

### Fn::GetAtt

`Href` - Href of the subnet.

`ResourceUid` - Cloud resource_uid.

`IsDefault` - Indicates whether the subnet is the network default subnet. (true or false).

`State` - Indicates whether subnet is pending, available etc.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_subnet](https://www.terraform.io/docs/providers/rightscale/r/subnet.html) in the _Terraform Provider Documentation_