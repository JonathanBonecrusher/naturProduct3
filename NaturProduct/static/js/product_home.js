window.onload=function(){
    var button1 = document.getElementById('button-add');

    var newCode = `
    <div class="buttons-prod-buttons">
        <button id="button-plus" type="button" class="buttons-place btn btn-outline-secondary me-0">
            <a href="#" class="text-secondary">+</a>
        </button>
        <span id="selected-num" class="numb-style">0</span>
        <button id="button-minus" type="button" class="buttons-place btn btn-outline-secondary me-0">
            <a href="#" class="text-secondary">-</a>
        </button>
    </div>`;

    function add_to_card() {
        $('.buttons-place').remove();
        $('.buttons-prod-buttons').append(newCode);
    }

    button1.addEventListener("click", add_to_card, false);
}

