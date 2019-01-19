# Terraform::AWS::EksCluster

Manages an EKS Cluster.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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