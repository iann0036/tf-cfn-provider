# Terraform::RightScale::NetworkGateway

Use this resource to create, update or destroy RightScale [network gateways](http://reference.rightscale.com/api1.5/resources/ResourceNetworkGateways.html) in cloud management.

## Properties

`CloudHref` - (Required) Cloud you want to create the network gateway in.

`Type` - (Required) Type of network gateway.  Options are "internet" or "vpc".

`Name` - (Required) Network gateway name.

`Description` - (Optional) Network gateway description.

`NetworkHref` - (Optional) Href of network you want to attach the network gateway to.


## Return Values

### Fn::GetAtt

`Href` - Href of the network gateway.

`CreatedAt` - Date the network gateway was created at.

`UpdatedAt` - Date the network gateway was updated at.

`State` - State of the network gateway.  ("available" means attached to a network).

`ResourceUid` - Cloud resource_uid.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_network_gateway](https://www.terraform.io/docs/providers/rightscale/r/network_gateway.html) in the _Terraform Provider Documentation_