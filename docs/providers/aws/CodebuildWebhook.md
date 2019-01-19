# Terraform::AWS::CodebuildWebhook

Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.

## Properties

`ProjectName` - (Required) The name of the build project.

`BranchFilter` - (Optional) A regular expression used to determine which branches get built. Default is all branches are built.


## Return Values

### Fn::GetAtt

`Id` - The name of the build project.

`PayloadUrl` - The CodeBuild endpoint where webhook events are sent.

`Secret` - The secret token of the associated repository. Not returned by the CodeBuild API for all source types.

`Url` - The URL to the webhook.

## See Also

* [aws_codebuild_webhook](https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html) in the _Terraform Provider Documentation_