# Terraform::AWS::WafregionalRegexPatternSet

Provides a WAF Regional Regex Pattern Set Resource

## Properties

`Name` - (Required) The name or description of the Regex Pattern Set.

`RegexPatternStrings` - (Optional) A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Regional Regex Pattern Set.

## See Also

* [aws_wafregional_regex_pattern_set](https://www.terraform.io/docs/providers/aws/r/wafregional_regex_pattern_set.html) in the _Terraform Provider Documentation_