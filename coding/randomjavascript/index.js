
let i=0
z=0
let ops = {}
while (z < 1){
    let num1 = prompt("Enter your first number")
    let num2 = prompt("Enter your secodn number")
    let op = prompt("Enter the operation you woould like to perform")
    if (op == "add"){
        ops[i] = Number(num1) + Number(num2)
        console.log(ops[i])
        i+=1
    }
    if (op == "subtract"){
        ops[i] = Number(num1) - Number(num2)
        console.log(ops[i])
        i+=1
    }
    if (op=="divide"){
        ops[i] = Number(num1) / Number(num2)
        console.log(ops[i])
        i+=1
    }
    if (op=="multiply"){
        ops[i] = Number(num1) + Number(num2)
        console.log(ops[i])
        i+=1
    }
    if (op=="back"){
        console.log(ops[i-1])
    }
}
