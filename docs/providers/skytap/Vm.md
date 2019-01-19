# Terraform::Skytap::Vm

Provides a Skytap Virtual Machine (VM) resource. The environment VM resource represents an image of a single virtual machine.

~> **NOTE:**
* VMs do not exist outside of environments or templates.
* An environment or template can have multiple VMs.
* Each VM is a unique resource. Therefore, a VM in a template will have a different ID than a VM in an environment created from that template.
* The VM will be run immediately after creation.

## Properties

TBC

## See Also

* [skytap_vm](https://www.terraform.io/docs/providers/skytap/r/vm.html) in the _Terraform Provider Documentation_