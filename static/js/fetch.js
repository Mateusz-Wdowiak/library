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

function updateQuantity(buttonElement) {
    const bookDiv = buttonElement.closest('.book');
    const id = bookDiv.dataset.id;
    const quantityInput = bookDiv.querySelector('input[type="number"]');
    const quantityToDecrease = Number(quantityInput.value);

    if (quantityToDecrease <= 0 || !Number.isInteger(quantityToDecrease)) {
        alert('Proszę podać prawidłową ilość (liczba całkowita większa od 0)');
        return Promise.reject();
    }

    return fetch(`/api/books/${id}`)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(err.error || 'Error fetching data');
                });
            }
            return response.json();
        })
        .then(data => {
            const currentStock = data.quantity;
            console.log(quantityInput)
            console.log(currentStock)
            if (quantityToDecrease > currentStock) {
                throw new Error(`Zbyt duże zamówienie, stan książki: ${currentStock}`);
            }

            return fetch(`/api/books/${id}`, {
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ quantity: -quantityToDecrease })
            });
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(err.error || 'Update failed');
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            alert('Zamówienie zaktualizowane pomyślnie!');
        })
        .catch(error => {
            console.error("Error:", error);
            alert(error.message || 'Wystąpił błąd');
            throw error;
        });
}

function deleteBook(id) {
    fetch(`/api/books/${id}`, {
        method: "DELETE",
        headers: { 'Content-Type': 'application/json' },
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("error", error))
}


