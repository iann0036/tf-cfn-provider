# Terraform::OCI::HealthChecksHttpProbe

This resource provides the Http Probe resource in Oracle Cloud Infrastructure Health Checks service.

Creates an on-demand HTTP probe. The location response header contains the URL for
fetching the probe results.

*Note:* On-demand probe configurations are not saved.

## Properties

`CompartmentId` - (Required) The OCID of the compartment.

`Headers` - (Optional) A dictionary of HTTP request headers.

`Method` - (Optional) The supported HTTP methods available for probes.

`Path` - (Optional) The optional URL path to probe, including query parameters.

`Port` - (Optional) The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

`Protocol` - (Required) The supported protocols available for HTTP probes.

`Targets` - (Required) An array of A target hostname or IP address of the probe.

`TimeoutInSeconds` - (Optional) The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`VantagePointNames` - (Optional) An array of The name of a vantage point from which to execute the probe.


## Return Values

### Fn::GetAtt

`TimeoutInSeconds` - The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.

`Protocol` - The supported protocols available for HTTP probes.

`CompartmentId` - The OCID of the compartment.

`Id` - The OCID of the resource.

`Targets` - An array of A target hostname or IP address of the probe.

`Headers` - A dictionary of HTTP request headers.

`VantagePointNames` - An array of The name of a vantage point from which to execute the probe.

`ResultsUrl` - A URL for fetching the probe results.

`Path` - The optional URL path to probe, including query parameters.

`Method` - The supported HTTP methods available for probes.

`Port` - The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.

## See Also

* [oci_health_checks_http_probe](https://www.terraform.io/docs/providers/oci/r/health_checks_http_probe.html) in the _Terraform Provider Documentation_