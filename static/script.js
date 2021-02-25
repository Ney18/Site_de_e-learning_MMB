const url_api = 'http://localhost:5000/api/query_data/js';


function add_data_html(data_list) {
    document.querySelector('section#data').innerHTML = '';
    for(let key in data_list) {
        document.querySelector('section#data').innerHTML += `<div> ${data_list[key].lien}
        <p>${data_list[key].titre}</p>
        <p>${data_list[key].videaste}</p>
        <p>${data_list[key].vue} vues</p>
        <p>${data_list[key].duree}</p>
        <p>${data_list[key].theme}</p> </div>`;
    }
}


async function getData(url) {
    const response = await fetch(url);
    let data = await response.json()
    console.log(data);
    add_data_html(data)
    return;
}

getData(url_api);
