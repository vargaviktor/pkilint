from pkilint import loader
from pkilint.cabf import serverauth
from pkilint.cabf.serverauth.serverauth_constants import CertificateType

_TEST_CASES = {
    CertificateType.DV_FINAL_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIFpzCCBI+gAwIBAgIKd3d3d3d3d3d3dzANBgkqhkiG9w0BAQsFADBFMQswCQYD
VQQGEwJVUzETMBEGA1UEChMKQ2VydHMgUiBVczEhMB8GA1UEAxMYQ2VydHMgUiBV
cyBJc3N1aW5nIENBIEcxMB4XDTIzMDYwMjAwMDAwMFoXDTI0MDYwMTIzNTk1OVow
ADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJjfM1nBO6c4jF2eL+PP
y+pQOjb+d6eYUk3CypR4j+bzV104d/LT12ukkEL3cR5YapINlZFfMnGxkxz12+AK
1tKo2m8agDlXTeWvl1hS0axCGOGZL16wvR078oxejK2nmfWlUdFhSmWpFyOeuxCG
tTaeqjOHjABvKOwqXNlRTlw0CCQ6j2GFqLGPbJ5yfqGLiDGBB+iVdS8oCQ6RtPks
HH/FNBVeWbwhHE6jrH+yTHbkxJzZwc5W86YHH0PwmsXdCT9gdyfYD1UFm4Ly9iBA
CgUEYbnXEeYmiZV40yDFbwkZ2JvhmtjN4zJpEc4/DP40wMolSZ1F0Gd+2XjJDjSV
iDkCAwEAAaOCAtwwggLYMB8GA1UdIwQYMBaAFGpOUL+YaJ1beyB11FkBeUhmkjIG
MB0GA1UdEQEB/wQTMBGCD3d3dy5leGFtcGxlLmNvbTAOBgNVHQ8BAf8EBAMCB4Aw
HQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMDYGA1UdHwQvMC0wK6ApoCeG
JWh0dHA6Ly9jcmwuY2VydHNydXMuY29tL0lzc3VpbmdDQS5jcmwwEwYDVR0gBAww
CjAIBgZngQwBAgEwgYoGCCsGAQUFBwEBBH4wfDAdBggrBgEFBQcwAYIRb2NzcC5j
ZXJ0c3J1cy5jb20wJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmNlcnRzcnVzLmNv
bTA1BggrBgEFBQcwAoYpaHR0cDovL2NhY2VydHMuY2VydHNydXMuY29tL0lzc3Vp
bmdDQS5jcnQwDAYDVR0TAQH/BAIwADCCAX0GCisGAQQB1nkCBAIEggFtBIIBaQFn
AHcAdv+IPwq2+5VRwmHM9Ye6NLSkzbsp3GhCCp/mZ0xaOnQAAAGI+L2vAAAABAMA
SDBGAiEAiev929CATzEwc9gZ87Q7RJYzqZUyiyfuWi6Up0zIvJ4CIQCgOQbjHxVv
843QttJy7o5ptSP/K4pCA6EndDN4xKyvGAB1AEiw42vapkc0D+VqAvqdMOscUgHL
Vt0sgdm7v6s52IRzAAABiPi9rzIAAAQDAEYwRAIgeas2P/kiseEt9FcWV504hXDn
C4oEy8w3O5FeF40GjzcCID64kMdoTmBM3gT6ct/RtJWTPhQLITKtORQ/VUZesoMW
AHUAO1N3dT4tuYBOizBbBv5AO2fYT8P0x70ADS1yb+H61BcAAAGI+L2vLAAABAMA
RjBEAiA69JJVgg4dBqYhkMOf9UE+J0/R6Vlu1VC+mx4MFUiABQIgVGJ0QWCbpeXs
efEyRqLwo4trTnmwpnxs29XLOhSDBycwDQYJKoZIhvcNAQELBQADggEBAF339kVi
In6T3J5aYis8ivEGm7IYd875NtzqMfi2u23ne/5SECD/1hK/7OR9c8XuLNwlON+f
AywZl/dwfaDKfmn6xzyZf2ZBAL1YRDrTPjnsKDpY2qIvFJlgutIpnhlU+DSGReyN
5ooJnfPvK7mjMA4Gn0WTcJm2Q/UuVtL+F4cZzLCdNmekdtPZg+LGufz6qL7loBnI
+uGI0rKcojULqGEJv/xOZe7uHZ/fWXRmENn4AZk3z+rJgzxpkbMuneAuyla987b8
J57rdt1CZYvoJQ5SlobEXx4DGy1dkIev3kdHqL35PG7dfEKrx6fD8xlYnWOYSnqN
et6EZBCFe+ZNTp8=
-----END CERTIFICATE-----
    """,
    CertificateType.DV_PRE_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIFFjCCA/6gAwIBAgIIAfqjHGsLKR4wDQYJKoZIhvcNAQELBQAwgbQxCzAJBgNV
BAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMRow
GAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjEtMCsGA1UECxMkaHR0cDovL2NlcnRz
LmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMTMwMQYDVQQDEypHbyBEYWRkeSBTZWN1
cmUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwHhcNMjMwODAxMTgzOTAyWhcN
MjQwOTAxMTgzOTAyWjATMREwDwYDVQQDEwhsb2NpLmNlbzCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAO6TUJeRi3dxO+aQUgAi37UDxYd2OEvwa3b7TDqX
ERGdKHww8YONMzy+pFHmSi8opws06prDqBlZ+MSvqB6rlCfA8Fc+xD+dz2WvTz/l
1vmtohNfDnp/JFJ5wVlmkvZyZ6qpKPE12QHYFjc6a2Epli4NdkpbFhHtOKKB8v6e
b96PTIY+R70cXWQfh64FOirzssJ+uDhkYdQhmIt1AjnYRRFIBYHfj1KtOjw6X+Bc
2ODkFyNsLOBl2Rxz4qZhDz1nsWy4XMPDKY+AY/V9P5QRAXXBjV8HnmM6R+wPgYbh
C/GFpE7xohZxDyXQ6yaNZtmR2wKyOyjRYaGYE4Wj3bcGVTcCAwEAAaOCAcowggHG
MAwGA1UdEwEB/wQCMAAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMA4G
A1UdDwEB/wQEAwIFoDA4BgNVHR8EMTAvMC2gK6AphidodHRwOi8vY3JsLmdvZGFk
ZHkuY29tL2dkaWcyczEtNzY5Mi5jcmwwXQYDVR0gBFYwVDBIBgtghkgBhv1tAQcX
ATA5MDcGCCsGAQUFBwIBFitodHRwOi8vY2VydGlmaWNhdGVzLmdvZGFkZHkuY29t
L3JlcG9zaXRvcnkvMAgGBmeBDAECATB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUH
MAGGGGh0dHA6Ly9vY3NwLmdvZGFkZHkuY29tLzBABggrBgEFBQcwAoY0aHR0cDov
L2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5L2dkaWcyLmNydDAf
BgNVHSMEGDAWgBRAwr0njsw0gzCiM9f7bLPwtCyAzjAhBgNVHREEGjAYgghsb2Np
LmNlb4IMd3d3LmxvY2kuY2VvMB0GA1UdDgQWBBTG7yvEd2P4KQs3+Q1f8d2QkUnr
nDATBgorBgEEAdZ5AgQDAQH/BAIFADANBgkqhkiG9w0BAQsFAAOCAQEASjpifdl0
L1PHOTMv2ZqU7NIqpfwLyZ91/uMj4H1a38d8dLggjYAmQSIkNKMt4rm/46AmoEuu
twAjyKT5KD7cNtLHaBHroU5FnFtgHcbx5o0nXJ2r1an71W10MVpDMvwJevvJkgvn
/WIvsk6lR66AloMNS4gy23qViUWpDq7ok2gs0DVz8U4pslAD6c9CE4Maz9KbevdE
9Z04JPGXPcRAU7lSGetVe7sjBOXvH5f0fEt0LV3oqBfMB211smJNfcQHhjfZA/45
KXAJ4vfhHsghBg5dX+Hcsz0Ldl+IEolDXT1oBmIdr42MBtI+UG3MHC6cAD3ZhOrv
LiQkK3Kz1414/Q==
-----END CERTIFICATE-----
    """,
    CertificateType.EV_FINAL_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIHZTCCBU2gAwIBAgIMS9Kjc1CWWKwCO6fGMA0GCSqGSIb3DQEBCwUAMEUxCzAJ
BgNVBAYTAlVTMRMwEQYDVQQKEwpDZXJ0cyBSIFVzMSEwHwYDVQQDExhDZXJ0cyBS
IFVzIElzc3VpbmcgQ0EgRzEwHhcNMjIwODE4MDgwNjI3WhcNMjMwOTE5MDgwNjI2
WjCBkzEdMBsGA1UEDwwUUHJpdmF0ZSBPcmdhbml6YXRpb24xCjAIBgNVBAUTATEx
EzARBgsrBgEEAYI3PAIBAxMCWloxCzAJBgNVBAYTAkZSMQ4wDAYDVQQIEwVQYXJp
czEOMAwGA1UEBxMFUGFyaXMxEjAQBgNVBAoMCUxlIEJhbnF1ZTEQMA4GA1UEYRMH
VkFURlItMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAO9nVDw4uupr
zYf8r/JZLnmH0Q3FGQbCXgD9OAp13ilLJwt0R5NEZjPnqpPLgnbx8gln4lQWx7M3
wORBdr+KjrQNhBasC6kLDmqiz4edUdlLgVuv9aCw3bZv1Z/uWx5RyEgQbUC/pBw4
y3qjMvZ2dj58JNEqmtEjsGkblFF4Mh1Rovj0kyX75eeJcj/x0VQAN4x8KHWYpv1C
wEeBhcuPu75QUb+8HOEEvDfQltzzx0a1/H0ow/4I0JLglCOUMLwX8QAWUwoCvZAC
k6RnW1o+QlScV8AZ13qtmHJljv/rhQhOTF/XGZ4NaNHaCEL/WPwOlh5FKrWIoH9M
oneECVKsCYsCAwEAAaOCAwQwggMAMA4GA1UdDwEB/wQEAwIHgDBrBggrBgEFBQcB
AQRfMF0wJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmNlcnRzcnVzLmNvbTA1Bggr
BgEFBQcwAoYpaHR0cDovL2NhY2VydHMuY2VydHNydXMuY29tL0lzc3VpbmdDQS5j
cnQwSAYDVR0gBEEwPzA9BgVngQwBATA0MDIGCCsGAQUFBwIBFiZodHRwczovL2Nl
cnRzcnVzLmNvbS9jYXJ0ZS1ibGFuY2hlLnBkZjAMBgNVHRMBAf8EAjAAMBcGBWeB
DAMBBA4wDBMDVkFUEwJGUgwBMTA2BgNVHR8ELzAtMCugKaAnhiVodHRwOi8vY3Js
LmNlcnRzcnVzLmNvbS9Jc3N1aW5nQ0EuY3JsMBYGA1UdEQQPMA2CC2V4YW1wbGUu
Y29tMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAfBgNVHSMEGDAWgBTs
vd5Zrf2bVRfncEwGV58hIrB3ADCCAX4GCisGAQQB1nkCBAIEggFuBIIBagFoAHYA
6D7Q2j71BjUy51covIlryQPTy9ERa+zraeF3fW0GvW4AAAGCr/1QKgAABAMARzBF
AiB7PuoyVpHriNj+ZMpDR064TwMTGUsuuFTGhLrrUg61sgIhAL/i8tJEha87kCyf
fy++W4L9t2A5ZESyVs3oL2M5//QUAHYAb1N2rDHwMRnYmQCkURX/dxUcEdkCwQAp
Bo2yCJo32RMAAAGCr/1N0wAABAMARzBFAiEA40CK73m7eKVnXTCK6f/iZW/UxNoP
HZSE90nBWeQljfUCIANhPFauDSA/YeH2y2fu5k8Fo0gzmUdsbEm3BVgfpyu/AHYA
s3N3B+GEUPhjhtYFqdwRCUp5LbFnDAuH3PADDnk2pZoAAAGCr/1PRwAABAMARzBF
AiBYeQUv173xuZ8l8MCH+q4GzkQukTxJQUhtvaOX1ZO1tgIhAK3nUB4tyBJdrWCg
HsZUhNcxnWrkPFGInT6zhC+wqNvYMA0GCSqGSIb3DQEBCwUAA4ICAQA8OdWkhx+Y
i0Gd7uUIqdLay+n2DW8f8wFiLCOMltzBSMnaswWYUoKxi1yggB+VRdOE0iM+5txp
9cnZYb04nLNxs5Ly9MgB03Hyjk8wteQAJszjOYAc69S1c+WJLC1Uu8Qjsi1xYR/4
92vmrYQTQnAHouty8BwnAmLYqnxkOedbJpM4jwsJej59nOHQXcDB4VJikOOMgf8q
w6QuI2KDmFS1ojVlGhggugH8WsTEw5RFfAmyRkdwRYxuPdQmnEWhzYYCDbG2LzEY
t0U7VLE/M2OAqhds6zGG6ZSRM6RxVgkOSqQOx+EmV7RbG459jk4PycOAbd1NFukS
IphzxzrCHUEGw/Zn9jc+iAyKb1AheZahf9/vt6LTK+XGL3n3wpOufLPuNWgtYTqk
/dnsw1Tl6wyz6kG8BVjdg/bdBDpjGM8yBGU4kJapN4BaWbPBHmbC6TspzukNpGDT
WWPYrZRm+kqaykycauRRbE3NNDYPibf5StwHk2utSbeBwiy6lfELMh30/2cBLOzl
iCX7GnE4J1FEhYiUkGbmQXtIkeuecQgnxP9Ndq25ELKtZrhhrGlx2fpwVtx33dqS
cgd31N7xna/yxpE94tAK0WIJN7n0id0wsnzDCu7Q4dyjyovhB/1Vy4Myk1ZRkYOn
qj0RoAmDOU4cZGyTk1lMJmRek5pSOQ1Kzg==
-----END CERTIFICATE-----
    """,
    CertificateType.EV_PRE_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIICTCCBfGgAwIBAgIJJ1vvDlrQrL6XMA0GCSqGSIb3DQEBCwUAMIHTMQswCQYD
VQQGEwJFUzEWMBQGA1UECwwNQUMgQ0FNRVJGSVJNQTEbMBkGA1UECgwSQUMgQ2Ft
ZXJmaXJtYSBTLkEuMRIwEAYDVQQFEwlBODI3NDMyODcxSzBJBgNVBAcMQk1hZHJp
ZCAoc2VlIGN1cnJlbnQgYWRkcmVzcyBhdCBodHRwczovL3d3dy5jYW1lcmZpcm1h
LmNvbS9hZGRyZXNzKTEuMCwGA1UEAwwlQ2FtZXJmaXJtYSBDb3Jwb3JhdGUgU2Vy
dmVyIElJIC0gMjAxNTAeFw0xOTA5MjQwNjU5MDdaFw0yMTA5MjMwNjU5MDdaMIG2
MQ8wDQYDVQQHDAZNQURSSUQxEzARBgsrBgEEAYI3PAIBAxMCRVMxHTAbBgNVBA8M
FFByaXZhdGUgT3JnYW5pemF0aW9uMRIwEAYDVQQFEwlBODI3NDMyODcxETAPBgNV
BAsMCFNJU1RFTUFTMRswGQYDVQQKDBJBQyBDQU1FUkZJUk1BIFMuQS4xHjAcBgNV
BAMMFXNlY3VyZS5jYW1lcmZpcm1hLmNvbTELMAkGA1UEBhMCRVMwggEiMA0GCSqG
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDCCQOaFifDy54bvCALvRJB1QtepM4WCOg0
RforI+sV/gYwru40tJ/loIzqD66C11j4XlYOLxyjtdbV/etZ4ovH1keXinkm4ubR
BPeIZ+lW+52V+MTt7RBVVFo3g+bxYrwRUqZiPB+eEfVKjh6+Gvpd2nYUoVVmZwK2
XhxH4cCxb45j0vFjcEXKwv9eybP7+A0VFxxugPjPDTHj46s1teLUsCuxvYLA9lVG
HyfQEayM3tpWoEoVVBljGNiltcZHUBRJkdpxy1GTdaCyWMZjpZvAAf4pjor8x5G0
EuqyX9fTDnqGl0SEf0m9pmQs+ANt7fBXG+/ezLtl1LezM0AtyN69AgMBAAGjggL5
MIIC9TAMBgNVHRMBAf8EAjAAMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggr
BgEFBQcDAgYIKwYBBQUHAwEwHQYDVR0OBBYEFIswU4wh1tfB8sRmuV7tH4yYjjDB
MBMGCisGAQQB1nkCBAMBAf8EAgUAMIGBBggrBgEFBQcBAQR1MHMwSQYIKwYBBQUH
MAKGPWh0dHA6Ly93d3cuY2FtZXJmaXJtYS5jb20vY2VydHMvY2FtZXJmaXJtYV9j
c2VydmVyaWktMjAxNS5jcnQwJgYIKwYBBQUHMAGGGmh0dHA6Ly9vY3NwLmNhbWVy
ZmlybWEuY29tMIHiBgNVHSMEgdowgdeAFGPp8PBWAGhlsCFsDlzXGQidCDRloYG0
pIGxMIGuMQswCQYDVQQGEwJFVTFDMEEGA1UEBxM6TWFkcmlkIChzZWUgY3VycmVu
dCBhZGRyZXNzIGF0IHd3dy5jYW1lcmZpcm1hLmNvbS9hZGRyZXNzKTESMBAGA1UE
BRMJQTgyNzQzMjg3MRswGQYDVQQKExJBQyBDYW1lcmZpcm1hIFMuQS4xKTAnBgNV
BAMTIENoYW1iZXJzIG9mIENvbW1lcmNlIFJvb3QgLSAyMDA4gghiH/McSJuhNjCB
iQYDVR0fBIGBMH8wPaA7oDmGN2h0dHA6Ly9jcmwuY2FtZXJmaXJtYS5jb20vY2Ft
ZXJmaXJtYV9jc2VydmVyaWktMjAxNS5jcmwwPqA8oDqGOGh0dHA6Ly9jcmwxLmNh
bWVyZmlybWEuY29tL2NhbWVyZmlybWFfY3NlcnZlcmlpLTIwMTUuY3JsMDsGA1Ud
EQQ0MDKCGXNlY3VyZXRlc3QuY2FtZXJmaXJtYS5jb22CFXNlY3VyZS5jYW1lcmZp
cm1hLmNvbTBQBgNVHSAESTBHMDwGDSsGAQQBgYcuCg4CAQIwKzApBggrBgEFBQcC
ARYdaHR0cHM6Ly9wb2xpY3kuY2FtZXJmaXJtYS5jb20wBwYFZ4EMAQEwDQYJKoZI
hvcNAQELBQADggIBAEvPze5pCCUmxeGi8ZmcFGxU7SY/H1Cqhx0nn32kcq9DqTrX
9Neds/FFVusjtM5/q00FwkrlasK7BtfPSyrWoGKtW+oqc8uLeQpUa1DljT6WjX+4
v+UP0UtKyUX/UCX0V2kMaEPIjdY78XeU/2UIsiAx6X4vnvwhAqYqbWeTkzuBFEyx
6FFkh1bE5MbQuQzNyfZVRf7lwP6sLg1PRJp3/SgZzXYH1J5nfdOXa01aN088D7NW
SNRtcAUSiyDPltFg4Zlg9iAukJMzq/pM1K9bUYaedTB6omwR9cTgDFCTRO/RO473
xsWKbQQFoJ4CSTSWQQ+MY21gr77smaXwEQJxCU2jFS1/dBZbkUdRd55xVITrwV9r
zIXlVDv46o8SlAZWHjEiIt01/K1zzbsF9cFiRkeJ3vJk+QJoq2BjIxkxtUaNElar
zJlSOYWx0BTpswFbeWKsYOxf2RS/zQYLd+u9Wy9aPl/saBdg958IbHWAWYMU6V3E
fgOgtmU1hi980PR+mSmn5xsPRPJPkmzjiDVX+tuP7ZvtK7dKQQ1x9YvL9tNEngMF
6tz80zdK0RSObX5CwQeSWpbXBHzwcKFOeAtmSv0ZGQ3tn4JQt7KpNtX2ZfCg95iT
xUWSzYeNejYOncdpRsoC81z0NbQoGbdAgY0/i8B25GMA7OZoTjmwWVwLdxgg
-----END CERTIFICATE-----
    """,
    CertificateType.INTERNAL_CONSTRAINED_TLS_CA: """-----BEGIN CERTIFICATE-----
MIIH6DCCBdCgAwIBAgIQO0d/eogVxAXy2Bkifl6VDzANBgkqhkiG9w0BAQsFADCB
pjELMAkGA1UEBhMCR1IxDzANBgNVBAcTBkF0aGVuczFEMEIGA1UEChM7SGVsbGVu
aWMgQWNhZGVtaWMgYW5kIFJlc2VhcmNoIEluc3RpdHV0aW9ucyBDZXJ0LiBBdXRo
b3JpdHkxQDA+BgNVBAMTN0hlbGxlbmljIEFjYWRlbWljIGFuZCBSZXNlYXJjaCBJ
bnN0aXR1dGlvbnMgUm9vdENBIDIwMTUwHhcNMjAwMTIxMTIxNjIwWhcNMjgwMTE5
MTIxNjIwWjB2MQswCQYDVQQGEwJHUjE3MDUGA1UECgwuSGVsbGVuaWMgQWNhZGVt
aWMgYW5kIFJlc2VhcmNoIEluc3RpdHV0aW9ucyBDQTEuMCwGA1UEAwwlVW5pdmVy
c2l0eSBvZiBQYXRyYXMgVExTIFJTQSBTdWJDQSBSMTCCAiIwDQYJKoZIhvcNAQEB
BQADggIPADCCAgoCggIBAOwvhzGP5w63pMuzQDdqX80aOSZkqArNTUjiDg9TgRoZ
VznAdzBw+W2gBHbLq3nW7oWJjKxfZdjL12V4oaGjWKzoSlF8kbG1nWyke/ZpMrf1
nCBnrRAEV21hI3/WIFz0f7dLsyraD4qndetN3ccbpEQ6UJZf12IUHeu8wfS5aQFc
pij1PZZiiRo721SMNrFXyMrzXoa9VQbXQxMlEXNYDDBSHpB9rhMbLPvELeHJIQu6
L3nMS6FMRKyDdE5VoMDy/xD1AXsdZV8w0Jy0XD8aLH4tnMk+GOFjJQ0S3wsEROE2
c9ikWtHAMB0Pj239GfuOleR4F3nLjAL7rRaGVjqQ5rM7ZRVtjl34xU63C+ZwZse+
QoInmIAg1gN6YbRUAMPyGcH5yxqbqaILG9teN8medvCk5PdlNdbmk6WZWFvqn79W
bjxsIY0KC4wC1+/WtuTEeRBOvFJVY9+Vx4PI/a/r+oFtrHy78o0q/84gXCMRNaO7
xScK8jJac7sOpiA704lAjpaYFuS3cJub3iF2FwXJ3sA1IQxWmseNaPs93a0OhjwL
XcrOVv3bjfq5QChmDCYcLtq7XjGaKKr1HzX18QzSCovjRtetKjNeLRSxCllDAgpf
Yz7l08+pyBh25YLCva8QrNg2jiWkIVe/0uSNhzxgcL6pq+VdF6WJ3wgPKnumufNp
AgMBAAGjggI/MIICOzASBgNVHRMBAf8ECDAGAQH/AgEAMB8GA1UdIwQYMBaAFHEV
Z8jIyb11XXLQOBhqnfNxJFQLMG8GCCsGAQUFBwEBBGMwYTA8BggrBgEFBQcwAoYw
aHR0cDovL3JlcG8uaGFyaWNhLmdyL2NlcnRzL0hhcmljYVJvb3RDQTIwMTUuY3J0
MCEGCCsGAQUFBzABhhVodHRwOi8vb2NzcC5oYXJpY2EuZ3IwgekGA1UdHgSB4TCB
3qCBmzBBpD8wPTELMAkGA1UEBhMCR1IxDzANBgNVBAcMBlBhdHJhczEdMBsGA1UE
CgwUVW5pdmVyc2l0eSBvZiBQYXRyYXMwVqRUMFIxCzAJBgNVBAYTAkdSMRMwEQYD
VQQHDArOoM6sz4TPgc6xMS4wLAYDVQQKDCXOoM6xzr3Otc+AzrnPg8+Ezq7OvM65
zr8gzqDOsc+Ez4HPjs69oT4wDIIKdGVpd2VzdC5ncjAKhwgAAAAAAAAAADAihyAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADARBgNVHSAECjAIMAYGBFUd
IAAwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMEYGA1UdHwQ/MD0wO6A5
oDeGNWh0dHA6Ly9jcmx2MS5oYXJpY2EuZ3IvSGFyaWNhUm9vdENBMjAxNS9jcmx2
MS5kZXIuY3JsMB0GA1UdDgQWBBTqRm4pDlHhAMqziNgUQe0oL0lCBTAOBgNVHQ8B
Af8EBAMCAYYwDQYJKoZIhvcNAQELBQADggIBABQHGwBEM7EQ8PFdOmYqh8BT1vIt
ZAeg3BcJKgMcgEjchXwosEaIFM6zhF5AhEoeLeOVXGQqgUWgb+2CAlcwfxHS75nS
5tUrUidTHQ4gCKtZlfjylkt1MA/mVWVoSXpNXztg167f3qZLWI86oB6es86G7nEF
dOiradKYwTye8a3kR6mPr1N2PE59hbS9iJhV2v7fraI2RAswuqXYjaRf7zoNu4eN
OnREOdS/N1LhACUMdiwjIyVHOdWcNuI3gicmLDepO3uzPWeJLN+XR9pgRgUWFu61
t8gZm6ewd7fIMQlJAMjZjd/IaS/OI3ow7zRJs0gdsuoa0RAJwrlSpTGVkFDPO/f/
1LPeFSn3xb5uHyDsAAra+zneH/CApkaRn3POTNJjhnbJMWVW8Z76mtNEvpGlRepu
qPWEDVNLfJ1sha9/lNJyHW6LAbBQg84rrDlKNiVF/FHqlHVr/A6JknvjiqcSA+Pc
wz39nJ/YlZ4oq8DiiRKwkmooNTGPB4uiKGeHJeud3Er+QUB4ZlGjhAYATK5P6x6h
hdiZcTMw0bhitOgoh/8fnUyaSIA2FspD8IFJ7FBPryh13I/t3VaPCkfv8RnjuaFS
kAfRJ9wPLuge+CCbp6nL+lr/ac75Rzfmx9XeCVkBkEItpCoiaDp0JkbxyZr5wZJC
83qfYkjv1c1NhGF6
-----END CERTIFICATE-----
    """,
    CertificateType.INTERNAL_UNCONSTRAINED_TLS_CA: """-----BEGIN CERTIFICATE-----
MIIGCzCCA/OgAwIBAgIQC6LQHcvLd3borGUJesElQTANBgkqhkiG9w0BAQwFADCB
hTELMAkGA1UEBhMCR0IxGzAZBgNVBAgTEkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4G
A1UEBxMHU2FsZm9yZDEaMBgGA1UEChMRQ09NT0RPIENBIExpbWl0ZWQxKzApBgNV
BAMTIkNPTU9ETyBSU0EgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMTQwOTI1
MDAwMDAwWhcNMjkwOTI0MjM1OTU5WjCBkjELMAkGA1UEBhMCR0IxGzAZBgNVBAgT
EkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4GA1UEBxMHU2FsZm9yZDEaMBgGA1UEChMR
Q09NT0RPIENBIExpbWl0ZWQxODA2BgNVBAMTL0NPTU9ETyBSU0EgRG9tYWluIFZh
bGlkYXRpb24gU2VjdXJlIFNlcnZlciBDQSAyMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAu6tLGm5b8m2eTAtPlWDJzV8bcpcw8w/ttjVKAXWd9ObtFQ4T
tIjyVhHirwfhPCEoYLhePcwJW9SVwMIsj9Ox+HMD1LTm1gbelT9A3OprIxgzxu//
HH1hUryAK1ngv8Vrw+T5cmcOfMOGmqDWxykFCpQSi3UX3d0KZ53vcAdogXIBHIp6
6UuWiec9CN969AGX4mo8/9kKZvSaOxP6JXbMnlxVajvGposEPpI8iZAlXSEUTYIh
eUyzwuNwH8+nXBg7mwzhcoKD0BV8wRNyjcYfAOnP16vm0InwIEUvElOdqvisVUvN
WrusXglfS8/YZ5Bsj4Okjrrthv7ZUKDejwegdwIDAQABo4IBZjCCAWIwHwYDVR0j
BBgwFoAUu69+Aj36pvE8hI6t7jiY7NkyMtQwHQYDVR0OBBYEFNSw9P1PnEKkbNw9
Lu5bQRjJrQP2MA4GA1UdDwEB/wQEAwIBhjASBgNVHRMBAf8ECDAGAQH/AgEAMB0G
A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAbBgNVHSAEFDASMAYGBFUdIAAw
CAYGZ4EMAQIBMEwGA1UdHwRFMEMwQaA/oD2GO2h0dHA6Ly9jcmwuY29tb2RvY2Eu
Y29tL0NPTU9ET1JTQUNlcnRpZmljYXRpb25BdXRob3JpdHkuY3JsMHIGCCsGAQUF
BwEBBGYwZDA7BggrBgEFBQcwAoYvaHR0cDovL2NydC5jb21vZG9jYS5jb20vQ09N
T0RPUlNBQWRkVHJ1c3RDQS5jcnQwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLmNv
bW9kb2NhNC5jb20wDQYJKoZIhvcNAQEMBQADggIBABAXFDLLULq2T67ml0Ts3U/u
K1VCkUf7pl3eEzOuEP0fi96xs7NWVkV3yI1Mwy3lg21BiTxwlbNX5wbejsLIItTn
3vGd05nJ8/cz58uPmWghDdgIrxON3Jl57RrFHJ0oebUbBPE5m9O4ELYavy9Su8p1
9wyHraEFbVVzT8KDlJlDjNM62s2jbt+h8i0RqT0mc89XYxEjLYS6gWZMb2u7ITqI
XR/70gq2P5FCF7SiAialW1Bnso6TzTZzgr9G0fMoAeFqZynC+Bf3R+2llm+8CuG9
iym+q7cylcUCsGU+Nb1n2An9vjBYE1X1m1NbAW5Fx9KlK8bP0I4w/DGpFZbHl+fJ
ZGm9jL7qfJCjWBp/Sau7UAkfCDA2AWAOsiCaVCn2WDWadIdfb2JrSI+y3MUZremV
bMRtilVoZmUWjcF6d2u438kgscUf1nfZxA7NvRrpH4dFrAC13a6pYYHiTVlRdXCE
IvFAUyYdBCmqvpdccsKcsvrK9Tl0JXufmOtAmqP/Z6yCHzxORVjc8WDbH1eUNHWB
5AJfvNk6sAYJ5+9iWZpd8wEbnWVw/yZFTliDcpD1QOsWIdWKjBPSM0fof+mkQAzM
VSWsErokodPYflsJTHKqRxY3lGqroH0bakT2GdD8REw8IN4D3CJ5JaqpAYVWgc+9
7O7lc82QVOgklrnwCqD3
-----END CERTIFICATE-----
    """,
    CertificateType.IV_FINAL_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIILDCCBxSgAwIBAgIQV3cUGtqpvJiyHInpuoun6zANBgkqhkiG9w0BAQsFADB4
MQswCQYDVQQGEwJJTDEWMBQGA1UEChMNU3RhcnRDb20gTHRkLjEpMCcGA1UECxMg
U3RhcnRDb20gQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkxJjAkBgNVBAMTHVN0YXJ0
Q29tIENsYXNzIDIgSVYgU2VydmVyIENBMB4XDTE2MTIyMTA2NDIxNVoXDTE4MTIy
MTA2NDIxNVowgeExCzAJBgNVBAYTAlJVMRQwEgYDVQQIDAtNb3Njb3cgQ2l0eTEP
MA0GA1UEBwwGTW9zY293MREwDwYDVQQEDAhWYXJhbmtpbjF4MHYGA1UEKgxvQWxl
eGFuZGVyYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFh
YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFh
YWFhYWFhYWFhYWFhMR4wHAYDVQQDDBVvd25jbG91ZC5hbHBpbmEtdG0ucnUwggIi
MA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC8NpG02PqvBtTkqufxbss1yxnM
4Dn+72Okz9nOmC1zbCxOigv8vBTPjLUve+kRPbvOO45S2caxmVrdRIZ/7AB3oIDI
RDdQmjA6psHBjStab5SL8s5oz1DVTrtejaiNj8oBG6nU0R8lFcvCwBpY7aRMTQsp
p2UXED6mf1RC8ZSWKA7NXMDcqGcWMNWMPRVoTfOPF+2uxXEyTaOoHfg+2RxqYfOt
f40L83dJ0ZkPD9bwm7PVP8XeV5hwz9hOX24utlhfza1Ic81LeMjAt3CsTnVpIpJ4
uczv7rGlhBZvdU6vXRPo2tzWwGco45sgDflPl7ri19M13xmHlRsKufPjnCcRou2r
xLFwRrwo3i6ewkSKAgLcj/bwal6pbvOXmIxQ1KeszSsMgdF8FE4iEBxhFucselZa
qwJDA7R5FfOnqdALv0i2K6a0v9oSRNDFfx3EiI5WhRyV8Pn2uwygv4dH4Nqwa6sp
NfO00CO9EcBBHNfX6KwGbDMT3CQrjWy7lZwK9SZu8y2ttB/dFEOsb9qiZGPMF9Li
5+o9lgjxMTjVKnI8CHjK+F+13Nb1DtMsLPtZc09P455MPauYHHqF3E4rhSIDCycF
JI1aJIpyRPk73DImlUjq7OtzFTZ6/CNfpPJCp3TV6rMum0UINh3ceLU0SODRGjk8
GkfaL/WOFLStXULvkQIDAQABo4IDRjCCA0IwDgYDVR0PAQH/BAQDAgWgMB0GA1Ud
JQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDATAJBgNVHRMEAjAAMB0GA1UdDgQWBBQh
PTiEuJonHGdR2ZB/OSLfENuiKjAfBgNVHSMEGDAWgBSU3oVBKqXZRfZgLC5Mkwmm
LCN+PjBvBggrBgEFBQcBAQRjMGEwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLnN0
YXJ0c3NsLmNvbTA5BggrBgEFBQcwAoYtaHR0cDovL2FpYS5zdGFydHNzbC5jb20v
Y2VydHMvc2NhLnNlcnZlcjIuY3J0MDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly9j
cmwuc3RhcnRzc2wuY29tL3NjYS1zZXJ2ZXIyLmNybDAgBgNVHREEGTAXghVvd25j
bG91ZC5hbHBpbmEtdG0ucnUwIwYDVR0SBBwwGoYYaHR0cDovL3d3dy5zdGFydHNz
bC5jb20vMFEGA1UdIARKMEgwCAYGZ4EMAQIDMDwGCysGAQQBgbU3AQIFMC0wKwYI
KwYBBQUHAgEWH2h0dHBzOi8vd3d3LnN0YXJ0c3NsLmNvbS9wb2xpY3kwggF/Bgor
BgEEAdZ5AgQCBIIBbwSCAWsBaQB1AEGy3C6J5jzkrxunuym/aMbe5vnxzAR+MN/6
47O6JZJjAAABWSBQlv8AAAQDAEYwRAIgLKXFpYGfyM/sKi59fWO1EdsGEckrvxF8
X/AvUWKlmAACIBjD5t5WoyFZoyQxbz+TLeMuuVoj8GBc57+VtwDwpoB3AHcApLkJ
kLQYWBSHuxOizGdwCjw1mAT5G9+443fNDsgN3BAAAAFZIFCYNAAABAMASDBGAiEA
4CpIDb39zQIyeT709VCMjt/HQt75cXRvVq8m4XopaQgCIQCgOpt+fdn0leUdoGB8
oorakok4/k+o38a/PNLt/JCv7wB3ADS7atbD35wD7qikmf94kUhsnV5crJLQH3v9
G84Z20jvAAABWSBQk2wAAAQDAEgwRgIhANlDAHg6UzZeJExIT4gUlumwt21CL2xs
48iCZj1nXARrAiEA915IxaT/y3Wwz4LroeYqGKM75oGE13tRDHfGA6sBw2owDQYJ
KoZIhvcNAQELBQADggEBAIzbF+Pa7G8YVoKlpfRFPnr04apl92R2xeKkwBLM+ao7
LSglvNF7IclcDDI2ZRG+/vnWF8br+RKkUZrwfqqCTxl7mSlG6WbZ5+O8gGa3foSV
UNHkwnDMpfT/xlY+MOufV3HpkA2EBUauZ7P8MB7xuyaePnkbDdsIB1kV+dAxTsPh
OQMq91v5iKEtE35voGg5dH8MJ3cAYYTs3euKiP9M5PuGhFigU390jBiMVlRp4fxa
fzNkWCGp+Rmx+GvwUhS1alBMDnIlPtJTZoTftmMWHtvei3mbgOm/ZDYt293r9u7d
CV+kQLyUe7o3cBcRJqlG7QIOT/F1hRSDuJe8eb+lOI0=
-----END CERTIFICATE-----
    """,
    CertificateType.IV_PRE_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIGOTCCBSGgAwIBAgIQCT0AWCURBcSVOrd4s9KxJDANBgkqhkiG9w0BAQsFADBN
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E
aWdpQ2VydCBTSEEyIFNlY3VyZSBTZXJ2ZXIgQ0EwHhcNMjIwNjEzMDAwMDAwWhcN
MjMwNjEzMjM1OTU5WjBiMQswCQYDVQQGEwJVUzENMAsGA1UECBMEVXRhaDEXMBUG
A1UEBxMORWFnbGUgTW91bnRhaW4xEjAQBgNVBAoTCUJlbiBNb3JzZTEXMBUGA1UE
AxMOaW52ZXJ0ZWQuc3BhY2UwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoIC
AQDVD3qfDlXq71TsGve9HbXsPoa9sKCTYbbHozn+M0xVZ2ILEb0J8NCQg2d14Gl/
6nOH9bQBGNIGGQVh2YgrXnFgV+by6bv5t41+IqPVjEdbJqa0vQ4015f498Sf9Jo+
CrWoxBV+3/aBO/U6U4lUbxTw6jbUEbddWT3278Qcv6ckKiiq+LYXIo9g3NY5qUOz
mg0jmM+EziY7EpTk4Rux6JIMILANf7hv6GNumoutVlgiQyrf4nN6pSk7iStOUk1A
Nzj4Rqc1OAA/9G8CUinGwcwVkfETFHri3ALGVIu0KXefpMiOkIRGAIxiO/kvKQ8H
KmWB8tBhP23F4hgzDs+KXIz3CfVMNrHF8T6TlKeQarrcFjQctdWGhzJj2ZiPb7mO
5yA09cYZdWJOXXlXYbIU03EmMP31p83s8aYG9CcFstEd7KIGtlJ3iAywfeLUqSyM
dCCGcvBTnplcUKd22twSflFZ45F1fAv7QsgJaPVVNC9oienKhB6OrGg4WUvKfbmG
EIZIAhLKkl9ZAZ/7xQx1tQfSWoLQ5bcTBos1FyGO5ko5lpH5psdsvm4zGC8Tav8K
9szo9tSsRSqlbKZF/PRxvZ1IhAhV1vNIlWqi/AEc5IfWouuGewer1hwvEYC3v3B5
9I7sr6HQ3/4uj9X/8Li7bMjA9M57c8/RBOFpIvLBgy5RAwIDAQABo4IB/jCCAfow
HwYDVR0jBBgwFoAUD4BhHIIxYdUvKOeNRji0LOHG2eIwHQYDVR0OBBYEFJICMXE3
HBk8KIjpLWGpmdtN51VbMBkGA1UdEQQSMBCCDmludmVydGVkLnNwYWNlMA4GA1Ud
DwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwgY0GA1Ud
HwSBhTCBgjA/oD2gO4Y5aHR0cDovL2NybDMuZGlnaWNlcnQuY29tL0RpZ2ljZXJ0
U0hBMlNlY3VyZVNlcnZlckNBLTEuY3JsMD+gPaA7hjlodHRwOi8vY3JsNC5kaWdp
Y2VydC5jb20vRGlnaWNlcnRTSEEyU2VjdXJlU2VydmVyQ0EtMS5jcmwwPgYDVR0g
BDcwNTAzBgZngQwBAgMwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2Vy
dC5jb20vQ1BTMH4GCCsGAQUFBwEBBHIwcDAkBggrBgEFBQcwAYYYaHR0cDovL29j
c3AuZGlnaWNlcnQuY29tMEgGCCsGAQUFBzAChjxodHRwOi8vY2FjZXJ0cy5kaWdp
Y2VydC5jb20vRGlnaUNlcnRTSEEyU2VjdXJlU2VydmVyQ0EtMi5jcnQwCQYDVR0T
BAIwADATBgorBgEEAdZ5AgQDAQH/BAIFADANBgkqhkiG9w0BAQsFAAOCAQEAn8TR
OaGEC0/8YfmBuie6lR9ZMQIPBzCW7WF5nFoY7i5Wx6ZlDaRXACc7+IL4P6GGOjYQ
IIBpz7orB41DU58vzsT+SCL5oTXYzFTQLSGi74K89RL12yzamGbsNABqCQTCKW/e
86yY7GskLKz1Jfo0jJkt0iNc4dARC95CPIQvgiCJGXyxYKQQzWXz7NADbx1M050l
ujIBYs2oZ2Q4LTWlsOjwGykEcfdE4lang134vw1Wsdl4pqA4ifuukiq2ZZbLU7gH
bRM2ixptcf+qlKEoBGzguDnLANjG00vQrGKZ0+f7Wt3Gm5MLPL9izbSYYP4e80df
9VWH+jOimD/Tw4JLRQ==
-----END CERTIFICATE-----
    """,
    CertificateType.NON_TLS_CA: """-----BEGIN CERTIFICATE-----
MIIEsDCCBFagAwIBAgIUOZ3slKUGXk92D1qRTpltfNEfd80wCgYIKoZIzj0EAwIw
QDELMAkGA1UEBhMCVVMxHzAdBgNVBAoMFkZvbyBJbmR1c3RyaWVzIExpbWl0ZWQx
EDAOBgNVBAMMB1Jvb3QgQ0EwHhcNMjMwNTAxMDAwMDAwWhcNMjMxMDI4MjM1OTU5
WjBIMQswCQYDVQQGEwJVUzEfMB0GA1UECgwWRm9vIEluZHVzdHJpZXMgTGltaXRl
ZDEYMBYGA1UEAwwPSW50ZXJtZWRpYXRlIENBMIICIjANBgkqhkiG9w0BAQEFAAOC
Ag8AMIICCgKCAgEAs4tJYOY75qjbqJqCl47x9jJE5Vd9jPWGFtXKV1nUnMjZNsM4
qjy5sRHBSX5bUa9pLyYR5on3Z1SAwLD0w2VPQ6+F/oyK1zTgQqitoF/XZQjgC6D3
VsNEO76DPqfRANT7Nn7r1gvbZIZ3/H3rlCRNrRr47tHGWBLAPnxz9/NY6UG8ZkWP
97uXpJqYoRgH4CwaO5rTOlc64YDh/0Mq5VgMycq/q2AvMlvNoJfoe8em1040qH1g
ikP+suT/8fS452hqmEddtRpuvQgXKldBd0kkiyFVyLkG4NVA6Mso9MAK3J/kdYoa
w2SrOeThVSiYVEQVP+7GrUxTSLLjj/VQ9fpYM5eTNzDICIG/Ee7o/jhtW1EoSamD
mUOr89lyIHaXuOwkEaJhnVXKBCM8WiztxvKG2CnQ6Dcge3ZSmqJEhyEmjcAVC7ew
fnMxOnE+WJW6rzrf+mA5WMVn+FzyWx2AondWow0aUKHkaY7amhIrsKp6YPfNImyx
Flz8+cqDCmBswPsUh/JJ5eDHHIhibFcSgIHedsEjhLbUSLZ/DnEjru90qIWWA3R1
VIPykKfeZkZeInsrFzGPikkFKwFF+6KDdyvCmltYEqzO46tigXAZ5UgH8oiXEre4
8wO6X+FH+cLzQ0q3A8HZRnNDgqCjU/Tgy76iaku/Ic6eteedR1fX3gJ/IOUCAwEA
AaOCAVkwggFVMBIGA1UdEwEB/wQIMAYBAf8CAQAwDgYDVR0PAQH/BAQDAgGGMB8G
A1UdIwQYMBaAFFtwp5gX95/2N9L349xEbCEJ17vUMB0GA1UdDgQWBBTWRAAyfKgN
/6xPa2buta6bLMU4VDARBgNVHSAECjAIMAYGBFUdIAAwOgYDVR0fBDMwMTAvoC2g
K4YpaHR0cDovL2NybC5jYS5leGFtcGxlLmNvbS9yb290X2NhX2NybC5jcmwwgYAG
CCsGAQUFBwEBBHQwcjA4BggrBgEFBQcwAoYsaHR0cDovL3JlcG9zaXRvcnkuY2Eu
ZXhhbXBsZS5jb20vcm9vdF9jYS5kZXIwNgYIKwYBBQUHMAGGKmh0dHA6Ly9yZXBv
c2l0b3J5LmNhLmV4YW1wbGUuY29tL29jc3AuYXNweDAdBgNVHSUEFjAUBggrBgEF
BQcDBAYIKwYBBQUHAwIwCgYIKoZIzj0EAwIDSAAwRQIhAOCvgM8hveUjvBvEdhJZ
9P1re/mqou9d6o9f7XcubP29AiAMA1aqNACzlZdAvhHk1o2fjCYYodSWbLbAd5cN
AzPftw==
-----END CERTIFICATE-----
    """,
    CertificateType.OCSP_RESPONDER: """-----BEGIN CERTIFICATE-----
MIIFvTCCA6WgAwIBAgIRCAsao2gJ+krAAAAAAAAAAAswDQYJKoZIhvcNAQELBQAw
UjELMAkGA1UEBhMCU0sxEzARBgNVBAcTCkJyYXRpc2xhdmExEzARBgNVBAoTCkRp
c2lnIGEucy4xGTAXBgNVBAMTEENBIERpc2lnIFJvb3QgUjIwHhcNMjEwMzE2MTM0
OTM0WhcNMjQwMzE1MTM0OTM0WjCBhzELMAkGA1UEBhMCU0sxEzARBgNVBAcMCkJy
YXRpc2xhdmExFzAVBgNVBAUTDk5UUlNLLTM1OTc1OTQ2MRMwEQYDVQQKDApEaXNp
ZyBhLnMuMRYwFAYDVQQLDA1SZXNwb25kZXIgMV8zMR0wGwYDVQQDDBRPQ1NQIFJv
b3RDQSBSMiBEaXNpZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMBc
xfJ8FAlAUjzpXEZUJyKRdcRr1HlwS1wlGQncEHNW/vzeqxVIJb7wcjbBVG80fhUW
KgL2lm4LVnETGtQWpk2pvQahPwg8CyKsDTXlMX1n8FRGMiqh7dTFsL7xoT/CGPyR
Ha7sL4Z6qs4WsYV9F79/py5FGOh6RNZ0tgruSAmP/FM4bNcmndvfvMdP48M5oeQs
9729vhjYY70MXWBROj4c5nGYs1RY4wbh9cM5eLu/0RkrHhbItiGblvKgTdoLeAkv
cnzWfREGBM4nN1cwcTIjb3NHcvAfZH2c8laVM8ebsv3mKs9lbgg0ze3kevw5fljA
QCecyMQj+HoBxyDWW08CAwEAAaOCAVYwggFSMB0GA1UdDgQWBBSOJuTCmaPEshK5
f98ENRMnzhSVYDAfBgNVHSMEGDAWgBS1mfivsJT14yDWCq3OTlakLm5C7TALBgNV
HQ8EBAMCB4AwdQYDVR0fBG4wbDA0oDKgMIYuaHR0cDovL2NkcDEuZGlzaWcuc2sv
cm9vdGNhcjIvY3JsL3Jvb3RjYXIyLmNybDA0oDKgMIYuaHR0cDovL2NkcDIuZGlz
aWcuc2svcm9vdGNhcjIvY3JsL3Jvb3RjYXIyLmNybDATBgNVHSUEDDAKBggrBgEF
BQcDCTAZBgNVHSAEEjAQMA4GDCuBHpGT5goAAAABATBLBggrBgEFBQcBAQQ/MD0w
OwYIKwYBBQUHMAKGL2h0dHA6Ly9jZHAxLmRpc2lnLnNrL3Jvb3RjYXIyL2NlcnQv
cm9vdGNhcjIuZGVyMA8GCSsGAQUFBzABBQQCBQAwDQYJKoZIhvcNAQELBQADggIB
AF86AKzHhmFB/dpKFBo++AWviWmJ4jF1VpEf+kwil11ZRp4Bx9Akivp9g0Wiz1hY
4katUeqkbtPw1Xasv84Zyr8vmHnE3VObDV4Nm3pT1USksH+WIcJ/tf5+Dyi+YFB+
ECshShycLEXtTgYD0kXbK6FFx2fKFZzhSnpZCGtCcT8PvdBH30I/Kcm+JU7DFv9Y
PyehNlVD2Tv+TWY2BcdDeJYkqYs99n5fDa7VDeoRioO5QYE5MhgJYidJWKTjjAAV
n/kmG8yNYvvtLl+GeXirsCWFXFB0YeN7vn21Wb48E0x18YW3vLOT017RPfUEma7Y
ZV/kYatlX2xa3eyPvMz7GCYmPWeyndCop5H72X3P/gagp4QzLbndrVssK3swBbHG
x5jmwiz5A0fgB8WKDSRoj8wGeu6xPR7+Au7HOEiGzxexoyLgKP26/s+jst5xRVet
s2K+P5ya9fmAi9Bp7S5W0F434gJs2P3VH67TYOCFSCgDhCURh8DAxoORS8CWoyDd
UyQG7lOx407drFL/fqwVb+iFWJeRqqlafgYDgraJsbyvWbDJu+XvjmUmSpXotHO0
cJjYT3h+Atyp7nA2mQ8R1xQp8ylZ4tbekXNYZ/cMoU2CL6OKG78Ia2Mhlnc0DUTI
XBrupgnLhLFolrX7xr0CpOkcj4Qb0MY7hVDI4b8Neb/O
-----END CERTIFICATE-----
    """,
    CertificateType.OV_FINAL_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIGrTCCBZWgAwIBAgIDAlRTMA0GCSqGSIb3DQEBBQUAMIGMMQswCQYDVQQGEwJJ
TDEWMBQGA1UEChMNU3RhcnRDb20gTHRkLjErMCkGA1UECxMiU2VjdXJlIERpZ2l0
YWwgQ2VydGlmaWNhdGUgU2lnbmluZzE4MDYGA1UEAxMvU3RhcnRDb20gQ2xhc3Mg
MiBQcmltYXJ5IEludGVybWVkaWF0ZSBTZXJ2ZXIgQ0EwHhcNMTQwNzE3MTg1ODA2
WhcNMTYwNzE3MDg1MTE4WjCBtDEZMBcGA1UEDRMQMjFObWFaeWtuNEkxeVpuNDEL
MAkGA1UEBhMCR0IxEjAQBgNVBAgTCUhhbXBzaGlyZTEWMBQGA1UEBxMNV2F0ZXJs
b292aWxsZTEbMBkGA1UEChMSTHVrZSBHcmFuZ2VyLUJyb3duMRwwGgYDVQQDExNz
ZWN1cmUtMS5sdWtlZ2IuY29tMSMwIQYJKoZIhvcNAQkBFhR3ZWJtYXN0ZXJAbHVr
ZWdiLmNvbTCCASAwDQYJKoZIhvcNAQEBBQADggENADCCAQgCggEBAM+Gmn1cn70z
u8KxBqg+xRjzAQTdejgOjo0QqvhkSYKmFp3Zrl5/m1PLuynamEcmiC4dZLO8fpY6
p9aH9vU/pzvTxdVhPGMF+bxkHXFl9cjoZEE1iIFrKiS73Z91T+o15TJ2Wot6tZJl
NLeIQl1BC9EALUNHVWA8DmAEXIgTx0JVFjEygbreqVbr22Z/MbrohxrMrZCGS6dt
1cG352dWQfcDswlhY7WwGXvFkciWW2qAoVMPmke1mkRTvZPj5M4MFxFRHf1sdOTs
Ks5XJ8yDmAgyLNV1qSf+ql5IyUaaKT/mAU2XSnDRXfjACyPLvvVwC8LywDOcxIs5
fj3GIzmamN0CAQGjggLuMIIC6jAJBgNVHRMEAjAAMAsGA1UdDwQEAwIDqDAdBgNV
HSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwEwHQYDVR0OBBYEFC5MPLrQI2dDrJZ3
if4Q1R1hwgAXMB8GA1UdIwQYMBaAFBHbI0X9VMxqcW+EigPXvvcBLyaGMCoGA1Ud
EQQjMCGCE3NlY3VyZS0xLmx1a2VnYi5jb22CCmx1a2VnYi5jb20wggFWBgNVHSAE
ggFNMIIBSTAIBgZngQwBAgIwggE7BgsrBgEEAYG1NwECAzCCASowLgYIKwYBBQUH
AgEWImh0dHA6Ly93d3cuc3RhcnRzc2wuY29tL3BvbGljeS5wZGYwgfcGCCsGAQUF
BwICMIHqMCcWIFN0YXJ0Q29tIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MAMCAQEa
gb5UaGlzIGNlcnRpZmljYXRlIHdhcyBpc3N1ZWQgYWNjb3JkaW5nIHRvIHRoZSBD
bGFzcyAyIFZhbGlkYXRpb24gcmVxdWlyZW1lbnRzIG9mIHRoZSBTdGFydENvbSBD
QSBwb2xpY3ksIHJlbGlhbmNlIG9ubHkgZm9yIHRoZSBpbnRlbmRlZCBwdXJwb3Nl
IGluIGNvbXBsaWFuY2Ugb2YgdGhlIHJlbHlpbmcgcGFydHkgb2JsaWdhdGlvbnMu
MDUGA1UdHwQuMCwwKqAooCaGJGh0dHA6Ly9jcmwuc3RhcnRzc2wuY29tL2NydDIt
Y3JsLmNybDCBjgYIKwYBBQUHAQEEgYEwfzA5BggrBgEFBQcwAYYtaHR0cDovL29j
c3Auc3RhcnRzc2wuY29tL3N1Yi9jbGFzczIvc2VydmVyL2NhMEIGCCsGAQUFBzAC
hjZodHRwOi8vYWlhLnN0YXJ0c3NsLmNvbS9jZXJ0cy9zdWIuY2xhc3MyLnNlcnZl
ci5jYS5jcnQwIwYDVR0SBBwwGoYYaHR0cDovL3d3dy5zdGFydHNzbC5jb20vMA0G
CSqGSIb3DQEBBQUAA4IBAQB+b3CkugXNnuO+1y8AThEIqJVOfdzV994DCYLOKMf7
g1d4xztQUd/3FiZDQFhRQojeXSlqu8bk4SSIVI/LyhgtstlWIVvqsBKPEr4W12PN
A3/IIhOIxt/oUJRfOsWKVpM4mhgWT2z7K5l0VWTpnD+NGU42Gqvxzfk6gu0gnhCJ
yj2f5bOLcMHMoC8f1a6NlpwlKMWDjXt6VroWr/IA8ijNo4bsyR8UE257SCohikTX
24/vr8vT4mizPH0/PfTpq8e0iGbptYGgdRlQHRXJquYdl/ARPAmxI4BN0kM2+aNr
ValY138U0Q7Rt8OllJyHFeIHk81HE6hBOP0sG43NzTsH
-----END CERTIFICATE-----
    """,
    CertificateType.OV_PRE_CERTIFICATE: """-----BEGIN CERTIFICATE-----
MIIE4zCCA8ugAwIBAgIQfh8NX3syTEqNBtw/a2NQKzANBgkqhkiG9w0BAQsFADBA
MQswCQYDVQQGEwJDTjERMA8GA1UECgwIVW5pVHJ1c3QxHjAcBgNVBAMMFVNIRUNB
IE9WIFNlcnZlciBDQSBHNTAeFw0yMzA0MTEwNzA5MjZaFw0yNDA0MTExNTU5NTla
MIGOMQswCQYDVQQGEwJDTjESMBAGA1UECAwJ6buR6b6Z5rGfMRIwEAYDVQQHDAnl
k4jlsJTmu6gxNjA0BgNVBAoMLeS4reWbveenu+WKqOmAmuS/oembhuWboum7kem+
meaxn+aciemZkOWFrOWPuDEfMB0GA1UEAwwWMjQwOTo4Yzg1OjFhMDA6Mzc0Ojo2
YzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANutOWFjIqyifN6c6MU1
bVaTUNjqj4Mj+gBYaf72tRhKqhsx94EgEv8Hta6X31Uplx9cvY54NFggNd5j28h/
n8Jt2nGCFvQq6M672hIWKP1LPwRz0NaPKLR7yPYZJ6u/VmFf5ekSx/ojvL1ACI83
FMCR4pw8G0uSBx9hnprQIn30u0NhE+ZK9KhnesUC4OhtxlJZy2kzXuGonkvTc93O
0LMtky+7FxbG/wTwwJzO35HmJ397/uQvDieedi0bMVTGrhyMgITWDI1Z3JhL/vcK
zLwIxHq1NUGjQUK1q/QnZ6pGuGcwzYBzi7/qq2d3LgcqZ8ojmMWYhd+qSvnSZd1n
tg0CAwEAAaOCAYgwggGEMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjB3
BggrBgEFBQcBAQRrMGkwMAYIKwYBBQUHMAGGJGh0dHA6Ly9vY3NwLmdsb2JhbC5z
aGVjYS5jb20vb3ZzY2FnNTA1BggrBgEFBQcwAoYpaHR0cDovL2NlcnRzLmdsb2Jh
bC5zaGVjYS5jb20vb3ZzY2FnNS5jZXIwHwYDVR0jBBgwFoAUA3mjjVJf1OmIkh9D
WFQlAvSHi34wGwYDVR0RBBQwEocQJAmMhRoAA3QAAAAAAAAAbDAdBgNVHQ4EFgQU
6NMDJAZjg2LnFWHVbfOQxLQQVlwwDgYDVR0PAQH/BAQDAgWgMAwGA1UdEwEB/wQC
MAAwIAYDVR0gBBkwFzALBgkqgRyG7zoBAQIwCAYGZ4EMAQICMBMGCisGAQQB1nkC
BAMBAf8EAgUAMDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly9jcmwuZ2xvYmFsLnNo
ZWNhLmNvbS9vdnNjYWc1LmNybDANBgkqhkiG9w0BAQsFAAOCAQEAS6azeMzimcTD
f2FkWshT3BQZBaSWuWXuO9KfLePZAumJyOi8vr6FhAyJqXgz2rYzPe82y+BmSCUu
PIvY2LhCHbueslW18If3opCfT9SagBfF6ZmZyJa3Gx9mPsXwxeSt2DImkxmRhZKl
lqwg2ltRP3NPC4m7OQSY/Swuy3L4/gzkSNPkSen1IrJi+4pQYM6+HuUp2JOPHvbH
UY4twVSHFMjGxe5Qk+Iue43kFcNWMshDBDLrOatFJc1mUr03dNt0deHWR1/mzrz3
+ET+tC9qDnTRajzEbFA7LVckzsJ7nLpYSLP9ecOyYXr611fwBmA5I2GyuNDK1mZZ
W1N+LcIQdg==
-----END CERTIFICATE-----
    """,
    CertificateType.PRECERT_SIGNING_CA: """-----BEGIN CERTIFICATE-----
MIIE8zCCA9ugAwIBAgITBs6DUL9D2jPoNMSAlqcn9S1umDANBgkqhkiG9w0BAQsF
ADCBtTELMAkGA1UEBhMCVVMxETAPBgNVBAgTCElsbGlub2lzMRAwDgYDVQQHEwdD
aGljYWdvMSEwHwYDVQQKExhUcnVzdHdhdmUgSG9sZGluZ3MsIEluYy4xPTA7BgNV
BAMTNFRydXN0d2F2ZSBPcmdhbml6YXRpb24gVmFsaWRhdGlvbiBTSEEyNTYgQ0Es
IExldmVsIDExHzAdBgkqhkiG9w0BCQEWEGNhQHRydXN0d2F2ZS5jb20wHhcNMTgw
MjA2MTI0NzQ0WhcNMjgwMjI0MDUyNzQ0WjCBhjEvMC0GA1UEAxMmVHJ1c3R3YXZl
IE9WIFNIQTI1NiBQcmUtQ2VydGlmaWNhdGUgQ0ExITAfBgNVBAoTGFRydXN0d2F2
ZSBIb2xkaW5ncywgSW5jLjEQMA4GA1UEBxMHQ2hpY2FnbzERMA8GA1UECBMISWxs
aW5vaXMxCzAJBgNVBAYTAlVTMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC
AQEAj/lU7kWSQeMYl8oUOh9gJPeqCpPqb2AsrKxr+a8U/SF2oA4j5yJAwO9NwhZP
XujHupQKyOVWsOUnGrIX6SEFArKCvsxaZPp7qkQC7M2L1fl3TnvjuCpMnn8Somh1
CFFcbpWZUZHPfvFwGfp+wnidQSP5i4xcEyRohLju9yzsfslWwa+PYR0axT1e4euY
03/AgtwQrBRfKXY6XcV5tD1/JjQ7ZJ6yLIHVxjODVBQ489mwXtgujs7JYxvb8Z//
FvGl6AvjNQrJLCCkfkCowcoQVmPVwSMsbW6u+A+Lua/yUnsDdfOBmSW13DpjIReO
sgMhYh5S65AigSg+aFvYnA9S3wIDAQABo4IBJzCCASMwEgYDVR0TAQH/BAgwBgEB
/wIBADAiBgNVHSUBAf8EGDAWBgorBgEEAdZ5AgQEBggrBgEFBQcDATAdBgNVHQ4E
FgQUwM5MsAZIIQtN9KWs92v3ut1OBE8wHwYDVR0jBBgwFoAUys4dGAN3HhzzfFiy
mnCoCIAW9K4wNgYDVR0fBC8wLTAroCmgJ4YlaHR0cDovL2NybC50cnVzdHdhdmUu
Y29tL09WQ0EyX0wxLmNybDBxBggrBgEFBQcBAQRlMGMwJgYIKwYBBQUHMAGGGmh0
dHA6Ly9vY3NwLnRydXN0d2F2ZS5jb20vMDkGCCsGAQUFBzAChi1odHRwOi8vc3Ns
LnRydXN0d2F2ZS5jb20vaXNzdWVycy9PVkNBMl9MMS5jcnQwDQYJKoZIhvcNAQEL
BQADggEBAA1kV5Sf3zGaFfqxmtPdl06qzanB6piTkWApCQGBLxgsUvT1s0pCjKOe
gIbBAj4IkLf3KH8ikg5f15mlcs0NsGkgMqxkHo9zXjtBaR5l94p8ZTfhe8k1Oq8X
gZOfYqtFiAiPQJUknkoY9rwxob7ku95PK2WsnbDG/gymYROj3Hsxsj5G9WQTF9EM
Jz/Ic1q72wYGZZDVUOFsJZl58V44hr2p2cwaLUOD7K5jlgUh33KF4fXyI8i0/Ea6
o17BHTCJTmX59vIsKMR9zEFB4eOEPq+I8onUr9dAwycz9AiPhFz/VIbpBTbuS/1+
lASFarGnyLyLbARn8NZL9zhP0eWoRrM=
-----END CERTIFICATE-----
    """,
    CertificateType.ROOT_CA: """-----BEGIN CERTIFICATE-----
MIIB5DCCAYugAwIBAgIUc/TEV61o3Z3SDDrpgo/kfWsJlRAwCgYIKoZIzj0EAwIw
QDELMAkGA1UEBhMCVVMxHzAdBgNVBAoMFkZvbyBJbmR1c3RyaWVzIExpbWl0ZWQx
EDAOBgNVBAMMB1Jvb3QgQ0EwHhcNMjMwNTAxMDAwMDAwWhcNMzMwNDI1MjM1OTU5
WjBAMQswCQYDVQQGEwJVUzEfMB0GA1UECgwWRm9vIEluZHVzdHJpZXMgTGltaXRl
ZDEQMA4GA1UEAwwHUm9vdCBDQTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABEIl
SPiPt4L/teyjdERSxyoeVY+9b3O+XkjpMjLMRcWxbEzRDEy41bihcTnpSILImSVy
mTQl9BQZq36QpCpJQnKjYzBhMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQD
AgGGMB8GA1UdIwQYMBaAFGtwp5gX95/2N9L349xEbCEJ17vUMB0GA1UdDgQWBBRb
cKeYF/ef9jfS9+PcRGwhCde71DAKBggqhkjOPQQDAgNHADBEAiAJEd/70/vsKbGt
2pkddnSQHtglbIgCvq4KjyVAxYT0nwIgG90c0Hq1GNvXk9qi8YK6+wKJnbxl+0mi
iIiOYyHjbn4=
-----END CERTIFICATE-----
    """,
}


def test_determine():
    for expected_type, pem in _TEST_CASES.items():
        cert = loader.load_pem_certificate(pem)

        assert expected_type == serverauth.determine_certificate_type(cert)
