# Terraform::DigitalOcean::Firewall

Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.

## Properties

`Name` - (Required) The Firewall name.

`InboundRule` - (Optional) The inbound access rule block for the Firewall. The `InboundRule` block is documented below.

`OutboundRule` - (Optional) The outbound access rule block for the Firewall. The `OutboundRule` block is documented below.

### InboundRule Properties

`SourceAddresses` - (Optional) An array of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the inbound traffic will be accepted.

`SourceDropletIds` - (Optional) An array containing the IDs of the Droplets from which the inbound traffic will be accepted.

`SourceTags` - (Optional) An array containing the names of Tags corresponding to groups of Droplets from which the inbound traffic will be accepted.

`SourceLoadBalancerUids` - (Optional) An array containing the IDs of the Load Balancers from which the inbound traffic will be accepted.

### OutboundRule Properties

`Protocol` - (Required) The type of traffic to be allowed. This may be one of "tcp", "udp", or "icmp".

`PortRange` - (Optional) The ports on which traffic will be allowed specified as a string containing a single port, a range (e.g. "8000-9000"), or "1-65535" to open all ports for a protocol. Required for when protocol is `tcp` or `udp`.

`DestinationAddresses` - (Optional) An array of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the outbound traffic will be allowed.

`DestinationDropletIds` - (Optional) An array containing the IDs of the Droplets to which the outbound traffic will be allowed.

`DestinationTags` - (Optional) An array containing the names of Tags corresponding to groups of Droplets to which the outbound traffic will be allowed. traffic.

`DestinationLoadBalancerUids` - (Optional) An array containing the IDs of the Load Balancers to which the outbound traffic will be allowed.


## Return Values

### Fn::GetAtt

`Id` - A unique ID that can be used to identify and reference a Firewall.

`Status` - A status string indicating the current state of the Firewall.

`CreatedAt` - A time value given in ISO8601 combined date and time format.

`PendingChanges` - An list of object containing the fields, "droplet_id",.

`Name` - The name of the Firewall.

`DropletIds` - The list of the IDs of the Droplets assigned to.

`Tags` - The names of the Tags assigned to the Firewall.

`InboundRules` - The inbound access rule block for the Firewall.

`OutboundRules` - The outbound access rule block for the Firewall.

## See Also

* [digitalocean_firewall](https://www.terraform.io/docs/providers/digitalocean/r/firewall.html) in the _Terraform Provider Documentation_