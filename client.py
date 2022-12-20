import tkinter
from tkinter import messagebox
import socket
import threading
from threading import Thread

clientWindow = tkinter.Tk()
clientWindow.title("Client")
username = " "

# top frame
topFrame = tkinter.Frame(clientWindow)
nameLabel = tkinter.Label(topFrame, text="Name: ").pack(side=tkinter.LEFT)
enterName = tkinter.Entry(topFrame)
enterName.pack(side=tkinter.LEFT)
connectButton = tkinter.Button(topFrame, text = "Connect", command=lambda: connect())
connectButton.pack(side=tkinter.LEFT)
topFrame.pack(side=tkinter.TOP)

# display frame
displayFrame = tkinter.Frame(clientWindow)
lineLabel = tkinter.Label(displayFrame, text=" ").pack()
scrollBar = tkinter.Scrollbar(displayFrame)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tkinterClientDisplay = tkinter.Text(displayFrame, height=20, width=55)
tkinterClientDisplay.pack(side=tkinter.LEFT, fill=tkinter.Y, padx=(5, 0))
tkinterClientDisplay.tag_config("tag_your_message", foreground="purple")
scrollBar.config(command=tkinterClientDisplay.yview)
tkinterClientDisplay.config(yscrollcommand=scrollBar.set, background="#ebe6fa", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tkinter.TOP)

# bottom frame
bottomFrame = tkinter.Frame(clientWindow)
tkinterMessage = tkinter.Text(bottomFrame, height=1, width=55)
tkinterMessage.pack(side=tkinter.LEFT, padx=(5, 12), pady=(5, 10))
tkinterMessage.config(highlightbackground="grey", state="disabled")
tkinterMessage.bind("<Return>", lambda event: get_messages(tkinterMessage.get("1.0", tkinter.END)))
bottomFrame.pack(side=tkinter.BOTTOM)

# client
client = None
HOST_ADDRESS = "127.0.0.1"
HOST_PORT = 8080


def connect():
    global username, client
    if len(enterName.get()) < 1:
        tkinter.messagebox.showerror(title=":(", message="Enter your name.")
    else:
        username = enterName.get()
        connect_to_server(username)


def connect_to_server(name):
    global client, HOST_ADDRESS, HOST_PORT
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDRESS, HOST_PORT))
        client.send(bytes(name, 'utf-8'))

        enterName.config(state=tkinter.DISABLED)
        connectButton.config(state=tkinter.DISABLED)
        tkinterMessage.config(state=tkinter.NORMAL)

        Thread(target=receive_message_from_server, args=(client, "m")).start()
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror(title=":(", message="Can't connect to host " + HOST_ADDRESS + " on port " + str(HOST_PORT) + ".")


def receive_message_from_server(sck, m):
    print(username, "has entered the chat...")
    while True:
        from_server = sck.recv(4096)

        if from_server:

            print("hi :)")

            texts = tkinterClientDisplay.get("1.0", tkinter.END).strip()
            tkinterClientDisplay.config(state=tkinter.NORMAL)

            if len(texts) < 1:
                tkinterClientDisplay.insert(tkinter.END, from_server.decode("utf-8"))

            else:
                tkinterClientDisplay.insert(tkinter.END, "\n\n" + from_server.decode("utf-8"))

        tkinterClientDisplay.config(state=tkinter.DISABLED)
        tkinterClientDisplay.see(tkinter.END)

    sck.close()
    clientWindow.destroy()


def get_messages(msg):
    msg = msg.replace('\n', '')
    texts = tkinterClientDisplay.get("1.0", tkinter.END).strip()

    tkinterClientDisplay.config(state=tkinter.DISABLED)

    send_message_to_server(bytes(msg, "utf-8"))

    tkinterClientDisplay.see(tkinter.END)
    tkinterMessage.delete('1.0', tkinter.END)

    print("just checking")


def send_message_to_server(msg):
    client.send(msg)
    if msg == "exit":
        client.close()
        socket.close()
        window.destroy()
    print("sending...")


clientWindow.mainloop()