// open close menu
let menuBtn = document.getElementById('menu_btn');
let closeBtn = document.getElementById('btn_close');
let menu = document.getElementById("sidebar");
menuBtn.addEventListener("click",()=>{
    menu.classList.add("show_sidebar")
})

closeBtn.addEventListener("click",()=>{
    menu.classList.remove("show_sidebar")
})


// form preventdefault submit

function mySubmitFunction(e) {
    e.preventDefault();
    const depositData = {
        'receiver_account_number': document.getElementById('receiver-account-number').value,
        'amount': document.getElementById('sending-amount').value,
    }

    $.ajax({
        type: 'POST',
        url: '/api/send/',
        data: JSON.stringify(depositData),
        contentType: 'application/json',
        success: function (response) {
            console.log(response)
            if (response.status == 200) {
                alert(response.message)
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });

function myDepositFunction(e) {
        e.preventDefault();
        const depositData = {
            'amount': document.getElementById('self-deposit-amount').value,
        }

        $.ajax({
            type: 'POST',
            url: '/api/deposit/',
            data: JSON.stringify(depositData),
            contentType: 'application/json',
            success: function (response) {
                console.log(response)
                if (response.status == 200) {
                    alert(response.message)
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    return false;
  }
