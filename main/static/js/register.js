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

// var div_id_name = document.getElementById("div_id_registeredBy");
// div_id_name.style.position = "relative";
// var icon_div = document.createElement("div");
// icon_div.classList.add("icon");
// var img = document.createElement("img");
// img.src = "https://socialconclave.com/static/images/Register/author.png";
// icon_div.appendChild(img);
// div_id_name.appendChild(icon_div);

function SHDiv(sRadio) {
  if (
    document.getElementsByClassName("topic1")[0].checked ==
      document.getElementsByClassName("topic1")[1].checked &&
    document.getElementsByClassName("topic1")[0].checked ==
      document.getElementsByClassName("topic1")[2].checked
  ) {
    console.log("topic1");
    for (let i = 0; i < 3; i++) {
      document.getElementsByClassName("topic1")[i].removeAttribute("disabled");
    }
  }

  if (
    document.getElementsByClassName("topic2")[0].checked ==
      document.getElementsByClassName("topic2")[1].checked &&
    document.getElementsByClassName("topic2")[0].checked ==
      document.getElementsByClassName("topic2")[2].checked
  ) {
    console.log("topic2");
    for (let i = 0; i < 3; i++) {
      document.getElementsByClassName("topic2")[i].removeAttribute("disabled");
    }
  }

  if (
    document.getElementsByClassName("topic3")[0].checked ==
      document.getElementsByClassName("topic3")[1].checked &&
    document.getElementsByClassName("topic3")[0].checked ==
      document.getElementsByClassName("topic3")[2].checked
  ) {
    console.log("topic3");
    for (let i = 0; i < 3; i++) {
      document.getElementsByClassName("topic3")[i].removeAttribute("disabled");
    }
  }

  if (
    document.getElementsByClassName("topic4")[0].checked ==
      document.getElementsByClassName("topic4")[1].checked &&
    document.getElementsByClassName("topic4")[0].checked ==
      document.getElementsByClassName("topic4")[2].checked
  ) {
    console.log("topic4");
    for (let i = 0; i < 3; i++) {
      document.getElementsByClassName("topic4")[i].removeAttribute("disabled");
    }
  }

  for (let i = 0; i < 3; i++) {
    document.getElementsByClassName(sRadio)[i].setAttribute("disabled", "true");
  }
}

var id_topicPref1_0 = document.getElementById("id_topicPref1_0");
var id_topicPref1_1 = document.getElementById("id_topicPref1_1");
var id_topicPref1_2 = document.getElementById("id_topicPref1_2");
var id_topicPref1_3 = document.getElementById("id_topicPref1_3");

var id_topicPref2_0 = document.getElementById("id_topicPref2_0");
var id_topicPref2_1 = document.getElementById("id_topicPref2_1");
var id_topicPref2_2 = document.getElementById("id_topicPref2_2");
var id_topicPref2_3 = document.getElementById("id_topicPref2_3");

var id_topicPref3_0 = document.getElementById("id_topicPref3_0");
var id_topicPref3_1 = document.getElementById("id_topicPref3_1");
var id_topicPref3_2 = document.getElementById("id_topicPref3_2");
var id_topicPref3_3 = document.getElementById("id_topicPref3_3");

id_topicPref1_0.classList.add("topic1");
id_topicPref1_1.classList.add("topic2");
id_topicPref1_2.classList.add("topic3");
id_topicPref1_3.classList.add("topic4");

id_topicPref2_0.classList.add("topic1");
id_topicPref2_1.classList.add("topic2");
id_topicPref2_2.classList.add("topic3");
id_topicPref2_3.classList.add("topic4");

id_topicPref3_0.classList.add("topic1");
id_topicPref3_1.classList.add("topic2");
id_topicPref3_2.classList.add("topic3");
id_topicPref3_3.classList.add("topic4");

id_topicPref1_0.addEventListener("click", SHDiv("topic1"));
id_topicPref1_1.addEventListener("click", SHDiv("topic2"));
id_topicPref1_2.addEventListener("click", SHDiv("topic3"));
id_topicPref1_3.addEventListener("click", SHDiv("topic4"));

// id_topicPref2_0.setAttribute("onclick", SHDiv("topic1"));
// id_topicPref2_1.setAttribute("onclick", SHDiv("topic2"));
// id_topicPref2_2.setAttribute("onclick", SHDiv("topic3"));
// id_topicPref2_3.setAttribute("onclick", SHDiv("topic4"));

// id_topicPref3_0.setAttribute("onclick", SHDiv("topic1"));
// id_topicPref3_1.setAttribute("onclick", SHDiv("topic2"));
// id_topicPref3_2.setAttribute("onclick", SHDiv("topic3"));
// id_topicPref3_3.setAttribute("onclick", SHDiv("topic4"));
