var postCount = 1;
var input = document.getElementById("image-input");
var preview = document.getElementById("image-preview");
var preview_box = document.getElementById("preview");
var form = document.getElementById("upload-details");

form.reset();

function previewImage() {

    var file = input.files[0];
    var reader = new FileReader();

    reader.addEventListener("load", function() {
        preview.src = reader.result;
        preview_box.style.visibility = "visible";
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
}

function postImage() {
    var image = input.files[0];
    var reader = new FileReader();
    reader.addEventListener("load", function() {
        addPost(reader);
    }, false);

    if (image) {
        reader.readAsDataURL(image);
    }
    
    
}

function addPost(reader) {
    var newNode = document.createElement("div");
    newNode.classList.add("postNode");
    newNode.innerHTML = `<h2>Post #${postCount++}:</h2> <img src="${reader.result}"/> <p id="image-details">${document.getElementById("photo-caption").value}</p>`;
    document.querySelector(".profile-feed").appendChild(newNode);

    form.reset();
    preview_box.style.visibility = "collapse";
}