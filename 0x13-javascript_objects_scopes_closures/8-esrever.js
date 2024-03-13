#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let b = 0;
  while ((len - b) > 0) {
    const aux = list[len];
    list[len] = list[b];
    list[b] = aux;
    b++;
    len--;
  }
  return list;
};
