# Terraform::RightScale::Deployment

Use this resource to create, update or destroy RightScale [deployments](http://reference.rightscale.com/api1.5/resources/ResourceDeployments.html).

## Properties

`Name` - (Required) Deployment name.

`Description` - (Optional) Deployment description.

`ResourceGroupHref` - (Optional) Href of the Windows Azure Resource Group attached to the deployment.

`Locked` - (Optional) Set to true to lock the deployment.

`ServerTagScope` - (Optional) Routing scope for tags for servers in the deployment.  Options are 'account' or 'deployment,' defaults to 'deployment.'.


## Return Values

### Fn::GetAtt

`Href` - Href of the deployment.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_deployment](https://www.terraform.io/docs/providers/rightscale/r/deployment.html) in the _Terraform Provider Documentation_