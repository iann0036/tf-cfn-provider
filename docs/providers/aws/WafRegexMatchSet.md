# Terraform::AWS::WafRegexMatchSet

Provides a WAF Regex Match Set Resource

## Properties

`Name` - (Required) The name or description of the Regex Match Set.

`RegexMatchTuple` - (Required) The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. See below.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Regex Match Set.

## See Also

* [aws_waf_regex_match_set](https://www.terraform.io/docs/providers/aws/r/waf_regex_match_set.html) in the _Terraform Provider Documentation_