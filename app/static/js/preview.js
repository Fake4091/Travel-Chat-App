const fileSelector = document.getElementById("img");
fileSelector.addEventListener("change", (event) => {
  const fileList = event.target.files;
  console.log(fileList);
});
