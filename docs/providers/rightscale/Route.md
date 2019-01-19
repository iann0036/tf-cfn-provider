# Terraform::RightScale::Route

Use this resource to create, update or destroy RightScale [routes](http://reference.rightscale.com/api1.5/resources/ResourceRoutes.html).

## Properties

`RouteTableHref` - (Required) Href of route table in which to create new route.

`DestinationCidrBlock` - (Required) Destination network in CIDR nodation.

`NextHopType` - (Required) The route next hop type.  Options are 'instance', 'network_interface', 'network_gateway', 'ip_string', and 'url'.

`NextHopHref` - (Contextual) The href of the Route's next hop. Required if 'next_hop_type' is 'instance', 'network_interface', or 'network_gateway'.

`NextHopIp` - (Contextual) The IP Address of the Route's next hop. Required if 'next_hop_type' is 'ip_string'.

`NextHopUrl` - (Contextual) The URL of the Route's next hop. Required if 'next_hop_type' is 'url'.

`Description` - (Optional) Route description.


## Return Values

### Fn::GetAtt

`Href` - Href of the route.

`ResourceUid` - Route resource_uid.

`Links` - Hrefs of related API resources.

`CreatedAt` - Created at datestamp.

`UpdatedAt` - Last updated at datestamp.

## See Also

* [rightscale_route](https://www.terraform.io/docs/providers/rightscale/r/route.html) in the _Terraform Provider Documentation_