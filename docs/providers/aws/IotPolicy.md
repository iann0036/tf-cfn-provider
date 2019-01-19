# Terraform::AWS::IotPolicy

Provides an IoT policy.

## Properties

`Name` - (Required) The name of the policy.

`Policy` - (Required) The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## Return Values

### Fn::GetAtt

`Arn` - The ARN assigned by AWS to this policy.

`Name` - The name of this policy.

`DefaultVersionId` - The default version of this policy.

`Policy` - The policy document.

## See Also

* [aws_iot_policy](https://www.terraform.io/docs/providers/aws/r/iot_policy.html) in the _Terraform Provider Documentation_