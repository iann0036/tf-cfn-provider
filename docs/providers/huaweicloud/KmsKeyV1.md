# Terraform::HuaweiCloud::KmsKeyV1

Manages a V1 key resource within KMS.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`KeyAlias` - See Argument Reference above.

`KeyDescription` - See Argument Reference above.

`Realm` - See Argument Reference above.

`KeyId` - The globally unique identifier for the key.

`DefaultKeyFlag` - Identification of a Master Key. The value 1 indicates a Default.

`ScheduledDeletionDate` - Scheduled deletion time (time stamp) of a key.

`DomainId` - ID of a user domain for the key.

`ExpirationTime` - Expiration time.

`CreationDate` - Creation time (time stamp) of a key.

`IsEnabled` - See Argument Reference above.

## See Also

* [huaweicloud_kms_key_v1](https://www.terraform.io/docs/providers/huaweicloud/r/kms_key_v1.html) in the _Terraform Provider Documentation_