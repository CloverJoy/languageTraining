pragma solidity ^0.8.1;

contract StartStop {

    address public owner;
    bool public isPause;

    // call one time
    constructor() {
        owner = msg.sender;
    }

    function sendMoney() public payable {

    }

    function setPause(bool _isPause) public {
        require(owner == msg.sender, "That's not you!!");
        isPause = _isPause;
    }

    function withdrawAllMoney(address payable _to) public {
        require(owner == msg.sender, "That's not you man!!");
        require(!isPause, "transaction is paused!!");
        _to.transfer(address(this).balance);

    }
    // maybe no longer implemented later
    function destroySmartContract(address payable _to) public {
        require(msg.sender == owner, "You are not the owner");
        selfdestruct(_to);
    }
}