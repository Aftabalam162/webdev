function previewImage() {
    var input = document.getElementById("image-input");
    var preview = document.getElementById("image-preview");

    var file = input.files[0];
    var reader = new FileReader();

    reader.addEventListener("load", function() {
        preview.src = reader.result;
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
}
