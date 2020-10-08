from unittest import TestCase, mock
import re
from iptables_oop import IpMethods
import iptc


"""
What to test:
 - test the function input
 -mock the functions having the correct behavior

"""



class IpTests(TestCase):

    # pattern = "[0-9]{12,12}"
    # test_input = ""

    # def check_input(self):
    #     self.assertTrue(re.math(pattern,test_input))

    @mock.patch.object(IpMethods, "add_ip_to_iptables_inbound")
    def check_add_inbound(self, mock_add ):
        false_input = "134.121.254.24"
        self.assertFalse(mock_add.add_ip_to_iptable_inbound(false_input, "eth0"))

    @mock.patch.object(IpMethods, "add_ip_to_iptables_outbound")
    def check_add_inbound(self, mock_add ):
        false_input = "134.121.254.22"
        self.assertFalse(mock_add.add_ip_to_iptable_outbound(false_input, "eth0"))

    @mock.patch.object(IpMethods, "delete_ip_from_iptable_inbound")
    def check_add_inbound(self, mock_delete ):
        false_input = "134.121.254.25"
        self.assertFalse(mock_delete.delete_ip_from_iptable_inbound(false_input, "eth0"))

    @mock.patch.object(IpMethods, "add_ip_to_iptables_inbound")
    def check_add_inbound(self, mock_delete):
        false_input = "134.431.254.22"
        self.assertFalse(mock_delete.delete_ip_from_iptables_outbound(false_input, "eth0"))


    # mock iptc in the context of iptables_oop

        
        

    



    



