# Terraform::NSXT::AlgorithmTypeNsService

This resource provides a way to configure a networking and security service which can be used with the NSX firewall. A networking and security service is an object that contains the TCP/UDP algorithm, source ports and destination ports in a single entity.

## Properties

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description.

`DestinationPort` - (Required) a single destination port.

`SourcePorts` - (Optional) Set of source ports/ranges.

`Algorithm` - (Required) Algorithm one of "ORACLE_TNS", "FTP", "SUN_RPC_TCP", "SUN_RPC_UDP", "MS_RPC_TCP", "MS_RPC_UDP", "NBNS_BROADCAST", "NBDG_BROADCAST", "TFTP".

`Tag` - (Optional) A list of scope + tag pairs to associate with this service.


## Return Values

### Fn::GetAtt

`Id` - ID of the NS service.

`DefaultService` - The default NSServices are created in the system by default. These NSServices can't be modified/deleted.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_algorithm_type_ns_service](https://www.terraform.io/docs/providers/nsxt/r/algorithm_type_ns_service.html) in the _Terraform Provider Documentation_