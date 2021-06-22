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
            
            switch(items[i].getAttribute('aria-checked')) {

                case "true":
                    fetch("/home", {
                        method: "POST",
                        body: JSON.stringify({
                            id: items[i].value,
                            complete: true
                        }),
                        headers: {
                            'Content-type': 'application/json; charset=UTF-8'
                        }
                    })
                    .then(handleErrors)
                    .catch(function(error) {
                        console.log(error);
                    });
                
                case "false":
                    fetch("/home", {
                        method: "POST",
                        body: JSON.stringify({
                            id: items[i].value,
                            complete: false
                        }),
                        headers: {
                            'Content-type': 'application/json; charset=UTF-8'
                        }
                    })
                    .then(handleErrors)
                    .catch(function(error) {
                        console.log(error);
                    });
            }
        })
    }
}