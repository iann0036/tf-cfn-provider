# Terraform::OPC::ComputeVnicSet

The ``Terraform::OPC::ComputeVnicSet`` resource creates and manages a virtual NIC set in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The unique (within this identity domain) name of the virtual nic set.

`Description` - (Optional) A description of the virtual nic set.

`AppliedAcls` - (Optional) A list of the ACLs to apply to the virtual nics in the set.

`VirtualNics` - (Optional) List of virtual NICs associated with this virtual NIC set.

`Tags` - (Optional) A list of tags to apply to the storage volume.


## See Also

* [opc_compute_vnic_set](https://www.terraform.io/docs/providers/opc/r/compute_vnic_set.html) in the _Terraform Provider Documentation_