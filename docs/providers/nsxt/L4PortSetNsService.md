# Terraform::NSXT::L4PortSetNsService

This resource provides a way to configure a networking and security service which can be used within NSX. This specific service is for configuration of layer 4 ports.

## Properties

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`DestinationPorts` - (Optional) Set of destination ports.

`SourcePorts` - (Optional) Set of source ports.

`Protocol` - (Required) L4 protocol. Accepted values - 'TCP' or 'UDP'.

`Tag` - (Optional) A list of scope + tag pairs to associate with this service.


## Return Values

### Fn::GetAtt

`Id` - ID of the NS service.

`DefaultService` - The default NSServices are created in the system by default. These NSServices can't be modified/deleted.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_l4_port_set_ns_service](https://www.terraform.io/docs/providers/nsxt/r/l4_port_set_ns_service.html) in the _Terraform Provider Documentation_