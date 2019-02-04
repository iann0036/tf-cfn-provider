# Terraform::Vault::GithubUser

Manages policy mappings for Github Users authenticated via Github. See the [Vault 
documentation](https://www.vaultproject.io/docs/auth/github.html) for more
information.

## Properties

`Backend` - (Required) Path where the github auth backend is mounted. Defaults to `github`
if not specified.

`User` - (Required) GitHub user name.

`Policies` - (Optional) A list of policies to be assigned to this user.


## See Also

* [vault_github_user](https://www.terraform.io/docs/providers/vault/r/github_user.html) in the _Terraform Provider Documentation_