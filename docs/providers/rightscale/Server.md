# Terraform::RightScale::Server

Use this resource to create, update or destroy RightScale [servers](http://reference.rightscale.com/api1.5/resources/ResourceServers.html).

## Properties

`Name` - (Required) The name of the server.

`DeploymentHref` - (Required) The href of the deployment the server will be placed in.

`Instance` - (Required) See [rightscale_instance](https://github.com/terraform-providers/terraform-provider-rightscale/blob/master/website/docs/r/cm_instance.markdown).

`CloudHref` - (Required) The Href of the cloud the server will be launched in.

`Description` - (Optional) A description of the server.

`Optimized` - (Optional) A flag indicating whether instances of this server should be optimized for high-performance volumes.

`Tags` - (Optional) Any tags you want attached to the server and any instances created from this server object.


## Return Values

### Fn::GetAtt

`Links` - Hrefs of related API resources.

`CreatedAt` - Datestamp of server creation.

`UpdatedAt` - Datestamp of when server was updated last.

`State` - The state of the server (operational, terminating, pending, stranded, etc.).

`Href` - Href of the server.

`ResourceUid` - Cloud resource_uid as reported by cm platform.

## See Also

* [rightscale_server](https://www.terraform.io/docs/providers/rightscale/r/server.html) in the _Terraform Provider Documentation_