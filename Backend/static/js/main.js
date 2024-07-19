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
    document.getElementById('loader').style.display = 'flex';
    const depositData = {
        'receiver_account_number': document.getElementById('receiver-account-number').value,
        'amount': document.getElementById('sending-amount').value,
    }
    if (depositData.receiver_account_number.length < 10) {
        alert('Receiver Account Number must be 10 digits')
        return;
        
    }
    if (depositData.amount < 1) {
        alert('Amount must be greater than 0')
        return;
    }
    if (depositData.amount == '') {
        alert('Amount must be greater than 0')
        return;
    }
    if (depositData.receiver_account_number.length>=10 && depositData.amount >= 1) {
        document.getElementById('loader').style.display = 'flex';
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
        },
        complete: function () {
            document.getElementById('loader').style.display = 'none';
            document.getElementById('receiver-account-number').value = '';
            document.getElementById('sending-amount').value= '';


            alert('Transaction Successful')
            location.reload();
    }
    });
    }


    return false;
  }
