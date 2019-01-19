# Terraform::AWS::ConfigConfigRule

Provides an AWS Config Rule.

~> **Note:** Config Rule requires an existing [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - The ARN of the config rule.

`RuleId` - The ID of the config rule.

## See Also

* [aws_config_config_rule](https://www.terraform.io/docs/providers/aws/r/config_config_rule.html) in the _Terraform Provider Documentation_