var eye = document.getElementById("eye");
var pwd = document.getElementById("pwd");

function showhide() {
  if (pwd.type == "password") {
    pwd.type = "text";
    eye.className = "fa fa-eye-slash";
  } else {
    pwd.type = "password";
    eye.className = "fa fa-eye";
  }
}