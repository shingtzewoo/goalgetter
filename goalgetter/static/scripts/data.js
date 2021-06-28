function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.status);
    }
    return response.json().then(function(data) {
        console.log(data)
    });
}

function submit(task) {
    
    let items = getItemByClass(task);
    
    for (let i = 0 ; i < items.length; i++) {

        items[i].addEventListener("click", function() {

                    fetch("/home", {
                        method: "POST",
                        body: JSON.stringify({
                            id: items[i].value,
                            complete: items[i].getAttribute('aria-checked'),
                        }),
                        headers: {
                            'Content-type': 'application/json; charset=UTF-8'
                        }
                    })
                    .then(handleErrors)
                    .catch(function(error) {
                        console.log(error);
                    })
        })
    }
}