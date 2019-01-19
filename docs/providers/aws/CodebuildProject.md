# Terraform::AWS::CodebuildProject

Provides a CodeBuild Project resource. See also the [`aws_codebuild_webhook` resource](/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The name (if imported via `name`) or ARN (if created via Terraform or imported via ARN) of the CodeBuild project.

`Arn` - The ARN of the CodeBuild project.

`BadgeUrl` - The URL of the build badge when `badge_enabled` is enabled.

## See Also

* [aws_codebuild_project](https://www.terraform.io/docs/providers/aws/r/codebuild_project.html) in the _Terraform Provider Documentation_