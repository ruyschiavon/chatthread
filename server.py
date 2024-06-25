import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()  # Recebe dados do cliente
        if not data:
            break
        print("Mensagem recebida do cliente:", data)
        response = input("Digite sua mensagem: ")  # Lê a mensagem de resposta do servidor
        client_socket.send(response.encode())  # Envia a resposta ao cliente
    client_socket.close()  # Fecha o socket do cliente após a comunicação

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP/IP
    server_socket.bind(('localhost', 8000))  # Associa o socket a um endereço e porta
    server_socket.listen(1)  # Habilita o socket para aceitar conexões
    print("Servidor está na porta 8000")

    while True:
        client_socket, client_address = server_socket.accept()  # Aceita uma nova conexão do cliente
        print(f"Nova conexão de {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))  # Cria uma thread para lidar com a comunicação do cliente
        client_thread.start()  # Inicia a thread para tratar a comunicação com o cliente

start_server()  # Inicia o servidor
