# Terraform::OCI::IdentityPolicy

This resource provides the Policy resource in Oracle Cloud Infrastructure Identity service.

Creates a new policy in the specified compartment (either the tenancy or another of your compartments).
If you're new to policies, see [Getting Started with Policies](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

You must specify a *name* for the policy, which must be unique across all policies in your tenancy
and cannot be changed.

You must also specify a *description* for the policy (although it can be an empty string). It does not
have to be unique, and you can change it anytime with [UpdatePolicy](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Policy/UpdatePolicy).

You must specify one or more policy statements in the statements array. For information about writing
policies, see [How Policies Work](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policies.htm) and
[Common Policies](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
New policies take effect typically within 10 seconds.

## Properties

`CompartmentId` - (Required) The OCID of the compartment containing the policy (either the tenancy or another compartment).

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - (Required) (Updatable) The description you assign to the policy during creation. Does not have to be unique, and it's changeable.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Name` - (Required) The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed.

`Statements` - (Required) (Updatable) An array of policy statements written in the policy language. See [How Policies Work](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policies.htm) and [Common Policies](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

`VersionDate` - (Optional) (Updatable) The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


## Return Values

### Fn::GetAtt

`Statements` - An array of one or more policy statements written in the policy language.

`Description` - The description you assign to the policy. Does not have to be unique, and it's changeable.

`CompartmentId` - The OCID of the compartment containing the policy (either the tenancy or another compartment).

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`TimeCreated` - Date and time the policy was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`State` - The policy's current state.

`VersionDate` - The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.

`Id` - The OCID of the policy.

`Name` - The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed.

## See Also

* [oci_identity_policy](https://www.terraform.io/docs/providers/oci/r/identity_policy.html) in the _Terraform Provider Documentation_