$( function() {
//select機能--------------------------------------------------------

    $('.sfc').hide();

//.boxのカテゴリネームと同じカテゴリボックスをクリック
    let box = $(".box");
    $('.box').on('click', function(){
        $('.index-flex-container').hide();
        $('.sfc').show();
        const index = $(this).index();
        $(".category-box").eq(index).click();
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
        var taxtext = "(税込み)" 
        pricelist.each(function(index, val){
            total = total + val;
            
        });
        $(".pricecount").text(totaltext + total + taxtext);
    }

//patient機能--------------------------------------------------------


}); 


