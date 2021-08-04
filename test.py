import unittest
import  requests

class zendeskTest(unittest.TestCase):
    def test_viewAllTickets(self): 
       response = requests.get("https://zccudc.zendesk.com/api/v2/tickets", auth = ('getaante.yilma@udc.edu', 'zendesk12345@'))
       assert response.status_code == 200
    def test_ViewTicket(self): 
       response = requests.get("https://zccudc.zendesk.com/api/v2/search?query=1", auth = ('getaante.yilma@udc.edu', 'zendesk12345@'))
       assert response.status_code == 200

if __name__ == '__main__':
   unittest.main()