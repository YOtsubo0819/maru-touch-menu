$( function() {
//select機能--------------------------------------------------------

    $('.sfc').hide();
    $('.tab-container').hide();
//.boxのカテゴリネームと同じカテゴリボックスをクリック
    let box = $(".box");
    $('.box').on('click', function(){
        $('.index-flex-container').hide();
        $('.sfc').show();
        $('.tab-container').show();
        const index = $(this).index();
        $(".category-box").eq(index).click();
        $("#tab-1").click();
    });

//Topに戻る
    $('.topicon').on('click', () => {
        $('.index-flex-container').show();
        $('.sfc').hide();
    });

//category別name表示
    let cbox = $(".category-box");
    $(".category-box").on("click", function(){
        $(".c-active").removeClass("c-active");
        $(this).addClass("c-active");
        const index = $(this).index();
        $(".s-name").removeClass("show").eq(index).addClass("show")
    });

// タブ色変
    $(".tab").on("click", function(){
        $(".tab-active").removeClass("tab-active");
        $(this).addClass("tab-active");
    });
//タブ切り替え
    $("#tab-1").on("click", function(){
        $(".category-box-container").show();
        $(".name-box-container").show();
        $(".category-box-container-tab2").hide();
        $(".category-box-container-tab3").hide();
        $(".name-box-container-tab2").hide();
        $(".name-box-container-tab3").hide();
    })
    $("#tab-2").on("click", function(){
        $(".category-box-container-tab2").show();
        $(".name-box-container-tab2").show();
        $(".category-box-container").hide();
        $(".category-box-container-tab3").hide();
        $(".name-box-container").hide();
        $(".name-box-container-tab3").hide();
    })
    $("#tab-3").on("click", function(){
        $(".category-box-container-tab3").show();
        $(".name-box-container-tab3").show();
        $(".category-box-container").hide();
        $(".category-box-container-tab2").hide();
        $(".name-box-container").hide();
        $(".name-box-container-tab2").hide();
    })

    sum();
//注文内容追加
    $(".category-name").on("click", function(){
        
        var ordername = $(this).find(".order-n").text();
        var orderprice = $(this).find(".order-p").text().replace(/[^0-9]/g, '');
        if(orderprice != ""){
            html_input =    '<div class="order-box">' +
                                '<div class="order-box-m">' +
                                    '<p>' + ordername +  '</p>' + 
                                    '<p style="font-weight:bold;" class="o-price">' + '¥' + orderprice + '</p>' +
                                '</div>' +
                                '<input name="ordername" type="hidden" value="' + ordername + '">'+
                            '</div>'
                            
            $(".order-form").prepend(html_input);
        }else{
            html_input =    '<div class="order-box">' +
                                '<div class="order-box-m">' +
                                    '<p>' + ordername +  '</p>' +
                                '</div>' +
                                '<input name="ordername" type="hidden" value="' + ordername + '">' + 
                            '</div>'
                            
            $(".order-form").prepend(html_input);
        }   
        sum();
    });

//注文削除
    $(document).on('click', '.order-box', function(){
        $(this).remove();
        sum();
    });


    $(".cancel-button").on("click", function(){
        $(".order-box").remove();
        sum();
    });

//注文priceCount
    function sum(){
        var pricelist = $(".order-form p[class=o-price]").map(function(index, val){
            var price = parseInt($(val).text().replace(/[^0-9]/g, ''));
            if (price >= 0) {
                return price;
            }else{
                return null;
            }
            
        });
        var total = 0;
        var totaltext = "合計：¥";
        pricelist.each(function(index, val){
            total = total + val;
        });
        $(".pricecount").find("p").text(totaltext + Math.ceil(total));
    }

//patient機能--------------------------------------------------------


}); 


