#!/usr/bin/node

// script that concats 2 files.
// fs: Stands for file sytem 
const fs = require('fs');
// utf-8: It enables interpreter to read the contents of a file
//readFileSync: Reads the contents of a file
const data1 = fs.readFileSync(process.argv[2], 'utf-8');
const data2 = fs.readFileSync(process.argv[3], 'utf-8');
// using template literal
//writeFileSync: Allows user to write content to file
fs.writeFileSync(process.argv[4], `${data1}${data2}`);
