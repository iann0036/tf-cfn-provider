# Terraform::RightScale::RouteTable

Use this resource to create, update or destroy RightScale [route tables](http://reference.rightscale.com/api1.5/resources/ResourceRouteTables.html).

## Properties

`CloudHref` - (Required) Href of the cloud you want to create the route table in.

`NetworkHref` - (Required) Href of the network that owns the route table.

`Name` - (Required) Route table name.

`Description` - (Optional) Route table description.


## Return Values

### Fn::GetAtt

`Href` - Href of the route table.

`ResourceUid` - Cloud resource_uid.

`Links` - Hrefs of related API resources.

`CreatedAt` - Created at datestamp.

`UpdatedAt` - Last updated at datestamp.

## See Also

* [rightscale_route_table](https://www.terraform.io/docs/providers/rightscale/r/route_table.html) in the _Terraform Provider Documentation_