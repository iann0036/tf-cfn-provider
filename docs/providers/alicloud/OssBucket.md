# Terraform::Alicloud::OssBucket

Provides a resource to create a oss bucket and set its attribution.

~> **NOTE:** The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.

## Properties

`Bucket` - (Optional, Forces New Resorce) The name of the bucket. If omitted, Terraform will assign a random and unique name.

`Acl` - (Optional) The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".

`CorsRule` - (Optional) A list rules of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of cors rule are no more than 10 for every OSS bucket.

`Website` - (Optional) A list website objects(documented below). The items of website are no more than 1 for every OSS bucket.

`Logging` - (Optional) A list settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below). The items of logging are no more than 1 for every OSS bucket.

`LoggingIsenable` - (Optional) The flag of using logging enable container. Defaults true.

`RefererConfig` - (Optional) A list configurations of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below). The items of referer_config are no more than 1 for every OSS bucket.

`LifecycleRule` - (Optional) A list configurations of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below). The items of rules are no more than 1000 for every OSS bucket.


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