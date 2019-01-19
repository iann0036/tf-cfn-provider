# Terraform::AWS::OpsworksApplication

Provides an OpsWorks application resource.

## Properties

`Name` - (Required) A human-readable name for the application.

`ShortName` - (Required) A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

`StackId` - (Required) The id of the stack the application will belong to.

`Type` - (Required) Opsworks application type. One of `aws-flow-ruby`, `java`, `rails`, `php`, `nodejs`, `static` or `other`.

`Description` - (Optional) A description of the app.

`Environment` - (Optional) Object to define environment variables.  Object is described below.

`EnableSsl` - (Optional) Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

`SslConfiguration` - (Optional) The SSL configuration of the app. Object is described below.

`AppSource` - (Optional) SCM configuration of the app as described below.

`DataSourceArn` - (Optional) The data source's ARN.

`DataSourceType` - (Optional) The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

`DataSourceDatabaseName` - (Optional) The database name.

`Domains` -  (Optional) A list of virtual host alias.

`DocumentRoot` - (Optional) Subfolder for the document root for application of type `rails`.

`AutoBundleOnDeploy` - (Optional) Run bundle install when deploying for application of type `rails`.

`RailsEnv` - (Required if `Type` = `rails`) The name of the Rails environment for application of type `rails`.

`AwsFlowRubySettings` - (Optional) Specify activity and workflow workers for your app using the aws-flow gem.

### AppSource Properties

`Type` - (Required) The type of source to use. For example, "archive".

`Url` - (Required) The URL where the app resource can be found.

`Username` - (Optional) Username to use when authenticating to the source.

`Password` - (Optional) Password to use when authenticating to the source.

`SshKey` - (Optional) SSH key to use when authenticating to the source.

`Revision` - (Optional) For sources that are version-aware, the revision to use.

### Environment Properties

`Key` - (Required) Variable name.

`Value` - (Required) Variable value.

`Secure` - (Optional) Set visibility of the variable value to `true` or `false`.

### SslConfiguration Properties

`PrivateKey` - (Required) The private key; the contents of the certificate's domain.key file.

`Certificate` - (Required) The contents of the certificate's domain.crt file.

`Chain` - (Optional)  Can be used to specify an intermediate certificate authority key or client authentication.


## Return Values

### Fn::GetAtt

`Id` - The id of the application.

## See Also

* [aws_opsworks_application](https://www.terraform.io/docs/providers/aws/r/opsworks_application.html) in the _Terraform Provider Documentation_