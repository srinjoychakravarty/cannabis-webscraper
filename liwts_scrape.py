import httplib2, requests
from bs4 import BeautifulSoup
from bigchaindb_driver import BigchainDB
#Imports this class to create private key & public key
from bigchaindb_driver.crypto import generate_keypair

#connects with BigchainDB's testnet
bdb_root_url = BigchainDB('https://test.bigchaindb.com')

#creates private key & public key for 2 users
kin, srinjoy = generate_keypair(), generate_keypair()

# tx = bdb_root_url.transactions.prepare(
#     operation='CREATE',
#     signers=kin.public_key,
#     asset={'data': {'message': ''}})
# signed_tx = bdb_root_url.transactions.fulfill(
#     tx,
#     private_keys=kin.private_key)
# bdb_root_url.transactions.send_commit(signed_tx)

href_array = []
strains_url = 'https://www.liwts.org/strain-reviews/indica-strains/page/'
page_num = 4
hyperlink = strains_url + str(page_num)
http = httplib2.Http()
status, response = http.request(hyperlink)
http_code = status.status
if (http_code == 200):
    print ("Success 200 Okay!")
    soup = BeautifulSoup(response, features="html.parser")
    for a in soup.select('h2.entry-title a[href]'):
        href_array.append(a.get('href'))
else:
    print ("Oh no! Error: " + http_code)
print(href_array)
