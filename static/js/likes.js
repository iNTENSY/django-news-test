

let like_button = document.getElementById('like')

like_button.addEventListener('click', function () {
    $.ajax({
        url: "{% url 'api:like' %}",
        type: "POST",
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            obj: '{{ post.pk }}',
            status: 'like'
        // any other data you want to send
    },
        success: function (response) {
            console.log(response);
        }
        })
})