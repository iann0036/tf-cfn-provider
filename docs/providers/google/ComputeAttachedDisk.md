# Terraform::Google::ComputeAttachedDisk

Persistent disks can be attached to a compute instance using [the `attached_disk`
section within the compute instance configuration](https://www.terraform.io/docs/providers/google/r/compute_instance.html#attached_disk).
However there may be situations where managing the attached disks via the compute
instance config isn't preferable or possible, such as attaching dynamic
numbers of disks using the `count` variable.


To get more information about attaching disks, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instances/attachDisk)
* [Resource: google_compute_disk](https://www.terraform.io/docs/providers/google/r/compute_disk.html)
* How-to Guides
    * [Adding a persistent disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk)

## Properties


## See Also

* [google_compute_attached_disk](https://www.terraform.io/docs/providers/google/r/compute_attached_disk.html) in the _Terraform Provider Documentation_