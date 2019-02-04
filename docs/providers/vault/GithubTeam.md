# Terraform::Vault::GithubTeam

Manages policy mappings for Github Teams authenticated via Github. See the [Vault 
documentation](https://www.vaultproject.io/docs/auth/github.html) for more
information.

## Properties

`Backend` - (Required) Path where the github auth backend is mounted. Defaults to `github`
if not specified.

`Team` - (Required) GitHub team name in "slugified" format, for example: Terraform Developers -> `terraform-developers`.

`Policies` - (Optional) A list of policies to be assigned to this team.


## See Also

* [vault_github_team](https://www.terraform.io/docs/providers/vault/r/github_team.html) in the _Terraform Provider Documentation_