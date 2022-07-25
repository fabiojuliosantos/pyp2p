import socket

chatCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatCliente.connect(('localhost', 8000))

finalizado = False
print('Digite fechar para finalizar o chat.')

while not finalizado:
    chatCliente.send(input('Mensagem: ').encode('utf-8'))
    msg = chatCliente.recv(1024).decode('utf-8')
    if msg == 'fechar':
        finalizado = True
    else:
        print(msg)

chatCliente.close()