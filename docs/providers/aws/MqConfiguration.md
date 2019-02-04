# Terraform::AWS::MqConfiguration

Provides an MQ Configuration Resource. 

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

## Properties

`Data` - (Required) The broker configuration in XML format.
See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
for supported parameters and format of the XML.

`Description` - (Optional) The description of the configuration.

`EngineType` - (Required) The type of broker engine.

`EngineVersion` - (Required) The version of the broker engine.

`Name` - (Required) The name of the configuration.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The unique ID that Amazon MQ generates for the configuration.

`Arn` - The ARN of the configuration.

`LatestRevision` - The latest revision of the configuration.

## See Also

* [aws_mq_configuration](https://www.terraform.io/docs/providers/aws/r/mq_configuration.html) in the _Terraform Provider Documentation_