#Done by Shokhrukh Talatov

import socket


def start_server():
    try:    
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 8000))
        server.listen(4)
        while True:
            print('Listening...')
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    
    
    except KeyboardInterrupt:
        server.close()
        print('shutdown')


def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        if path == '/':
            path = '/index.html'
        with open('htdocs'+path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry, buddy! No page found...').encode('utf-8')

if __name__=='__main__':
    start_server()
