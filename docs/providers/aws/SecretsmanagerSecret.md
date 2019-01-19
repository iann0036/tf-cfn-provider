# Terraform::AWS::SecretsmanagerSecret

Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`Terraform::AWS::SecretsmanagerSecretVersion` resource](/docs/providers/aws/r/secretsmanager_secret_version.html).

## Properties

`Name` - (Optional) Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `NamePrefix`.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - (Optional) A description of the secret.

`KmsKeyId` - (Optional) Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.

`Policy` - (Optional) A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`RecoveryWindowInDays` - (Optional) Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.

`RotationLambdaArn` - (Optional) Specifies the ARN of the Lambda function that can rotate the secret.

`RotationRules` - (Optional) A structure that defines the rotation configuration for this secret. Defined below.

`Tags` - (Optional) Specifies a key-value map of user-defined tags that are attached to the secret.


## See Also

* [aws_secretsmanager_secret](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret.html) in the _Terraform Provider Documentation_