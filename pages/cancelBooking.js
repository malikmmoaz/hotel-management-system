// Sample reservations data
const reservations = [
    { id: 1, name: "Reservation 1", date: "2023-04-01" },
    { id: 2, name: "Reservation 2", date: "2023-04-05" },
    { id: 3, name: "Reservation 3", date: "2023-04-10" },
    { id: 4, name: "Reservation 4", date: "2023-04-15" },
  ];

  const reservationsContainer = document.getElementById("reservations-container");
  
  
  reservations.forEach(reservation => {
    const reservationItem = document.createElement("div");
    reservationItem.classList.add("reservation-item");
    
    const reservationName = document.createElement("h2");
    reservationName.textContent = reservation.name;
    reservationItem.appendChild(reservationName);
    
    const reservationDate = document.createElement("p");
    reservationDate.textContent = reservation.date;
    reservationItem.appendChild(reservationDate);
    
    const cancelButton = document.createElement("button");
    cancelButton.classList.add("cancel-button");
    cancelButton.textContent = "Cancel Reservation";
    reservationItem.appendChild(cancelButton);
    
    cancelButton.addEventListener("click", () => {
      reservationItem.remove();
    });
    
    reservationsContainer.appendChild(reservationItem);
  });


  const toggleButton = document.getElementsByClassName('toggle-button')[0]
  const navbarLinks = document.getElementsByClassName('navbar-links')[0]
  
  toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
  })