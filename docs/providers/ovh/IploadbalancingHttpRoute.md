# Terraform::OVH::IploadbalancingHttpRoute

Manage http route for a loadbalancer service

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`DisplayName` - Human readable name for your route, this field is for you.

`Weight` - Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action.

`Action.status` - HTTP status code for "redirect" and "reject" actions.

`Action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target.

`Action.type` - (Required) Action to trigger if all the rules of this route matches.

`FrontendId` - Route traffic for this frontend.


## Return Values

### Fn::GetAtt

`ServiceName` - See Properties above.

`DisplayName` - See Properties above.

`Weight` - See Properties above.

`Action.status` - See Properties above.

`Action.target` - See Properties above.

`Action.type` - See Properties above.

`FrontendId` - See Properties above.

## See Also

* [ovh_iploadbalancing_http_route](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_http_route.html) in the _Terraform Provider Documentation_