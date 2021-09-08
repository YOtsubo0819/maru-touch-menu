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

//注文priceCount
    var priceCount = 0;
    for (var i = 0; i < $('.order-box').length; i++ ){
        $('.pricecount').text(i);
    }
    

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
    });

//注文削除
    $(document).on('click', '.order-box', function(){
        $(this).remove();
    });


    $(".cancel-button").on("click", function(){
        $(".order-box").remove();
    });


//patient機能--------------------------------------------------------

$('.first-patient-input').hide();
$('.return-patient-input').hide();
$('.ic-or-noneic-flex-box').hide();


$('#first').on("click", function(){
    $('.first-or-return-flex-box').hide();
    $('.first-patient-input').show();
});

$('#return').on("click", function(){
    $('.first-or-return-flex-box').hide();
    $('.ic-or-noneic-flex-box').show();

});

$('#icnone').on("click", function(){
    $('.ic-or-noneic-flex-box').hide();
    $('.return-patient-input').show();
});

}); 


