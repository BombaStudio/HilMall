import hashlib
import time

class Block:
	def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
		self.index = index #bloğun blok zincirindeki konumunu takip eder
		self.proof_no = proof_no #oluşan blokta üretilen sayı (mining)
		self.prev_hash = prev_hash #blok zinciri içerisinde önceki bloğun karması
		self.data = data #yapılan tüm işlemlerin kaydı
		self.timestamp = timestamp or time.time() #bu işlem için yerleştirilen zaman damgası
		
		
	@property
	def calc(self):
		block_of_string = "{}{}{}{}{}".format(
			self.index,
			self.proof_no,self.prev_hash,
			self.data,
			self.timestamp
		)
		return hashlib.sha256(block_of_string.encode()).hexdigest()
		
	def __repr__(self):
		return "{}{}{}{}{}".format(
			self.index,
			self.proof_no,self.prev_hash,
			self.data,
			self.timestamp
		)
		
class Chain:
	def __init__(self):
		self.chain = [] #değişken tüm blokları tutar
		self.current_data = [] #tüm işlemleri blokta tutar
		self.nodes = set() 
		self.c_genesis() #ilk bloğu oluşturmaya özen gösterir
		
	def c_genesis(self):
		self.c_block(proof_no=0, prev_hash=0)
	def c_block(self, proof_no, prev_hash):
		block = Block(
			index = len(self.chain),
			proof_no = proof_no,		
			prev_hash = prev_hash,
			data=self.current_data
		)
		self.current_data = []
		self.chain.append(block)
		return block
		
	@staticmethod
	def check_valid():
		if prev_block.index + 1 != block.index:
			return False
		elif prev_block.calc != block.prev_hash:
			return False
		elif not Chain.verifying_proof(block.proof_no, prev_block.proof_no):
			return False
		elif block.timestamp <= prev_block.timestamp:
			return False
		return True
		
	def new_data(self, sender, recipient, quantity):
		self.current_data.append({
			'sender': sender,
			'recipient': recipient,
			'quantity': quantity
		})
		return True
	
	@staticmethod
	def proof_of_work(last_proof):
		proof_no = 0
		while Chain.verifying_proof(proof_no, last_proof) is False:
			proof_no += 1
		return proof_no
		
		
	@staticmethod
	def verifying_proof(last_proof, proof):
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

	@staticmethod
	def c_proof_of_work(prev_proof):
		pass
	
	@property
	def latest_block(self):
		return self.chain[-1]
		
	def block_mining(self, details_miner):
		self.new_data(
			sender="0",
			recipient=details_miner,
			quantity= 1,
		)
		last_block = self.latest_block
		last_proof_no = last_block.proof_no
		proof_no = self.proof_of_work(last_proof_no)
		
		last_hash = last_block.calc
		block = self.c_block(proof_no, last_hash)
		
		return vars(block)
			
	def create_node(self, address):
		self.nodes.add(address)
		return True
	
	@staticmethod
	def obtain_block_object(block_data):
		#obtains block object from the block data
		return Block(
			block_data['index'],
			block_data['proof_no'],
			block_data['prev_hash'],
			block_data['data'],
			timestamp=block_data['timestamp']
		)
