# Terraform::Google::ComputeGlobalForwardingRule

Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
information see [the official
documentation](https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules) and
[API](https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules).

## Properties

`Name` - (Required) A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

`Target` - (Required) URL of target HTTP or HTTPS proxy.

`Description` - (Optional) Textual description field.

`IpAddress` - (Optional) The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the `self_link`
to a `Terraform::Google::ComputeGlobalAddress` resource. (If using a `googleComputeGlobalAddress`
resource, use the `address` property instead of the `self_link` property.).

`IpProtocol` - (Optional) The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP". (default "TCP").

`PortRange` - (Optional) A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

`IpVersion` - (Optional)
The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.
You cannot provide this and `IpAddress`.

`Labels` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html))
A set of key/value label pairs to assign to the resource.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_global_forwarding_rule](https://www.terraform.io/docs/providers/google/r/compute_global_forwarding_rule.html) in the _Terraform Provider Documentation_