var n1 ="name1";
var n2 ="name2";
var n3 ="name3";

var wid=[
    {
        name:n1,
        width:120
    },
    {
        name:n2,
        width:220
    }

]
var pt1 ={
    cG:"cGdesu",
    filter:"fildesu",
    items : new Array(
        {
            id:"id1",
            width:100,
            name:n1
        },
        {
            id:"id2",
            width:200,
            name:n2
        },
        {
            id:"id3",
            width:300,
            name:n3
        }

    )
}

console.log(1);

pt1.items[0].name = "oreore";
var ptc = {...pt1.items};
console.log(ptc[0]);
for (let index = 0; index < ptc.length; index++) {
    if(array[index].name === n2){
        console.log("a"+index);
    }
    
}
//console.log(pt1.items.map(el => el.name));