# Terraform::AzureRM::AutomationRunbook

Manages a Automation Runbook.

## Properties

`Name` - (Required) Specifies the name of the Runbook. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AccountName` - (Required) The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

`RunbookType` - (Required) The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

`LogProgress` - (Required) Progress log option.

`LogVerbose` - (Required) Verbose log option.

`PublishContentLink` - (Required) The published runbook content link.

`Description` - (Optional) A description for this credential.

`Content` - (Optional) The desired content of the runbook.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### PublishContentLink Properties

`Uri` - (Required) The uri of the runbook content.


## Return Values

### Fn::GetAtt

`Id` - The Automation Runbook ID.

## See Also

* [azurerm_automation_runbook](https://www.terraform.io/docs/providers/azurerm/r/automation_runbook.html) in the _Terraform Provider Documentation_