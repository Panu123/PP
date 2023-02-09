'use strict'
//functions Challenge 1 for fundementals 2



const calcAvarage = (score1, score2, score3) => (score1 + score2 + score3) / 3;

const scoreDolphins = calcAvarage(100, 23, 71)
const scoreKoalas = calcAvarage(2, 54, 27)

console.log(`Avarage score for Dolphins is ${scoreDolphins}`);
console.log(`Avarage score for Koalas is ${scoreKoalas}`);

function checkWinner(avgDolphins, avgKoalas) {
    if (avgDolphins > avgKoalas * 2) {
        console.log(`Dolphins win (${avgDolphins} vs ${avgKoalas})`)


    } else if (avgKoalas > avgDolphins * 2) {
        console.log(`Koalas win (${avgKoalas} vs ${avgDolphins})`)

    } else {
        console.log("No Winner")
    }
}

checkWinner(scoreDolphins, scoreKoalas);



const bill = [125, 555, 44]

function calcTip(bill) {
    if (bill > 50 && bill < 300) {
        return bill * 0.15
    } else {

        return bill * 0.20;

    }
}



const tip = [calcTip(bill[0]), calcTip(bill[1]), calcTip(bill[2])]

const total = [(tip[0] + bill[0]), (tip[1] + bill[1]), (tip[2] + bill[2])]

console.log(`Your bill is ${bill[0]}, tip is ${tip[0]} and total is ${total[0]} `)


//challnege 3
const mark = {
    fullName: 'Mar Miller',
    weight: 78,
    height: 1.69,

    calcBMI: function () {
        this.bmiMark = (this.weight / (this.height ** 2));
        return this.bmiMark;
    }

}

const john = {
    fullName: 'John Smith',
    weight: 92,
    height: 1.95,

    calcBMI: function () {
        this.bmiJohn = (this.weight / (this.height ** 2));
        return this.bmiJohn;
    }


}

john.calcBMI();
mark.calcBMI();

if (john.bmiJohn > mark.bmiMark) {
    console.log(`Johns BMI (${john.bmiJohn}) is higher than Marks (${mark.bmiMark})`)
} else {
    console.log(`Marks BMI (${mark.bmiMark}) is higher than Johns (${john.bmiJohn})`)
}


const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
const tips = [];
const totals = [];

for (let i = 0; i < bills.length; i++) {
    const ti = calcTip(bills[i]);
    tips.push(ti);
    for (let y = 0; y < 1; y++) {
        const to = bills[i] + tips[i];
        totals.push(to)
    }
}
console.log(bills, tips, totals)

//codin challenge 1

