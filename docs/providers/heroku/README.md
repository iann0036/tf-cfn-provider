# Heroku Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/heroku**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Heroku API token. It must be provided, but it can also
  be sourced from the `HEROKU_API_KEY` environment variable.

* `email` - (Required) Email to be notified by Heroku. It must be provided, but
  it can also be sourced from the `HEROKU_EMAIL` environment variable.

* `headers` - (Optional) Additional Headers to be sent to Heroku. If not provided,
  it can also be sourced from the `HEROKU_HEADERS` environment variable.

* `delays` - (Optional) A `delays` block (documented below). Only one
  `delays` block may be in the configuration. Delays help mitigate issues with 
  eventual consistency in the Heroku back-end service.

The nested `delays` block supports the following:

* `post_app_create_delay` - (Optional) The number of seconds to wait after an app is created. Default is to wait 5 seconds.

* `post_space_create_delay` - (Optional) The number of seconds to wait after a private space is created. Default is to wait 5 seconds.

* `post_domain_create_delay` - (Optional) The number of seconds to wait after a domain is created. Default is to wait 5 seconds.


## Supported Resources

* [Terraform::Heroku::AccountFeature](docs/providers/heroku/AccountFeature.md)
* [Terraform::Heroku::AddonAttachment](docs/providers/heroku/AddonAttachment.md)
* [Terraform::Heroku::Addon](docs/providers/heroku/Addon.md)
* [Terraform::Heroku::AppFeature](docs/providers/heroku/AppFeature.md)
* [Terraform::Heroku::AppRelease](docs/providers/heroku/AppRelease.md)
* [Terraform::Heroku::App](docs/providers/heroku/App.md)
* [Terraform::Heroku::Build](docs/providers/heroku/Build.md)
* [Terraform::Heroku::Cert](docs/providers/heroku/Cert.md)
* [Terraform::Heroku::Domain](docs/providers/heroku/Domain.md)
* [Terraform::Heroku::Drain](docs/providers/heroku/Drain.md)
* [Terraform::Heroku::Formation](docs/providers/heroku/Formation.md)
* [Terraform::Heroku::PipelineCoupling](docs/providers/heroku/PipelineCoupling.md)
* [Terraform::Heroku::Pipeline](docs/providers/heroku/Pipeline.md)
* [Terraform::Heroku::Slug](docs/providers/heroku/Slug.md)
* [Terraform::Heroku::SpaceInboundRuleset](docs/providers/heroku/SpaceInboundRuleset.md)
* [Terraform::Heroku::SpaceMember](docs/providers/heroku/SpaceMember.md)
* [Terraform::Heroku::SpacePeeringConnectionAccepter](docs/providers/heroku/SpacePeeringConnectionAccepter.md)
* [Terraform::Heroku::SpaceVpnConnection](docs/providers/heroku/SpaceVpnConnection.md)
* [Terraform::Heroku::Space](docs/providers/heroku/Space.md)
* [Terraform::Heroku::TeamCollaborator](docs/providers/heroku/TeamCollaborator.md)
* [Terraform::Heroku::TeamMember](docs/providers/heroku/TeamMember.md)