# Terraform::AWS::CloudwatchLogResourcePolicy

Provides a resource to manage a CloudWatch log resource policy.

## Properties

`PolicyDocument` - (Required) Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.

`PolicyName` - (Required) Name of the resource policy.


## Return Values

### Fn::GetAtt

`Id` - The name of the CloudWatch log resource policy.

## See Also

* [aws_cloudwatch_log_resource_policy](https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_resource_policy.html) in the _Terraform Provider Documentation_