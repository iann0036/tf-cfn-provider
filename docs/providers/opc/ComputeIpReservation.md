# Terraform::OPC::ComputeIpReservation

The ``Terraform::OPC::ComputeIpReservation`` resource creates and manages an IP reservation in an Oracle Cloud Infrastructure Compute Classic identity domain for the Shared Network.

## Properties

`Permanent` - (Required) Whether the IP address remains reserved even when it is no longer associated with an instance (if true), or may be returned to the pool and replaced with a different IP address when an instance is restarted, or deleted and recreated (if false).

`ParentPool` - (Optional) The pool from which to allocate the IP address. Defaults to `/oracle/public/ippool`, and is currently the only acceptable input.

`Name` - (Optional) Name of the IP Reservation. Will be generated if unspecified.

`Tags` - (Optional) List of tags that may be applied to the IP reservation.


## Return Values

### Fn::GetAtt

`Ip` - The Public IP address.

`Used` - indicates that the IP reservation is associated with an instance.

## See Also

* [opc_compute_ip_reservation](https://www.terraform.io/docs/providers/opc/r/compute_ip_reservation.html) in the _Terraform Provider Documentation_