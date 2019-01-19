# Terraform::AWS::WafByteMatchSet

Provides a WAF Byte Match Set Resource

## Properties

`Name` - (Required) The name or description of the Byte Match Set.

`ByteMatchTuples` - Specifies the bytes (typically a string that corresponds with ASCII characters) that you want to search for in web requests, the location in requests that you want to search, and other settings.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF Byte Match Set.

## See Also

* [aws_waf_byte_match_set](https://www.terraform.io/docs/providers/aws/r/waf_byte_match_set.html) in the _Terraform Provider Documentation_