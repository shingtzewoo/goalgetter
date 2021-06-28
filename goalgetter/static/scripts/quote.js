/*
Interact with Quotes REST API https://quotes.rest/ and output their quote of the day
Help received regarding this topic: https://dev.to/ramonak/javascript-how-to-access-the-return-value-of-a-promise-object-1bck
*/

const get_quote_of_the_day = fetch("https://quotes.rest/qod", { method: "GET" })
  .then((response) => response.json())
  .then((data) => {
    return data;
  })
  .catch(error => {console.log('Error with fetching API', error)});

const get_quote = async () => {
  const res = await get_quote_of_the_day;
  console.log(res);
  quote = document.getElementById("quote");
  quote.innerHTML = res["contents"]["quotes"][0]["quote"]
};