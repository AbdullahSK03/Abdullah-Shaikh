const quote = document.getElementById('quote')
const api = "https://api.quotable.io/random"



async function get_quote(url){
    const response = await fetch(url)
    var data = await response.json()
    console.log(data)
    quote.innerHTML = data.content
    author.innerHTML = data.author
}

get_quote(api)