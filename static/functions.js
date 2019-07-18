// user activity
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

// search movie
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

// get movies in playlist
function content(button) {
    let buttonID = button.getAttribute("href").substring(1);
    let playlistName = button.innerHTML;
    let sendData = "playlist=" + playlistName;

    // create table
    let tbl = document.createElement('table');
    tbl.setAttribute("id", "movie-table")
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
            let imdbLink = "https://www.imdb.com/title/" + movie["guid"];

            let row = document.createElement('tr');
            row.setAttribute("scope", "col");

            // add title
            let title = document.createElement('td');
            let aTitle = document.createElement('a');
            aTitle.innerHTML = movie["title"];
            aTitle.setAttribute('href', imdbLink);
            aTitle.setAttribute('target', "_blank");

            title.appendChild(aTitle);
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

// select all button
function selectAllUsers(self) {
    let checkboxes = document.getElementsByName('user-checkbox');

    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = true;
    }
};

// add playlist to plex
$(document).ready(function () {
    $("#addPlaylistButton").click(function () {

        // Hide previous alerts
        $(".alert").hide();

        let imdb = document.getElementById('imdb-ls').value;
        let name = document.getElementById('playlist-name').value;
        let section = document.getElementById('select-section').value;

        let users = document.getElementsByName('user-checkbox');
        let checkedUsers = [];

        for (let i = 0; i < users.length; i++) {
            if (users[i].checked) {
                checkedUsers.push(users[i].value);
            };
        };

        $.post("/addplaylisttoplex", {
            imdb: imdb,
            name: name,
            section: section,
            users: JSON.stringify(checkedUsers)
        }, function (data) {

            if (data) {
                $('#playlist-success').show();
            } else {
                $('#playlist-failed').show();
            }

        });
    });
});

// show spinner while adding playlist
$(document).ready(function () {

    $(document).ajaxStart(function () {
        $("#load-playlist").css('visibility', 'visible');
    }).ajaxStop(function () {
        $("#load-playlist").css('visibility', 'hidden');
    })
})
