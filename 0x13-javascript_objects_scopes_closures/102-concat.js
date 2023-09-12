#!/usr/bin/node
//fs: File System
const fs = require('fs');
// readFileSync: responsible for reading files
const data1 = fs.readFileSync(process.argv[2], 'utf-8');
const data2 = fs.readFileSync(process.argv[3], 'utf-8');
// writeFileSync: responsible for  writing a file
// uisng template literal
fs.writeFileSync(process.argv[4], `${data1}${data2}`);
