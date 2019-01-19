# Terraform::RightScale::Instance

Use this resource to create, update or destroy RightScale [instances](http://reference.rightscale.com/api1.5/resources/ResourceInstances.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Links` - Hrefs of related API resources.

`CreatedAt` - Datestamp of instance creation.

`UpdatedAt` - Datestamp of when instance was updated last.

`State` - The state of the instance (operational, terminating, pending, stranded, etc.).

`Href` - Href of the instance.

`ResourceUid` - Cloud resource_uid as reported by cm platform.

`PublicIpAddresses` - List of public IP addresses associated to the instance.

`PrivateIpAddresses` - List of private IP addresses associated to the instance.

## See Also

* [rightscale_instance](https://www.terraform.io/docs/providers/rightscale/r/instance.html) in the _Terraform Provider Documentation_