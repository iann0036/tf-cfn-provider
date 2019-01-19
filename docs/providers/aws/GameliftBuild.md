# Terraform::AWS::GameliftBuild

Provides an Gamelift Build resource.

## Properties

`Name` - (Required) Name of the build.

`OperatingSystem` - (Required) Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

`StorageLocation` - (Required) Information indicating where your game build files are stored. See below.

`Version` - (Optional) Version that is associated with this build.


## Return Values

### Fn::GetAtt

`Id` - Build ID.

## See Also

* [aws_gamelift_build](https://www.terraform.io/docs/providers/aws/r/gamelift_build.html) in the _Terraform Provider Documentation_