console.log('Hi there')

var updateBtns = document.getElementsByClassName('update-cart')

// dataset property Not Supported By Browser

// for (let i = 0; i < updateBtns.length; i++) {
//         updateBtns[i].addEventListener('click', function () {
//             var productId = this.dataset.product
//                 action = this.dataset.action
//                 console.log('product, action')
//         })

// }

function fun(obj) {
    productId = obj.getAttribute('data-product')
    action = obj.getAttribute('data-action')
    // console.log('productId', productId,'action', action)

    // console.log('User:', user)

    if (user == 'AnonymousUser') {
        console.log('user is authenticated')
        // addCookieItem(productId, action)
    } else {
        updateUserOrder(productId, action)
    }
}

// function addCookieItem(productId, action) {
//     if (action == 'add') {
//         if (cart[productId] == 'undefined') {
//             cart[productId] = { 'quantity': 1 }
//         }
//         else {
//             cart[productId]['quantity'] += 1
//         }
//     }
//     if (action == 'remove') {
//         cart[productId]['quantity'] -= 1
//         if (cart[productId]['quantity'] <= 0) {
//             delete cart[productId]
//         }
//     }

    // document.cookie = 'cart'= 'json'.stringify(cart) + ';domain = ;path=/'
// }

function updateUserOrder(productId, action) {
    console.log('User is Authenticated, sending data..')

    var url = '/update_item'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // console.log('Data', data)
            location.reload()
        });
}