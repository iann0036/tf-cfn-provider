# Terraform::Alicloud::OssBucket

Provides a resource to create a oss bucket and set its attribution.

~> **NOTE:** The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.

## Properties

`Bucket` - (Optional, Forces New Resorce) The name of the bucket. If omitted, Terraform will assign a random and unique name.

`Acl` - (Optional) The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".

`CoreRule` - (Optional) A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.

`Website` - (Optional) A website object(documented below).

`Logging` - (Optional) A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).

`LoggingIsenable` - (Optional) The flag of using logging enable container. Defaults true.

`RefererConfig` - (Optional) The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).

`LifecycleRule` - (Optional) A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).


## Return Values

### Fn::GetAtt

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