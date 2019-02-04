# Terraform::VSphere::ResourcePool

The `Terraform::VSphere::ResourcePool` resource can be used to create and manage
resource pools in standalone hosts or on compute clusters.

For more information on vSphere resource pools, see [this
page][ref-vsphere-resource_pools].

[ref-vsphere-resource_pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html

## Properties

`Name` - (Required) The name of the resource pool.

`ParentResourcePoolId` - (Required) The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a resource pool
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

`CpuShareLevel` - (Optional) The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `CpuShares` will be
ignored.  Default: `normal`.

`CpuShares` - (Optional) The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`CpuShareLevel` must be `custom`.

`CpuReservation` - (Optional) Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`.

`CpuExpandable` - (Optional) Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`.

`CpuLimit` - (Optional) The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`.

`MemoryShareLevel` - (Optional) The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `MemoryShares` will be
ignored.  Default: `normal`.

`MemoryShares` - (Optional) The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`MemoryShareLevel` must be `custom`.

`MemoryReservation` - (Optional) Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`.

`MemoryExpandable` - (Optional) Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`.

`MemoryLimit` - (Optional) The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.


## See Also

* [vsphere_resource_pool](https://www.terraform.io/docs/providers/vsphere/r/resource_pool.html) in the _Terraform Provider Documentation_