# Terraform::AWS::ElasticBeanstalkApplicationVersion

Provides an Elastic Beanstalk Application Version Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates a Beanstalk Application Version that can be deployed to a Beanstalk
Environment.

~> **NOTE on Application Version Resource:**  When using the Application Version resource with multiple 
[Elastic Beanstalk Environments](elastic_beanstalk_environment.html) it is possible that an error may be returned
when attempting to delete an Application Version while it is still in use by a different environment.
To work around this you can:
<ol>
<li>Create each environment in a separate AWS account</li>
<li>Create your `Terraform::AWS::ElasticBeanstalkApplicationVersion` resources with a unique names in your 
Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
</ol>

## Properties

`Name` - (Required) A unique name for the this Application Version.

`Application` - (Required) Name of the Beanstalk Application the version is associated with.

`Description` - (Optional) Short description of the Application Version.

`Bucket` - (Required) S3 bucket that contains the Application Version source bundle.

`Key` - (Required) S3 object that is the Application Version source bundle.

`ForceDelete` - (Optional) On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.


## Return Values

### Fn::GetAtt

`Name` - The Application Version name.

## See Also

* [aws_elastic_beanstalk_application_version](https://www.terraform.io/docs/providers/aws/r/elastic_beanstalk_application_version.html) in the _Terraform Provider Documentation_