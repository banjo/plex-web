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

};

function search() {
    let query = document.getElementById("query").value;

    $.get("/search?query=" + query, function (data) {
        let ul = document.getElementById("query-list");
        ul.innerHTML = "";

        data = data["movies"];

        for (let i = 0; i < data.length; i++) {
            let movie = data[i];

            let li = document.createElement("li");
            li.classList.add("list-group-item");
            li.appendChild(document.createTextNode(movie));

            ul.appendChild(li);
        }

    })

};

function content(button) {
    let buttonID = button.getAttribute("href").substring(1);
    let playlistName = button.innerHTML;
    let sendData = "playlist=" + playlistName;

    // create table
    let tbl = document.createElement('table');
    tbl.classList.add('table')

    // create parts of table
    let thead = document.createElement('thead');
    let tr = document.createElement('tr');

    // create headers

    let th1 = document.createElement('th');
    th1.setAttribute('scope', 'col')
    th1.innerHTML = "Movie";

    let th2 = document.createElement('th');
    th2.setAttribute('scope', 'col')
    th2.innerHTML = "Year";

    let th3 = document.createElement('th');
    th3.setAttribute('scope', 'col')
    th3.innerHTML = "Rating";

    // create body
    let tbody = document.createElement('tbody');

    // add body element
    tbl.appendChild(tbody);

    // add header elements
    tr.appendChild(th1);
    tr.appendChild(th2);
    tr.appendChild(th3);
    thead.appendChild(tr);
    tbl.appendChild(thead);


    $.get("/playdata?" + sendData, function (data) {
        let elem = document.getElementById(buttonID);
        elem.innerHTML = "";

        for (let i = 0; i < data.length; i++) {
            movie = data[i];

            let row = document.createElement('tr');
            row.setAttribute("scope", "col");

            // add title
            let title = document.createElement('td');
            title.innerHTML = movie["title"];
            row.appendChild(title);

            // add year
            let year = document.createElement('td');
            year.innerHTML = movie["year"];
            row.appendChild(year);

            // add rating
            let rating = document.createElement('td');
            rating.innerHTML = movie["rating"];
            row.appendChild(rating);

            tbody.appendChild(row);
        }

        elem.appendChild(tbl);
    })

};
