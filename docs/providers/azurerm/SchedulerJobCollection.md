# Terraform::AzureRM::SchedulerJobCollection

Manages a Scheduler Job Collection.

~> **NOTE:** Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.

## Properties

`Name` - (Required) Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Sku` - (Required) Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

`State` - (Optional) Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

`Quota` - (Optional) Configures the Job collection quotas as documented in the `Quota` block below.

### Quota Properties

`MaxJobCount` - (Optional) Sets the maximum number of jobs in the collection.

`MaxRecurrenceFrequency` - (Required) The maximum frequency of recurrence. Possible values include: `Minute`, `Hour`, `Day`, `Week`, `Month`.

`MaxRecurrenceInterval` - (Optional) The maximum interval between recurrence.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Scheduler Job Collection.

## See Also

* [azurerm_scheduler_job_collection](https://www.terraform.io/docs/providers/azurerm/r/scheduler_job_collection.html) in the _Terraform Provider Documentation_