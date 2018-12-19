
function searchPlant() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search_plant");
  filter = input.value.toUpperCase();
  table = document.getElementById("zero_config");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td1 = tr[i].getElementsByTagName("td")[0];
    td2 = tr[i].getElementsByTagName("td")[1];
    if (td1 || td2) {
      txtValue1 = td1.textContent || td1.innerText;
      txtValue2 = td2.textContent || td2.innerText;
      if (txtValue1.toUpperCase().indexOf(filter) > -1 || txtValue2.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}

function searchPlantDrop(){
  var input = document.getElementById("search-dropdown-plant");
  var filter = input.value.toLowerCase();
    $(".dropdown-menu li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(filter) > -1)
    });
}