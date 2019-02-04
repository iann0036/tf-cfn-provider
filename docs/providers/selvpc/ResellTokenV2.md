# Terraform::SelVPC::ResellTokenV2

Manages a V2 token resource within Resell Selectel VPC.

ID of this resource can be used within the OpenStack API Identity service as
the `X-Auth-Token` value.

## Properties

`ProjectId` - (Optional) An associated Selectel VPC project. Changing this
creates a new token.

`AccountName` - (Optional) An associated Selectel VPC account. Changing this
creates a new token.


## See Also

* [selvpc_resell_token_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_token_v2.html) in the _Terraform Provider Documentation_