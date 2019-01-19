# Terraform::OPC::ComputeSecurityList

The ``Terraform::OPC::ComputeSecurityList`` resource creates and manages a security list in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The unique (within the identity domain) name of the security list.

`Policy` - (Required) The policy to apply to instances associated with this list. Must be one of `permit`, `reject` (packets are dropped but a reply is sent) and `deny` (packets are dropped and no reply is sent).

`OutputCidrPolicy` - (Required) The policy for outbound traffic from the security list. Must be one of `permit`, `reject` (packets are dropped but a reply is sent) and `deny` (packets are dropped and no reply is sent).


## See Also

* [opc_compute_security_list](https://www.terraform.io/docs/providers/opc/r/compute_security_list.html) in the _Terraform Provider Documentation_