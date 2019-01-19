# Terraform::AWS::WafSqlInjectionMatchSet

Provides a WAF SQL Injection Match Set Resource

## Properties

`Name` - (Required) The name or description of the SizeConstraintSet.

`SqlInjectionMatchTuples` - (Optional) The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF SQL Injection Match Set.

## See Also

* [aws_waf_sql_injection_match_set](https://www.terraform.io/docs/providers/aws/r/waf_sql_injection_match_set.html) in the _Terraform Provider Documentation_