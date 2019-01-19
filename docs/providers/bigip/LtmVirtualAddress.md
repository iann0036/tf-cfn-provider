# Terraform::BIGIP::LtmVirtualAddress

`Terraform::BIGIP::LtmVirtualAddress` Configures Virtual Server

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the virtual address.

`Description` - (Optional) Description of the virtual address.

`AdvertizeRoute` - (Optional) Enabled dynamic routing of the address.

`ConnLimit` - (Optional, Default=0) Max number of connections for virtual address.

`Enabled` - (Optional, Default=true) Enable or disable the virtual address.

`Arp` - (Optional, Default=true) Enable or disable ARP for the virtual address.

`AutoDelete` - (Optional, Default=true) Automatically delete the virtual address with the virtual server.

`IcmpEcho` - (Optional, Default=true) Enable/Disable ICMP response to the virtual address.

`TrafficGroup` - (Optional, Default=/Common/traffic-group-1) Specify the partition and traffic group.


## See Also

* [bigip_ltm_virtual_address](https://www.terraform.io/docs/providers/bigip/r/ltm_virtual_address.html) in the _Terraform Provider Documentation_