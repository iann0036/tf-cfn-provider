# Terraform::Atlas::Artifact

Provides access to deployment artifacts managed by Atlas. This
can be used to dynamically configure instantiation and provisioning of
resources.

~> **This provider is deprecated,** and the service it interacts with has been discontinued.

~> **This resource is deprecated!** Please use the
[Artifact Data Source](/docs/providers/terraform-enterprise/d/artifact.html)

## Properties

`Name` - (Required) Name of the artifact in Atlas. This is given
in slug format like "organization/artifact".

`Type` - (Required) The type of artifact to query for.

`Build` - (Optional) The build number responsible for creating
the version of the artifact to filter on. This can be "latest",
to find a matching artifact in the latest build, "any" to find a
matching artifact in any build, or a specific number to pin to that
build. If `Build` and `Version` are unspecified, `Version` will default
to "latest". Cannot be specified with `Version`. Note: `Build` is only
present if Atlas builds the image.

`Version` - (Optional)  The version of the artifact to filter on. This can
be "latest", to match against the latest version, "any" to find a matching artifact
in any version, or a specific number to pin to that version. Defaults to
"latest" if neither `Build` or `Version` is specified. Cannot be specified
with `Build`.

`MetadataKeys` - (Optional) If given, only an artifact containing
the given keys will be returned. This is used to disambiguate when
multiple potential artifacts match. An example is "aws" to filter
on an AMI.

`Metadata` - (Optional) If given, only an artifact matching the
metadata filters will be returned. This is used to disambiguate when
multiple potential artifacts match. An example is "arch" = "386" to
filter on architecture.


## Return Values

### Fn::GetAtt

`Id` - The ID of the artifact. This could be an AMI ID, GCE Image ID, etc.

`FileUrl` - For artifacts that are binaries, this is a download path.

`MetadataFull` - Contains the full metadata of the artifact. The keys are sanitized.

`VersionReal` - The matching version of the artifact.

`Slug` - The artifact slug in Atlas.

## See Also

* [atlas_artifact](https://www.terraform.io/docs/providers/atlas/r/artifact.html) in the _Terraform Provider Documentation_