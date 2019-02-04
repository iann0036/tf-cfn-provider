# Terraform::HuaweiCloud::LbL7ruleV2

Manages a V2 L7 Rule resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`Region` argument of the provider is used. Changing this creates a new
L7 Rule.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the L7 Rule.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Rule.

`Description` - (Optional) Human-readable description for the L7 Rule.

`Type` - (Required) The L7 Rule type - can either be HOST\_NAME or PATH. Changing this creates a new L7 Rule.

`CompareType` - (Required) The comparison type for the L7 rule - can either be
STARTS\_WITH, EQUAL_TO or REGEX.

`L7policyId` - (Required) The ID of the L7 Policy to query. Changing this creates a new
L7 Rule.

`Value` - (Required) The value to use for the comparison. For example, the file type to
compare.

`Key` - (Optional) The key to use for the comparison. For example, the name of the cookie to
evaluate. Valid when `Type` is set to COOKIE or HEADER. Changing this creates a new L7 Rule.

`AdminStateUp` - (Optional) The administrative state of the L7 Rule.
The value can only be true (UP).


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the L7 Rule.

`Region` - See Properties above.

`TenantId` - See Properties above.

`Type` - See Properties above.

`CompareType` - See Properties above.

`L7policyId` - See Properties above.

`Value` - See Properties above.

`Key` - See Properties above.

`Invert` - See Properties above.

`AdminStateUp` - See Properties above.

`ListenerId` - The ID of the Listener owning this resource.

## See Also

* [huaweicloud_lb_l7rule_v2](https://www.terraform.io/docs/providers/huaweicloud/r/lb_l7rule_v2.html) in the _Terraform Provider Documentation_