# fell free to use https://github.com/ldx/python-iptables  
import iptc
import iptables as ip

def ip_interact(ip, interface, chain, target):
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), chain)
  rule = iptc.Rule()
  rule.in_interface = interface
  rule.src = ip
  target = rule.create_target(target)
  chain.insert_rule(rule)

# Example opf ip_inteface super INPUTon
s

if __name__ == "__main__":
    try:
        outbound_add = ip_interact("134.121.254.242","eth0","OUTPUT","ADD")
        outbound_drop = ip_interact("134.121.254.252","eth0","OUTPUT","DROP")
        inbound_add = ip_interact("134.121.254.292","eth0","INPUT","ADD")
        inbound_drop = ip_interact("134.431.254.222","eth0","INPUT","DROP")
    except Exception as e:
        print(e)

    
    