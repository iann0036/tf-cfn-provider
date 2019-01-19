# Terraform::Consul::Keys

The `Terraform::Consul::Keys` resource writes sets of individual values into Consul.
This is a powerful way to expose infrastructure details to clients.

This resource manages individual keys, and thus it can create, update
and delete the keys explicitly given. However, it is not able to detect
and remove additional keys that have been added by non-Terraform means.
To manage *all* keys sharing a common prefix, and thus have Terraform
remove errant keys not present in the configuration, consider using the
`Terraform::Consul::KeyPrefix` resource instead.

## Properties

`Datacenter` - (Optional) The datacenter to use. This overrides the datacenter in the provider setup and the agent's default datacenter.

`Token` - (Optional) The ACL token to use. This overrides the token that the agent provides by default.

`Key` - (Required) Specifies a key in Consul to be written. Supported values documented below.

### Key Properties

`Path` - (Required) This is the path in Consul that should be written to.

`Value` - (Required) The value to write to the given path.

`Delete` - (Optional) If true, then the key will be deleted when either its configuration block is removed from the configuration or the entire resource is destroyed. Otherwise, it will be left in Consul. Defaults to false.


## Return Values

### Fn::GetAtt

`Datacenter` - The datacenter the keys are being written to.

## See Also

* [consul_keys](https://www.terraform.io/docs/providers/consul/r/keys.html) in the _Terraform Provider Documentation_