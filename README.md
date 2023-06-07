# Getting Started With CrowdFund-Tutorial-Boilerplate

- This project was created as a boilerplate to assist with The [Crowdfund-Tutorial](http://place-link-here).

## Requirements

- [Node.js](https://nodejs.org/en/download)

- [Python](https://www.python.org/downloads/)

## Installations

### Install Ganche-cli

```bash
npm install ganache --global
```
### Clone The Boilerplate From This Repo

```bash
git clone https://github.com/lukrycyfa/crowdfund-tutorial-boilerplate.git
```
### Cd Into The Root Directory

```bash
pip install -r requirements.txt
```
### Install Contract Dependencies

```bash
brownie pm install OpenZeppelin/openzeppelin-contracts@4.8.2
```
## Testing Contract On Ganache Local Network

### Start Ganache-cli On A Separate Terminal

```bash
ganache-cli
```
### Compile, Deploy And Test The Contract On Ganache.

```bash
brownie compile
```
```bash
brownie run deploy.py
```
```bash
brownie test tests/test_OnGanache.py
```


## Testing Contract On Celo Alfajores Network

### Add The Alfajores Network To Brownie

```bash
brownie networks add Alfajores alfajores host=https://alfajores-forno.celo-testnet.org chainid=44787 explorer=https://alfajores-blockscout.celo-testnet.org
```

### Add Your Metamask Private Key To The .env file in the root
- create a .env file in the root directory 

```yaml
export PRIVATE_KEY_OWNER= "Your Metamask Private Key"
```
### Compile, Deploy And Test The Contract On Alfajores

```bash
brownie compile
```
```bash
brownie run deploy.py --network alfajores
```
```bash
brownie test tests/test_OnAlfajores.py --network alfajores
```
