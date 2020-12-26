from hilmall import *


blockchain = Chain()

print("")
print(blockchain.chain)
while True:
	last_block = blockchain.latest_block
	last_proof_no = last_block.proof_no
	proof_no = blockchain.proof_of_work(last_proof_no)
	blockchain.new_data(
    sender="0",
    recipient="Büyük Hilmi",
    quantity=
    5,  
)

	last_hash = last_block.calc 
	block = blockchain.c_block(proof_no, last_hash)

	print("")
	print(blockchain.chain)
	print("\n")
