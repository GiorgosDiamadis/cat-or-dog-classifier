const predict_button = document.getElementById("predict_button");
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

predict_button.addEventListener("click", function () {
  const preview_container = document.getElementById("image_preview_cont");
  const preview_image = preview_container.querySelector(".img_preview__image");
  var canvas = document.createElement("canvas");
  canvas.width = preview_image.width;
  canvas.height = preview_image.height;

  var ctx = canvas.getContext("2d");
  ctx.drawImage(preview_image, 0, 0);

  var dataURL = canvas.toDataURL("image/jpeg").toString();

  $.ajax({
    type: "post",
    url: "/predict",
    data: dataURL,
    success: function (response) {
      modal.style.display = "block";
      document.getElementById("prediction").innerHTML =
        "Prediction: " + response;
    },
  });
});

span.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
