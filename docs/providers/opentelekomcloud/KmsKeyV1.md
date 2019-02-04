# Terraform::OpenTelekomCloud::KmsKeyV1

Manages a V1 key resource within KMS.

## Properties

`KeyAlias` - (Required) The alias in which to create the key. It is required when
we create a new key. Changing this updates the alias of key.

`KeyDescription` - (Optional) The description of the key as viewed in OpenTelekomCloud console.
Changing this updates the description of key.

`Realm` - (Optional) Region where a key resides. Changing this creates a new key.

`PendingDays` - (Optional) Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 1096 days. Defaults to 7.
It only be used when delete a key.

`IsEnabled` - (Optional) Specifies whether the key is enabled. Defaults to true.
Changing this updates the state of existing key.


## Return Values

### Fn::GetAtt

`KeyAlias` - See Properties above.

`KeyDescription` - See Properties above.

`Realm` - See Properties above.

`KeyId` - The globally unique identifier for the key.

`DefaultKeyFlag` - Identification of a Master Key. The value 1 indicates a Default.

`Origin` - Origin of a key. The default value is kms.

`ScheduledDeletionDate` - Scheduled deletion time (time stamp) of a key.

`DomainId` - ID of a user domain for the key.

`ExpirationTime` - Expiration time.

`CreationDate` - Creation time (time stamp) of a key.

`IsEnabled` - See Properties above.

## See Also

* [opentelekomcloud_kms_key_v1](https://www.terraform.io/docs/providers/opentelekomcloud/r/kms_key_v1.html) in the _Terraform Provider Documentation_