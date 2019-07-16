function update_activity() {

    list_element = document.getElementById("user-list");
    li = list_element.getElementsByTagName("li");

    for (let i = 0; i < li.length; ++i) {
        user = li[i].innerHTML;

        $.post("/update_activity?user=" + user, function (answer) {
            console.log(answer)
        });

    }

}
