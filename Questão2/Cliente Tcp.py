import socket

# Endereço IP e porta do servidor
SERVER_IP = '127.0.0.1'
SERVER_PORT = 10402

# Criação do socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
cliente.connect((SERVER_IP, SERVER_PORT))

print("Conectado ao servidor. Digite 'QUIT' para sair.")

while True:
    # Envia mensagem para o servidor
    mensagem = input("Você: ")
    cliente.sendall(mensagem.encode())

    # Verifica se o cliente quer sair
    if mensagem.upper() == "QUIT":
        break

    # Recebe resposta do servidor
    resposta = cliente.recv(1024).decode()
    print("Servidor:", resposta)

    # Caso o servidor também envie QUIT
    if resposta.upper() == "QUIT":
        break

cliente.close()
print("Conexão encerrada.")