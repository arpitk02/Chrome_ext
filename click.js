document.getElementById("send").addEventListener("click", function send() {
  var input = document.getElementById("input").value;
  alert(input);
  console.log("input", input);
  fetch("http://localhost:5000/predict").then((response) => response.json());
});
