# Terraform::OPC::StorageContainer

Creates and manages a Container in the Oracle Cloud Infrastructure Storage Classic service. `storage_endpoint` must be set in the
provider or environment to manage these resources.

## Properties

`Name` - (Required) The name of the Storage Container.

`ReadAcls` - (Optional) The list of ACLs that grant read access. See [Setting Container ACLs](#setting-container-acls).

`WriteAcls` - (Optional) The list of ACLs that grant write access. See [Setting Container ACLs](#setting-container-acls).

`PrimaryKey` - (Optional) The primary secret key value for temporary URLs.

`SecondaryKey` - (Optional) The secondary secret key value for temporary URLs.

`AllowedOrigins` - (Optional) List of origins that are allowed to make cross-origin requests.

`ExposedHeaders` - (Optional) List of headers exposed to the user agent (e.g. browser) in the actual request response.

`MaxAge` - (Optional) Maximum age in seconds for the origin to hold the preflight results.

`QuotaBytes` - (Optional) Maximum size of the container, in bytes.

`QuotaCount` - (Optional) Maximum object count of the container.

`Metadata` - (Optional) Additional object metadata headers. See [Container Metadata ](#container-metadata) below for more information.


## See Also

* [opc_storage_container](https://www.terraform.io/docs/providers/opc/r/storage_container.html) in the _Terraform Provider Documentation_