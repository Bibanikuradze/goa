const student = {
    name: "ბიბა",
    surname: "ნიკურაძე",
    academy: "GOA",
    city: "თბილისი",
    role: "მოსწავლე",
    favColor: "frozen green",
    
    printFullName: function() {
        console.log(this.name + " " + this.surname);
    },

    printFavColor: function() {
        console.log(this.favColor);
    }
};

console.log(student);

console.log(student.city);

student.printFullName();

student.favColor = "frozen green";
console.log(student.favColor);









function userOperations() {
  let answer1 = confirm("გსურს პროგრამირების სწავლა?");
  let answer2 = confirm("გსურს GOA-ში სწავლა?");

  console.log("AND ოპერაცია (answer1 && answer2):", answer1 && answer2);
  console.log("OR ოპერაცია (answer1 || answer2):", answer1 || answer2);
}

window.onload = userOperations;