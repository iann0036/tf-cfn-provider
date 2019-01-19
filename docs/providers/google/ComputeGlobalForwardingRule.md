# Terraform::Google::ComputeGlobalForwardingRule

Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
information see [the official
documentation](https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules) and
[API](https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_global_forwarding_rule](https://www.terraform.io/docs/providers/google/r/compute_global_forwarding_rule.html) in the _Terraform Provider Documentation_