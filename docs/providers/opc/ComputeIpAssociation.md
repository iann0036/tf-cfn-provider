# Terraform::OPC::ComputeIpAssociation

The ``Terraform::OPC::ComputeIpAssociation`` resource creates and manages an association between an IP address and an instance in
an Oracle Cloud Infrastructure Compute Classic identity domain, for the Shared Network.

## Properties

`Vcable` - (Required) The vcable of the instance to associate the IP address with.

`ParentPool` - (Required) The pool from which to take an IP address. To associate a specific reserved IP address, use
the prefix `ipreservation:` followed by the name of the IP reservation. To allocate an IP address from a pool, use the
prefix `ippool:`, e.g. `ippool:/oracle/public/ippool`.


## See Also

* [opc_compute_ip_association](https://www.terraform.io/docs/providers/opc/r/compute_ip_association.html) in the _Terraform Provider Documentation_