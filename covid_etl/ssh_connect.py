from typing import List
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

from covid_etl.consts import (
    SERVER_MACHINE_IP,
    SSH_USERNAME,
    SSH_PASSWORD,
    SSH_PORT,
    SAMPLES_COVID_FOLDER_PATH,
)


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
        raise(ConnectionError(f"Nao possivel realizar a conexao por ssh {e}"))


def exec_command(client: SSHClient, command: str) -> List[str]:
    stdin, stdout, stderr = client.exec_command(command)
    return [line.strip('\n') for line in stdout]


def main() -> None:
    client = get_ssh_connection()
    scp = SCPClient(client.get_transport())
    scp.get(SAMPLES_COVID_FOLDER_PATH, recursive=True)
    scp.close()
    client.close()


if __name__ == "__main__":
    main()
