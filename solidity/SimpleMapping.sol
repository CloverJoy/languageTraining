pragma solidity ^0.8.1;

contract SimpleMapping {
  mapping(uint => bool) public myMapping;
  mapping(address => bool) public myAddress;

  function setValue(uint _index) public {
    myMapping[_index] = true;
  }

  function setAddress() public {
    myAddress[msg.sender] = true;
  }
}