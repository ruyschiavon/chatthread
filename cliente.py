import socket

def connect_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria o objeto TCP/IP usando a função socket.socket passando o AF_INET para especificar o endereço IP e o tipo de socket como TCP
    client_socket.connect(('localhost', 8000)) #É estabelecido a conexão com o servidor 

    while True:
        message = input("Digite sua mensagem: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode() 
        print("Mensagem recebida do servidor:", response) #A mensagem é enviada para o servidor e é aguardado uma resposta do mesmo

    client_socket.close() #Aqui se fecha a conexão

connect_server()