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
<h2>Conexão Airflow com banco MySQL</h2>
<div>Para conectar ao banco MySQL sendo executado no windows enquanto o airflow é executado no MySQL é necessário seguir os passos:</div>
<ul>
    <li>Instalar o MySQL client no Ubuntu <code>sudo apt install mysql-client-core-8.0</code></li>
    <li>No MySQL configurar o host para aceitar qualquer tipo de conexão <code>UPDATE mysql.user SET host = '%' WHERE user = 'seu_usuario';</code></li>
    <li>No terminal do wsl executar o comando <code>mysql -u {usuario} -h {ip_windows} -P {porta_mysql} -D {seu_bd} -p</code> Após isso irá solicitar a senha do seu usuário no MySQL</li>
    <li>No airflow.cfg adicionar a linha <code>sql_alchemy_conn = mysql+mysqlconnector://{seu_usuario}:{sua_senha}@{seu_ip_windows}:{porta_mysql}/{seu_bd}</code></li>
    <li>Link do tutorial <a href="https://dataqoil.com/2022/03/13/running-airflow-in-wsl-but-using-mysql-server-from-windows-as-default/">tutorial</a></li>
</ul>