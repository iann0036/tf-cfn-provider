# Terraform CloudFormation Resource Provider

> Deploy over 2,000 new resource types with CloudFormation.

<img src="https://github.com/iann0036/tf-cfn-provider/raw/master/assets/screen1.png" width="558" height="491">

:exclamation: **CAUTION:** This project is currently in beta stages. Some resources may not work as expected and fields may not be validated.


## Installation

<a href="https://console.aws.amazon.com/cloudformation/home?#/stacks/new?&templateURL=https://s3.amazonaws.com/ianmckay-ap-southeast-2/terraform/custom_resource.yaml" target="_blank"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"></a>

Click the above link to deploy the stack which is required to deploy the Transform and Custom Resource handler. This is required to be in place for any future stack deployments.

If you prefer, you can also manually upsert the [custom_resource.yaml](custom_resource.yaml) stack from source and compile your own copy of the Lambda source. Please note that if you do this, the Python requirements must be vendored.


## Usage

Once the handler stack is created, you may use the below resources by adding the `Terraform` transform to your stack. This will transform your input template to convert the Terraform resources into Custom Resources that will handle the lifecycle within that provider.

Most providers will require you to store credentials and/or other provider-specific settings within AWS Secrets Manager in order to access their services. See the provider documentation for more information on how to configure those secrets.

Click [here](docs/README.md) to see all supported resources and provider documentation.
