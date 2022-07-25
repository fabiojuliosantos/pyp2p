import socket

chatServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatServidor.bind(('localhost', 8000))

chatServidor.listen()
chatCliente, end = chatServidor.accept()

finalizado = False

while not finalizado:
    msg = chatCliente.recv(1024).decode('utf-8')
    if msg == 'fechar':
        finalizado = True
    else:
        print(msg)
    chatCliente.send(input('Mensagem: ').encode('utf-8'))

chatCliente.close()
chatServidor.close()