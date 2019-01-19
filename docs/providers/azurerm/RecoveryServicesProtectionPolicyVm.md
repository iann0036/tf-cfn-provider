# Terraform::AzureRM::RecoveryServicesProtectionPolicyVm

Manages an Recovery Services VM Protection Policy.

## Properties

`Name` - (Required) Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

`RecoveryVaultName` - (Required) Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

`Backup` - (Required) Configures the Policy backup frequecent, times & days as documented in the `Backup` block below.

`Timezone` - (Optional) Specifies the timezone. Defaults to `UTC`.

`RetentionDaily` - (Optional) Configures the policy daily retention as documented in the `RetentionDaily` block below. Required when backup frequency is `Daily`.

`RetentionWeekly` - (Optional) Configures the policy weekly retention as documented in the `RetentionWeekly` block below. Required when backup frequency is `Weekly`.

`RetentionMonthly` - (Optional) Configures the policy monthly retention as documented in the `RetentionMonthly` block below.

`RetentionYearly` - (Optional) Configures the policy yearly retention as documented in the `RetentionYearly` block below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Backup Properties

`Frequency` - (Required) Sets the backup frequency. Must be either `Daily` or`Weekly`.

`Times` - (Required) The time of day to preform the backup in 24hour format.

`Weekdays` - (Optional) The days of the week to perform backups on. Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

### RetentionDaily Properties

`Count` - (Required) The number of daily backups to keep. Must be between `1` and `9999`.

### RetentionWeekly Properties

`Count` - (Required) The number of weekly backups to keep. Must be between `1` and `9999`.

`Weekdays` - (Required) The weekday backups to retain. Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

### RetentionMonthly Properties

`Count` - (Required) The number of monthly backups to keep. Must be between `1` and `9999`.

`Weekdays` - (Required) The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

`Weeks` - (Required) The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.

### RetentionYearly Properties

`Count` - (Required) The number of yearly backups to keep. Must be between `1` and `9999`.

`Weekdays` - (Required) The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

`Weeks` - (Required) The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.

`Months` - (Required) The months of the year to retain backups of. Must be one of `January`, `Febuary`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Recovery Services VM Protection Policy.

## See Also

* [azurerm_recovery_services_protection_policy_vm](https://www.terraform.io/docs/providers/azurerm/r/recovery_services_protection_policy_vm.html) in the _Terraform Provider Documentation_