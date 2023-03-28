// Sample reservations data
const reservations = [
    { id: 1, name: "Reservation 1", date: "2023-04-01" },
    { id: 2, name: "Reservation 2", date: "2023-04-05" },
    { id: 3, name: "Reservation 3", date: "2023-04-10" },
  ];
  
  // Get the reservations container element
  const reservationsContainer = document.getElementById("reservations-container");
  
  // Add each reservation as a new item to the reservations container
  reservations.forEach(reservation => {
    // Create a new div element for the reservation item
    const reservationItem = document.createElement("div");
    reservationItem.classList.add("reservation-item");
    
    // Add the reservation details to the item
    const reservationName = document.createElement("h2");
    reservationName.textContent = reservation.name;
    reservationItem.appendChild(reservationName);
    
    const reservationDate = document.createElement("p");
    reservationDate.textContent = reservation.date;
    reservationItem.appendChild(reservationDate);
    
    // Add a cancel button to the item
    const cancelButton = document.createElement("button");
    cancelButton.classList.add("cancel-button");
    cancelButton.textContent = "Cancel Reservation";
    reservationItem.appendChild(cancelButton);
    
    // Add a click event listener to the cancel button to remove the reservation item from the page
    cancelButton.addEventListener("click", () => {
      reservationItem.remove();
    });
    
    // Add the reservation item to the reservations container
    reservationsContainer.appendChild(reservationItem);
  });