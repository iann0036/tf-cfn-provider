# Terraform::Alicloud::OssBucket

Provides a resource to create a oss bucket and set its attribution.

~> **NOTE:** The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The name of the bucket.

`Acl` - The acl of the bucket.

`CreationDate` - The creation date of the bucket.

`ExtranetEndpoint` - The extranet access endpoint of the bucket.

`IntranetEndpoint` - The intranet access endpoint of the bucket.

`Location` - The location of the bucket.

`Owner` - The bucket owner.

`StorageClass` - The bucket storage type.

## See Also

* [alicloud_oss_bucket](https://www.terraform.io/docs/providers/alicloud/r/oss_bucket.html) in the _Terraform Provider Documentation_