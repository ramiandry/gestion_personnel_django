function uploadImage(idInput, idImage) {
  var input = document.getElementById(idInput);
  if (input.files.length == 0) {
    return;
  }

  let file = input.files[0];
  let url = URL.createObjectURL(file);
  document.getElementById(idImage).src = url;
}

//uploadImage('image', 'imageView');

function assignedValue(idInput, idList) {
  var id1 = document.getElementById(idInput);
  var id2 = document.getElementById(idList).textContent;
  id1.value = id2.trim().toString();
}
