# Terraform::AWS::ElasticsearchDomain

Manages an AWS Elasticsearch Domain.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - Amazon Resource Name (ARN) of the domain.

`DomainId` - Unique identifier for the domain.

`DomainName` - The name of the Elasticsearch domain.

`Endpoint` - Domain-specific endpoint used to submit index, search, and data upload requests.

`KibanaEndpoint` - Domain-specific endpoint for kibana without https scheme.

`VpcOptions.0.availabilityZones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.

`VpcOptions.0.vpcId` - If the domain was created inside a VPC, the ID of the VPC.

## See Also

* [aws_elasticsearch_domain](https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain.html) in the _Terraform Provider Documentation_