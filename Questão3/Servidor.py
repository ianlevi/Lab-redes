import socket
import threading

HOST = '127.0.0.1'
PORT = 10402

clientes = []
nomes = []


def broadcast(mensagem, cliente_remetente=None):
    clientes_remover = []

    for cliente in clientes:
        if cliente != cliente_remetente:
            try:
                cliente.sendall(mensagem.encode())
            except:
                clientes_remover.append(cliente)

    for cliente in clientes_remover:
        remover_cliente(cliente)


def remover_cliente(cliente):
    if cliente in clientes:
        indice = clientes.index(cliente)
        nome = nomes[indice]

        clientes.remove(cliente)
        nomes.remove(nome)

        try:
            cliente.close()
        except:
            pass

        print(f"{nome} desconectou.")
        broadcast(f"{nome} saiu do chat.")


def tratar_cliente(cliente):
    try:
        nome = cliente.recv(1024).decode().strip()

        if not nome:
            cliente.close()
            return

        clientes.append(cliente)
        nomes.append(nome)

        print(f"{nome} entrou no chat.")
        cliente.sendall("Conectado ao chat com sucesso! Digite QUIT para sair.".encode())
        broadcast(f"{nome} entrou no chat.", cliente)

        while True:
            mensagem = cliente.recv(1024).decode().strip()

            if not mensagem:
                remover_cliente(cliente)
                break

            if mensagem.upper() == "QUIT":
                cliente.sendall("Você saiu do chat.".encode())
                remover_cliente(cliente)
                break

            texto_final = f"{nome}: {mensagem}"
            print(texto_final)
            broadcast(texto_final, cliente)

    except:
        remover_cliente(cliente)


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor iniciado em {HOST}:{PORT}")
    print("Aguardando conexões...")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Nova conexão de {endereco}")

        thread = threading.Thread(target=tratar_cliente, args=(cliente,))
        thread.start()


if __name__ == "__main__":
    iniciar_servidor()