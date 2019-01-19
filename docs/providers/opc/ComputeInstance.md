# Terraform::OPC::ComputeInstance

The ``opc_compute_instance`` resource creates and manages an instance in an Oracle Cloud Infrastructure Compute Classic identity domain.

~> **Caution:** The ``opc_compute_instance`` resource can completely delete your
instance just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your instance resources as an extra safety measure.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The `id` of the instance.

`Attributes` - The full attributes of the instance, as a JSON string.

`AvailabilityDomain` - The availability domain the instance is in.

`Domain` - The default domain to use for the hostname and for DNS lookups.

`Entry` - Imagelist entry number.

`Fingerprint` - SSH server fingerprint presented by the instance.

`Fqdn` - The fully qualified domain name of the instance.

`ImageFormat` - The format of the image.

`IpAddress` - The IP Address of the instance.

`PlacementRequirements` - The array of placement requirements for the instance.

`Platform` - The OS Platform of the instance.

`Priority` - The priority at which the instance was ran.

`QuotaReservation` - Reference to the QuotaReservation, to be destroyed with the instance.

`Relationships` - The array of relationship specifications to be satisfied on instance placement.

`Resolvers` - Array of resolvers to be used instead of the default resolvers.

`Site` - The site the instance is running on.

`StartTime` - The launch time of the instance.

`State` - The instance's state.

`VcableId` - vCable ID for the instance.

`Virtio` - Boolean that determines if the instance is a virtio device.

`VncAddress` - The VNC address and port of the instance.

## See Also

* [opc_compute_instance](https://www.terraform.io/docs/providers/opc/r/compute_instance.html) in the _Terraform Provider Documentation_