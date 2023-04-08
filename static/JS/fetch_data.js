let category = document.querySelector('#category');
let fetch_data = document.querySelector('#fetch_data');
let download = document.querySelector('#download');

fetch_data.addEventListener('click', function(){

    $(document).ajaxSend(function(){
        $("#loader").fadeIn(500);
    })

    $.ajax({

        url: '/fetch/wuzzuf/',
        data: {'category':category.value},
        dataType: 'json',
        success: function(data){

            console.log('done');

        }

    }).done(function(){
        setTimeout(function(){
            $("#loader").fadeOut(500);
            download.style.display = 'block';
        }, 1000);
        
    });
})