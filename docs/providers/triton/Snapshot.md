# Terraform::Triton::Snapshot

The `triton_snapshot` resource represents a snapshot of a Triton machine.
Snapshots are not usable with other instances; they are a point-in-time snapshot of the current instance.
Snapshots can also only be taken of instances that are not of brand `kvm`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [triton_snapshot](https://www.terraform.io/docs/providers/triton/r/snapshot.html) in the _Terraform Provider Documentation_