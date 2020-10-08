# fell free to use https://github.com/ldx/python-iptables  
import iptc
import logging as log

log.basicConfig(filename='agent.log',level=log.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def rule_logic(interface, ip, add_or_drop):
  log.info("Setting up the rules")
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target("ACCEPT")
  log.info("Rules set")
  return rule
 
    

def add_ip_to_iptables_inbound(ip, interface, add_drop = "ADD"):
  log.info("creating chain in adding to inbound")
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
  rule_result = rule_logic(interface, ip, add_drop)
  chain.insert_rule(rule_result)
  log.info("Chain created")

 

def delete_ip_from_iptable_inbound(ip, interface, add_drop = "DROP"):
  log.info("creating chain in delete from inbound")
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
  rule_result = rule_logic(interface, ip, add_drop)
  chain.insert_rule(rule_result)
  log.info("Chain created")
    
    

def add_ip_to_iptable_outbound(ip, interface, add_drop = "ADD"):
  log.info("creating chain in add to outbound")
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
  rule_result = rule_logic(interface, ip, add_drop)
  chain.insert_rule(rule_result)
  log.info("done creating chain")

def delete_ip_from_iptables_outbound(ip,interface, add_drop = "DROP"):
  log.info("Creating chain in delete from outbound")
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
  rule_result = rule_logic(interface, ip, add_drop)
  chain.insert_rule(rule_result)
  log.info("Chain created")

if __name__ == "__main__":
    try:
        add_ip_to_iptables_inbound("134.121.254.242","eth0")
        delete_ip_from_iptable_inbound("134.121.254.252","eth0")
        add_ip_to_iptable_outbound("134.121.254.222","eth0")
        delete_ip_from_iptables_outbound("134.431.254.222","eth0")
    except Exception as e:
      print(e)


  # check if the ip is already aded to the table
  # command to list all of the info about ipttables: iptables -L
  # figure out why the REJECT is not working 
    


