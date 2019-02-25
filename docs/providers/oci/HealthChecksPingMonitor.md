# Terraform::OCI::HealthChecksPingMonitor

This resource provides the Ping Monitor resource in Oracle Cloud Infrastructure Health Checks service.

Creates a ping monitor. Vantage points will be automatically selected if not specified,
and probes will be initiated from each vantage point to each of the targets at the frequency
specified by `intervalInSeconds`.

## Properties

`CompartmentId` - (Required) The OCID of the compartment.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Required) (Updatable) A user-friendly and mutable name suitable for display in a user interface.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`IntervalInSeconds` - (Required) (Updatable) The monitor interval in seconds. Valid values: 10, 30, and 60.

`IsEnabled` - (Optional) (Updatable) Enables or disables the monitor. Set to 'true' to launch monitoring.

`Port` - (Optional) (Updatable) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`Protocol` - (Required) (Updatable) The protocols for ping probes.

`Targets` - (Required) (Updatable) An array of A target hostname or IP address of the probe.

`TimeoutInSeconds` - (Optional) (Updatable) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`VantagePointNames` - (Optional) (Updatable) An array of The name of a vantage point from which to execute the probe.


## Return Values

### Fn::GetAtt

`IsEnabled` - Enables or disables the monitor. Set to 'true' to launch monitoring.

`IntervalInSeconds` - The monitor interval in seconds. Valid values: 10, 30, and 60.

`TimeoutInSeconds` - The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`DisplayName` - A user-friendly and mutable name suitable for display in a user interface.

`CompartmentId` - The OCID of the compartment.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Port` - The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`Targets` - An array of A target hostname or IP address of the probe.

`VantagePointNames` - An array of The name of a vantage point from which to execute the probe.

`ResultsUrl` - A URL for fetching the probe results.

`Protocol` - The protocols for ping probes.

`Id` - The OCID of the resource.

## See Also

* [oci_health_checks_ping_monitor](https://www.terraform.io/docs/providers/oci/r/health_checks_ping_monitor.html) in the _Terraform Provider Documentation_