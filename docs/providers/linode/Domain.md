# Terraform::Linode::Domain

Provides a Linode Domain resource.  This can be used to create, modify, and delete Linodes Domains.
For more information, see [DNS Manager](https://www.linode.com/docs/platform/manager/dns-manager/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createDomain).

## Properties

`Domain` - (Required) The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.

`Type` - (Required) If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).

`SoaEmail` - (Required) Start of Authority email address. This is required for master Domains.

`MasterIps` - (Required for type="slave") The IP addresses representing the master DNS for this Domain.

`Status` - (Optional) Used to control whether this Domain is currently being rendered (defaults to "active").

`Description` - (Optional) A description for this Domain. This is for display purposes only.

`Group` - (Optional) The group this Domain belongs to. This is for display purposes only.

`TtlSec` - (Optional) 'Time to Live' - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.

`RetrySec` - (Optional) The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.

`ExpireSec` - (Optional) The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.

`RefreshSec` - (Optional) The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.

`AxfrIps` - (Optional) The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.

`Tags` - (Optional) A list of tags applied to this object. Tags are for organizational purposes only.


## See Also

* [linode_domain](https://www.terraform.io/docs/providers/linode/r/domain.html) in the _Terraform Provider Documentation_