# Terraform::AWS::WafregionalByteMatchSet

Provides a WAF Regional Byte Match Set Resource for use with Application Load Balancer.

## Properties

`Name` - (Required) The name or description of the ByteMatchSet.

`ByteMatchTuple` - **Deprecated**, use `ByteMatchTuples` instead.

`ByteMatchTuples` - (Optional)Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.

`FieldToMatch` - (Required) Settings for the ByteMatchTuple. FieldToMatch documented below.

`PositionalConstraint` - (Required) Within the portion of a web request that you want to search.

`TargetString` - (Required) The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.

`TextTransformation` - (Required) The formatting way for web request.

`Data` - (Optional) When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.

`Type` - (Required) The part of the web request that you want AWS WAF to search for a specified string.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF ByteMatchSet.

## See Also

* [aws_wafregional_byte_match_set](https://www.terraform.io/docs/providers/aws/r/wafregional_byte_match_set.html) in the _Terraform Provider Documentation_