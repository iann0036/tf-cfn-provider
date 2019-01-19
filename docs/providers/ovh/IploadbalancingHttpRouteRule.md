# Terraform::OVH::IploadbalancingHttpRouteRule

Manage rules for HTTP route.

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`RouteId` - (Required) The route to apply this rule.

`DisplayName` - Human readable name for your rule, this field is for you.

`Field` - (Required) Name of the field to match like "protocol" or "host". See "/ipLoadbalancing/{serviceName}/availableRouteRules" for a list of available rules.

`Match` - (Required) Matching operator. Not all operators are available for all fields. See "/ipLoadbalancing/{serviceName}/availableRouteRules".

`Negate` - Invert the matching operator effect.

`Pattern` - Value to match against this match. Interpretation if this field depends on the match and field.

`SubField` - Name of sub-field, if applicable. This may be a Cookie or Header name for instance.


## Return Values

### Fn::GetAtt

`ServiceName` - See Properties above.

`RouteId` - See Properties above.

`DisplayName` - See Properties above.

`Field` - See Properties above.

`Match` - See Properties above.

`Negate` - See Properties above.

`Pattern` - See Properties above.

`SubField` - See Properties above.

## See Also

* [ovh_iploadbalancing_http_route_rule](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_http_route_rule.html) in the _Terraform Provider Documentation_