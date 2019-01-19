# Terraform::Kubernetes::ReplicationController

A Replication Controller ensures that a specified number of pod “replicas” are running at any one time. In other words, a Replication Controller makes sure that a pod or homogeneous set of pods are always up and available. If there are too many pods, it will kill some. If there are too few, the Replication Controller will start more.

~> **WARNING:** In many cases it is recommended to create a Deployment instead of a Replication Controller.

## Properties

TBC

## See Also

* [kubernetes_replication_controller](https://www.terraform.io/docs/providers/kubernetes/r/replication_controller.html) in the _Terraform Provider Documentation_