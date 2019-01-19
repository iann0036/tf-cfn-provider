# Terraform::AWS::Codepipeline

Provides a CodePipeline.

~> **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The codepipeline ID.

`Arn` - The codepipeline ARN.

## See Also

* [aws_codepipeline](https://www.terraform.io/docs/providers/aws/r/codepipeline.html) in the _Terraform Provider Documentation_