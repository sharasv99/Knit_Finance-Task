// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Mytoken.sol";

contract TokenExchange {
    MyToken public tokenContract;
    address public owner;
    uint256 public buyPrice;  // Price in USDT to buy 1 MTK
    uint256 public sellPrice; // Price in USDT to sell 1 MTK

    event BuyExecuted(address indexed buyer, uint256 amount, uint256 cost);
    event SellExecuted(address indexed seller, uint256 amount, uint256 revenue);

    constructor(address _tokenContractAddress) {
        tokenContract = MyToken(_tokenContractAddress);
        owner = msg.sender;
        buyPrice = 1e18;    // 1 USDT in wei (1e18 wei = 1 USDT)
        sellPrice = 0.95e18; // 0.95 USDT in wei (0.95e18 wei = 0.95 USDT)
    }

    function buyTokens(uint256 amount) external {
        uint256 cost = amount * buyPrice;
        require(tokenContract.allowance(msg.sender, address(this)) >= cost, "Insufficient MTK allowance.");
        tokenContract.transferFrom(msg.sender, owner, cost);
        tokenContract.transfer(msg.sender, amount);
        emit BuyExecuted(msg.sender, amount, cost);
    }

    function sellTokens(uint256 amount) external {
        require(tokenContract.balanceOf(msg.sender) >= amount, "Insufficient MTK balance.");
        uint256 revenue = amount * sellPrice;
        require(tokenContract.balanceOf(address(this)) >= amount, "Insufficient MTK in the contract.");

        tokenContract.transferFrom(msg.sender, owner, amount);
        tokenContract.transfer(msg.sender, revenue);
        emit SellExecuted(msg.sender, amount, revenue);
    }
}


