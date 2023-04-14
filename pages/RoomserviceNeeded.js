
// Define an array of room service objects
let roomServices = [
    { roomNumber: 691, servicesNeeded: "Laundry" },
    { roomNumber: 692, servicesNeeded: "Condiments" },
    { roomNumber: 693, servicesNeeded: "Massage" },
    { roomNumber: 694, servicesNeeded: "Room Cleaning" },
    { roomNumber: 696, servicesNeeded: "Clean Towels" },
    { roomNumber: 696, servicesNeeded: "Bed linen change" }
  ];
  
  // Loop through the room services array and create table rows for each service
  let servicesTable = document.getElementById("services-table");
  for (let i = 0; i < roomServices.length; i++) {
    let row = servicesTable.insertRow(i);
    let roomNumberCell = row.insertCell(0);
    let servicesNeededCell = row.insertCell(1);
    let checkboxCell = row.insertCell(2);
    
    roomNumberCell.innerHTML = roomServices[i].roomNumber;
    servicesNeededCell.innerHTML = roomServices[i].servicesNeeded;
    
    // Add checkbox with event listener to remove row when checked
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", function() {
      if (this.checked) {
        let row = this.parentNode.parentNode;
        row.parentNode.removeChild(row);
      }
    });
    checkboxCell.appendChild(checkbox);
  }
  
  const toggleButton = document.getElementsByClassName('toggle-button')[0]
  const navbarLinks = document.getElementsByClassName('navbar-links')[0]
  
  toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
  })
