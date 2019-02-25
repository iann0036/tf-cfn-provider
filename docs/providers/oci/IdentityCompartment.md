# Terraform::OCI::IdentityCompartment

This resource provides the Compartment resource in Oracle Cloud Infrastructure Identity service.

Creates a new compartment in the specified compartment.

**Important:** Unless `EnableDelete` is explicitly set to true:
* Terraform will not delete compartments on destroy, and
* For backwards compatibility, an existing compartment with the same name will be automatically imported into the state. Properties of the existing compartment will be updated to what is defined in the new configuration. This can cause a problem if multiple Terraform configurations are using the same compartment, but, for example, specify a different compartment description.

Specify the parent compartment's OCID as the compartment ID in the request object. Remember that the tenancy
is simply the root compartment. For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You must also specify a *name* for the compartment, which must be unique across all compartments in
your tenancy. You can use this name or the OCID when writing policies that apply
to the compartment. For more information about policies, see
[How Policies Work](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

You must also specify a *description* for the compartment (although it can be an empty string). It does
not have to be unique, and you can change it anytime with
[UpdateCompartment](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Compartment/UpdateCompartment).

## Properties

`CompartmentId` - (Required) The OCID of the parent compartment containing the compartment. In most cases, the 'compartment_id' will be the 'tenancy_ocid' with the exception of nested compartments.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - (Required) (Updatable) The description you assign to the compartment during creation. Does not have to be unique, and it's changeable.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Name` - (Required) (Updatable) The name you assign to the compartment during creation. The name must be unique across all compartments in the parent compartment. Avoid entering confidential information.

`EnableDelete` - (Optional) Defaults to false. If omitted or set to false the provider will implicitly import the compartment if there is a name collision, and will not actually delete the compartment on destroy or removal of the resource declaration. If set to true, the provider will throw an error on a name collision with another compartment, and will attempt to delete the compartment on destroy or removal of the resource declaration.


## Return Values

### Fn::GetAtt

`Description` - The description you assign to the compartment. Does not have to be unique, and it's changeable.

`CompartmentId` - The OCID of the parent compartment containing the compartment.

`IsAccessible` - Indicates whether or not the compartment is accessible for the user making the request. Returns true when the user has INSPECT permissions directly on a resource in the compartment or indirectly (permissions can be on a resource in a subcompartment).

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`TimeCreated` - Date and time the compartment was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`State` - The compartment's current state.

`Id` - The OCID of the compartment.

`Name` - The name you assign to the compartment during creation. The name must be unique across all compartments in the parent. Avoid entering confidential information.

## See Also

* [oci_identity_compartment](https://www.terraform.io/docs/providers/oci/r/identity_compartment.html) in the _Terraform Provider Documentation_