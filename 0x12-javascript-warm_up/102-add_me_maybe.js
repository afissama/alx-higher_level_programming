#!/usr/bin/node
exports.addMeMaybe = function (number, func) {
  number = number + 1;
  func(number);
};
