# Terraform::OPC::ComputeSecurityAssociation

The ``Terraform::OPC::ComputeSecurityAssociation`` resource creates and manages an association between an instance and a security
list in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Optional) The Name for the Security Association. If not specified, one is created automatically. Changing this forces a new resource to be created.

`Vcable` - (Required) The `Vcable` of the instance to associate to the security list.

`Seclist` - (Required) The name of the security list to associate the instance to.


## See Also

* [opc_compute_security_association](https://www.terraform.io/docs/providers/opc/r/compute_security_association.html) in the _Terraform Provider Documentation_