from urllib import request
import zipfile


## Downlaod Fatos

## Exportações
url_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip'
file_EXP = 'EXP_COMPLETA.zip'
request.urlretrieve(url_EXP, file_EXP)
with zipfile.ZipFile(file_EXP,"r") as zip_ref_exp:
    zip_ref_exp.extractall("Fatos")

## Importações
url_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip'
file_IMP = 'IMP_COMPLETA.zip'
request.urlretrieve(url_IMP, file_IMP)
with zipfile.ZipFile(file_IMP,"r") as zip_ref_imp:
    zip_ref_imp.extractall("Fatos")