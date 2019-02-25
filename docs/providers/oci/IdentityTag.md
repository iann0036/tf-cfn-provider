# Terraform::OCI::IdentityTag

This resource provides the Tag resource in Oracle Cloud Infrastructure Identity service.

Creates a new tag in the specified tag namespace.

You must specify either the OCID or the name of the tag namespace that will contain this tag definition.

You must also specify a *name* for the tag, which must be unique across all tags in the tag namespace
and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters.
Names are case insensitive. That means, for example, "myTag" and "mytag" are not allowed in the same namespace.
If you specify a name that's already in use in the tag namespace, a 409 error is returned.

You must also specify a *description* for the tag.
It does not have to be unique, and you can change it with
[UpdateTag](https://docs.cloud.oracle.com/iaas/api/#/en/tagging/20170901/Tag/UpdateTag).

## Properties

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - (Required) (Updatable) The description you assign to the tag during creation.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`IsCostTracking` - (Optional) (Updatable) Indicates whether the tag is enabled for cost tracking.

`Name` - (Required) The name you assign to the tag during creation. The name must be unique within the tag namespace and cannot be changed.

`TagNamespaceId` - (Required) The OCID of the tag namespace.

`IsRetired` - (Optional) (Updatable) Indicates whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions](https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).


## Return Values

### Fn::GetAtt

`IsCostTracking` - Indicates whether the tag is enabled for cost tracking.

`Description` - The description you assign to the tag.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}``.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`TimeCreated` - Date and time the tag was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`.

`TagNamespaceId` - The OCID of the namespace that contains the tag definition.

`IsRetired` - Indicates whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm#Retiring).

`Id` - The OCID of the tag definition.

`Name` - The name of the tag. The name must be unique across all tags in the tag namespace and can't be changed.

## See Also

* [oci_identity_tag](https://www.terraform.io/docs/providers/oci/r/identity_tag.html) in the _Terraform Provider Documentation_