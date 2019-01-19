# Terraform::Google::ComputeSecurityPolicy

A Security Policy defines an IP blacklist or whitelist that protects load balanced Google Cloud services by denying or permitting traffic from specified IP ranges. For more information
see the [official documentation](https://cloud.google.com/armor/docs/configure-security-policies)
and the [API](https://cloud.google.com/compute/docs/reference/rest/beta/securityPolicies).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Fingerprint` - Fingerprint of this resource.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_security_policy](https://www.terraform.io/docs/providers/google/r/compute_security_policy.html) in the _Terraform Provider Documentation_