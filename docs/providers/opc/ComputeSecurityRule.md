# Terraform::OPC::ComputeSecurityRule

The ``Terraform::OPC::ComputeSecurityRule`` resource creates and manages a security rule in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The name of the security rule.

`FlowDirection` - (Required) Specify the direction of flow of traffic, which is relative to the instances, for this security rule. Allowed values are ingress or egress.

`Disabled` - (Optional) Whether to disable this security rule. This is useful if you want to temporarily disable a rule without removing it outright from your Terraform resource definition. Defaults to `false`.

`Acl` - (Optional) Name of the ACL that contains this security rule.

`DstIpAddressPrefixes` - (Optional) List of IP address prefix set names to match the packet's destination IP address.

`SrcIpAddressPrefixes` - (Optional) List of names of IP address prefix set to match the packet's source IP address.

`DstVnicSet` - (Optional) Name of virtual NIC set containing the packet's destination virtual NIC.

`SrcVnicSet` - (Optional) Name of virtual NIC set containing the packet's source virtual NIC.

`SecurityProtocols` - (Optional) List of security protocol object names to match the packet's protocol and port.

`Description` - (Optional) A description of the security rule.

`Tags` - (Optional) List of tags that may be applied to the security rule.


## Return Values

### Fn::GetAtt

`Uri` - The Uniform Resource Identifier of the security rule.

## See Also

* [opc_compute_security_rule](https://www.terraform.io/docs/providers/opc/r/compute_security_rule.html) in the _Terraform Provider Documentation_