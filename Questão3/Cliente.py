import socket
import threading

HOST = '127.0.0.1'
PORT = 10402


def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode()

            if not mensagem:
                print("Conexão encerrada pelo servidor.")
                break

            print(f"\n{mensagem}")
        except:
            print("\nConexão encerrada.")
            break


def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    nome = input("Digite seu nome: ").strip()
    while not nome:
        nome = input("Digite um nome válido: ").strip()

    cliente.sendall(nome.encode())

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True)
    thread_receber.start()

    while True:
        mensagem = input()

        cliente.sendall(mensagem.encode())

        if mensagem.upper() == "QUIT":
            break

    cliente.close()
    print("Cliente encerrado.")


if __name__ == "__main__":
    iniciar_cliente()