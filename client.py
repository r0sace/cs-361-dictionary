import zmq



def password_strength(password):
    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(password)

    message = socket.recv()
    print(message.decode())

password_strength("")