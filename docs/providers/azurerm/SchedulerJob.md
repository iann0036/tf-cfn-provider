# Terraform::AzureRM::SchedulerJob

Manages a Scheduler Job.

~> **NOTE:** Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Scheduler Job ID.

`Thumbprint` - (Computed) The certificate thumbprint.

`Expiration` - (Computed)  The certificate expiration date.

`SubjectName` - (Computed) The certificate's certificate subject name.

## See Also

* [azurerm_scheduler_job](https://www.terraform.io/docs/providers/azurerm/r/scheduler_job.html) in the _Terraform Provider Documentation_