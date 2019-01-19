# Terraform::VSphere::Datacenter

Provides a VMware vSphere datacenter resource. This can be used as the primary
container of inventory objects such as hosts and virtual machines.

## Properties

`Name` - (Required) The name of the datacenter. This name needs to be unique within the folder. Forces a new resource if changed.

`Folder` - (Optional) The folder where the datacenter should be created. Forces a new resource if changed.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See [here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) Map of custom attribute ids to value strings to set for datacenter resource. See [here][docs-setting-custom-attributes] for a reference on how to set values for custom attributes.


## See Also

* [vsphere_datacenter](https://www.terraform.io/docs/providers/vsphere/r/datacenter.html) in the _Terraform Provider Documentation_