<h1>Airflow Celery e Redis</h1>
<h2>Configuração do ambiente Linux</h2>
<ul>
    <li>Para atualizar os pacotes do Ubuntu <code>sudo apt update</code>, <code>sudo apt upgrade</code></li>
    <li>Para instalar diferentes versões do python no Ubuntu <code>sudo add-apt-repository ppa:deadsnakes/ppa</code></li>
    <li>Instalando python e ambiente virtual <code>sudo apt install python3.9</code> <code>sudo apt install python3.9-venv</code></li>
    <li>Para criar o ambiente virutal execute <code>python3.9 -m venv venv</code> e para ativar <code>source venv/bin/activate</code></li>
</ul>
<h2>Utilização Apache Airflow</h2>
<ul>
    <li>Instale o airflow com Celery  <code>pip install apache-airflow[postgres,celery,redis]==2.3.2 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"</code></li>
    <li>Sempre que for executar o Airflow exporte a variável de ambiente para a pasta desejada <code>export AIRFLOW_HOME=~/celery_airflow/airflow</code></li>
    <li>Execução do Airflow: <code>airflow standalone</code></li>
</ul>