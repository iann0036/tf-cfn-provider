# Heroku Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/heroku** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) Heroku API token.

* `email` - (Required) Email to be notified by Heroku.

* `headers` - (Optional) Additional Headers to be sent to Heroku.

* `delays` - (Optional) A `delays` block (documented below). Only one
  `delays` block may be in the configuration. Delays help mitigate issues with 
  eventual consistency in the Heroku back-end service.

The nested `delays` block supports the following:

* `post_app_create_delay` - (Optional) The number of seconds to wait after an app is created. Default is to wait 5 seconds.

* `post_space_create_delay` - (Optional) The number of seconds to wait after a private space is created. Default is to wait 5 seconds.

* `post_domain_create_delay` - (Optional) The number of seconds to wait after a domain is created. Default is to wait 5 seconds.


## Supported Resources

* [Terraform::Heroku::AccountFeature](AccountFeature.md)
* [Terraform::Heroku::AddonAttachment](AddonAttachment.md)
* [Terraform::Heroku::Addon](Addon.md)
* [Terraform::Heroku::AppFeature](AppFeature.md)
* [Terraform::Heroku::AppRelease](AppRelease.md)
* [Terraform::Heroku::App](App.md)
* [Terraform::Heroku::Build](Build.md)
* [Terraform::Heroku::Cert](Cert.md)
* [Terraform::Heroku::Domain](Domain.md)
* [Terraform::Heroku::Drain](Drain.md)
* [Terraform::Heroku::Formation](Formation.md)
* [Terraform::Heroku::PipelineCoupling](PipelineCoupling.md)
* [Terraform::Heroku::Pipeline](Pipeline.md)
* [Terraform::Heroku::Slug](Slug.md)
* [Terraform::Heroku::SpaceAppAccess](SpaceAppAccess.md)
* [Terraform::Heroku::SpaceInboundRuleset](SpaceInboundRuleset.md)
* [Terraform::Heroku::SpacePeeringConnectionAccepter](SpacePeeringConnectionAccepter.md)
* [Terraform::Heroku::SpaceVpnConnection](SpaceVpnConnection.md)
* [Terraform::Heroku::Space](Space.md)
* [Terraform::Heroku::TeamCollaborator](TeamCollaborator.md)
* [Terraform::Heroku::TeamMember](TeamMember.md)