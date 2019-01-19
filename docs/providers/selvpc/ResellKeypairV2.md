# Terraform::SelVPC::ResellKeypairV2

Manages a V2 keypair resource within Resell Selectel VPC.

## Properties

`Name` - (Required) Name of the keypair. Changing this creates a new keypair.

`PublicKey` - (Required) A pregenerated OpenSSH-formatted public key. Changing this creates a new keypair.

`Regions` - (Optional) List of region names where keypair is need to be created. Keypair will be created in all available regions if omitted. Changing this creates a new keypair.

`UserId` - (Required) An associated Selectel VPC user. Changing this creates a new keypair.


## See Also

* [selvpc_resell_keypair_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_keypair_v2.html) in the _Terraform Provider Documentation_