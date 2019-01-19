# Terraform::AWS::WafregionalRule

Provides an WAF Regional Rule Resource for use with Application Load Balancer.

## Properties

`Name` - (Required) The name or description of the rule.

`MetricName` - (Required) The name or description for the Amazon CloudWatch metric of this rule.

`Predicate` - (Optional) The objects to include in a rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Regional Rule.

## See Also

* [aws_wafregional_rule](https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html) in the _Terraform Provider Documentation_