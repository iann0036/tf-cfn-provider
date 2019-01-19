# Terraform::NSXT::LbSourceIpPersistenceProfile

Provides a resource to configure lb source ip persistence profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb source ip persistence profile.

`PersistenceShared` - (Optional) A boolean flag which reflects whether the cookie persistence is private or shared.

`HaPersistenceMirroring` - (Optional) A boolean flag which reflects whether persistence entries will be synchronized to the HA peer.

`Timeout` - (Optional) Persistence expiration time in seconds, counted from the time all the connections are completed. Defaults to 300 seconds.

`PurgeWhenFull` - (Optional) A boolean flag which reflects whether entries will be purged when the persistence table is full. Defaults to true.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb source ip persistence profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_source_ip_persistence_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_source_ip_persistence_profile.html) in the _Terraform Provider Documentation_