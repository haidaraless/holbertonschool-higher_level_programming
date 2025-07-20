#!/usr/bin/node
const args = process.argv;

if (args.length <= 2) {
    console.log('No arguemnt');
} else if (args.length === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
