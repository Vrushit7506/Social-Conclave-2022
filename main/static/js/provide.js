function changeActive(selectedLi, provideContent) {
    
    var selected = document.getElementById(selectedLi);
    var allLi = document.getElementsByClassName("provide-list");

    var selectedProvide = document.getElementById(provideContent);
    var allProvide = document.getElementsByClassName("teamsContent");


    for (index = 0; index < allLi.length; index++) { 
        allLi[index].classList.remove("active-provide"); 
    }

    for (index = 0; index < allProvide.length; index++) { 
        allProvide[index].classList.add("hideClass"); 
    }
    
    selected.classList.add("active-provide");
    selectedProvide.classList.remove("hideClass");
}


function changeActiveAgendas(selectedLi, provideContent) {
    
    var selected = document.getElementById(selectedLi);
    var allLi = document.getElementsByClassName("provide-listA");

    var selectedProvide = document.getElementById(provideContent);
    var allProvide = document.getElementsByClassName("agendasContent");


    for (index = 0; index < allLi.length; index++) { 
        allLi[index].classList.remove("active-provide"); 
    }

    for (index = 0; index < allProvide.length; index++) { 
        allProvide[index].classList.add("hideClass"); 
    }
    
    selected.classList.add("active-provide");
    selectedProvide.classList.remove("hideClass");
}

