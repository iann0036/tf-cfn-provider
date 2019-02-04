# Terraform::Google::ComposerEnvironment

An environment for running orchestration tasks.

Environments run Apache Airflow software on Google infrastructure.

To get more information about Environments, see:

* [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/composer/docs)
    * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
* [Apache Airflow Documentation](http://airflow.apache.org/)

~> **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
  as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
  including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
  Terraform will not be able to automatically find or manage many of these underlying resources. In particular:
  * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some 
    errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
    error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
    against GCP Cloud Composer before filing bugs against the Terraform provider. 
  * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment 
    deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).

## Properties

`Project` - (Optional) The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.


## See Also

* [google_composer_environment](https://www.terraform.io/docs/providers/google/r/composer_environment.html) in the _Terraform Provider Documentation_