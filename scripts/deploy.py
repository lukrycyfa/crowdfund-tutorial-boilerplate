from brownie import CountNfts, accounts, network, config
from brownie.network.gas.strategies import LinearScalingStrategy
import json

gas_strategy = LinearScalingStrategy("10 gwei", "50 gwei", 1.1)

def main():
    # This block of code deploy's the contract on alfajores
    if network.show_active()=='alfajores':
        adr = {}
        dev = accounts.add(config["wallets"]["from_key0"])
        print(network.show_active())
        deployed = CountNfts.deploy({'from':dev, "gas_price":gas_strategy})
        adr["address"] = deployed.address
        with open('./build/deployments/deployAlfajores.json', 'w') as outfile: 
            json.dump(adr, outfile, indent=4)                 
        return deployed

    # This block of code deploy's the contract on ganache.
    if network.show_active()=='development':
 
        adr = {}       
        owner = accounts[0]
        deployed = CountNfts.deploy({'from':owner, "gas_price":gas_strategy})
        adr["address"] = deployed.address
        with open('./build/deployments/deployLocal.json', 'w') as outfile: 
            json.dump(adr, outfile, indent=4)    
        return deployed
