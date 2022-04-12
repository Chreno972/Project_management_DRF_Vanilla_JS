function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var active_item = null;

buildList()

function buildList(){
    var wrapper = document.getElementById('list_wrapper')
    wrapper.innerHTML = ''

    var nb_tasks = document.getElementById('nb_of_tasks')

    var url = "http://127.0.0.1:8000/api/task-list/"

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data) {
        console.log('Data:', data)

        var list = data
        for (var i in list) {

            title = `<span class="title">${list[i].title}</span>`

            var item = `
                <div id="data_row_${i}" class="task_wrapper flex_wrapper">
                    <div style="width:60%; text-align:left;">
                        ${title}
                    </div>
                    <div class="the_buttons">
                        <button style="width:90px; padding:15px;background-color:#4285F4;" class="edit">Edit</button>
                        <button style="width:90px; padding:15px;background-color: #DB4437;" class="delete">Delete</button>
                    </div>
                </div>
            `
            wrapper.innerHTML += item;
        }

        for (var i in list) {
            let editBtn = document.getElementsByClassName('edit')[i]
            let deleteBtn = document.getElementsByClassName('delete')[i]
            let title = document.getElementsByClassName('title')[i]

            if (list[i].completed) {
                var parent = document.getElementById(`data_row_${i}`)
                parent.style.textDecoration = 'line-through'
                parent.style.opacity = '0.2'
            }

            editBtn.addEventListener('click', (function(item) {
                return function() {
                    edit_item(item)
                }
            })(list[i]))


            deleteBtn.addEventListener('click', (function(item) {
                    return function() {
                        delete_item(item)
                    }
                    
            })(list[i]))


            title.addEventListener('click', (function(item) {
                return function() {
                    strike_unstrike(item)
                }
                
            })(list[i]))
        }

        nb_tasks.innerHTML = list.length
    })
}

var form_wrapper = document.getElementById('form_wrapper')

form_wrapper.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('Form submitted')
    var url = "http://127.0.0.1:8000/api/task-create/"

    if (active_item != null) {
        var url = `http://127.0.0.1:8000/api/task-update/${active_item.id}/`
        active_item = null
    }

    var title = document.getElementById('title').value
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                title: title
            })
        }
    ).then(function(response) {
        buildList()
        document.getElementById('form').reset()
    })
})

// EDIT ITEM

function edit_item(item) {
    active_item = item
    document.getElementById('title').value = active_item.title
}

// DELETE ITEM

function delete_item(item) {
    fetch(`http://127.0.0.1:8000/api/task-delete/${item.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            "X-Requested-With": "XMLHttpRequest",
            'X-CSRFToken': csrftoken,
        },
    }).then((response) => {
        buildList()
    })
}

// STRIKE UNSTRIKE ITEM

function strike_unstrike(item) {
    item.completed = !item.completed
    fetch(`http://127.0.0.1:8000/api/task-update/${item.id}/`, {
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'title': item.title, 'completed': item.completed})
    }).then((response) => {
        buildList()
    })
}