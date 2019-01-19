# Terraform::OPC::ComputeSecRule

The ``Terraform::OPC::ComputeSecRule`` resource creates and manages a sec rule in an Oracle Cloud Infrastructure Compute Classic identity domain, which joins together a source security list (or security IP list), a destination security list (or security IP list), and a security application.

## Properties

`Name` - (Required) The unique (within the identity domain) name of the security rule.

`Description` - (Optional) A description for this security rule.

`SourceList` - (Required) The source security list (prefixed with `seclist:`), or security IP list (prefixed with `seciplist:`).

`DestinationList` - (Required) The destination security list (prefixed with `seclist:`), or security IP list (prefixed with `seciplist:`).

`Application` - (Required) The name of the application to which the rule applies.

`Action` - (Required) Whether to `permit`, `refuse` or `deny` packets to which this rule applies. This will ordinarily be `permit`.

`Disabled` - (Optional) Whether to disable this security rule. This is useful if you want to temporarily disable a rule without removing it outright from your Terraform resource definition. Defaults to `false`.

`Uri` - The Uniform Resource Identifier of the sec rule.


## See Also

* [opc_compute_sec_rule](https://www.terraform.io/docs/providers/opc/r/compute_sec_rule.html) in the _Terraform Provider Documentation_