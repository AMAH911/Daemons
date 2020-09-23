# fell free to use https://github.com/ldx/python-iptables  
import iptc

def accept_ip():
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target("ACCEPT")
  global chain.insert_rule(rule)
    

def add_ip_to_iptables_inbound(ip, interface, chain,target):
  
  accept_ip(ip, interface)
 


    

def delete_ip_from_iptable_inbound(ip, interface):
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target("DROP")
  chain.insert_rule(rule)
    
    

def add_ip_to_iptable_outbound(ip, interface):
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target("ACCEPT")
  chain.insert_rule(rule)

def delete_ip_from_iptables_outbound(ip,interface):
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target("DROP")
  chain.insert_rule(rule)

if __name__ == "__main__":
    add_ip_to_iptables_inbound()
    delete_ip_from_iptable_inbound()
    add_ip_to_iptable_outbound()
    delete_ip_from_iptables_outbound()



# put the functions in a try catch block
# make the code DRY





 
    