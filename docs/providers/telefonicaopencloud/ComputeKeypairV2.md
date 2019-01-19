# Terraform::TelefonicaOpenCloud::ComputeKeypairV2

Manages a V2 keypair resource within TelefonicaOpenCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. Keypairs are associated with accounts, but a Compute client is needed to create one. If omitted, the `Region` argument of the provider is used. Changing this creates a new keypair.

`Name` - (Required) A unique name for the keypair. Changing this creates a new keypair.

`PublicKey` - (Required) A pregenerated OpenSSH-formatted public key. Changing this creates a new keypair.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`PublicKey` - See Properties above.

## See Also

* [telefonicaopencloud_compute_keypair_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/compute_keypair_v2.html) in the _Terraform Provider Documentation_