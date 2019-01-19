# Terraform::Consul::Keys

The `consul_keys` resource writes sets of individual values into Consul.
This is a powerful way to expose infrastructure details to clients.

This resource manages individual keys, and thus it can create, update
and delete the keys explicitly given. However, it is not able to detect
and remove additional keys that have been added by non-Terraform means.
To manage *all* keys sharing a common prefix, and thus have Terraform
remove errant keys not present in the configuration, consider using the
`consul_key_prefix` resource instead.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Datacenter` - The datacenter the keys are being written to.

## See Also

* [consul_keys](https://www.terraform.io/docs/providers/consul/r/keys.html) in the _Terraform Provider Documentation_