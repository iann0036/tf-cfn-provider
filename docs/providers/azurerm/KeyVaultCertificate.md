# Terraform::AzureRM::KeyVaultCertificate

Manages a Key Vault Certificate.

## Properties

`VaultUri` - (Required) Specifies the URI used to access the Key Vault instance, available on the `Terraform::AzureRM::KeyVault` resource.

`Certificate` - (Optional) A `Certificate` block as defined below, used to Import an existing certificate.

`CertificatePolicy` - (Required) A `CertificatePolicy` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### SubjectAlternativeNames Properties

`DnsNames` - (Optional) A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.

`Emails` - (Optional) A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.

`Upns` - (Optional) A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.

### LifetimeAction Properties

`Action` - (Required) A `Action` block as defined below.

`Trigger` - (Required) A `Trigger` block as defined below.

### IssuerParameters Properties

`Name` - (Required) The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

### SecretProperties Properties

`ContentType` - (Required) The Content-Type of the Certificate, such as `application/x-pkcs12` for a PFX or `application/x-pem-file` for a PEM. Changing this forces a new resource to be created.

### Certificate Properties

`Contents` - (Required) The base64-encoded certificate contents. Changing this forces a new resource to be created.

`Password` - (Optional) The password associated with the certificate. Changing this forces a new resource to be created.

### X509CertificateProperties Properties

`ExtendedKeyUsage` - (Optional) A list of Extended/Enhanced Key Usages. Changing this forces a new resource to be created.

`KeyUsage` - (Required) A list of uses associated with this Key. Possible values include `cRLSign`, `dataEncipherment`, `decipherOnly`, `digitalSignature`, `encipherOnly`, `keyAgreement`, `keyCertSign`, `keyEncipherment` and `nonRepudiation` and are case-sensitive. Changing this forces a new resource to be created.

`Subject` - (Required) The Certificate's Subject. Changing this forces a new resource to be created.

`SubjectAlternativeNames` - (Optional) A `SubjectAlternativeNames` block as defined below.

`ValidityInMonths` - (Required) The Certificates Validity Period in Months. Changing this forces a new resource to be created.

### Action Properties

`ActionType` - (Required) The Type of action to be performed when the lifetime trigger is triggerec. Possible values include `AutoRenew` and `EmailContacts`. Changing this forces a new resource to be created.

### Trigger Properties

`DaysBeforeExpiry` - (Optional) The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with `LifetimePercentage`.

`LifetimePercentage` - (Optional) The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with `DaysBeforeExpiry`.

### KeyProperties Properties

`Exportable` - (Required) Is this Certificate Exportable? Changing this forces a new resource to be created.

`KeySize` - (Required) The size of the Key used in the Certificate. Possible values include `2048` and `4096`. Changing this forces a new resource to be created.

`KeyType` - (Required) Specifies the Type of Key, such as `RSA`. Changing this forces a new resource to be created.

`ReuseKey` - (Required) Is the key reusable? Changing this forces a new resource to be created.

### CertificatePolicy Properties

`IssuerParameters` - (Required) A `IssuerParameters` block as defined below.

`KeyProperties` - (Required) A `KeyProperties` block as defined below.

`LifetimeAction` - (Optional) A `LifetimeAction` block as defined below.

`SecretProperties` - (Required) A `SecretProperties` block as defined below.

`X509CertificateProperties` - (Optional) A `X509CertificateProperties` block as defined below.


## Return Values

### Fn::GetAtt

`Id` - The Key Vault Certificate ID.

`SecretId` - The ID of the associated Key Vault Secret.

`Version` - The current version of the Key Vault Certificate.

`CertificateData` - The raw Key Vault Certificate.

`Thumbprint` - The X509 Thumbprint of the Key Vault Certificate returned as hex string.

## See Also

* [azurerm_key_vault_certificate](https://www.terraform.io/docs/providers/azurerm/r/key_vault_certificate.html) in the _Terraform Provider Documentation_