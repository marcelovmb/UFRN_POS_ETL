from urllib import request

## Download Dimensões

## NCM Geral
url_NCM = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv'
file_NCM = 'NCM.csv'
request.urlretrieve(url_NCM, file_NCM)

## NCM Exportações
url_NCM_PPE = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_PPE.csv'
file_NCM_PPE = 'NCM_PPE.csv'
request.urlretrieve(url_NCM_PPE, file_NCM_PPE)

## NCM Importações
url_NCM_PPI = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_PPI.csv'
file_NCM_PPI   = 'NCM_PPI.csv'
request.urlretrieve(url_NCM_PPI, file_NCM_PPI)

## NCM Importações
url_NCM_UNIDADE = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_UNIDADE.csv'
file_NCM_UNIDADE   = 'NCM_UNIDADE.csv'
request.urlretrieve(url_NCM_UNIDADE, file_NCM_UNIDADE)

## Paises   
url_PAISES =  'https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv'
file_PAISES = 'PAIS.csv'
request.urlretrieve(url_PAISES, file_PAISES)

## Vias
url_VIAS = 'https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv'
file_VIAS = 'VIA.csv'
request.urlretrieve(url_VIAS, file_VIAS)

## UF
url_UF = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF.csv'
file_uf = 'UF.csv'
request.urlretrieve(url_UF, file_uf)




