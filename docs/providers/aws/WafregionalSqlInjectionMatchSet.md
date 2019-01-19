# Terraform::AWS::WafregionalSqlInjectionMatchSet

Provides a WAF Regional SQL Injection Match Set Resource for use with Application Load Balancer.

## Properties

`Name` - (Required) The name or description of the SizeConstraintSet.

`SqlInjectionMatchTuple` - (Optional) The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF SqlInjectionMatchSet.

## See Also

* [aws_wafregional_sql_injection_match_set](https://www.terraform.io/docs/providers/aws/r/wafregional_sql_injection_match_set.html) in the _Terraform Provider Documentation_