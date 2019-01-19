# Terraform::AWS::WafregionalRuleGroup

Provides a WAF Regional Rule Group Resource

## Properties

`Name` - (Required) A friendly name of the rule group.

`MetricName` - (Required) A friendly name for the metrics from the rule group.

`ActivatedRule` - (Optional) A list of activated rules, see below.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Regional Rule Group.

## See Also

* [aws_wafregional_rule_group](https://www.terraform.io/docs/providers/aws/r/wafregional_rule_group.html) in the _Terraform Provider Documentation_