# Terraform::FlexibleEngine::MrsJobV1

Manages resource job within FlexibleEngine MRS.

## Properties

`JobType` - (Required) Job type 1: MapReduce 2: Spark 3: Hive Script 4: HiveQL
(not supported currently) 5: DistCp, importing and exporting data.  6: Spark
Script 7: Spark SQL, submitting Spark SQL statements. (not supported in this
APIcurrently) NOTE: Spark and Hive jobs can be added to only clusters including
Spark and Hive components.

`JobName` - (Required) Job name Contains only 1 to 64 letters, digits, hyphens
(-), and underscores (_). NOTE: Identical job names are allowed but not recommended.

`ClusterId` - (Required) Cluster ID.

`JarPath` - (Required) Path of the .jar package or .sql file for program
execution The parameter must meet the following requirements: Contains a maximum
of 1023 characters, excluding special characters such as ;|&><'$. The address
cannot be empty or full of spaces. Starts with / or s3a://. Spark Script must
end with .sql; while MapReduce and Spark Jar must end with .jar. sql and jar
are case-insensitive.

`Arguments` - (Optional) Key parameter for program execution. The parameter
is specified by the function of the user's program. MRS is only responsible
for loading the parameter. The parameter contains a maximum of 2047 characters,
excluding special characters such as ;|&>'<$, and can be empty.

`Input` - (Optional) Path for inputting data, which must start with / or s3a://.
A correct OBS path is required. The parameter contains a maximum of 1023 characters,
excluding special characters such as ;|&>'<$, and can be empty.

`Output` - (Optional) Path for outputting data, which must start with / or
s3a://. A correct OBS path is required. If the path does not exist, the system
automatically creates it. The parameter contains a maximum of 1023 characters,
excluding special characters such as ;|&>'<$, and can be empty.

`JobLog` - (Optional) Path for storing job logs that record job running status.
This path must start with / or s3a://. A correct OBS path is required. The parameter
contains a maximum of 1023 characters, excluding special characters such as
;|&>'<$, and can be empty.

`HiveScriptPath` - (Optional) SQL program path This parameter is needed
by Spark Script and Hive Script jobs only and must meet the following requirements:
Contains a maximum of 1023 characters, excluding special characters such as
;|&><'$. The address cannot be empty or full of spaces. Starts with / or s3a://.
Ends with .sql. sql is case-insensitive.

`IsProtected` - (Optional) Whether a job is protected true false The current
version does not support this function.

`IsPublic` - (Optional) Whether a job is public true false The current version
does not support this function.


## Return Values

### Fn::GetAtt

`JobType` - See Properties above.

`JobName` - See Properties above.

`ClusterId` - See Properties above.

`JarPath` - See Properties above.

`Arguments` - See Properties above.

`Input` - See Properties above.

`Output` - See Properties above.

`JobLog` - See Properties above.

`HiveScriptPath` - See Properties above.

`IsProtected` - See Properties above.

`IsPublic` - See Properties above.

## See Also

* [flexibleengine_mrs_job_v1](https://www.terraform.io/docs/providers/flexibleengine/r/mrs_job_v1.html) in the _Terraform Provider Documentation_