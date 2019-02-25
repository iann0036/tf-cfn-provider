# Terraform::Spotinst::MultaiBalancer

Provides a Spotinst Multai Balancer.

## Properties

`Name` - (Required) The balancer name. May contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

`Scheme` - (Optional).

`DnsCnameAliases` - (Optional).

`ConnectionTimeouts` - (Optional).

`Idle` - (Optional) The idle timeout value, in seconds. (range: 1 - 3600).

`Draining` - (Optional) The time for the load balancer to keep connections alive before reporting the target as de-registered, in seconds (range: 1 - 3600).

`Tags` - (Optional) A list of key:value paired tags.

`Key` - (Required) The tag's key.

`Value` - (Required) The tag's value.


## See Also

* [spotinst_multai_balancer](https://www.terraform.io/docs/providers/spotinst/r/multai_balancer.html) in the _Terraform Provider Documentation_