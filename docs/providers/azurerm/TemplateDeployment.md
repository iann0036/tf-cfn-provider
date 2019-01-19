# Terraform::AzureRM::TemplateDeployment

Manage a template deployment of resources

~> **Note on ARM Template Deployments:** Due to the way the underlying Azure API is designed, Terraform can only manage the deployment of the ARM Template - and not any resources which are created by it.
This means that when deleting the `Terraform::AzureRM::TemplateDeployment` resource, Terraform will only remove the reference to the deployment, whilst leaving any resources created by that ARM Template Deployment.
One workaround for this is to use a unique Resource Group for each ARM Template Deployment, which means deleting the Resource Group would contain any resources created within it - however this isn't ideal. [More information](https://docs.microsoft.com/en-us/rest/api/resources/deployments#Deployments_Delete).

## Properties

`Name` - (Required) Specifies the name of the template deployment. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the template deployment.

`DeploymentMode` - (Required) Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`. Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not specified within the template, and Terraform will not be aware of this.

`TemplateBody` - (Optional) Specifies the JSON definition for the template.

`Parameters` - (Optional) Specifies the name and value pairs that define the deployment parameters for the template.

`ParametersBody` - (Optional) Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references.


## Return Values

### Fn::GetAtt

`Id` - The Template Deployment ID.

`Outputs` - A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using `.outputs["name"]`.

## See Also

* [azurerm_template_deployment](https://www.terraform.io/docs/providers/azurerm/r/template_deployment.html) in the _Terraform Provider Documentation_