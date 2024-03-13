#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let b = 0; b < list.length; b++) {
    if (searchElement === list[b]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
