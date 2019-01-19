# Terraform::OCI::DnsZone

This resource provides the Zone resource in Oracle Cloud Infrastructure Dns service.

Creates a new zone in the specified compartment.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment containing the zone.

`DefinedTags` - Usage of predefined tag keys. These predefined keys are scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

`ExternalMasters` - External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

`Address` - The server's IP address (IPv4 or IPv6).

`Port` - The server's port. Port value must be a value of 53, otherwise omit the port value.

`Tsig` - A TSIG key.

`Algorithm` - TSIG Algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see [RFC 4635](https://tools.ietf.org/html/rfc4635#section-2).

`Name` - The name of the zone.

`Secret` - A base64 string encoding the binary shared secret.

`FreeformTags` - Simple key-value pair that is applied without any predefined name, type, or scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"bar-key": "value"}`.

`Id` - The OCID of the zone.

`Nameservers` - The authoritative nameservers for the zone.

`Hostname` - The hostname of the nameserver.

`Self` - The canonical absolute URL of the resource.

`Serial` - The current serial of the zone. As seen in the zone's SOA record.

`State` - The current state of the zone resource.

`TimeCreated` - The date and time the resource was created in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

`Version` - Version is the never-repeating, totally-orderable, version of the zone, from which the serial field of the zone's SOA record is derived.

`ZoneType` - The type of the zone. Must be either `PRIMARY` or `SECONDARY`.

## See Also

* [oci_dns_zone](https://www.terraform.io/docs/providers/oci/r/dns_zone.html) in the _Terraform Provider Documentation_