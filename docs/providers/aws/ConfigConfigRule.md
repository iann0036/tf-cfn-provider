# Terraform::AWS::ConfigConfigRule

Provides an AWS Config Rule.

~> **Note:** Config Rule requires an existing [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

## Properties

`Name` - (Required) The name of the rule.

`Description` - (Optional) Description of the rule.

`InputParameters` - (Optional) A string in JSON format that is passed to the AWS Config rule Lambda function.

`MaximumExecutionFrequency` - (Optional) The maximum frequency with which AWS Config runs evaluations for a rule.

`Scope` - (Optional) Scope defines which resources can trigger an evaluation for the rule as documented below.

`Source` - (Required) Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the config rule.

`RuleId` - The ID of the config rule.

## See Also

* [aws_config_config_rule](https://www.terraform.io/docs/providers/aws/r/config_config_rule.html) in the _Terraform Provider Documentation_