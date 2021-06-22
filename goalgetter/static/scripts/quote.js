function get_quote_of_the_day() {
    /*
    Fetching quote of the day from They Said So Quotes API
    */
    fetch("https://quotes.rest/qod", {
        method: "GET",
    })
    .then(handleErrors)
    .catch(function(error) {
        console.log(error);
    });
}