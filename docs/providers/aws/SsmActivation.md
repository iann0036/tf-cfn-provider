# Terraform::AWS::SsmActivation

Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.

## Properties

`Name` - (Optional) The default name of the registered managed instance.

`Description` - (Optional) The description of the resource that you want to register.

`ExpirationDate` - (Optional) A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.

`IamRole` - (Required) The IAM Role to attach to the managed instance.

`RegistrationLimit` - (Optional) The maximum number of managed instances you want to register. The default value is 1 instance.


## Return Values

### Fn::GetAtt

`ActivationCode` - The code the system generates when it processes the activation.

`Name` - The default name of the registered managed instance.

`Description` - The description of the resource that was registered.

`Expired` - If the current activation has expired.

`ExpirationDate` - The date by which this activation request should expire. The default value is 24 hours.

`IamRole` - The IAM Role attached to the managed instance.

`RegistrationLimit` - The maximum number of managed instances you want to be registered. The default value is 1 instance.

`RegistrationCount` - The number of managed instances that are currently registered using this activation.

## See Also

* [aws_ssm_activation](https://www.terraform.io/docs/providers/aws/r/ssm_activation.html) in the _Terraform Provider Documentation_