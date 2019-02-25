# Terraform::OCI::ObjectstoragePreauthrequest

This resource provides the Preauthenticated Request resource in Oracle Cloud Infrastructure Object Storage service.

Creates a pre-authenticated request specific to the bucket.

## Properties

`AccessType` - (Required) The operation that can be performed on this resource.

`Bucket` - (Required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`.

`Name` - (Required) A user-specified name for the pre-authenticated request. Helpful for management purposes.

`Namespace` - (Required) The top-level namespace used for the request.

`Object` - (Optional) The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is, the pre-authenticated request grants access to the entire bucket.

`TimeExpires` - (Required) The expiration date for the pre-authenticated request as per [RFC 3339](https://tools.ietf.org/rfc/rfc3339). After this date the pre-authenticated request will no longer be valid.


## Return Values

### Fn::GetAtt

`Name` - The user-provided name of the pre-authenticated request.

`Bucket` - The name of the bucket.  Example: `my-new-bucket1`.

`Object` - The name of the object that is being granted access to by the pre-authenticated request. This can be null and if so, the pre-authenticated request grants access to the entire bucket. Avoid entering confidential information. Example: test/object1.log.

`Namespace` - The top-level namespace used for the request.

`AccessType` - The operation that can be performed on this resource.

`TimeCreated` - The date when the pre-authenticated request was created as per specification [RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`TimeExpires` - The expiration date for the pre-authenticated request as per [RFC 3339](https://tools.ietf.org/rfc/rfc3339). After this date the pre-authenticated request will no longer be valid.

`Id` - The unique identifier to use when directly addressing the pre-authenticated request.

`AccessUri` - The URI to embed in the URL when using the pre-authenticated request.

## See Also

* [oci_objectstorage_preauthrequest](https://www.terraform.io/docs/providers/oci/r/objectstorage_preauthrequest.html) in the _Terraform Provider Documentation_