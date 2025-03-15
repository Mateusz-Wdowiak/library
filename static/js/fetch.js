function addBook(body) {
    fetch('/api/books', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}

function getBooksList() {
    fetch('/api/books', {
        method: "GET",
        headers: { 'Content-Type': 'application/json' },
        body: {}
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}

function getBook(id) {
    fetch('/api/books', {
        method: "GET",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(id)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}


function updateBook(body) {
    fetch('/api/books', {
        method: "PUT",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}


function deleteBook(id) {
    fetch('/api/books', {
        method: "DELETE",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(id)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}
