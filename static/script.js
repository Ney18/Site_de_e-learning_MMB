// const url_api = 'http://localhost:5000/video_theme?theme=javascript';
const url_api = 'http://localhost:5000/database';
let data_api = "";

document.getElementById('search').addEventListener('click', e => {
    let value_search = document.getElementById('input_search').value.toLowerCase();
    console.log('when click to seacrh', value_search)
    let list_theme = null;
    list_theme = data_api.filter( x => x.theme === value_search )
    console.log("lit_theme search bar =", list_theme)
    add_data_html(list_theme);
});

document.querySelectorAll('i.main_icon.fab').forEach(e => {
    e.addEventListener("click", () => {
        let list_theme = null;
        list_theme = data_api.filter( x => x.theme === e.dataset.theme );
        
        if ( e.dataset.theme === 'all' ) {
            add_data_html(data_api);
            

        } else {
            add_data_html(list_theme);
        }
    })
});

function add_data_html(data_list) {
    const div_main = document.querySelector('div.main_container');
    div_main.innerHTML = '';
    if ( data_list <= 0 ) {
        div_main.innerHTML += "This catagory doesn't have video yet";
        
        return;
    } else {
        for(let key in data_list) {
            div_main.innerHTML += `<div class="video_link">
            ${data_list[key].link}
            <p class="title_video">${data_list[key].title}</p>
            </div>`;
            
        }

    }
}


async function getData(url) {
    const response = await fetch(url);
    data_api = await response.json()
    add_data_html(data_api);
    console.log(data_api)
    return data_api;
}

getData(url_api);
//getData('http://localhost:5000//database');
//getData('http://localhost:5000/video_theme?theme=python')