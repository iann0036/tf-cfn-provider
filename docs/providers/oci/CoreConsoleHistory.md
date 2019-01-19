# Terraform::OCI::CoreConsoleHistory

This resource provides the Console History resource in Oracle Cloud Infrastructure Core service.

Captures the most recent serial console data (up to a megabyte) for the
specified instance.

The `CaptureConsoleHistory` operation works with the other console history operations
as described below.

1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the
most recent console history. This call returns a `ConsoleHistory`
object. The object will have a state of REQUESTED.
2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with
the identifier of the console history metadata. The state of the
`ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and
then SUCCEEDED (or FAILED).
3. Use `GetConsoleHistoryContent` to get the actual console history data (not the
metadata).
4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata
and the console history data.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The availability domain of an instance.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My console history metadata`.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the console history metadata object.

`InstanceId` - The OCID of the instance this console history was fetched from.

`State` - The current state of the console history.

`TimeCreated` - The date and time the history was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_console_history](https://www.terraform.io/docs/providers/oci/r/core_console_history.html) in the _Terraform Provider Documentation_