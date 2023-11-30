window.addEventListener("DOMContentLoaded", (event) => {

    var newCode = `
    <div class="buttons-prod-buttons">
        <button id="button-plus" type="button" class="button-plus buttons-place btn btn-outline-secondary me-0">
            <a href="#" class="text-secondary">+</a>
        </button>
        <span id="selected-num" class="numb-style">1</span>
        <button id="button-minus" type="button" class="button-minus buttons-place btn btn-outline-secondary me-0">
            <a href="#" class="text-secondary">-</a>
        </button>
    </div>`;


    $('.button-add').on("click", function() {
        $(this).style.visibility = "hidden";
        $(this).closest(".prod-buttons").style.visibility = "visible";
    });

    $('.button-plus').on("click", function() {
        var num = $(this).closest(".numb-style");
        if(Number(num.textContent) < 100){
            num.textContent = Number(num_place.textContent) + 1;  
        } 
    });

    $('.button-minus').on("click", function() {
        var num = $(this).closest(".numb-style");
        if(Number(num.textContent) > 0){
            num.textContent = Number(num_place.textContent) - 1;
        }
        if(Number(num.textContent) === 1){
            document.getElementById('.prod-buttons').classList.toggle('hidden');
            document.getElementById('.button-add').classList.toggle('visible');
        }
    });
});

