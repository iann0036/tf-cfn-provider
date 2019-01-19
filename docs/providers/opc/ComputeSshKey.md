# Terraform::OPC::ComputeSshKey

The ``Terraform::OPC::ComputeSshKey`` resource creates and manages an SSH key in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The unique (within this identity domain) name of the SSH key.

`Key` - (Required) The SSH key itself.

`Enabled` - (Optional) Whether or not the key is enabled. This is useful if you want to temporarily disable an SSH key, without removing it entirely from your Terraform resource definition. Defaults to `true`.


## See Also

* [opc_compute_ssh_key](https://www.terraform.io/docs/providers/opc/r/compute_ssh_key.html) in the _Terraform Provider Documentation_