# Terraform::RightScale::SshKey

Use this resource to create, update or destroy RightScale [SSH keys](http://reference.rightscale.com/api1.5/resources/ResourceSshKeys.html).

## Properties

`CloudHref` - (Required) The href of the cloud with the ssh key you want.

`Name` - (Required) SSH Key name.


## Return Values

### Fn::GetAtt

`ResourceUid` - Cloud resource_uid.

`Links` - Hrefs of related API resources.

## See Also

* [rightscale_ssh_key](https://www.terraform.io/docs/providers/rightscale/r/ssh_key.html) in the _Terraform Provider Documentation_