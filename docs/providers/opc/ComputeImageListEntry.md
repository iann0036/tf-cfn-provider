# Terraform::OPC::ComputeImageListEntry

The ``Terraform::OPC::ComputeImageListEntry`` resource creates and manages an Image List Entry in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The name of the Image List.

`MachineImages` - (Required) An array of machine images.

`Version` - (Required) The unique version of the image list entry, as an integer.

`Attributes` - (Optional) JSON String of optional data that will be passed to an instance of this machine image when it is launched.


## Return Values

### Fn::GetAtt

`Uri` - The Unique Resource Identifier for the Image List Entry.

## See Also

* [opc_compute_image_list_entry](https://www.terraform.io/docs/providers/opc/r/compute_image_list_entry.html) in the _Terraform Provider Documentation_