import iptc
import logging as log
import re

log.basicConfig(filename='agent.log',level=log.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class IpMethods():

  def __init__(self):
      self.chain = iptc.Chain()

  def check_ip(ip):
      if
      pattern = "[0-9]{12,12}
      if re.math(pattern,ip):
          return ip
      else:
          return False

  def rule_logic(self, interface, ip, add_or_drop):
    log.info("Setting up the rules")
    rule = iptc.Rule()
    rule.in_interface = interface
    rule.src = self.check_ip(ip)
    target = rule.create_target("ACCEPT")
    log.info("Rules set")
    return rule
    
    

  def add_ip_to_iptables_inbound(self, ip, interface, add_drop = "ADD"):
    log.info("creating chain in adding to inbound")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    rule_result = self.rule_logic(interface, ip, add_drop)
    chain.insert_rule(rule_result)
    log.info("Chain created")

 

  def delete_ip_from_iptable_inbound(self, ip, interface, add_drop = "DROP"):
    log.info("creating chain in delete from inbound")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    rule_result = self.rule_logic(interface, ip, add_drop)
    chain.insert_rule(rule_result)
    log.info("Chain created")
    
    

  def add_ip_to_iptable_outbound(self, ip, interface, add_drop = "ADD"):
    log.info("creating chain in add to outbound")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
    rule_result = self.rule_logic(interface, ip, add_drop)
    chain.insert_rule(rule_result)
    log.info("done creating chain")

  def delete_ip_from_iptables_outbound(self, ip,interface, add_drop = "DROP"):
    log.info("Creating chain in delete from outbound")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
    rule_result = self.rule_logic(interface, ip, add_drop)
    chain.insert_rule(rule_result)
    log.info("Chain created")

