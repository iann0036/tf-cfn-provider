# Terraform::HCloud::FloatingIpAssignment

Provides a Hetzner Cloud Floating IP Assignment to assign a Floating IP to a Hetzner Cloud Server. Deleting a Floating IP Assignment will unassign the Floating IP from the Server.

## Properties

`FloatingIpId` - (Required, int) ID of the Floating IP. - `ServerId` - (Required, int) Server to assign the Floating IP to.

`ServerId` - (Required, int) Server to assign the Floating IP to.


## See Also

* [hcloud_floating_ip_assignment](https://www.terraform.io/docs/providers/hcloud/r/floating_ip_assignment.html) in the _Terraform Provider Documentation_