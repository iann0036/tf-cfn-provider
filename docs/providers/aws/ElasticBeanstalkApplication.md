# Terraform::AWS::ElasticBeanstalkApplication

Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates an application that has one configuration template named
`default`, and no application versions

## Properties

`Name` - (Required) The name of the application, must be unique within your account.

`Description` - (Optional) Short description of the application.

`ServiceRole` - (Required) The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.

`MaxCount` - (Optional) The maximum number of application versions to retain.

`MaxAgeInDays` - (Optional) The number of days to retain an application version.

`DeleteSourceFromS3` - (Optional) Set to `true` to delete a version's source bundle from S3 when the application version is deleted.


## See Also

* [aws_elastic_beanstalk_application](https://www.terraform.io/docs/providers/aws/r/elastic_beanstalk_application.html) in the _Terraform Provider Documentation_