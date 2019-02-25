# Terraform::OCI::CoreServiceGateway

This resource provides the Service Gateway resource in Oracle Cloud Infrastructure Core service.

Creates a new service gateway in the specified compartment.

For the purposes of access control, you must provide the OCID of the compartment where you want
the service gateway to reside. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the service gateway, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

## Properties

`CompartmentId` - (Required) The [OCID] (https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)  of the compartment to contain the service gateway.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Services` - (Required) (Updatable) List of the service OCIDs. These are the services that will be enabled on the service gateway. This list can be empty.
* `ServiceId` - (Required) (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service.

`ServiceId` - (Required) (Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service.

`VcnId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.


## Return Values

### Fn::GetAtt

`BlockTraffic` - Whether the service gateway blocks all traffic through it. The default is `false`. When this is `true`, traffic is not routed to any services, regardless of route rules.  Example: `true`.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the service gateway.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service gateway.

`Services` - List of the services enabled on this service gateway. The list can be empty. You can enable a particular service by using [AttachServiceId](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/ServiceGateway/AttachServiceId).

`ServiceId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the service.

`ServiceName` - The name of the service.

`State` - The service gateway's current state.

`TimeCreated` - The date and time the service gateway was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the service gateway belongs to.

## See Also

* [oci_core_service_gateway](https://www.terraform.io/docs/providers/oci/r/core_service_gateway.html) in the _Terraform Provider Documentation_