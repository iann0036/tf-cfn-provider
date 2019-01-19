# Terraform::AWS::ConfigConfigurationAggregator

Manages an AWS Config Configuration Aggregator

## Properties

`Name` - (Required) The name of the configuration aggregator.

`AccountAggregationSource` - (Optional) The account(s) to aggregate config data from as documented below.

`OrganizationAggregationSource` - (Optional) The organization to aggregate config data from as documented below.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the aggregator.

## See Also

* [aws_config_configuration_aggregator](https://www.terraform.io/docs/providers/aws/r/config_configuration_aggregator.html) in the _Terraform Provider Documentation_