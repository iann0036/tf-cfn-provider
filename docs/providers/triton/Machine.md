# Terraform::Triton::Machine

The `Terraform::Triton::Machine` resource represents a virtual machine or infrastructure container running in Triton.

~> **Note:** Starting with Triton 0.2.0, Please note that when you want to specify the networks that you want the machine to be attached to, use the `Networks` parameter
and not the `nic` parameter.

## Properties

`Name` - (string)
The friendly name for the machine. Triton will generate a name if one is not specified.

`Tags` - (map)
A mapping of tags to apply to the machine.

`Cns` - (map of CNS attributes, Optional)
A mapping of [CNS](https://docs.joyent.com/public-cloud/network/cns) attributes to apply to the machine.

`Metadata` - (map, optional)
A mapping of metadata to apply to the machine.

`Package` - (string, Required)
The name of the package to use for provisioning.

`Image` - (string, Required)
The UUID of the image to provision.

`Networks` - (list, optional)
The list of networks to associate with the machine. The network ID will be in hex form, e.g `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

`Affinity` - (list of Affinity rules, Optional)
A list of valid [Affinity Rules](https://apidocs.joyent.com/cloudapi/#affinity-rules) to apply to the machine which assist in data center placement. Using this attribute will force resource creation to be serial. NOTE: Affinity rules are best guess and assist in placing instances across a data center. They're used at creation and not referenced after.

`(Deprecated) locality` - (map of Locality hints, Optional)
A mapping of [Locality](https://apidocs.joyent.com/cloudapi/#CreateMachine) attributes to apply to the machine that assist in data center placement. NOTE: Locality hints are only used at the time of machine creation and not referenced after. Locality is deprecated as of
[CloudAPI v8.3.0](https://apidocs.joyent.com/cloudapi/#830).

`FirewallEnabled` - (boolean)  Default: `false`
Whether the cloud firewall should be enabled for this machine.

`RootAuthorizedKeys` - (string)
The public keys authorized for root access via SSH to the machine.

`UserData` - (string)
Data to be copied to the machine on boot. **NOTE:** The content of `UserData`
will _not be executed_ on boot. The data will only be written to the file on each
boot before the content of the script from `UserScript` is to be run.

`UserScript` - (string)
The user script to run on boot (every boot on SmartMachines). To learn more about
both the user script and user data see the [metadata API][2] documentation and the
[Joyent Metadata Data Dictionary][1] specification.

`AdministratorPw` - (string)
The initial password for the Administrator user. Only used for Windows virtual machines.

`CloudConfig` - (string)
Cloud-init configuration for Linux brand machines, used instead of `UserData`.

`DeletionProtectionEnabled` - (bool)
Whether an instance is destroyable. Default is `false`.


## See Also

* [triton_machine](https://www.terraform.io/docs/providers/triton/r/machine.html) in the _Terraform Provider Documentation_