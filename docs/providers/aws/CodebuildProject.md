# Terraform::AWS::CodebuildProject

Provides a CodeBuild Project resource. See also the [`Terraform::AWS::CodebuildWebhook` resource](/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).

## Properties

`Artifacts` - (Required) Information about the project's build output artifacts. Artifact blocks are documented below.

`Environment` - (Required) Information about the project's build environment. Environment blocks are documented below.

`Name` - (Required) The projects name.

`Source` - (Required) Information about the project's input source code. Source blocks are documented below.

`BadgeEnabled` - (Optional) Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

`BuildTimeout` - (Optional) How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

`Cache` - (Optional) Information about the cache storage for the project. Cache blocks are documented below.

`Description` - (Optional) A short description of the project.

`EncryptionKey` - (Optional) The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

`ServiceRole` - (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`VpcConfig` - (Optional) Configuration for the builds to run inside a VPC. VPC config blocks are documented below.

`SecondaryArtifacts` - (Optional) A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.

`SecondarySources` - (Optional) A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.

### Artifacts Properties

`Type` - (Required) The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.

`EncryptionDisabled` - (Optional) If set to true, output artifacts will not be encrypted. If `Type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.

`Location` - (Optional) Information about the build output artifact location. If `Type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `Type` is set to `S3`, this is the name of the output bucket. If `Path` is not also specified, then `Location` can also specify the path of the output artifact in the output bucket.

`Name` - (Optional) The name of the project. If `Type` is set to `S3`, this is the name of the output artifact object.

`NamespaceType` - (Optional) The namespace to use in storing build artifacts. If `Type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.

`Packaging` - (Optional) The type of build output artifact to create. If `Type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`.

`Path` - (Optional) If `Type` is set to `S3`, this is the path to the output artifact.

### Cache Properties

`Type` - (Optional) The type of storage that will be used for the AWS CodeBuild project cache. Valid values: `NO_CACHE` and `S3`. Defaults to `NO_CACHE`.

`Location` - (Required when cache type is `S3`) The location where the AWS CodeBuild project stores cached resources. For type `S3` the value must be a valid S3 bucket name/prefix.

### Environment Properties

`ComputeType` - (Required) Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM` or `BUILD_GENERAL1_LARGE`. `BUILD_GENERAL1_SMALL` is only valid if `Type` is set to `LINUX_CONTAINER`.

`Image` - (Required) The *image identifier* of the Docker image to use for this build project ([list of Docker images provided by AWS CodeBuild.](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html)). You can read more about the AWS curated environment images in the [documentation](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCuratedEnvironmentImages.html).

`Type` - (Required) The type of build environment to use for related builds. Available values are: `LINUX_CONTAINER` or `WINDOWS_CONTAINER`.

`EnvironmentVariable` - (Optional) A set of environment variables to make available to builds for this build project.

`PrivilegedMode` - (Optional) If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.

`Certificate` - (Optional) The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.

### EnvironmentVariable Properties

`Name` - (Required) The environment variable's name or key.

`Value` - (Required) The environment variable's value.

`Type` - (Optional) The type of environment variable. Valid values: `PARAMETER_STORE`, `PLAINTEXT`.

### Source Properties

`Type` - (Required) The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET`, `S3` or `NO_SOURCE`.

`Auth` - (Optional) Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.

`Buildspec` - (Optional) The build spec declaration to use for this build project's related builds. This must be set when `Type` is `NO_SOURCE`.

`GitCloneDepth` - (Optional) Truncate git history to this many commits.

`InsecureSsl` - (Optional) Ignore SSL warnings when connecting to source control.

`Location` - (Optional) The location of the source code from git or s3.

`ReportBuildStatus` - (Optional) Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when the `Type` is `BITBUCKET` or `GITHUB`.

### Auth Properties

`Type` - (Required) The authorization type to use. The only valid value is `OAUTH`.

`Resource` - (Optional) The resource value that applies to the specified authorization type.

### VpcConfig Properties

`SecurityGroupIds` - (Required) The security group IDs to assign to running builds.

`Subnets` - (Required) The subnet IDs within which to run builds.

`VpcId` - (Required) The ID of the VPC within which to run builds.

### SecondaryArtifacts Properties

`Type` - (Required) The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.

`ArtifactIdentifier` - (Required) The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.

`EncryptionDisabled` - (Optional) If set to true, output artifacts will not be encrypted. If `Type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.

`Location` - (Optional) Information about the build output artifact location. If `Type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `Type` is set to `S3`, this is the name of the output bucket. If `Path` is not also specified, then `Location` can also specify the path of the output artifact in the output bucket.

`Name` - (Optional) The name of the project. If `Type` is set to `S3`, this is the name of the output artifact object.

`NamespaceType` - (Optional) The namespace to use in storing build artifacts. If `Type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.

`Packaging` - (Optional) The type of build output artifact to create. If `Type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`.

`Path` - (Optional) If `Type` is set to `S3`, this is the path to the output artifact.

### SecondarySources Properties

`Type` - (Required) The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.

`SourceIdentifier` - (Required) The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory.

`Auth` - (Optional) Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.

`Buildspec` - (Optional) The build spec declaration to use for this build project's related builds.

`GitCloneDepth` - (Optional) Truncate git history to this many commits.

`InsecureSsl` - (Optional) Ignore SSL warnings when connecting to source control.

`Location` - (Optional) The location of the source code from git or s3.

`ReportBuildStatus` - (Optional) Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.


## Return Values

### Fn::GetAtt

`Id` - The name (if imported via `Name`) or ARN (if created via Terraform or imported via ARN) of the CodeBuild project.

`Arn` - The ARN of the CodeBuild project.

`BadgeUrl` - The URL of the build badge when `BadgeEnabled` is enabled.

## See Also

* [aws_codebuild_project](https://www.terraform.io/docs/providers/aws/r/codebuild_project.html) in the _Terraform Provider Documentation_