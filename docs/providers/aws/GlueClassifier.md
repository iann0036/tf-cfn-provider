# Terraform::AWS::GlueClassifier

Provides a Glue Classifier resource.

~> **NOTE:** It is only valid to create one type of classifier (grok, JSON, or XML). Changing classifier types will recreate the classifier.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Name of the classifier.

## See Also

* [aws_glue_classifier](https://www.terraform.io/docs/providers/aws/r/glue_classifier.html) in the _Terraform Provider Documentation_