from hilmall import *


blockchain = Chain()

print("")
print(blockchain.chain)
while True:
	last_block = blockchain.latest_block
	last_proof_no = last_block.proof_no
	proof_no = blockchain.proof_of_work(last_proof_no)
	blockchain.new_data(
    sender="0",  #it implies that this node has created a new block
    recipient="Büyük Hilmi",  #let's send Quincy some coins!
    quantity=
    5,  #creating a new block (or identifying the proof number) is awarded with 1
)

	last_hash = last_block.calc 
	block = blockchain.c_block(proof_no, last_hash)

	print("")
	print(blockchain.chain)
	print("\n")