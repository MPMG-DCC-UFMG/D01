# Deduplicação de dados
Este projeto tem como objetivo consolidar todo o processo de casamento de entidades para o tipo de entidade Pessoa no ambiente do MPMG.


# Abordagem com arquivo csv

## Install

1 - Baixar projeto
git clone https://github.com/MPMG-DCC-UFMG/M05.git

2 - Install python3
sudo apt-get install python3.6

3 - Instalar o módulo interno casamento_entidade:
cd versao_vm/casamento_entidade
python3.6 setup.py install

4 - Instalar módulos externos
python3.6 -m pip install dedupe pandas tqdm matplotlib seaborn sklearn xlrd

# Test

## Teste de pares de escores
python3.6 score_pares.py

# Abordagem distribuída

Na abordagem distribuída estamos utilizando o software Zepplin que é um ambiente computacional baseado na Web para a análise de dados interativa através de interpretadores spark, jdbc, entre outros. O zepplin permite executar consultas no HIVE que é uma ferramenta de Data Warehouse para Apache Hadoop que permite a leitura e escrita de dados do HDFS usando uma linguagem baseada em SQL.


# Test
1 - Iniciar uma conexão ssh com a máquina no Ministério Público;

2 - Acessar o localhost do zepplin e entrar com o usuário e senha;

3 - Acessar o caminho MDM_V2/ufmg/dedupe/codigo_casamento_git

Este código tem o objetivo de realizar as etapas do casamento da entidade pessoa em ambiente distribuído.
