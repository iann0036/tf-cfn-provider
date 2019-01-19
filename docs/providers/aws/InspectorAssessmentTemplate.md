# Terraform::AWS::InspectorAssessmentTemplate

Provides a Inspector assessment template

## Properties

`Name` - (Required) The name of the assessment template.

`TargetArn` - (Required) The assessment target ARN to attach the template to.

`Duration` - (Required) The duration of the inspector run.

`RulesPackageArns` - (Required) The rules to be used during the run.


## Return Values

### Fn::GetAtt

`Arn` - The template assessment ARN.

## See Also

* [aws_inspector_assessment_template](https://www.terraform.io/docs/providers/aws/r/inspector_assessment_template.html) in the _Terraform Provider Documentation_