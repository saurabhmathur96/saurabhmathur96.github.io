new WOW().init();

var url = "https://api.github.com/users/saurabhmathur96/repos";
//var url = "./repos.json";
var request = new XMLHttpRequest();
var container = document.getElementById("repos");

var toggleClass = function (element, className) {
    var classes = element.className.split(" ");
    var index = classes.indexOf(className);
    if (index === -1) {
        classes.push(className);
    } else {
        classes.splice(index, 1);
    }
    element.className = classes.join(" ");
}

var showRepositories = function(parent, repositories) {
    for (var i=0; i<repositories.length; i++) {
        var container = document.createElement("div");
        container.className = "pure-u-1 pure-u-md-1-2 pure-u-lg-1-2 pure-u-xl-1-3 wow fadeIn";
        var box = document.createElement("div");
        box.className = "border-box";

        var title = document.createElement("h3");
        title.className = "heading color-2 double-pica double-small-pica-ns";
        title.textContent = repositories[i].name;
        box.appendChild(title);

        var description = document.createElement("p");
        description.className = "description english";
        description.textContent = repositories[i].description;
        box.appendChild(description);

        var footer = document.createElement("p");
        footer.className = "pure-g pica footer";
        var url = document.createElement("a");
        url.className = "pure-u-1-2";
        url.textContent = "[Code]"
        url.href = repositories[i].html_url;
        footer.appendChild(url);

        var language = document.createElement("em");
        language.className = "pure-u-1-2";
        language.style = "text-align: right";
        language.textContent = repositories[i].language;
        footer.appendChild(language);

        box.appendChild(footer);
        container.appendChild(box);
        parent.appendChild(container);
    }
    

}

request.open("GET", url, true);
request.setRequestHeader("Content-Type", "application/json");
request.onload = function (event) {
    var response = JSON.parse(event.target.response);
    var repositories = response.filter(function (e) { 
        return !e.fork && e.description !== null && e.description.length !== 0; 
    }).sort(function (a, b) {
        return new Date(b.pushed_at) - new Date(a.pushed_at); 
    });
    showRepositories(container, repositories);
    
}
request.send();