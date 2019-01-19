# Terraform::NSXT::VmTags

This resource provides a means to configure tags that are applied to objects such as virtual machines. A virtual machine is not directly managed by NSX however, NSX allows attachment of tags to a virtual machine. This tagging enables tag based grouping of objects. Deletion of `Terraform::NSXT::VmTags` resource will remove all tags from the virtual machine and is equivalent to update operation with empty tag set.

## Properties

`InstanceId` - (Required) BIOS Id of the Virtual Machine.

`Tag` - (Required) A list of scope + tag pairs to associate with this VM.


## See Also

* [nsxt_vm_tags](https://www.terraform.io/docs/providers/nsxt/r/vm_tags.html) in the _Terraform Provider Documentation_