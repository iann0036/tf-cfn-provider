# Terraform CloudFormation Resource Provider

> Deploy over 2,000 new resource types with CloudFormation.

![Screenshot](assets/screen1.png)

:exclamation: **CAUTION:** This project is currently in beta stages. Some resources may not work as expected and fields may not be validated.


## Installation

<a href="https://console.aws.amazon.com/cloudformation/home?#/stacks/new?&templateURL=https://s3.amazonaws.com/ianmckay-ap-southeast-2/terraform/custom_resource.yaml" target="_blank"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"></a>

Click the above link to deploy the stack which is required to deploy the Transform and Custom Resource handler. This is required to be in place for any future stack deployments.

If you prefer, you can also manually upsert the [custom_resource.yaml](custom_resource.yaml) stack from source and compile your own copy of the Lambda source. Please note that if you do this, the Python requirements must be vendored.


## Usage

Once the handler stack is created, you may use the below resources by adding the `Terraform` transform to your stack. This will transform your input template to convert the Terraform resources into Custom Resources that will handle the lifecycle within that provider.

The following resources are supported (click the link to see documentation):

Provider | Resource
-------- | --------
DigitalOcean | [Terraform::DigitalOcean::Droplet](docs/providers/digitalocean/droplet.md)
