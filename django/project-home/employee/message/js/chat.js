var milkcocoa = new MilkCocoa('xxxxxxxxx.mlkcca.com');
//データストアの指定
var ds = milkcocoa.dataStore('messages');

$('#msg_submit').on('click',function(){


    var message = $('#msg_txt').val();

    //メッセージの送信
    ds.send({message : message});

    //メッセージの保存
    ds.push({message : message});

    $('#msg_txt').val('');
})

ds.on('send', function(sended) {
    $('#msg_area').append('<div class="alert alert-warning" role="alert">'+ sended.value.message +'</div>');
});