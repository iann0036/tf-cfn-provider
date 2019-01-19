# Terraform::Datadog::IntegrationAws

Provides a Datadog - Amazon Web Services integration resource. This can be used to create and manage Datadog - Amazon Web Services integration.

Update operations are currently not supported with datadog API so any change forces a new resource.

## Properties

`AccountId` - (Required) Your AWS Account ID without dashes.

`RoleName` - (Required) Your Datadog role delegation name.

`FilterTags` - (Optional) Array of EC2 tags (in the form `key:value`) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used.

`HostTags` - (Optinal) Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.

`AccountSpecificNamespaceRules` - (Optinal) Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the [available namespace rules API endpoint](https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules).


## Return Values

### Fn::GetAtt

`ExternalId` - AWS External ID.

## See Also

* [datadog_integration_aws](https://www.terraform.io/docs/providers/datadog/r/integration_aws.html) in the _Terraform Provider Documentation_