# Terraform::AWS::AthenaNamedQuery

Provides an Athena Named Query resource.

## Properties

`Name` - (Required) The plain language name for the query. Maximum length of 128.

`Database` - (Required) The database to which the query belongs.

`Query` - (Required) The text of the query itself. In other words, all query statements. Maximum length of 262144.

`Description` - (Optional) A brief explanation of the query. Maximum length of 1024.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the query.

## See Also

* [aws_athena_named_query](https://www.terraform.io/docs/providers/aws/r/athena_named_query.html) in the _Terraform Provider Documentation_