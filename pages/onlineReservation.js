// const roomPrices = {
//     standard: 100,
//     deluxe: 150,
//     suite: 250
//   };
  
//   const maxGuests = {
//     standard: 2,
//     deluxe: 3,
//     suite: 4
//   };
  
//   const roomSelect = document.getElementById("room-select");
//   const guestsInput = document.getElementById("guests-input");
//   const calculateBtn = document.getElementById("calculate-btn");
//   const billResult = document.getElementById("bill-result");
  
//   calculateBtn.addEventListener("click", function() {
//     const selectedRoom = roomSelect.value;
//     const numGuests = guestsInput.valueAsNumber;
    
//     if (numGuests > maxGuests[selectedRoom]) {
//       billResult.textContent = `Error: Maximum of ${maxGuests[selectedRoom]} guests for ${selectedRoom} room.`;
//       return;
//     }
    
//     const roomPrice = roomPrices[selectedRoom];
//     const totalBill = roomPrice * numGuests;
    
//     billResult.textContent = `Total bill for ${numGuests} guests in ${selectedRoom} room: $${totalBill}`;
//   });

  const roomSelect = document.getElementById('room-select');
  const guestsInput = document.getElementById('guests-input');
  const checkInDate = document.getElementById('check-in-date');
  const checkOutDate = document.getElementById('check-out-date');
  const calculateBtn = document.getElementById('calculate-btn');
  const billResult = document.getElementById('bill-result');
  const bookNowBtn = document.getElementById('book-now-btn');
  
  function calculateBill() {
    const roomType = roomSelect.value;
    const numGuests = guestsInput.value;
    const startDate = new Date(checkInDate.value);
    const endDate = new Date(checkOutDate.value);
    const numNights = (endDate - startDate) / (1000 * 60 * 60 * 24);
    let roomPrice;
    switch (roomType) {
      case 'standard':
        roomPrice = 100;
        break;
      case 'deluxe':
        roomPrice = 150;
        break;
      case 'suite':
        roomPrice = 200;
        break;
    }
    const totalBill = roomPrice * numNights * numGuests;
    billResult.textContent = `Total Bill: $${totalBill}`;
    bookNowBtn.disabled = false;
  }
  
  calculateBtn.addEventListener('click', calculateBill);