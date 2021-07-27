# covid-etl

## Instalação

Para instalar esse script, você precisa instalar o `poetry`. Execute o seguinte comando:

    pip install poetry

Com o `poetry` instalado, execute:

    poetry install

# Rodar o script

Para rodar o script, utilize:

    poetry shell

Esse comando irá iniciar o shell do poetry. Com isso, execute:

    python covid_etl/ssh_connect.py

É preciso que seja feito a passagem por parâmetro da origem da onde você quer pegar os arquivos, dessa maneira:

    python covid_etl/ssh_connect.py -s /meu_usuario/test_dir
