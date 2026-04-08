import socket

# Endereço IP e porta do servidor
SERVER_IP = '127.0.0.1'   # Use localhost se estiver rodando na mesma máquina
SERVER_PORT = 10402       # Primeiros 5 números do seu TIA

# Criação do socket TCP do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao IP e porta
servidor.bind((SERVER_IP, SERVER_PORT))

# Coloca o servidor em modo de escuta
servidor.listen(1)

print("Servidor TCP esperando conexão na porta", SERVER_PORT)

# Aceita conexão do cliente
cliente, addr = servidor.accept()
print("Conexão estabelecida com", addr)

while True:
    # Recebe mensagem do cliente
    mensagem = cliente.recv(1024).decode()
    print("Cliente:", mensagem)

    # Verifica se o cliente quer sair
    if mensagem.upper() == "QUIT":
        break

    # Envia resposta ao cliente
    resposta = input("Você: ")
    cliente.sendall(resposta.encode())

    # Verifica se o servidor quer sair
    if resposta.upper() == "QUIT":
        break

cliente.close()
servidor.close()
print("Conexão encerrada.")