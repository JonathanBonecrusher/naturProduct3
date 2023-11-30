window.onload=function(){
    var button1 = document.getElementById('button-plus');
    var button2 = document.getElementById('button-minus');
    var num_place = document.getElementById('selected-num');

    function plus() {
        if(Number(num_place.textContent) < 100){
            num_place.textContent = Number(num_place.textContent) + 1;  
        }  
    }
    
    function minus() {
        if(Number(num_place.textContent) > 0){
            num_place.textContent = Number(num_place.textContent) - 1;  
        }
    }
    
    button1.addEventListener("click", plus, false);
    
    button2.addEventListener("click", minus, false);
}

