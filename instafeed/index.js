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
