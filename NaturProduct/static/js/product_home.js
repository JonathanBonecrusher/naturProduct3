window.addEventListener("DOMContentLoaded", (event) => {
    var basket = document.getElementById('end');
    var empty = document.getElementById('empty');
    var prod_array = [];

    $('.button-add').on("click", function() {
        var prod_id = this.id;
        if(document.querySelector(`#button-plus-${prod_id}`)){
            var numFind = document.querySelector(`#selected-num-${prod_id}`);
            if(Number(numFind.textContent) < 100){
                numFind.textContent = Number(numFind.textContent) + 1;  
            }
            return;
        }
        prod_array.push(prod_id);

        var newCodeInsert = `
        <div id="prod-${prod_id}" class="сonteiner alert-success item">
            <span>Продукт</span>
            <div class="buttons-prod-buttons">
                {% for prod in product %}
                    {% if cat == prod.productType %}
                        <h5>
                            <a href="{% url 'productPage' prod.pk %}" class="prod-link">{{ prod.productName }}</a>
                        </h5>
                    {% endif %}
                {% endfor %}
            </div>
        </div>`;

        // var newCodeInsert = `
        //     <div id="prod-${prod_id}" class="сonteiner alert-success item">
        //         <span>Продукт</span>
        //         <div class="buttons-prod-buttons">
        //             <form action="{% url 'cart:cart_add' prod.pk}" method="post">
        //                 <button id="button-plus-${prod_id}" type="button" class="button-plus buttons-place btn btn-outline-secondary me-0">
        //                     <snan href="#" class="text-secondary">+</span>
        //                 </button>
        //             </form>
        //             <form action="{% url 'cart:cart_remove' prod.pk}" method="post">
        //                 <span id="selected-num-${prod_id}" class="numb-style">1</span>
        //                 <button id="button-minus-${prod_id}" type="button" class="button-minus buttons-place btn btn-outline-secondary me-0">
        //                     <span href="#" class="text-secondary">-</span>
        //                 </button>
        //             </form>
        //         </div>
        //     </div>`;

        $("#prod-items").css("height", "75vh");
        $("#prod-items").css("width", "20vw");
        $("#prod-items").css("padding", "10px");
        empty.remove();
        $(basket).before(newCodeInsert);

        document.querySelector(`#button-plus-${prod_id}`).onclick = function(e) {
            var num = document.querySelector(`#selected-num-${prod_id}`);
            if(Number(num.textContent) < 100){
                num.textContent = Number(num.textContent) + 1;  
            }
        }

        document.querySelector(`#button-minus-${prod_id}`).onclick = function(e) {
            var num = document.querySelector(`#selected-num-${prod_id}`);
            if(Number(num.textContent) > 0){
                num.textContent = Number(num.textContent) - 1;  
            }
        }
    });
});

