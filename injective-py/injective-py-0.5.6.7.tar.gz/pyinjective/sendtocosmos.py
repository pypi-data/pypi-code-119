from web3 import Web3

from .wallet import Address

class Peggo:
    def __init__(self, network: str):
        self.network = network
    def SendToCosmos(self, ethereum_endpoint: str, private_key: str, token_contract: str, receiver: str, amount: int,
                     maxFeePerGas: int, maxPriorityFeePerGas: int, peggo_abi: str, decimals=18):
        if self.network == 'testnet':
            peggy_proxy_address = "0xd6Da9dA014806Fdb64bF39b48fcA386AE3420d21"
        elif self.network == 'mainnet':
            peggy_proxy_address = "0xF955C57f9EA9Dc8781965FEaE0b6A2acE2BAD6f3"
        else:
            print("SendToCosmos is only supported on Mainnet & Testnet")
        web3 = Web3(Web3.HTTPProvider(ethereum_endpoint))
        contract = web3.eth.contract(address=peggy_proxy_address, abi=peggo_abi)

        token_contract_address = web3.toChecksumAddress(token_contract)

        receiver_address = Address.from_acc_bech32(receiver)
        receiver_ethereum_address = Address.get_ethereum_address(receiver_address)
        receiver_address_checksum = web3.toChecksumAddress(receiver_ethereum_address)
        receiver_slice = receiver_address_checksum[2:]
        receiver_padded_address = '0x' + receiver_slice.zfill(64)

        destination = web3.toBytes(hexstr=receiver_padded_address)

        sender_ethereum_address = web3.eth.account.privateKeyToAccount(private_key).address
        sender_address_checksum = web3.toChecksumAddress(sender_ethereum_address)
        nonce = web3.eth.get_transaction_count(sender_address_checksum)

        amount_to_send = int(amount * pow(10, decimals))

        gas = contract.functions.sendToCosmos(
            token_contract_address,
            destination,
            amount_to_send,
        ).estimateGas({'from': sender_address_checksum})

        transaction_body = {
            'nonce': nonce,
            'gas': gas,
            'maxFeePerGas': web3.toWei(maxFeePerGas, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(maxPriorityFeePerGas, 'gwei'),
        }

        tx = contract.functions.sendToCosmos(
            token_contract_address,
            destination,
            amount_to_send,
        ).buildTransaction(transaction_body)

        signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key)

        try:
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print("Transferred {} {} from {} to {}".format(amount, token_contract, sender_ethereum_address, receiver))
            print("Transaction hash:", web3.toHex(tx_hash))
        except Exception as e:
            print("Transaction failed", e)