# Terraform::Cloudflare::AccessPolicy

Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.

## Properties

`ApplicationId` - (Required) The ID of the application the policy is
associated with.

`ZoneId` - (Required) The DNS zone to which the access rule should be
added.

`Decision` - (Required) The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.

`Name` - (Required) Friendly name of the Access Application.

`Precedence` - (Optional) The unique precedence for policies on a single application. Integer.

`Require` - (Optional) A series of access conditions, see below for
full list.

`Exclude` - (Optional) A series of access conditions, see below for
full list.

`Include` - (Required) A series of access conditions, see below for
full list.


## See Also

* [cloudflare_access_policy](https://www.terraform.io/docs/providers/cloudflare/r/access_policy.html) in the _Terraform Provider Documentation_