# Terraform::Consul::KeyPrefix

Allows Terraform to manage a "namespace" of Consul keys that share a common
name prefix.

Like `consul_keys`, this resource can write values into the Consul key/value
store, but *unlike* `consul_keys` this resource can detect and remove extra
keys that have been added some other way, thus ensuring that rogue data
added outside of Terraform will be removed on the next run.

This resource is thus useful in the case where Terraform is exclusively
managing a set of related keys.

To avoid accidentally clobbering matching data that existed in Consul before
a `consul_key_prefix` resource was created, creation of a key prefix instance
will fail if any matching keys are already present in the key/value store.
If any conflicting data is present, you must first delete it manually.

~> **Warning** After this resource is instantiated, Terraform takes control
over *all* keys with the given path prefix, and will remove any matching keys
that are not present in the configuration. It will also delete *all* keys under
the given prefix when a `consul_key_prefix` resource is destroyed, even if
those keys were created outside of Terraform.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Datacenter` - The datacenter the keys are being read/written to.

## See Also

* [consul_key_prefix](https://www.terraform.io/docs/providers/consul/r/key_prefix.html) in the _Terraform Provider Documentation_