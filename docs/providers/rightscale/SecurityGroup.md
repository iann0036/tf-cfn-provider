# Terraform::RightScale::SecurityGroup

Use this resource to create, update or destroy RightScale [security groups](http://reference.rightscale.com/api1.5/resources/ResourceSecurityGroups.html).

## Properties

`CloudHref` - (Required) Href of the cloud you want to create the security group in.

`NetworkHref` - (Required) Href of the network to create the security group in.

`Name` - (Required) Security group name.

`Description` - (Optional) Security group description.

`DeploymentHref` - (Optional) Href of the deployment that owns the security group.  If you wish to use a deployment object as top level ownership construct, perhaps allocating the new security group to a single deployment, then provide this href.


## Return Values

### Fn::GetAtt

`Href` - Href of the security group.

`ResourceUid` - Cloud resource_uid.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_security_group](https://www.terraform.io/docs/providers/rightscale/r/security_group.html) in the _Terraform Provider Documentation_