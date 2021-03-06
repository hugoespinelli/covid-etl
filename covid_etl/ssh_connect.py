import argparse
import logging
from typing import List

from paramiko import AutoAddPolicy, SSHClient
from scp import SCPClient

from covid_etl.consts import SERVER_MACHINE_IP, SSH_PASSWORD, SSH_PORT, SSH_USERNAME

logger = logging.getLogger()


def get_ssh_connection() -> SSHClient:
    try:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
            SERVER_MACHINE_IP,
            username=SSH_USERNAME,
            password=SSH_PASSWORD,
            port=SSH_PORT,
            look_for_keys=False,
            allow_agent=False,
            timeout=5000,
        )
        return client
    except Exception as e:
        raise (ConnectionError(f"Nao possivel realizar a conexao por ssh {e}"))


def exec_command(client: SSHClient, command: str) -> List[str]:
    stdin, stdout, stderr = client.exec_command(command)
    return [line.strip("\n") for line in stdout]


def transfer(source: str, destination: str) -> None:
    logger.info("Começando extração...")
    logger.info("Tentando conectar com o servidor...")
    client = get_ssh_connection()
    logger.info("Conexão efetuada com sucesso!")
    scp = SCPClient(client.get_transport())
    logger.info(f"Iniciando transferência {source} para {destination}")
    scp.get(remote_path=source, local_path=destination, recursive=True)
    scp.close()
    client.close()
    logger.info("Extração finalizada.")


def put(source: str, destination: str) -> None:
    logger.info("Começando extração...")
    logger.info("Tentando conectar com o servidor...")
    client = get_ssh_connection()
    logger.info("Conexão efetuada com sucesso!")
    scp = SCPClient(client.get_transport())
    logger.info(f"Iniciando transferência {source} para {destination}")
    scp.put(source, remote_path=destination, recursive=True)
    scp.close()
    client.close()
    logger.info("Extração finalizada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Programa sincronização de pastas utilizando ssh"
    )
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        required=True,
        help="O path de onde deseja pegar os arquivos",
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        default="",
        help="O path da onde deseja depositar os arquivos extraidos",
    )
    args = parser.parse_args()
    transfer(args.source, args.destination)
