# Terraform::Kubernetes::NetworkPolicy

Kubernetes supports network policies to specificy of how groups of pods are allowed to communicate with each other and other network endpoints.
NetworkPolicy resources use labels to select pods and define rules which specify what traffic is allowed to the selected pods.
Read more about network policies at https://kubernetes.io/docs/concepts/services-networking/network-policies/

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [kubernetes_network_policy](https://www.terraform.io/docs/providers/kubernetes/r/network_policy.html) in the _Terraform Provider Documentation_