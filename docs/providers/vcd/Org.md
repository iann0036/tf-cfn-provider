# Terraform::VCD::Org

Provides a vCloud Director Org resource. This can be used to create and delete an organization.
Requires system administrator privileges.

Supported in provider *v2.0+*

## Properties

`Name` - (Required) Org name.

`FullName` - (Required) Org full name.

`DeleteRecursive` - (Required) - pass `DeleteRecursive`=true as query parameter to remove an organization or VDC and any objects it contains that are in a state that normally allows removal.

`DeleteForce` - (Required) - pass `delete_force=true` and `delete_recursive=true` to remove an organization or VDC and any objects it contains, regardless of their state.

`IsEnabled` - (Optional) - True if this organization is enabled (allows login and all other operations). Default is `true`.

`Description` - (Optional) - Org description. Default is empty.

`DeployedVmQuota` - (Optional) - Maximum number of virtual machines that can be deployed simultaneously by a member of this organization. Default is unlimited (-1).

`StoredVmQuota` - (Optional) - Maximum number of virtual machines in vApps or vApp templates that can be stored in an undeployed state by a member of this organization. Default is unlimited (-1).

`CanPublishCatalogs` - (Optional) - True if this organization is allowed to share catalogs. Default is `true`.

`DelayAfterPowerOnSeconds` - (Optional) - Specifies this organization's default for virtual machine boot delay after power on. Default is `0`.


## See Also

* [vcd_org](https://www.terraform.io/docs/providers/vcd/r/org.html) in the _Terraform Provider Documentation_