# Terraform::RightScale::Credential

Use this resource to create, update or destroy RightScale [credentials](http://reference.rightscale.com/api1.5/resources/ResourceCredentials.html).

## Properties

`Name` - (Required) Name of the credential.

`Value` - (Required) Value of the credential.

`Description` - (Optional) Description of the credential.


## Return Values

### Fn::GetAtt

`Name` - Name of the credential.

`Description` - Description of the credential.

`Value` - Value of the credential.

`Links` - Hrefs of related API resources.

`CreatedAt` - Datestamp of credential creation.

`UpdatedAt` - Datestamp of when credential was updated last.

## See Also

* [rightscale_credential](https://www.terraform.io/docs/providers/rightscale/r/credential.html) in the _Terraform Provider Documentation_