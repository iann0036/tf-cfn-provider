# Terraform::Atlas::Artifact

Provides access to deployment artifacts managed by Atlas. This
can be used to dynamically configure instantiation and provisioning of
resources.

~> **This provider is deprecated,** and the service it interacts with has been discontinued.

~> **This resource is deprecated!** Please use the
[Artifact Data Source](/docs/providers/terraform-enterprise/d/artifact.html)

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the artifact. This could be an AMI ID, GCE Image ID, etc.

`FileUrl` - For artifacts that are binaries, this is a download path.

`MetadataFull` - Contains the full metadata of the artifact. The keys are sanitized.

`VersionReal` - The matching version of the artifact.

`Slug` - The artifact slug in Atlas.

## See Also

* [atlas_artifact](https://www.terraform.io/docs/providers/atlas/r/artifact.html) in the _Terraform Provider Documentation_