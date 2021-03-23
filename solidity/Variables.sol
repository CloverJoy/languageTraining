pragma solidity ^0.8.1;

contract TheVariable {
    uint256 public myUint;

    function setMyuint(uint mmyuint) public {
        myUint = mmyuint;
    }

    bool public myBool;

    function setMybool(bool mmybool) public {
        myBool = mmybool;
    }

    // uint 8 = 255

    uint8 public myUint8;

    function incrementUint() public {
        myUint8 ++;
    }

    function decrementUint() public {
        myUint8 --;
    }
    // solidity 0.8 auto check overflow underflow, must use unchecked if dont want check
    address public myAddress;

    function setMyAddress(address maddress) public {
        myAddress = maddress;
    }

    function checkBalance() public view returns(uint) {
        return myAddress.balance;
    }

    string public myString = 'Helloo warudo';

    function setMystring(string memory mstring) public {
        myString = mstring;
    }
}
