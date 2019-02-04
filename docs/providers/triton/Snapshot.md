# Terraform::Triton::Snapshot

The `Terraform::Triton::Snapshot` resource represents a snapshot of a Triton machine.
Snapshots are not usable with other instances; they are a point-in-time snapshot of the current instance.
Snapshots can also only be taken of instances that are not of brand `kvm`.

## Properties

`Name` - (string, Required)
The name for the snapshot.

`MachineId` - (string, Required)
The ID of the machine of which to take a snapshot.


## See Also

* [triton_snapshot](https://www.terraform.io/docs/providers/triton/r/snapshot.html) in the _Terraform Provider Documentation_