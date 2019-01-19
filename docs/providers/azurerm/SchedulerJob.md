# Terraform::AzureRM::SchedulerJob

Manages a Scheduler Job.

~> **NOTE:** Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.

## Properties

`Name` - (Required) The name of the Scheduler Job. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

`JobCollectionName` - (Required) Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

`ActionWeb` - (Optional) A `ActionWeb` block defining the job action as described below. Note this is identical to an `ErrorActionWeb` block.

`ActionStorageQueue` - (Optional) A `ActionStorageQueue` block defining a storage queue job action as described below. Note this is identical to an `ErrorActionStorageQueue` block.

`ErrorActionWeb` - (Optional) A `ErrorActionWeb` block defining the action to take on an error as described below. Note this is identical to an `ActionWeb` block.

`ErrorActionStorageQueue` - (Optional) A `ErrorActionStorageQueue` block defining the a web action to take on an error as described below. Note this is identical to an `ActionStorageQueue` block.

`Retry` - (Optional) A `Retry` block defining how to retry as described below.

`Recurrence` - (Optional) A `Recurrence` block defining a job occurrence schedule.

`StartTime` - (Optional) The time the first instance of the job is to start running at.

`State` - (Optional) The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`.

`Url` - (Required) Specifies the URL of the web request. Must be HTTPS for authenticated requests.

`Method` - (Optional) Specifies the method of the request. Defaults to `Get` and must be one of `Get`, `Put`, `Post`, `Delete`.

`Body` - (Optional) Specifies the request body.

`Headers` - (Optional) A map specifying the headers sent with the request.

`AuthenticationBasic` - (Optional) An `AuthenticationActiveDirectory` block which defines the Active Directory oauth configuration to use.

`AuthenticationCertificate` - (Optional) An `AuthenticationCertificate` block which defines the client certificate information to be use.

`AuthenticationActiveDirectory` - (Optional) An `AuthenticationActiveDirectory` block which defines the OAUTH Active Directory information to use.

### AuthenticationBasic Properties

`Username` - (Required) Specifies the username to use.

`Password` - (Required) Specifies the password to use.

### AuthenticationCertificate Properties

`Pfx` - (Required) Specifies the pfx certificate in base-64 format.

`Password` - (Required) Specifies the certificate password.

### AuthenticationActiveDirectory Properties

`ClientId` - (Required) Specifies the client ID to use.

`TenantId` - (Required) Specifies the tenant ID to use.

`ClientSecret` - (Required) Specifies the secret to use.

`Audience` - (Optional) Specifies the audience.

### ErrorActionStorageQueue Properties

`StorageAccountName` - (Required) Specifies the the storage account name.

`StorageQueueName` - (Required) Specifies the the storage account queue.

`SasToken` - (Required) Specifies a SAS token/key to authenticate with.

`Message` - (Required) The message to send into the queue.

### Retry Properties

`Interval` - (Required) Specifies the duration between retries.

`Count` - (Required) Specifies the number of times a retry should be attempted.

### Recurrence Properties

`Frequency` - (Required) Specifies the frequency of recurrence. Must be one of `Minute`, `Hour`, `Day`, `Week`, `Month`.

`Interval` - (Optional) Specifies the interval between executions. Defaults to `1`.

`Count` - (Optional) Specifies the maximum number of times that the job should run.

`EndTime` - (Optional) Specifies the time at which the job will cease running. Must be less then 500 days into the future.

`Minutes` - (Optional) Specifies the minutes of the hour that the job should execute at. Must be between `0` and `59`.

`Hours` - (Optional) Specifies the hours of the day that the job should execute at. Must be between `0` and `23`.

`WeekDays` - (Optional) Specifies the days of the week that the job should execute on. Must be one of `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`. Only applies when `Week` is used for frequency.

`MonthDays` - (Optional) Specifies the days of the month that the job should execute on. Must be non zero and between `-1` and `31`. Only applies when `Month` is used for frequency.

`MonthlyOccurrences` - (Optional) Specifies specific monthly occurrences like "last sunday of the month" with `MonthlyOccurrences` blocks. Only applies when `Month` is used for frequency.

### MonthlyOccurrences Properties

`Day` - (Optional) Specifies the day of the week that the job should execute on. Must be one of  one of `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`.

`Occurrence` - (Optional) Specifies the week the job should run on. For example  `1` for the first week, `-1` for the last week of the month. Must be between `-5` and `5`.


## Return Values

### Fn::GetAtt

`Id` - The Scheduler Job ID.

`Thumbprint` - (Computed) The certificate thumbprint.

`Expiration` - (Computed)  The certificate expiration date.

`SubjectName` - (Computed) The certificate's certificate subject name.

## See Also

* [azurerm_scheduler_job](https://www.terraform.io/docs/providers/azurerm/r/scheduler_job.html) in the _Terraform Provider Documentation_