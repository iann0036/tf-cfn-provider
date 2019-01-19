# Terraform::AWS::SecretsmanagerSecretVersion

Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the [`Terraform::AWS::SecretsmanagerSecret` resource](/docs/providers/aws/r/secretsmanager_secret.html).

~> **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from Terraform unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from Terraform to fully trigger version deprecation if necessary.

## Properties

`SecretId` - (Required) Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

`SecretString` - (Optional) Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.

`SecretBinary` - (Optional) Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.

`VersionStages` - (Optional) Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.


## See Also

* [aws_secretsmanager_secret_version](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html) in the _Terraform Provider Documentation_