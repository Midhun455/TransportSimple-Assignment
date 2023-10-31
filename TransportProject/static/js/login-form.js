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
  let Email = document.getElementById("email").value;
  let Password = document.getElementById("password").value;
  let Hintmail = document.getElementById("mail-hint");
  let HintPass = document.getElementById("pass-hint");

  let mailregex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let passregex = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;

  if (Email == "") {
    Hintmail.innerHTML = "E-mail must not be empty";
    Hintmail.style = "display:block";
    return false;
  } else if (!mailregex.test(Email)) {
    Hintmail.innerHTML = "Invalid format";
    Hintmail.style = "display:block";
    return false;
  } else if (Password == "") {
    HintPass.innerHTML = "Password needed";
    HintPass.style = "display:block";
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
  } else {
    document.getElementById("myForm").submit();
    return true;
  }
}

// (?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}
