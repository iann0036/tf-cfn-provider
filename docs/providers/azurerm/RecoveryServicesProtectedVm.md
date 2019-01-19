# Terraform::AzureRM::RecoveryServicesProtectedVm

Manages an Recovery Protected VM.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

`RecoveryVaultName` - (Required) Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

`SourceVmId` - (Required) Specifies the ID of the VM to backup. Changing this forces a new resource to be created.

`BackupPolicyId` - (Required) Specifies the id of the backup policy to use. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Recovery Services Vault.

## See Also

* [azurerm_recovery_services_protected_vm](https://www.terraform.io/docs/providers/azurerm/r/recovery_services_protected_vm.html) in the _Terraform Provider Documentation_