# Terraform::AWS::SesTemplate

Provides a resource to create a SES template.

## Properties

`Name` - (Required) The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.

`Html` - (Optional) The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.

`Subject` - (Optional) The subject line of the email.

`Text` - (Optional) The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.


## Return Values

### Fn::GetAtt

`Id` - The name of the SES template.

## See Also

* [aws_ses_template](https://www.terraform.io/docs/providers/aws/r/ses_template.html) in the _Terraform Provider Documentation_