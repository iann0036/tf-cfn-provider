# Terraform::OCI::ObjectstoragePreauthrequest

This resource provides the Preauthenticated Request resource in Oracle Cloud Infrastructure Object Storage service.

Creates a pre-authenticated request specific to the bucket.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AccessType` - The operation that can be performed on this resource.

`AccessUri` - The URI to embed in the URL when using the pre-authenticated request.

`Bucket` - The name of the bucket.  Example: `my-new-bucket1`.

`Id` - The unique identifier to use when directly addressing the pre-authenticated request.

`Name` - The user-provided name of the pre-authenticated request.

`Namespace` - The top-level namespace used for the request.

`Object` - The name of the object that is being granted access to by the pre-authenticated request. This can be null and if so, the pre-authenticated request grants access to the entire bucket. Avoid entering confidential information. Example: test/object1.log.

`TimeCreated` - The date when the pre-authenticated request was created as per specification [RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`TimeExpires` - The expiration date for the pre-authenticated request as per [RFC 3339](https://tools.ietf.org/rfc/rfc3339). After this date the pre-authenticated request will no longer be valid.

## See Also

* [oci_objectstorage_preauthrequest](https://www.terraform.io/docs/providers/oci/r/objectstorage_preauthrequest.html) in the _Terraform Provider Documentation_