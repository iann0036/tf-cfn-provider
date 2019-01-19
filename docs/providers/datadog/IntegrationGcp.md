# Terraform::Datadog::IntegrationGcp

Provides a Datadog - Google Cloud Platform integration resource. This can be used to create and manage Datadog - Google Cloud Platform integration.

## Properties

`ProjectId` - (Required) Your Google Cloud project ID found in your JSON service account key.

`PrivateKeyId` - (Required) Your private key ID found in your JSON service account key.

`PrivateKey` - (Required) Your private key name found in your JSON service account key.

`ClientEmail` - (Required) Your email found in your JSON service account key.

`ClientId` - (Required) Your ID found in your JSON service account key.

`HostFilters` - (Optional) Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.


## Return Values

### Fn::GetAtt

`ProjectId` - Google Cloud project ID.

`ClientEmail` - Google Cloud project service account email.

`HostFilters` - Host filters.

## See Also

* [datadog_integration_gcp](https://www.terraform.io/docs/providers/datadog/r/integration_gcp.html) in the _Terraform Provider Documentation_