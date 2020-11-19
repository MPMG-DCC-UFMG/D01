# Deduplicação de dados
Este projeto tem como objetivo consolidar todo o processo de casamento de entidades para o tipo de entidade Pessoa no ambiente do MPMG.

A figura abaixo exemplifica o cenário de interesse para o MPMG, onde é realizada a união dos atributos das entidades do tipo Pessoa "José da Silva" que consta da fonte de dados A e "José Silva" presente na fonte de dados B, uma vez que o módulo de integração de dados identificou ambas entidades como sendo a mesma pessoa. Este é um exemplo onde a solução proposta tem o objetivo de identificar os registro que representam a uma mesma pessoa.

![alt text](https://github.com/MPMG-DCC-UFMG/M05/blob/master/fig/figura1.png)

A implementação de uma solução para CE envolve comumente duas fases: blocagem e correspondência. A blocagem tem por objetivo filtrar o produto do cruzamento dos conjuntos A x B para um conjunto C candidato que somente inclui pares de registros de entidades considerados prováveis para serem consideradas como correspondentes. Os mecanismos de blocagem partem do pressuposto de que não podem ocorrer casos de falso negativo. O conjunto de candidatos C frequentemente ainda pode conter pares de registros de entidades não correspondentes, portanto, após a blocagem, a fase de correspondência visa identificar as verdadeiras instâncias de entidades correlacionadas. A figura abaixo apresenta o processo de blocagem e correspondência aplicada a fontes de dados.

![alt text](https://github.com/MPMG-DCC-UFMG/M05/blob/master/fig/figura2.png)


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
