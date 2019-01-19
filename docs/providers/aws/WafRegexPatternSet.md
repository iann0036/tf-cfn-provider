# Terraform::AWS::WafRegexPatternSet

Provides a WAF Regex Pattern Set Resource

## Properties

`Name` - (Required) The name or description of the Regex Pattern Set.

`RegexPatternStrings` - (Optional) A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Regex Pattern Set.

## See Also

* [aws_waf_regex_pattern_set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html) in the _Terraform Provider Documentation_