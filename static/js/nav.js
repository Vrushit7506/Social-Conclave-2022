var b = 1;
function openNav() {
  document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}
		function  myFunction() {
		if(b == 1){
		b+=1;
		openNav();
		}
		else{
		b=1;
		closeNav();
		}
		x=document.getElementById("smallone");
  x.classList.toggle("change");
}