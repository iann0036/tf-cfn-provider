# Terraform::Triton::Key

The `Terraform::Triton::Key` resource represents an SSH key for a Triton account.

## Properties

`Name` - (string, Change forces new resource) The name of the key. If this is left empty, the name is inferred from the comment in the SSH key material.

`Key` - (string, Required, Change forces new resource) The SSH key material. In order to read this from a file, use the `file` interpolation.


## See Also

* [triton_key](https://www.terraform.io/docs/providers/triton/r/key.html) in the _Terraform Provider Documentation_