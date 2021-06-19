function getItemByClass(cls) {
    let items = document.getElementsByClassName(cls)
    return items
}

function animation(cls, newClass1, newClass2) {

    /* Add new classes to the same item. */
    
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

    /* Adds borders to the checkboxes in the values questionnaire page */

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

    /* Disables targeted class when another class has an change event triggered */

    let event_class = getItemByClass(cls1);
    let to_disable_class = getItemByClass(cls2);

    for(let i = 0; i < event_class.length; i++) {

        event_class[i].addEventListener("change", function() {

                if (event_class[i].value.includes("every")) {
                    to_disable_class[i].disabled = true;
                }
                else {
                    to_disable_class[i].disabled = false;
                }

        }, false);
    }
}

function tickmark_task(class1, class2, class3, newClass1, newClass2,) {

    /* 
    Adding checkmarks to the divs and adding a line-through to the text
    . */
    
    let items1 = getItemByClass(class1)
    let items2 = getItemByClass(class2);
    let items3 = getItemByClass(class3);
    
    for (let i = 0 ; i < items1.length; i++) {

    
        items1[i].addEventListener("click", function() {
        
            switch(items1[i].getAttribute('aria-checked')) {

                case "true":
            
                    items1[i].setAttribute('aria-checked', "false");
                    items2[i].classList.remove(newClass1);
                    items3[i].classList.add(newClass2) 
                    break;

                case "false":

                    items1[i].setAttribute('aria-checked', "true");
                    items2[i].classList.add(newClass1);
                    items3[i].classList.remove(newClass2);
                    break;

            }
        },  false);

     }
}

