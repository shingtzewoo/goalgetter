function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.status);
    }
    return response.json();
}

function submit(checkbox, task) {
    
    let items1 = getItemByClass(checkbox);
    
    for (let i = 0 ; i < items.length; i++) {

        items1[i].addEventListener("click", function() {
            
            switch(items1[i].getAttribute('aria-checked')) {

                case "true":
                    fetch("/page/home", {
                        method: "POST",
                        body: JSON.stringify({
                            id: items1[i].value,
                            complete: true
                        })
                        headers: {
                            'Content-type': 'application/json; charset=UTF-8'
                        }
                    })
                    .then(handleErrors)
                    .catch(function(error) {
                        console.log(error);
                    });
                
                case "false":
                    fetch("/page/home", {
                        method: "POST",
                        body: JSON.stringify({
                            id: items1[i].value,
                            complete: false
                        })
                        headers: {
                            'Content-type': 'application/json; charset=UTF-8'
                        }
                    })
                    .then(handleErrors)
                    .catch(function(error) {
                        console.log(error);
                    });
            }
        }
    }
}