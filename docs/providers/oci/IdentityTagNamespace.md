# Terraform::OCI::IdentityTagNamespace

This resource provides the Tag Namespace resource in Oracle Cloud Infrastructure Identity service.

Creates a new tag namespace in the specified compartment.

You must specify the compartment ID in the request object (remember that the tenancy is simply the root
compartment).

You must also specify a *name* for the namespace, which must be unique across all namespaces in your tenancy
and cannot be changed. The name can contain any ASCII character except the space (_) or period (.).
Names are case insensitive. That means, for example, "myNamespace" and "mynamespace" are not allowed
in the same tenancy. Once you created a namespace, you cannot change the name.
If you specify a name that's already in use in the tenancy, a 409 error is returned.

You must also specify a *description* for the namespace.
It does not have to be unique, and you can change it with
[UpdateTagNamespace](https://docs.cloud.oracle.com/iaas/api/#/en/tagging/20170101/TagNamespace/UpdateTagNamespace).

Tag namespaces cannot be deleted, but they can be retired.
See [Retiring Key Definitions and Namespace Definitions](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm#Retiring) for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment that contains the tag namespace.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - The description you assign to the tag namespace.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Id` - The OCID of the tag namespace.

`IsRetired` - Whether the tag namespace is retired. For more information, see [Retiring Key Definitions and Namespace Definitions](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm#Retiring).

`Name` - The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.

`TimeCreated` - Date and time the tagNamespace was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_identity_tag_namespace](https://www.terraform.io/docs/providers/oci/r/identity_tag_namespace.html) in the _Terraform Provider Documentation_