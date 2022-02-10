// var div_id_name = document.getElementById("div_id_name");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// icon_div.classList.add("icon3");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/user.png";
// img.style.width = "33px";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_age");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/age.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_email");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/email.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_phoneNumber");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/phone.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_address");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// icon_div.classList.add("icon2");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/address.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_city");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/global.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_schoolName");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/school.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_courseName");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src =
//   "https://socialconclave.com/static/images/Register/online-learning.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_yearGrad");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/graduate.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_team");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/support.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

var div_id_teamyn_0 = document.getElementById("id_teamyn_0");
div_id_teamyn_0.setAttribute("onclick", "yesNoDiv()");

var div_id_teamyn_1 = document.getElementById("id_teamyn_1");
div_id_teamyn_1.setAttribute("onclick", "yesNoDiv()");

// var div_id_name = document.getElementById("div_id_registeredBy");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/author.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

// var div_id_name = document.getElementById("div_id_teamyn");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/author.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

function yesNoDiv() {
  var id_teamyn_0 = document.getElementById("id_teamyn_0");
  var div_id_team = document.getElementById("div_id_team");
  div_id_team.style.display = id_teamyn_0.checked ? "block" : "none";
}
