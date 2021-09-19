function showDescription(description) {
    var text = document.getElementById('description')
    text.innerHTML = "<p style='overflow-wrap: break-word; width: 100%;'>"+ description +"</p>"
    + "<button " + 'class="description-button"' + "onclick=" + '"hideDescription('+ "'" + description + "'" + ')">↑ Hide description ↑</button>'
};
function hideDescription(description) {
    var text = document.getElementById('description')
    text.innerHTML = "<p style='overflow-wrap: break-word; width: 100%;'>" + description.substring(0,100) + "..." + "</p>"
    + "<button " + 'class="description-button"' + "onclick=" + '"showDescription(' + "'" +  description + "'" + ')">↓ Show full description ↓</button>'
};