# Terraform::OCI::HealthChecksPingProbe

This resource provides the Ping Probe resource in Oracle Cloud Infrastructure Health Checks service.

Creates an on-demand ping probe. The location response header contains the URL for
fetching probe results.

*Note:* The on-demand probe configuration is not saved.

## Properties

`CompartmentId` - (Required) The OCID of the compartment.

`Port` - (Optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`Protocol` - (Required) The protocols for ping probes.

`Targets` - (Required) An array of A target hostname or IP address of the probe.

`TimeoutInSeconds` - (Optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`VantagePointNames` - (Optional) An array of The name of a vantage point from which to execute the probe.


## Return Values

### Fn::GetAtt

`VantagePointNames` - An array of The name of a vantage point from which to execute the probe.

`Protocol` - The protocols for ping probes.

`CompartmentId` - The OCID of the compartment.

`Id` - The OCID of the resource.

`Port` - The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`ResultsUrl` - A URL for fetching the probe results.

`TimeoutInSeconds` - The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`Targets` - An array of A target hostname or IP address of the probe.

## See Also

* [oci_health_checks_ping_probe](https://www.terraform.io/docs/providers/oci/r/health_checks_ping_probe.html) in the _Terraform Provider Documentation_