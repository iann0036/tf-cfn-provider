# Terraform::DigitalOcean::Firewall

Provides a DigitalOcean Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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