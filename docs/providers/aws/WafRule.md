# Terraform::AWS::WafRule

Provides a WAF Rule Resource

## Properties

`MetricName` - (Required) The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.

`Name` - (Required) The name or description of the rule.

`Predicates` - (Optional) One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF rule.

## See Also

* [aws_waf_rule](https://www.terraform.io/docs/providers/aws/r/waf_rule.html) in the _Terraform Provider Documentation_