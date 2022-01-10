let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];
// console.log(secretMessage.length)//24
secretMessage.pop();
// console.log(secretMessage.length)//23
secretMessage.push('to', 'Program')
// console.log(secretMessage.length)//25
secretMessage.splice(secretMessage.indexOf('easily'), 1, 'right')
// console.log(secretMessage.indexOf('right'))//7 
// console.log(secretMessage.indexOf('easily'))//-1 should not exist
secretMessage.shift()
// console.log(secretMessage.length) //24
secretMessage.unshift('Programming')
// console.log(secretMessage.indexOf('Programming'))//0
secretMessage.splice(secretMessage.indexOf('get'), 5, 'know')
// console.log(secretMessage.indexOf('know'))//6
console.log(secretMessage.join(' '))//Prints array as one sentance

