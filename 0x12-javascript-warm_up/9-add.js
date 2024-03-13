#!/usr/bin/node
function add (i, j) {
  const m = i + j;
  console.log(m);
}

add(Number(process.argv[2]), Number(process.argv[3]));
