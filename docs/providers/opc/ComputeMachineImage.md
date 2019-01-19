# Terraform::OPC::ComputeMachineImage

The ``Terraform::OPC::ComputeMachineImage`` resource creates and manages a machine image template of a virtual hard disk of a specific size with an installed operating system.

Before performing this creating the Machine Image, you must upload your machine image file to Oracle Cloud Infrastructure Object Storage Classic `compute_images` container

## Properties

`Account` - (Required) The two part name of the compute object storage account in the format `/Compute-{identity_domain}/cloud_storage`.

`Name` - (Required) The name of the Machine Image.

`File` - (Required) The name of the Machine Image .tar.gz file in the `compute_images` storage container.

`Description` - (Optional) A description of the Machine Image.

`Attributes` - (Optional) An optional JSON object of arbitrary attributes to be made available to the instance. These are user-defined tags. After defining attributes, you can view them from within an instance at http://192.0.0.192/.

`ErrorReason` - Description of the state of the machine image if there is an error.

`Hypervisor` -  Dictionary of hypervisor-specific attributes.

`ImageFormat` - The format of the image.

`Platform` - The OS platform of the image.

`State` - The state of the uploaded machine image.

`Uri` - The Uniform Resource Identifier for the Machine Image.


## See Also

* [opc_compute_machine_image](https://www.terraform.io/docs/providers/opc/r/compute_machine_image.html) in the _Terraform Provider Documentation_