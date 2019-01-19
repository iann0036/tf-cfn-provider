# Terraform::AWS::MediaPackageChannel

Provides an AWS Elemental MediaPackage Channel.

## Properties

`ChannelId` - (Required) A unique identifier describing the channel.

`Description` - (Optional) A description of the channel.


## Return Values

### Fn::GetAtt

`Id` - The same as `ChannelId`.

`Arn` - The ARN of the channel.

`HlsIngest` - A single item list of HLS ingest information.

`IngestEndpoints` - A list of the ingest endpoints.

`Password` - The password.

`Url` - The URL.

`Username` - The username.

## See Also

* [aws_media_package_channel](https://www.terraform.io/docs/providers/aws/r/media_package_channel.html) in the _Terraform Provider Documentation_