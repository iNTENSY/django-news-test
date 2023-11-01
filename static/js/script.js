document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    let loading = false;
    let page = 1;
    let endPage = false;

    function loadMoreItems() {
        if (loading) return;
        if (endPage) return;
        loading = true;
        fetch('http://127.0.0.1:8000/api/v1/news/?page=' + page)
            .then(response => response.json())
            .then(json => {
                    json.results.map((item) => {
                        const newItem = document.createElement('div');
                        newItem.classList.add('test');
                        newItem.innerText = 'Новость: ' + (item.title) + '\n' + (item.text) + '\n';
                        contentDiv.appendChild(newItem);
                        const button = document.createElement('button');
                        button.addEventListener("click", function() {
                            location.href = "http://127.0.0.1:8000/news/" + (item.pk);
                        });
                        button.innerHTML = 'Читать';
                        newItem.appendChild(button);
                    })
                    if(json.next === null) endPage = true;
                }
            )
            .then(() => page = page + 1)
            .then(() => loading = false)
    }

    loadMoreItems();

    window.addEventListener('scroll', () => {
        if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 100) {
            loadMoreItems();
        }
    });
});