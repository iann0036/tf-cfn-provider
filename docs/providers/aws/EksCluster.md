# Terraform::AWS::EksCluster

Manages an EKS Cluster.

## Properties

`RoleArn` - (Required) The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

`VpcConfig` - (Required) Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the Amazon EKS User Guide. Configuration detailed below.


## Return Values

### Fn::GetAtt

`Id` - The name of the cluster.

`Arn` - The Amazon Resource Name (ARN) of the cluster.

`CertificateAuthority` - Nested attribute containing `certificate-authority-data` for your cluster.

`Data` - The base64 encoded certificate data required to communicate with your cluster. Add this to the `certificate-authority-data` section of the `kubeconfig` file for your cluster.

`Endpoint` - The endpoint for your Kubernetes API server.

`PlatformVersion` - The platform version for the cluster.

`Version` - The Kubernetes server version for the cluster.

`VpcConfig` - Additional nested attributes:.

`VpcId` - The VPC associated with your cluster.

## See Also

* [aws_eks_cluster](https://www.terraform.io/docs/providers/aws/r/eks_cluster.html) in the _Terraform Provider Documentation_