# Terraform::AzureRM::AppServicePlan

Manage an App Service Plan component.

## Properties

`Name` - (Required) Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the App Service Plan component.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Kind` - (Optional) The kind of the App Service Plan to create. Possible values are `Windows` (also available as `App`), `Linux` and `FunctionApp` (for a Consumption Plan). Defaults to `Windows`. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as documented below.

`AppServiceEnvironmentId` - (Optional) The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.

`Reserved` - (Optional) Is this App Service Plan `Reserved`. Defaults to `false`.

`PerSiteScaling` - (Optional) Can Apps assigned to this App Service Plan be scaled independently? If set to `false` apps assigned to this plan will scale to all instances of the plan.  Defaults to `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Tier` - (Required) Specifies the plan's pricing tier.

`Size` - (Required) Specifies the plan's instance size.

`Capacity` - (Optional) Specifies the number of workers associated with this App Service Plan.


## Return Values

### Fn::GetAtt

`Id` - The ID of the App Service Plan component.

`MaximumNumberOfWorkers` - The maximum number of workers supported with the App Service Plan's sku.

## See Also

* [azurerm_app_service_plan](https://www.terraform.io/docs/providers/azurerm/r/app_service_plan.html) in the _Terraform Provider Documentation_