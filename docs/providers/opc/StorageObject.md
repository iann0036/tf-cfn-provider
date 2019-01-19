# Terraform::OPC::StorageObject

Creates and manages a Object in an Oracle Cloud Infrastructure Storage Classic container. `storage_endpoint` must be set in the provider or environment to manage these resources.

## Properties

`Name` - (Required) The name of the Storage Object.

`Container` - (Required) The name of Storage Container the store the object in.

`Content` - (Optional) Raw content in string-form of the data.

`File` - (Optional) File path for the content to use for data.

`CopyFrom` - (Optional) name of an existing object used to create the new object as a copy. The value is in form `container/object`. You must UTF-8-encode and then URL-encode the names of the container and object.

`ContentDisposition` - (Optional) Set the HTTP `Content-Disposition` header to specify the override behaviour for the browser, e.g. `inline` or `attachment`.

`ContentEncoding` - (Optional) set the HTTP `Content-Encoding` for the object.

`ContentType` - (Optional) set the MIME type for the object.

`DeleteAt` - (Optional) The date and time in UNIX Epoch time stamp format when the system removes the object.

`Etag` - (Optional) MD5 checksum value of the request body. Strongly Recommended.

`TransferEncoding` - (Optional) Set to `chunked` to enable chunked transfer encoding.

`Metadata` - (Optional) Additional object metadata headers. See [Object Metadata ](#object-metadata) below for more information.


## See Also

* [opc_storage_object](https://www.terraform.io/docs/providers/opc/r/storage_object.html) in the _Terraform Provider Documentation_