# Terraform::Google::DataprocJob

Manages a job resource within a Dataproc cluster within GCE. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).

!> **Note:** This resource does not support 'update' and changing any attributes will cause the resource to be recreated.

## Properties

`Placement.clusterName` - (Required) The name of the cluster where the job
will be submitted.

`XxxConfig` - (Required) Exactly one of the specific job types to run on the
cluster should be specified. If you want to submit multiple jobs, this will
currently require the definition of multiple `Terraform::Google::DataprocJob` resources
as shown in the example above, or by setting the `count` attribute.
The following job configs are supported:.

`Project` - (Optional) The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.

`Region` - (Optional) The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.

`ForceDelete` - (Optional) By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.

`Labels` - (Optional) The list of labels (key/value pairs) to add to the job.

`Scheduling.maxFailuresPerHour` - (Optional) Maximum number of times per hour a driver may be restarted as a result of driver terminating with non-zero code before job is reported failed.

`MainPythonFileUri` - (Required) The HCFS URI of the main Python file to use as the driver. Must be a .py file.

`Args` - (Optional) The arguments to pass to the driver.

`PythonFileUris` - (Optional) HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.

`JarFileUris` - (Optional) HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks.

`FileUris` - (Optional) HCFS URIs of files to be copied to the working directory of Python drivers and distributed tasks. Useful for naively parallel tasks.

`ArchiveUris` - (Optional) HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

`Properties` - (Optional) A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in `/etc/spark/conf/spark-defaults.conf` and classes in user code.

`LoggingConfig.driverLogLevels` - (Optional) The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

`MainClass` - (Optional) The class containing the main method of the driver. Must be in a
provided jar or jar that is already on the classpath. Conflicts with `MainJarFileUri`.

`MainJarFileUri` - (Optional) The HCFS URI of jar file containing
the driver jar. Conflicts with `MainClass`.

`Args` - (Optional) The arguments to pass to the driver.

`JarFileUris` - (Optional) HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.

`FileUris` - (Optional) HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks. Useful for naively parallel tasks.

`ArchiveUris` - (Optional) HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

`Properties` - (Optional) A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in `/etc/spark/conf/spark-defaults.conf` and classes in user code.

`LoggingConfig.driverLogLevels` - (Optional) The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

`MainClass` - (Optional) The name of the driver's main class. The jar file containing the class must be in the default CLASSPATH or specified in `JarFileUris`. Conflicts with `MainJarFileUri`.

`MainJarFileUri` - (Optional) The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `MainClass`.

`Args` - (Optional) The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.

`JarFileUris` - (Optional) HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.

`FileUris` - (Optional) HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.

`ArchiveUris` - (Optional) HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

`Properties` - (Optional) A mapping of property names to values, used to configure Hadoop. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in `/etc/hadoop/conf/*-site` and classes in user code..

`LoggingConfig.driverLogLevels` - (Optional) The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

`QueryList` - (Optional) The list of Hive queries or statements to execute as part of the job.
Conflicts with `QueryFileUri`.

`QueryFileUri` - (Optional) HCFS URI of file containing Hive script to execute as the job.
Conflicts with `QueryList`.

`ContinueOnFailure` - (Optional) Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.

`ScriptVariables` - (Optional) Mapping of query variable names to values (equivalent to the Hive command: `SET name="value";`).

`Properties` - (Optional)  A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in `/etc/hadoop/conf/*-site.xml`, `/etc/hive/conf/hive-site.xml`, and classes in user code..

`JarFileUris` - (Optional) HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs.

`QueryList` - (Optional) The list of Hive queries or statements to execute as part of the job.
Conflicts with `QueryFileUri`.

`QueryFileUri` - (Optional) HCFS URI of file containing Hive script to execute as the job.
Conflicts with `QueryList`.

`ContinueOnFailure` - (Optional) Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.

`ScriptVariables` - (Optional) Mapping of query variable names to values (equivalent to the Pig command: `name=[value]`).

`Properties` - (Optional) A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in `/etc/hadoop/conf/*-site.xml`, `/etc/pig/conf/pig.properties`, and classes in user code.

`JarFileUris` - (Optional) HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs.

`LoggingConfig.driverLogLevels` - (Optional) The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

`QueryList` - (Optional) The list of SQL queries or statements to execute as part of the job.
Conflicts with `QueryFileUri`.

`QueryFileUri` - (Optional) The HCFS URI of the script that contains SQL queries.
Conflicts with `QueryList`.

`ScriptVariables` - (Optional) Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).

`Properties` - (Optional) A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.

`JarFileUris` - (Optional) HCFS URIs of jar files to be added to the Spark CLASSPATH.

`LoggingConfig.driverLogLevels` - (Optional) The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.


## Return Values

### Fn::GetAtt

`Reference.0.clusterUuid` - A cluster UUID generated by the Cloud Dataproc service when the job is submitted.

`Status.0.state` - A state message specifying the overall job state.

`Status.0.details` - Optional job state details, such as an error description if the state is ERROR.

`Status.0.stateStartTime` - The time when this state was entered.

`Status.0.substate` - Additional state information, which includes status reported by the agent.

`DriverOutputResourceUri` - A URI pointing to the location of the stdout of the job's driver program.

`DriverControlsFilesUri` - If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.

## See Also

* [google_dataproc_job](https://www.terraform.io/docs/providers/google/r/dataproc_job.html) in the _Terraform Provider Documentation_