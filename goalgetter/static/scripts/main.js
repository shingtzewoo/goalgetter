function getItemByClass(cls) {
    let items = document.getElementsByClassName(cls)
    return items
}

function animation(cls, newClass1, newClass2) {

    /* This reusable function helps add new classes to DOM objects for animation purposes. */
    let items = getItemByClass(cls) 

    for (let i = 0 ; i < items.length; i++) {

        items[i].addEventListener("mouseenter", function(event) {

            event.target.classList.add(newClass1);
            event.target.classList.remove(newClass2);
        
        }, false);

        items[i].addEventListener("mouseleave", function(event) {

            event.target.classList.add(newClass2);
            event.target.classList.remove(newClass1);
        
        }, false);

     }
}

function chosen(checkboxes, cls) {

    /* This function adds borders to the checkboxes containing the values */

    let items1 = document.querySelectorAll(checkboxes);
    let items2 = getItemByClass(cls);

    count = 0;

    for(let i = 0; i < items1.length; i++) {

        items1[i].addEventListener("change", function() {

                if (items1[i].checked) {
                    items2[i].style.border = "1px solid silver";
                    items2[i].style.borderRadius = "25px"
                    if (count < 3) {
                        count+=1;
                    }
                    else {
                        items1[i].checked = false;
                        items2[i].style.border = null;
                        alert("Please choose only 3 values");
                    }
                } else if (items1[i].checked == false && count > 0) {
                    items2[i].style.border = null;
                    if (count > 0) {
                        count-=1;
                    }
                }
        }, false);
    }
}

function set_disable(cls1, cls2) {

    let event_class = getItemByClass(cls1);
    let to_disable_class = getItemByClass(cls2);

    for(let i = 0; i < event_class.length; i++) {

        event_class[i].addEventListener("change", function() {

                if (event_class[i].value.includes('every')) {
                    to_disable_class[i].disabled = true;
                }
                else {
                    to_disable_class[i].disabled = false;
                }

        }, false);
    }
}