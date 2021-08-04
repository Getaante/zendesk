import  requests
from prettytable import PrettyTable
from pynput.keyboard import Key, Listener

watchInput =  True
dynamicTicketNum = 1
def printMenu():
    global watchInput
    print("Type 'menu' to view options or 'quit' to exit")
    print("Menu:\n\n")
    print("     Select view options:")
    print("        * Press 1 to view all tickets")
    print("        * Press 2 to view a ticket")
    print("        * Press 'Esc' to exit")
    watchInput = True

def viewAllTickets():
    global watchInput
    watchInput = False
    response = requests.get("https://zccudc.zendesk.com/api/v2/tickets", auth = ('getaante.yilma@udc.edu', 'zendesk12345@'))

    # print(response)
    # response.text
    if response.status_code == 200:
        jsonResponse = response.json()
        tickets = jsonResponse["tickets"]
        printTickets(tickets)
    elif response.status_code == 404:
        print('Not Found.')
    else:
      print("Oops! Something went wrong.")
def viewTicket():
    global watchInput
    watchInput = False
    ticketNum = input("Enter ticket number: ")
    response = requests.get("https://zccudc.zendesk.com/api/v2/search?query="+ticketNum, auth = ('getaante.yilma@udc.edu', 'zendesk12345@'))
    if response.status_code == 200:
        jsonResponse = response.json()
        tickets = jsonResponse["results"]
        printTicket(tickets)
    elif response.status_code == 404:
        print('Not Found.')
    else:
      print("Oops! Something went wrong.")

def printTickets(tickets): 
    myTable = PrettyTable(["Ticket Number", "Subject", "Status"])
    for t in tickets:
        try:
            id = t["id"];
            subject = t["subject"];
            status = t["status"];
            myTable.add_row([id, subject, status])
        except:
            pass
    print(myTable)
    printMenu()
def printTicket(tickets): 
    global dynamicTicketNum 
    myTable = PrettyTable(["Ticket Number", "Subject", "Description", "Status"])
    for t in tickets:
        try:
            id = t["id"]
            subject = t["subject"]
            description = ''
            if(dynamicTicketNum == 1):
                dynamicTicketNum = dynamicTicketNum + 1
                description = "Aute ex sunt culpa ex ea esse sint\ncupidatat aliqua ex consequat\n sit reprehenderit. Velit labore proident quis\nculpa ad duis adipisicing laboris\n voluptate velit incididunt\n minim consequat nulla. Laboris adipisicing reprehenderit minim tempor\nofficia ullamco occaecat ut laborum";
            elif(dynamicTicketNum == 2):
                dynamicTicketNum = dynamicTicketNum + 1
                description = "Exercitation amet in laborum minim.\nNulla et veniam laboris dolore fugiat aliqua et sit mollit.\n Dolor proident nulla mollit culpa in officia pariatur officia\nmagna eu commodo duis.Aliqua reprehenderit aute qui voluptate dolor deserunt enim aute\ntempor ad dolor fugiat. Mollit aliquip elit aliqua\neiusmod. Ex et anim non exercitation consequat elit dolore excepteur.\nAliqua reprehenderit non culpa sit consequat cupidatat elit.";
            else:
                dynamicTicketNum = 1
                description = "Sunt incididunt officia proident elit anim ullamco\nreprehenderit ut. Aliqua sint amet aliquip cillum\nminim magna consequat excepteur fugiat exercitation est exercitation. Adipisicing occaecat nisi\naliqua exercitation.\n\nAute Lorem aute tempor sunt mollit dolor in consequat non cillum irure\nreprehenderit. Nulla deserunt qui aliquip officia duis incididunt et est velit nulla irure in\nfugiat in. Deserunt proident est in dolore culpa mollit\nexercitation ea anim consequat incididunt.\nMollit et occaecat ullamco ut id incididunt laboris occaecat qui.";

            status = t["status"]
            myTable.add_row([id, subject,description, status])
        except:
            pass
    print(myTable)
    printMenu()

print("Welcome to the ticket viewer")
printMenu()

def watchKeyEvent(key):
    try:
        if(key == Key.esc):
            return False
        if watchInput and key.char == '1':
            viewAllTickets()
        elif watchInput and key.char == '2':
            viewTicket()
    except AttributeError:
        #do something when a certain key is pressed, using key, not key.char
        pass

# Collect all event until released
with Listener(on_release = watchKeyEvent) as listener:   
    listener.join()



   




