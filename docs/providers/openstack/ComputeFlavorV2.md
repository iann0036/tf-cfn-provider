# Terraform::OpenStack::ComputeFlavorV2

Manages a V2 flavor resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. Flavors are associated with accounts, but a Compute client is needed to create one. If omitted, the `Region` argument of the provider is used. Changing this creates a new flavor.

`Name` - (Required) A unique name for the flavor. Changing this creates a new flavor.

`Ram` - (Required) The amount of RAM to use, in megabytes. Changing this creates a new flavor.

`Vcpus` - (Required) The number of virtual CPUs to use. Changing this creates a new flavor.

`Disk` - (Required) The amount of disk space in gigabytes to use for the root (/) partition. Changing this creates a new flavor.

`Swap` - (Optional) The amount of disk space in megabytes to use. If unspecified, the default is 0. Changing this creates a new flavor.

`RxTxFactor` - (Optional) RX/TX bandwith factor. The default is 1. Changing this creates a new flavor.

`IsPublic` - (Optional) Whether the flavor is public. Changing this creates a new flavor.

`ExtraSpecs` - (Optional) Key/Value pairs of metadata for the flavor.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Ram` - See Properties above.

`Vcpus` - See Properties above.

`Disk` - See Properties above.

`Swap` - See Properties above.

`RxTxFactor` - See Properties above.

`IsPublic` - See Properties above.

`ExtraSpecs` - See Properties above.

## See Also

* [openstack_compute_flavor_v2](https://www.terraform.io/docs/providers/openstack/r/compute_flavor_v2.html) in the _Terraform Provider Documentation_