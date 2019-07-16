function update_activity() {

    let list_element = document.getElementById("user-list");
    let li = list_element.getElementsByTagName("li");

    for (let i = 0; i < li.length; ++i) {
        user = li[i].innerHTML;

        $.get("/update_activity?username=" + user, function (data) {
            if (data) {
                li[i].classList.add("active");
                li[i].innerHTML = data["user"] + " - " + data["show"];
            }

        });

    }

}

function search() {
    let query = document.getElementById("query").value;

    $.get("/search?query=" + query, function (data) {
        let ul = document.getElementById("query-list");
        ul.innerHTML = "";

        data = data["movies"];

        for (let i = 0; i < data.length; i++) {
            let movie = data[i];

            let li = document.createElement("li");
            li.classList.add("list-group-item")
            li.appendChild(document.createTextNode(movie));

            ul.appendChild(li);
        }

    })

};
