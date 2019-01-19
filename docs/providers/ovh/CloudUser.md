# Terraform::OVH::CloudUser

Creates a user in a public cloud project.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ProjectId` - See Argument Reference above.

`Description` - See Argument Reference above.

`Username` - the username generated for the user. This username can be used with.

`Password` - (Sensitive) the password generated for the user. The password can.

`Status` - the status of the user. should be normally set to 'ok'.

`CreationDate` - the date the user was created.

`OpenstackRc` - a convenient map representing an openstack_rc file.

## See Also

* [ovh_cloud_user](https://www.terraform.io/docs/providers/ovh/r/cloud_user.html) in the _Terraform Provider Documentation_