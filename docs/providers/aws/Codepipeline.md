# Terraform::AWS::Codepipeline

Provides a CodePipeline.

~> **NOTE on `Terraform::AWS::Codepipeline`:** - the `GITHUBTOKEN` environment variable must be set if the GitHub provider is specified.

## Properties

`Name` - (Required) The action declaration's name.

`RoleArn` - (Optional) The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.

`Location` - (Required) The location where AWS CodePipeline stores artifacts for a pipeline, such as an S3 bucket.

`Type` - (Required) The type of key; currently only `KMS` is supported.

`EncryptionKey` - (Optional) The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don't specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An `EncryptionKey` block is documented below.

`Id` - (Required) The KMS key ARN or ID.

`Action` - (Required) The action(s) to include in the stage. Defined as an `Action` block below.

`Category` - (Required) A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.

`Owner` - (Required) The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.

`Provider` - (Required) The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.

`Version` - (Required) A string that identifies the action type.

`Configuration` - (Optional) A Map of the action declaration's configuration. Find out more about configuring action configurations in the [Reference Pipeline Structure documentation](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements).

`InputArtifacts` - (Optional) A list of artifact names to be worked on.

`OutputArtifacts` - (Optional) A list of artifact names to output. Output artifact names must be unique within a pipeline.

`RunOrder` - (Optional) The order in which actions are run.


## Return Values

### Fn::GetAtt

`Id` - The codepipeline ID.

`Arn` - The codepipeline ARN.

## See Also

* [aws_codepipeline](https://www.terraform.io/docs/providers/aws/r/codepipeline.html) in the _Terraform Provider Documentation_