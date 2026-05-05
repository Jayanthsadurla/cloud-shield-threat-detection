import hashlib


class GeekCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{transaction_list} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


def generateblockchain(blockc, f1):
    try:
        block = GeekCoinBlock(blockc, f1)
        datas = block.block_data
        haskey = block.block_hash

        return datas, haskey

    except Exception as e:
        return None, str(e)