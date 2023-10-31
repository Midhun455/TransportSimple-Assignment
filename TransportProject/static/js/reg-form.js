const inputName = () => {
  let Name = document.getElementById("name-hint");
  Name.style = "display:none";
};
const inputEmail = () => {
  let Email = document.getElementById("mail-hint");
  Email.style = "display:none";
};
const inputPhone = () => {
  let Phone = document.getElementById("phone-hint");
  Phone.style = "display:none";
};
const inputPassword = () => {
  let Password = document.getElementById("pass-hint");
  Password.style = "display:none";
};
const inputcnfPassword = () => {
  let ConfirmPass = document.getElementById("cnfpass-hint");
  ConfirmPass.style = "display:none";
};

function formSubmitHandler() {
  let Name = document.getElementById("input-name").value;
  let Email = document.getElementById("email").value;
  let Phone = document.getElementById("phone").value;
  let Password = document.getElementById("password").value;
  let ConfirmPass = document.getElementById("cnfpass").value;
  let HintPara = document.getElementById("name-hint");
  let Hintmail = document.getElementById("mail-hint");
  let Hintphone = document.getElementById("phone-hint");
  let HintPass = document.getElementById("pass-hint");
  let HintcnfPass = document.getElementById("cnfpass-hint");

  let mailregex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let passregex = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;

  if (Name == "") {
    HintPara.innerHTML = "Name must not be empty";
    HintPara.style = "display:block";
    return false;
  } else if (Email == "") {
    Hintmail.innerHTML = "E-mail must not be empty";
    Hintmail.style = "display:block";
    return false;
  } else if (!mailregex.test(Email)) {
    Hintmail.innerHTML = "Invalid format";
    Hintmail.style = "display:block";
    return false;
  } else if (Phone == "") {
    Hintphone.innerHTML = "Phone number needed";
    Hintphone.style = "display:block";
    return false;
  } else if (Phone.length != 10) {
    Hintphone.innerHTML = "Enter Correct number";
    Hintphone.style = "display:block";
    return false;
  } else if (Password == "") {
    HintPass.innerHTML = "Password needed";
    HintPass.style = "display:block";
    return false;
  } else if (ConfirmPass == "") {
    HintcnfPass.innerHTML = "Confirm Password";
    HintcnfPass.style = "display:block";
    return false;
  } else if (Password.length < 6) {
    HintPass.innerHTML = "Password should be more than 6 characters";
    HintPass.style = "display:block";
    return false;
  } else if (!passregex.test(Password)) {
    HintPass.innerHTML =
      "Must contain at least one  number and one uppercase and lowercase letter, and at least 6 or more characters";
    HintPass.style = "display:block";
    return false;
  } else if (Password != ConfirmPass) {
    HintcnfPass.innerHTML = "Password not matching";
    HintcnfPass.style = "display:block";
    return false;
  } else {
    document.getElementById("myForm").submit();
    return true;
  }
}
