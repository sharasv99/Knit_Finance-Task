from web3 import Web3, HTTPProvider

# Set up Web3 connection to Binance Smart Chain
w3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))

contract_address = "0x71E9F23Db8D9a975837f28De1215A6FE9d4e148c"
contract_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_tokenContractAddress", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "buyer", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "cost", "type": "uint256"},
        ],
        "name": "BuyExecuted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "seller", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
            {"indexed": False, "internalType": "uint256", "name": "revenue", "type": "uint256"},
        ],
        "name": "SellExecuted",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "buyPrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "buyTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "sellPrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "sellTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "tokenContract",
        "outputs": [{"internalType": "contract MyToken", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]


contract = w3.eth.contract(address=contract_address, abi=contract_abi)


result = contract.functions.sellPrice().call()
print(result)

# Specify the event you want to retrieve logs for
event_name = "BuyExecuted"  # Replace with the desired event name

# Create a filter for the specified event
event_filter = contract.events[event_name].create_filter(fromBlock="latest")

# Retrieve the event logs
event_logs = event_filter.get_all_entries()

# Process and interpret the event logs
for event_log in event_logs:
    # Process event data here
    print(event_log)
