# Terraform::Skytap::Vm

Provides a Skytap Virtual Machine (VM) resource. The environment VM resource represents an image of a single virtual machine.

~> **NOTE:**
* VMs do not exist outside of environments or templates.
* An environment or template can have multiple VMs.
* Each VM is a unique resource. Therefore, a VM in a template will have a different ID than a VM in an environment created from that template.
* The VM will be run immediately after creation.

## Properties

`EnvironmentId` - (Required, Force New) ID of the environment you want to add the VM to. If updating with a new one then the VM will be recreated.

`TemplateId` - (Required, Force New) ID of the template you want to create the vm from. If updating with a new one then the VM will be recreated.

`VmId` - (Required, Force New) ID of the VM you want to create the VM from. If updating with a new one then the VM will be recreated.

`Name` - (Required, Force New) A unique name for the published service. * `InternalPort` - (Required, Force New) The port that is exposed on the interface. Typically this will be dictated by standard usage (e.g., port 80 for http traffic, port 22 for SSH).

`Cpus` - (Optional, Computed) Number of CPUs allocated to this virtual machine. Valid range is 1 to 12. Maximum limit depends on the `max_cpus` setting.

`Ram` - (Optional, Computed) Amount of RAM allocated to this VM. Valid range is 256 and 131,072 (MB). Maximum limit depends on `max_ram` setting.

`OsDiskSize` - (Optional, Computed) The size of the OS disk. The disk size is in MiB; it will be converted to GiB in the Skytap UI. The maximum disk size is 2,096,128 MiB (1.999 TiB).

`Disk` - (Optional) Array of virtual disks within the VM. The disk size is in MiB; it will be converted to GiB in the Skytap UI. The maximum disk size is 2,096,128 MiB (1.999 TiB).

`Size` - (Required) Specify the size of the disk. The new disk’s size should be provided in MiB. The minimum disk size is 2048 MiB; the maximum is 2096128 MiB (1.999 TiB).

`NetworkInterface` - (Optional, Computed, ForceNew) A Skytap network adapter is a virtualized network interface card (also known as a network adapter). It is logically contained in a VM and attached to a network. * `InterfaceType` - (Required, Force New) Type of network that this network adapter is attached to. * `NetworkId` - (Required, Force New) ID of the network that this network adapter is attached to. *	`ip` - (Required, Force New) The IP address (for example, 10.1.0.37). Skytap will not assign the same IP address to multiple interfaces on the same network. * `Hostname` - (Required, Force New) Limited to 32 characters. Valid characters are lowercase letters, numbers, and hyphens. Cannot begin or end with hyphens. Cannot be `gw`. * `PublishedService` - (Optional, Force New) Generally, a published service represents a binding of a port on a network interface to an IP and port that is routable and accessible from the public Internet. This mechanism is used to selectively expose ports on the guest to the public Internet.

`InterfaceType` - (Required, Force New) Type of network that this network adapter is attached to. * `NetworkId` - (Required, Force New) ID of the network that this network adapter is attached to. *	`ip` - (Required, Force New) The IP address (for example, 10.1.0.37). Skytap will not assign the same IP address to multiple interfaces on the same network. * `Hostname` - (Required, Force New) Limited to 32 characters. Valid characters are lowercase letters, numbers, and hyphens. Cannot begin or end with hyphens. Cannot be `gw`. * `PublishedService` - (Optional, Force New) Generally, a published service represents a binding of a port on a network interface to an IP and port that is routable and accessible from the public Internet. This mechanism is used to selectively expose ports on the guest to the public Internet.

`NetworkId` - (Required, Force New) ID of the network that this network adapter is attached to. *	`ip` - (Required, Force New) The IP address (for example, 10.1.0.37). Skytap will not assign the same IP address to multiple interfaces on the same network. * `Hostname` - (Required, Force New) Limited to 32 characters. Valid characters are lowercase letters, numbers, and hyphens. Cannot begin or end with hyphens. Cannot be `gw`. * `PublishedService` - (Optional, Force New) Generally, a published service represents a binding of a port on a network interface to an IP and port that is routable and accessible from the public Internet. This mechanism is used to selectively expose ports on the guest to the public Internet.

`Hostname` - (Required, Force New) Limited to 32 characters. Valid characters are lowercase letters, numbers, and hyphens. Cannot begin or end with hyphens. Cannot be `gw`. * `PublishedService` - (Optional, Force New) Generally, a published service represents a binding of a port on a network interface to an IP and port that is routable and accessible from the public Internet. This mechanism is used to selectively expose ports on the guest to the public Internet.

`PublishedService` - (Optional, Force New) Generally, a published service represents a binding of a port on a network interface to an IP and port that is routable and accessible from the public Internet. This mechanism is used to selectively expose ports on the guest to the public Internet.

`InternalPort` - (Required, Force New) The port that is exposed on the interface. Typically this will be dictated by standard usage (e.g., port 80 for http traffic, port 22 for SSH).


## See Also

* [skytap_vm](https://www.terraform.io/docs/providers/skytap/r/vm.html) in the _Terraform Provider Documentation_