function submitForm(event) {
    
    let errors = [];
    let FullName = document.getElementById("FullName").value;
    let password1 = document.getElementById("password1").value;
    let password2 = document.getElementById("password2").value;
    let genders = [];
    for (let gender of ["male", "female", "other"]) {
        if (document.getElementById(`id_${gender}`).checked) {
            genders = gender;   
        }
    }

    let hobbies = [];
    for (let hobbie of ["sports", "tv", "movies", "music"]) {
        if (document.getElementById(`id_${hobbie}`).checked) {
            hobbies.push(hobbie);
        }
    }
    let BirthDate = document.getElementById("BirthDate").value;
    let Height = document.getElementById("amountInput").value;
    let Color = document.getElementById("color").value;

    for (let c of document.getElementById("id_country").options) {
        if (c.selected) {
            country = c.text;
            break;
        }
    }
    let profession = document.getElementById("myProfession").value;
    let message = document.getElementById("id_message").value;
    

    if (password1 != password2) {
        errors.push("passwords must match")
    }
    if (errors.length > 0){
        document.getElementById("id_result").innerText = errors.join("\n");
    }
    
    
    else {
        result = `Full Name: ${FullName}\n`;
        result += `Password1: ${password1}\n`;
        result += `Password2: ${password2}\n`;
        result += `Gender: ${genders}\n`;
        result += `Hobbies: ${hobbies}\n`;
        result += `Birth Date: ${BirthDate}\n`;
        result += `Height: ${Height}\n`;
        result += `Country: ${country}\n`;
        result += `Favourite Color: ${Color}\n`;
        result += `Profession: ${profession}\n`;
        result += `Message: ${message}\n`;
        document.getElementById("id_result").innerText = result;
    }
    
    
    
    
    event.preventDefault();
    console.log("success")
}
