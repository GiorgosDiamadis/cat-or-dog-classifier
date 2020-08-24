const input_image = document.getElementById("input_image");
const preview_container = document.getElementById("image_preview_cont");
const preview_image = preview_container.querySelector(".img_preview__image");
const preview_text = preview_container.querySelector(".img_preview__text");

input_image.addEventListener("change", function () {
  const file = this.files[0];

  if (file) {
    const reader = new FileReader();

    preview_text.style.display = "none";
    preview_image.style.display = "block";

    reader.addEventListener("load", function () {
      preview_image.setAttribute("src", this.result);
    });

    reader.readAsDataURL(file);
  } else {
    preview_text.style.display = null;
    preview_image.style.display = null;
    preview_image.setAttribute("src", "");
  }
});
