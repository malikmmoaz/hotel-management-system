const hotels = [
    {
      name: "Hotel A",
      price: 100,
      rating:4.1,
      image: "browsehotel1.jpg"
    },
    {
      name: "Hotel B",
      price: 150,
      rating:4.2,
      image: "browsehotel2.jpg"
    },
    {
      name: "Hotel C",
      price: 200,
      rating:4.3,
      image: "browsehotel3.jpg"
    },
    {
        name: "Hotel D",
        price: 250,
        rating:4.4,
        image: "browsehotel4.jpg"
    },
    {
        name: "Hotel E",
        price: 300,
        rating:4.5,
        image: "browsehotel5.jpg"
    },
    {
        name: "Hotel F",
        price: 350,
        rating:4.6,
        image: "browsehotel6.jpg"
    },
    {
        name: "Hotel G",
        price: 400,
        rating:4.7,
        image: "browsehotel7.jpg"
    },
    {
        name: "Hotel H",
        price: 450,
        rating:4.8,
        image: "browsehotel8.jpg"
    }

  ];
  
  const hotelsContainer = document.querySelector("#hotels");
  
  hotels.forEach(hotel => {
    const hotelDiv = document.createElement("div");
    hotelDiv.classList.add("hotel");
  
    const hotelImage = document.createElement("img");
    hotelImage.src = "../images/" + hotel.image;
    hotelDiv.appendChild(hotelImage);
  
    const hotelName = document.createElement("h2");
    hotelName.textContent = hotel.name;
    hotelDiv.appendChild(hotelName);
  
    const hotelPrice = document.createElement("p");
    hotelPrice.textContent = "Starting from Rs" + hotel.price;
    hotelDiv.appendChild(hotelPrice);

    const hotelRating = document.createElement("div");
    hotelRating.classList.add("hotel-rating");
    const ratingNumber = document.createElement("span");
    ratingNumber.textContent = hotel.rating;
    hotelRating.appendChild(ratingNumber);
    hotelDiv.appendChild(hotelRating);
  
    const hotelButton = document.createElement("button");
    hotelButton.textContent = "Book Now";
    hotelDiv.appendChild(hotelButton);
  
    hotelsContainer.appendChild(hotelDiv);
  });