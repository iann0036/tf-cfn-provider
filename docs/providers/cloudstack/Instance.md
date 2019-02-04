# Terraform::CloudStack::Instance

Creates and automatically starts a virtual machine based on a service offering,
disk offering, and template.

## Properties

`Name` - (Required) The name of the instance.

`DisplayName` - (Optional) The display name of the instance.

`ServiceOffering` - (Required) The name or ID of the service offering used
for this instance.

`NetworkId` - (Optional) The ID of the network to connect this instance
to. Changing this forces a new resource to be created.

`IpAddress` - (Optional) The IP address to assign to this instance. Changing
this forces a new resource to be created.

`Template` - (Required) The name or ID of the template used for this
instance. Changing this forces a new resource to be created.

`RootDiskSize` - (Optional) The size of the root disk in gigabytes. The
root disk is resized on deploy. Only applies to template-based deployments.
Changing this forces a new resource to be created.

`Group` - (Optional) The group name of the instance.

`AffinityGroupIds` - (Optional) List of affinity group IDs to apply to this
instance.

`AffinityGroupNames` - (Optional) List of affinity group names to apply to
this instance.

`SecurityGroupIds` - (Optional) List of security group IDs to apply to this
instance. Changing this forces a new resource to be created.

`SecurityGroupNames` - (Optional) List of security group names to apply to
this instance. Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

`Zone` - (Required) The name or ID of the zone where this instance will be
created. Changing this forces a new resource to be created.

`StartVm` - (Optional) This determines if the instances is started after it
is created (defaults true).

`UserData` - (Optional) The user data to provide when launching the
instance. This can be either plain text or base64 encoded text.

`Keypair` - (Optional) The name of the SSH key pair that will be used to
access this instance.

`Expunge` - (Optional) This determines if the instance is expunged when it is
destroyed (defaults false).


## Return Values

### Fn::GetAtt

`Id` - The instance ID.

`DisplayName` - The display name of the instance.

## See Also

* [cloudstack_instance](https://www.terraform.io/docs/providers/cloudstack/r/instance.html) in the _Terraform Provider Documentation_