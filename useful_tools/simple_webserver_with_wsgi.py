#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import socket
import io
import sys


class WSGIServer:
    address_family=socket.AF_INET
    socket_type=socket.SOCK_STREAM
    request_queue_size=1

    def __init__(self,server_address):
        #create a listening socket
        self.listen_socket=listen_socket=socket.socket(
            self.address_family,self.socket_type
        )
        #allow the same socket address
        listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #bind to the address
        listen_socket.bind(server_address)
        #activate to listening
        listen_socket.listen(self.request_queue_size)
        #get server host name and port
        host,port = self.listen_socket.getsockname()[:2]
        self.server_name=socket.getfqdn(host)
        self.server_port=port
        # return headers set by web frameworks/applications
        self.headers_set=[]

    def set_app(self,application):
        self.application=application

    def server_forever(self):
        listen_socket=self.listen_socket
        while True:
            # new connection from client
            self.client_connection,client_address=listen_socket.accept()
            #handle on request and close the client connection.then
            # loop over to wait for another client connection
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data=request_data=self.client_connection.recv(1024)
        # prient fornatted request data a la "curl -v"
        print(''.join('<{line}\n'.format(line=line) for line in request_data.splitlines))

        self.parse_request(request_data)

        # construct enviroment dictionary using request data
        env = self.get_environ()

        #it's time to call our appliction callable and get
        # back a result that will become http response body
        result= self.application(env,self.start_response)

        # construct a reponse and send it back to the client
        self.finish_response(result)

    def parse_request(self,text):
        request_line=text.splitlines()[0]
        request_line=request_line.rstrip('\r\n')
        # break down the request line into components
        (self.request_method,
         self.path,
         self.request_version)=request_line.split()

    def get_version(self):
        env={}
        # The following code snippet does not follow PEP8 conventions
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values
        #

        # Required WSGI variables
        env['wsgi.version']=(1,0)
        env['wsgi.url_scheme']='http'
        env['wsgi.input'] = io.StringIO(self.request_data)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.run_once'] = False

        #required CGI variables
        env['REQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT']=str(self.server_port)

        return env

    def start_response(self,status,response_headers,exc_info=None):
        # add necessary server headers
        server_headers=[('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),]
        self.headers_set=[status,response_headers+server_headers]
        # To adhere to WSGI specification the start_response must return
        # a 'write' callable. We simplicity's sake we'll ignore that detail
        # for now.
        # return self.finish_response

    def finish_response(self,result):
        try:
            status,response_headers=self.headers_set
            response='HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response+='{0}: {1}\r\n'.format(*header)
            response+='\r\n'
            for data in result:
                response+=data
            #print forn=matted data a la "curl -v"
            print("".join(">{line}\n".format(line=line) for line in response.splitlines()))
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()

SERVER_ADDRESS=(HOST,PORT)='',8888

def make_server(server_address,application):
    server=WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__=="__main__":
    if len(sys.argv)<2:
        sys.exit("provide a wsgi application as module:callable")
    app_path=sys.argv[1]
    module,application=app_path.split(':')
    module=__import__(module)
    application=getattr(module,application)
    httpd=make_server(SERVER_ADDRESS,application)
    print('WSGIserver:Serving http on the port {port}..\n'.format(port=PORT))
    httpd.server_forever()
