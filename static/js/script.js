// document.addEventListener('DOMContentLoaded', () => {
//     const contentDiv = document.getElementById('content');
//     let loading = false;
//
//     function loadMoreItems() {
//         if (loading) return;
//         loading = true;
//
//         fetch('https://jsonplaceholder.typicode.com/todos')
//             .then(response => response.json())
//             .then(json => json.map((item) => {
//                 const newItem = document.createElement('div');
//                 newItem.innerText = 'Элемент ' + (item.title);
//                 contentDiv.appendChild(newItem);
//             }))
//             .then(() => loading = false)
//     }
//
//     loadMoreItems();
//
//     window.addEventListener('scroll', () => {
//         if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 100) {
//             loadMoreItems();
//         }
//     });
// });
document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    let loading = false;
    let limit = 3;

    function loadMoreItems() {
        if (loading) return;
        loading = true;
        fetch('http://127.0.0.1:8000/api/v1/news/?page=' + limit)
            .then(response => response.json())
            .then(json => json.map((item) => {
                const newItem = document.createElement('div');
                newItem.classList.add('test');
                newItem.innerText = 'Элемент ' + (item.results.title);
                contentDiv.appendChild(newItem);
            }))
            .then(() => limit = limit + 1)
            .then(() => loading = false)
    }

    loadMoreItems();

    window.addEventListener('scroll', () => {
        if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 100) {
            loadMoreItems();
        }
    });
});