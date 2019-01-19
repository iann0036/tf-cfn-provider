# Terraform::RightScale::Server

Use this resource to create, update or destroy RightScale [servers](http://reference.rightscale.com/api1.5/resources/ResourceServers.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Links` - Hrefs of related API resources.

`CreatedAt` - Datestamp of server creation.

`UpdatedAt` - Datestamp of when server was updated last.

`State` - The state of the server (operational, terminating, pending, stranded, etc.).

`Href` - Href of the server.

`ResourceUid` - Cloud resource_uid as reported by cm platform.

## See Also

* [rightscale_server](https://www.terraform.io/docs/providers/rightscale/r/server.html) in the _Terraform Provider Documentation_