from typing import Any


class SequenceManager:
	def __init__(self, seq_owner, seq_name):
		self._owner = seq_owner
		self._name = seq_name
		self._seq = self._owner.seq[seq_name]
		if self._seq is None:
			raise  Exception(f"The Sequence '{seq_name}' does not exist in {seq_owner.path}")


		setattr(self, seq_name, TDSequence(self._owner, self._seq))
	


"""
	Wrapper for td.Sequence class
"""
class TDSequence:
	def __init__(self, seq_owner, seq_obj) -> None:

		#set attribute without being blocked by __setattr__
		object.__setattr__(self, "_owner", seq_owner)
		object.__setattr__(self, "_seq", seq_obj)
		pass

	def Add(self, qty: int = 1):
		new_blocks = [self._seq.insertBlock(0) for i in range(qty)]
		return new_blocks[0] if qty == 1 else new_blocks

	def Remove(self, idx):
		if idx >= self._seq.numBlocks:
			raise Exception(f"The block #{idx} does not exist in {self._seq.name}")

		self._seq.destroyBlock(idx)
		pass


	def __getattr__(self, attrName):
		if hasattr(self._seq, attrName):
			return getattr(self._seq, attrName)
	
	def __setattr__(self, name: str, value: Any) -> None:
		if hasattr(self._seq, name):
			if name == "name":
				raise Exception("Cannot dynamically change the name of a sequence, please use the TD's interface to rename the sequence and update the Extension's arguments accordingly.")
			else:
				setattr(self._seq, name, value)
		pass
	
		
# class TDSequence:
# 	def __init__(self, seq_owner, seq_name):
# 		self._owner = seq_owner
# 		self._name = seq_name
# 		self._bank = self._owner.seq[seq_name]
# 		if self._bank is None:
# 			raise  Exception(f"The Sequence '{seq_name}' does not exist in {seq_owner.path}")

# 		print(self)
# 		object.__setattr__(self, seq_name, self)

# 	def __getattr__(self, attrName):
# 		if attrName in self._bank.__class__.__dict__ :
# 			return self._bank.__class__.__dict__[attrName]

# class TDSequenceBlock:
# 	 def __init__(self):
# 		  pass
