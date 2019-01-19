# Terraform::AzureRM::MonitorActivityLogAlert

Manages an Activity Log Alert within Azure Monitor.

## Properties

`Name` - (Required) The name of the activity log alert. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the activity log alert instance.

`Scopes` - (Required) The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).

`Criteria` - (Required) A `Criteria` block as defined below.

`Action` - (Optional) One or more `Action` blocks as defined below.

`Enabled` - (Optional) Should this Activity Log Alert be enabled? Defaults to `true`.

`Description` - (Optional) The description of this activity log alert.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Action Properties

`ActionGroupId` - (Required) The ID of the Action Group can be sourced from [the `Terraform::AzureRM::MonitorActionGroup` resource](./monitor_action_group.html).

`WebhookProperties` - (Optional) The map of custom string properties to include with the post operation. These data are appended to the webhook payload.

### Criteria Properties

`Category` - (Required) The category of the operation. Possible values are `Administrative`, `Autoscale`, `Policy`, `Recommendation`, `Security` and `Service Health`.

`OperationName` - (Optional) The Resource Manager Role-Based Access Control operation name. Supported operation should be of the form: `<resourceProvider>/<resourceType>/<operation>`.

`ResourceProvider` - (Optional) The name of the resource provider monitored by the activity log alert.

`ResourceType` - (Optional) The resource type monitored by the activity log alert.

`ResourceGroup` - (Optional) The name of resource group monitored by the activity log alert.

`ResourceId` - (Optional) The specific resource monitored by the activity log alert. It should be within one of the `Scopes`.

`Caller` - (Optional) The email address or Azure Active Directory identifier of the user who performed the operation.

`Level` - (Optional) The severity level of the event. Possible values are `Verbose`, `Informational`, `Warning`, `Error`, and `Critical`.

`Status` - (Optional) The status of the event. For example, `Started`, `Failed`, or `Succeeded`.

`SubStatus` - (Optional) The sub status of the event.


## Return Values

### Fn::GetAtt

`Id` - The ID of the activity log alert.

## See Also

* [azurerm_monitor_activity_log_alert](https://www.terraform.io/docs/providers/azurerm/r/monitor_activity_log_alert.html) in the _Terraform Provider Documentation_