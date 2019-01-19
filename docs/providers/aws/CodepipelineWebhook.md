# Terraform::AWS::CodepipelineWebhook

Provides a CodePipeline Webhook.

## Properties

`Name` - (Required) The name of the webhook.

`Authentication` - (Required) The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.

`AuthenticationConfiguration` - (Optional) An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.

`TargetAction` - (Required) The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

`TargetPipeline` - (Required) The name of the pipeline.

### Filter Properties

`JsonPath` - (Required) The [JSON path](https://github.com/json-path/JsonPath) to filter on.

`MatchEquals` - (Required) The value to match on (e.g. `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.

### AuthenticationConfiguration Properties

`SecretToken` - (Optional) The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.

`AllowedIpRange` - (Optional) A valid CIDR block for `IP` filtering. Required for `IP`.


## Return Values

### Fn::GetAtt

`Id` - The CodePipeline webhook's ARN.

`Url` - The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.

## See Also

* [aws_codepipeline_webhook](https://www.terraform.io/docs/providers/aws/r/codepipeline_webhook.html) in the _Terraform Provider Documentation_