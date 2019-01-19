# Terraform::Heroku::Build

Provides a [Heroku Build](https://devcenter.heroku.com/articles/platform-api-reference#build)
resource, to deploy source code to a Heroku app.

Either a URL or local path, pointing to a [tarball](https://en.wikipedia.org/wiki/Tar_(computing)) of the source code, may be deployed. If a local path is used, it may instead point to a directory of source code, which will be tarballed automatically and then deployed.

This resource waits until the [build](https://devcenter.heroku.com/articles/build-and-release-using-the-api) & [release](https://devcenter.heroku.com/articles/release-phase) completes.

If the build fails, the error will contain a URL to view the build log. `curl "https://the-long-log-url-in-the-error"`.

To start the app from a successful build, use a [Formation resource](formation.html) to specify the process, dyno size, and dyno quantity.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Uuid` - The ID of the build.

`OutputStreamUrl` - URL that [streams the log output from the build](https://devcenter.heroku.com/articles/build-and-release-using-the-api#streaming-build-output).

`ReleaseId` - The Heroku app release created with a build's slug.

`SlugId` - The Heroku slug created by a build.

`Stack` - Name or ID of the [Heroku stack](https://devcenter.heroku.com/articles/stack).

`Status` - The status of a build. Possible values are `pending`, `successful` and `failed`.

`User` - Heroku account that created a build.

## See Also

* [heroku_build](https://www.terraform.io/docs/providers/heroku/r/build.html) in the _Terraform Provider Documentation_