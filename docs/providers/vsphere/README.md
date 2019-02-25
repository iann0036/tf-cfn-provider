# VMware vSphere Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vsphere** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Required) This is the username for vSphere API operations.
* `password` - (Required) This is the password for vSphere API operations.
* `vsphere_server` - (Required) This is the vCenter server name for vSphere API
  operations. Can also be specified with the `VSPHERE_SERVER` environment
  variable.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is `false`.


## Supported Resources

* [Terraform::VSphere::ComputeClusterHostGroup](ComputeClusterHostGroup.md)
* [Terraform::VSphere::ComputeClusterVmAffinityRule](ComputeClusterVmAffinityRule.md)
* [Terraform::VSphere::ComputeClusterVmAntiAffinityRule](ComputeClusterVmAntiAffinityRule.md)
* [Terraform::VSphere::ComputeClusterVmDependencyRule](ComputeClusterVmDependencyRule.md)
* [Terraform::VSphere::ComputeClusterVmGroup](ComputeClusterVmGroup.md)
* [Terraform::VSphere::ComputeClusterVmHostRule](ComputeClusterVmHostRule.md)
* [Terraform::VSphere::ComputeCluster](ComputeCluster.md)
* [Terraform::VSphere::CustomAttribute](CustomAttribute.md)
* [Terraform::VSphere::Datacenter](Datacenter.md)
* [Terraform::VSphere::DatastoreClusterVmAntiAffinityRule](DatastoreClusterVmAntiAffinityRule.md)
* [Terraform::VSphere::DatastoreCluster](DatastoreCluster.md)
* [Terraform::VSphere::DistributedPortGroup](DistributedPortGroup.md)
* [Terraform::VSphere::DistributedVirtualSwitch](DistributedVirtualSwitch.md)
* [Terraform::VSphere::DpmHostOverride](DpmHostOverride.md)
* [Terraform::VSphere::DrsVmOverride](DrsVmOverride.md)
* [Terraform::VSphere::File](File.md)
* [Terraform::VSphere::Folder](Folder.md)
* [Terraform::VSphere::HaVmOverride](HaVmOverride.md)
* [Terraform::VSphere::HostPortGroup](HostPortGroup.md)
* [Terraform::VSphere::HostVirtualSwitch](HostVirtualSwitch.md)
* [Terraform::VSphere::License](License.md)
* [Terraform::VSphere::NasDatastore](NasDatastore.md)
* [Terraform::VSphere::ResourcePool](ResourcePool.md)
* [Terraform::VSphere::StorageDrsVmOverride](StorageDrsVmOverride.md)
* [Terraform::VSphere::TagCategory](TagCategory.md)
* [Terraform::VSphere::Tag](Tag.md)
* [Terraform::VSphere::VappContainer](VappContainer.md)
* [Terraform::VSphere::VappEntity](VappEntity.md)
* [Terraform::VSphere::VirtualDisk](VirtualDisk.md)
* [Terraform::VSphere::VirtualMachineSnapshot](VirtualMachineSnapshot.md)
* [Terraform::VSphere::VirtualMachine](VirtualMachine.md)
* [Terraform::VSphere::VmfsDatastore](VmfsDatastore.md)