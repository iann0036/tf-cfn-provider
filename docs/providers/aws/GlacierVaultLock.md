# Terraform::AWS::GlacierVaultLock

Manages a Glacier Vault Lock. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) for a full explanation of the Glacier Vault Lock functionality.

~> **NOTE:** This resource allows you to test Glacier Vault Lock policies by setting the `CompleteLock` argument to `false`. When testing policies in this manner, the Glacier Vault Lock automatically expires after 24 hours and Terraform will show this resource as needing recreation after that time. To permanently apply the policy, set the `CompleteLock` argument to `true`. When changing `CompleteLock` to `true`, it is expected the resource will show as recreating.

!> **WARNING:** Once a Glacier Vault Lock is completed, it is immutable. The deletion of the Glacier Vault Lock is not be possible and attempting to remove it from Terraform will return an error. Set the `IgnoreDeletionError` argument to `true` and apply this configuration before attempting to delete this resource via Terraform or use `terraform state rm` to remove this resource from Terraform management.

## Properties

`CompleteLock` - (Required) Boolean whether to permanently apply this Glacier Lock Policy. Once completed, this cannot be undone. If set to `false`, the Glacier Lock Policy remains in a testing mode for 24 hours. After that time, the Glacier Lock Policy is automatically removed by Glacier and the Terraform resource will show as needing recreation. Changing this from `false` to `true` will show as resource recreation, which is expected. Changing this from `true` to `false` is not possible unless the Glacier Vault is recreated at the same time.

`Policy` - (Required) JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.

`VaultName` - (Required) The name of the Glacier Vault.

`IgnoreDeletionError` - (Optional) Allow Terraform to ignore the error returned when attempting to delete the Glacier Lock Policy. This can be used to delete or recreate the Glacier Vault via Terraform, for example, if the Glacier Vault Lock policy permits that action. This should only be used in conjunction with `CompleteLock` being set to `true`.


## Return Values

### Fn::GetAtt

`Id` - Glacier Vault name.

## See Also

* [aws_glacier_vault_lock](https://www.terraform.io/docs/providers/aws/r/glacier_vault_lock.html) in the _Terraform Provider Documentation_