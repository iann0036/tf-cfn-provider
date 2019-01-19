# Terraform::AWS::AppsyncDatasource

Provides an AppSync DataSource.

## Properties

`ApiId` - (Required) The API ID for the GraphQL API for the DataSource.

`Name` - (Required) A user-supplied name for the DataSource.

`Type` - (Required) The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.

`Description` - (Optional) A description of the DataSource.

`ServiceRoleArn` - (Optional) The IAM service role ARN for the data source.

`DynamodbConfig` - (Optional) DynamoDB settings. See [below](#dynamodb_config).

`ElasticsearchConfig` - (Optional) Amazon Elasticsearch settings. See [below](#elasticsearch_config).

`HttpConfig` - (Optional) HTTP settings. See [below](#http_config).

`LambdaConfig` - (Optional) AWS Lambda settings. See [below](#lambda_config).


## Return Values

### Fn::GetAtt

`Arn` - The ARN.

## See Also

* [aws_appsync_datasource](https://www.terraform.io/docs/providers/aws/r/appsync_datasource.html) in the _Terraform Provider Documentation_