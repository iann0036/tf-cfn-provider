# Terraform::OCI::ObjectstorageBucket

This resource provides the Bucket resource in Oracle Cloud Infrastructure Object Storage service.

Creates a bucket in the given namespace with a bucket name and optional user-defined metadata.

## Properties

`AccessType` - (Optional) (Updatable) The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

`CompartmentId` - (Required) (Updatable) The ID of the compartment in which to create the bucket.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`KmsKeyId` - (Optional) (Updatable) The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key.

`Metadata` - (Optional) (Updatable) Arbitrary string, up to 4KB, of keys and values for user-defined metadata.

`Name` - (Required) The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, and dashes. Bucket names must be unique within the namespace. Avoid entering confidential information. example: Example: my-new-bucket1.

`Namespace` - (Required) The top-level namespace used for the request.

`StorageTier` - (Optional) The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier' property is immutable after bucket is created.


## Return Values

### Fn::GetAtt

`AccessType` - The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

`ApproximateCount` - The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a lag between what is displayed and the actual object count.

`ApproximateSize` - The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will see a lag between what is displayed and the actual size of the bucket.

`CompartmentId` - The compartment ID in which the bucket is authorized.

`CreatedBy` - The OCID of the user who created the bucket.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Etag` - The entity tag for the bucket.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`KmsKeyId` - The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key.

`Metadata` - Arbitrary string keys and values for user-defined metadata.

`Name` - The name of the bucket. Avoid entering confidential information. Example: my-new-bucket1.

`Namespace` - The namespace in which the bucket lives.

`ObjectLifecyclePolicyEtag` - The entity tag for the live object lifecycle policy on the bucket.

`StorageTier` - The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the archive storage tier. The 'storageTier' property is immutable after bucket is created.

`TimeCreated` - The date and time the bucket was created, as described in [RFC 2616](https://tools.ietf.org/rfc/rfc2616), section 14.29.

## See Also

* [oci_objectstorage_bucket](https://www.terraform.io/docs/providers/oci/r/objectstorage_bucket.html) in the _Terraform Provider Documentation_