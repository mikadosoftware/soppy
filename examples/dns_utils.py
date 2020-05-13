import dns.query
import dns.zone
import dns.resolver

def query(domain, recordtype):
    try:
        answers = dns.resolver.query(domain, recordtype)
        for answer in answers:
            print(answer)    
    except Exception as e:
        print(e)
        
def show_records(domain):
    print(domain)
    print("----")
    print("A Records")
    query(domain, 'A')
    print("CNAME Records")
    query(domain, 'CNAME')    
    print("MX Records")
    query(domain, 'MX')

def test():
    z = dns.zone.from_xfr(dns.query.xfr('1.1.1.1', 'dnspython.org'))
    names = z.nodes.keys()
    names.sort()
    for n in names:
        print(z[n].to_text(n))
	      

if __name__ == '__main__':
    show_records('www.mikadosoftware.com')
    show_records('mikadosoftware.com')
    
