# Terraform::Triton::Machine

The `triton_machine` resource represents a virtual machine or infrastructure container running in Triton.

~> **Note:** Starting with Triton 0.2.0, Please note that when you want to specify the networks that you want the machine to be attached to, use the `networks` parameter
and not the `nic` parameter.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [triton_machine](https://www.terraform.io/docs/providers/triton/r/machine.html) in the _Terraform Provider Documentation_