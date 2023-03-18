var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var saberId = this.dataset.saber
        var action = this.dataset.action
        console.log('saberId: ' + saberId, 'action: ' + action)
        console.log('user', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged')
            document.getElementById('cart-icon').classList.add('NA')
        }
        else{
            document.getElementById('cart-icon').classList.remove('NA')
            updateUserOrder(saberId, action)
        }
    })
}


function updateUserOrder(saberId, action){
    console.log('Logged')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'saberId': saberId, 'action': action
        })
    })
        .then((response) =>{
            return response.json()
        })

        .then((data) =>{
            console.log('data:',data)
            if(action == 'remove')
            location.reload()
        })

}

