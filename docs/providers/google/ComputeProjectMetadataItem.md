# Terraform::Google::ComputeProjectMetadataItem

Manages a single key/value pair on metadata common to all instances for
a project in GCE. Using `Terraform::Google::ComputeProjectMetadataItem` lets you
manage a single key/value setting in Terraform rather than the entire
project metadata map.

## Properties

`Key` - (Required) The metadata key to set.

`Value` - (Required) The value to set for the given metadata key.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.


## See Also

* [google_compute_project_metadata_item](https://www.terraform.io/docs/providers/google/r/compute_project_metadata_item.html) in the _Terraform Provider Documentation_