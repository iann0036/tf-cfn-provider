# Terraform::Google::ComputeSecurityPolicy

A Security Policy defines an IP blacklist or whitelist that protects load balanced Google Cloud services by denying or permitting traffic from specified IP ranges. For more information
see the [official documentation](https://cloud.google.com/armor/docs/configure-security-policies)
and the [API](https://cloud.google.com/compute/docs/reference/rest/beta/securityPolicies).

## Properties

`Name` - (Required) The name of the security policy.

`Description` - (Optional) An optional description of this rule. Max size is 64.

`Project` - (Optional) The project in which the resource belongs. If it is not provided, the provider project is used.

`Rule` - (Optional) The set of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "\*"). If no rules are provided when creating a security policy, a default rule with action "allow" will be added. Structure is documented below.

`Action` - (Required) Action to take when `Match` matches the request. Valid values: * "allow" : allow access to target * "deny(status)" : deny access to target, returns the  HTTP response code specified (valid values are 403, 404 and 502).

`Priority` - (Required) An unique positive integer indicating the priority of evaluation for a rule. Rules are evaluated from highest priority (lowest numerically) to lowest priority (highest numerically) in order.

`Match` - (Required) A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding `Action` is enforced. Structure is documented below.

`Preview` - (Optional) When set to true, the `Action` specified above is not enforced. Stackdriver logs for requests that trigger a preview action are annotated as such.

`Config` - (Required) The configuration options available when specifying `VersionedExpr`. Structure is documented below.

`VersionedExpr` - (Required) Predefined rule expression. Available options: * SRC_IPS_V1: Must specify the corresponding `SrcIpRanges` field in `Config`.

`SrcIpRanges` - (Required) Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation to match against inbound traffic. There is a limit of 5 IP ranges per rule. A value of '\*' matches all IPs (can be used to override the default behavior).


## Return Values

### Fn::GetAtt

`Fingerprint` - Fingerprint of this resource.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_security_policy](https://www.terraform.io/docs/providers/google/r/compute_security_policy.html) in the _Terraform Provider Documentation_