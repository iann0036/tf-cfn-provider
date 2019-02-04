# Terraform::AWS::GlacierVault

Provides a Glacier Vault Resource. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html) for a full explanation of the Glacier Vault functionality

~> **NOTE:** When removing a Glacier Vault, the Vault must be empty.

## Properties

`Name` - (Required) The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

`AccessPolicy` - (Optional) The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy.

`Notification` - (Optional) The notifications for the Vault. Fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Events` - (Required) You can configure a vault to publish a notification for `ArchiveRetrievalCompleted` and `InventoryRetrievalCompleted` events.

`SnsTopic` - (Required) The SNS Topic ARN.


## Return Values

### Fn::GetAtt

`Location` - The URI of the vault that was created.

`Arn` - The ARN of the vault.

## See Also

* [aws_glacier_vault](https://www.terraform.io/docs/providers/aws/r/glacier_vault.html) in the _Terraform Provider Documentation_