# VMware vSphere Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vsphere**. The below arguments may be included as the key/value or JSON properties in the secret:

* `user` - (Required) This is the username for vSphere API operations. Can also
  be specified with the `VSPHERE_USER` environment variable.
* `password` - (Required) This is the password for vSphere API operations. Can
  also be specified with the `VSPHERE_PASSWORD` environment variable.
* `vsphere_server` - (Required) This is the vCenter server name for vSphere API
  operations. Can also be specified with the `VSPHERE_SERVER` environment
  variable.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is `false`. Can also be specified with the `VSPHERE_ALLOW_UNVERIFIED_SSL`
  environment variable.


## Supported Resources

* [Terraform::VSphere::ComputeClusterHostGroup](docs/providers/vsphere/ComputeClusterHostGroup.md)
* [Terraform::VSphere::ComputeClusterVmAffinityRule](docs/providers/vsphere/ComputeClusterVmAffinityRule.md)
* [Terraform::VSphere::ComputeClusterVmAntiAffinityRule](docs/providers/vsphere/ComputeClusterVmAntiAffinityRule.md)
* [Terraform::VSphere::ComputeClusterVmDependencyRule](docs/providers/vsphere/ComputeClusterVmDependencyRule.md)
* [Terraform::VSphere::ComputeClusterVmGroup](docs/providers/vsphere/ComputeClusterVmGroup.md)
* [Terraform::VSphere::ComputeClusterVmHostRule](docs/providers/vsphere/ComputeClusterVmHostRule.md)
* [Terraform::VSphere::ComputeCluster](docs/providers/vsphere/ComputeCluster.md)
* [Terraform::VSphere::CustomAttribute](docs/providers/vsphere/CustomAttribute.md)
* [Terraform::VSphere::Datacenter](docs/providers/vsphere/Datacenter.md)
* [Terraform::VSphere::DatastoreClusterVmAntiAffinityRule](docs/providers/vsphere/DatastoreClusterVmAntiAffinityRule.md)
* [Terraform::VSphere::DatastoreCluster](docs/providers/vsphere/DatastoreCluster.md)
* [Terraform::VSphere::DistributedPortGroup](docs/providers/vsphere/DistributedPortGroup.md)
* [Terraform::VSphere::DistributedVirtualSwitch](docs/providers/vsphere/DistributedVirtualSwitch.md)
* [Terraform::VSphere::DpmHostOverride](docs/providers/vsphere/DpmHostOverride.md)
* [Terraform::VSphere::DrsVmOverride](docs/providers/vsphere/DrsVmOverride.md)
* [Terraform::VSphere::File](docs/providers/vsphere/File.md)
* [Terraform::VSphere::Folder](docs/providers/vsphere/Folder.md)
* [Terraform::VSphere::HaVmOverride](docs/providers/vsphere/HaVmOverride.md)
* [Terraform::VSphere::HostPortGroup](docs/providers/vsphere/HostPortGroup.md)
* [Terraform::VSphere::HostVirtualSwitch](docs/providers/vsphere/HostVirtualSwitch.md)
* [Terraform::VSphere::License](docs/providers/vsphere/License.md)
* [Terraform::VSphere::NasDatastore](docs/providers/vsphere/NasDatastore.md)
* [Terraform::VSphere::ResourcePool](docs/providers/vsphere/ResourcePool.md)
* [Terraform::VSphere::StorageDrsVmOverride](docs/providers/vsphere/StorageDrsVmOverride.md)
* [Terraform::VSphere::TagCategory](docs/providers/vsphere/TagCategory.md)
* [Terraform::VSphere::Tag](docs/providers/vsphere/Tag.md)
* [Terraform::VSphere::VappContainer](docs/providers/vsphere/VappContainer.md)
* [Terraform::VSphere::VappEntity](docs/providers/vsphere/VappEntity.md)
* [Terraform::VSphere::VirtualDisk](docs/providers/vsphere/VirtualDisk.md)
* [Terraform::VSphere::VirtualMachineSnapshot](docs/providers/vsphere/VirtualMachineSnapshot.md)
* [Terraform::VSphere::VirtualMachine](docs/providers/vsphere/VirtualMachine.md)
* [Terraform::VSphere::VmfsDatastore](docs/providers/vsphere/VmfsDatastore.md)