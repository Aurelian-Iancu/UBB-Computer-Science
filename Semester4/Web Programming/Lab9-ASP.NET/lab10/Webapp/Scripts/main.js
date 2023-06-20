class EventHandling {
    constructor() {
        this.currentPage = 0;
        this.currentPage2 = 0;
        this.currentPageBooked = 0;
        const thisObject = this;

        this.selectedId = -1;
        this.selectedIdBooked = -1;

        this.category = "all";
        this.type = "all";
        this.price = 0;
        this.hotel = "all";

        this.start = "none";
        this.end = "none";

        this.bookCateg = "";
        this.bookType = "";
        this.bookPrice = "";
        this.bookHotel = "";

        thisObject.loadRooms(thisObject.currentPage, thisObject);
        thisObject.loadRoomsBooked(thisObject.currentPage2, thisObject);

        document.getElementById("home-page").addEventListener("click", this.homeBtnClicked);
        document.getElementById("db-insert").addEventListener("click", this.dbInsertBtnClicked);
        document.getElementById("db-update").addEventListener("click", this.dbUpdateBtnClicked);
        document.getElementById("db-delete").addEventListener("click", this.dbDeleteBtnClicked);

        document.getElementById("prev-rooms-btn").addEventListener("click", function () {
            if (thisObject.currentPage > 0) {
                thisObject.currentPage--;
                thisObject.loadRooms(thisObject.currentPage, thisObject);
            }
        });

        document.getElementById("next-rooms-btn").addEventListener("click", function () {
            thisObject.currentPage++;
            thisObject.loadRooms(thisObject.currentPage, thisObject);
        });

        document.getElementById("prev-rooms-btn2").addEventListener("click", function () {
            if (thisObject.currentPage2 > 0) {
                thisObject.currentPage2--;
                thisObject.loadRoomsBooked(thisObject.currentPage2, thisObject);
            }
        });

        document.getElementById("next-rooms-btn2").addEventListener("click", function () {
            thisObject.currentPage2++;
            thisObject.loadRoomsBooked(thisObject.currentPage2, thisObject);
        });

        document.getElementById("filter-button").addEventListener("click", function () {

            thisObject.category = document.getElementById("room-category").value;
            thisObject.type = document.getElementById("room-type").value;
            thisObject.price = document.getElementById("room-price").value;
            thisObject.hotel = document.getElementById("room-hotel").value;

            thisObject.loadRooms(thisObject.currentPage, thisObject);

        });

        document.getElementById("book-button").addEventListener("click", () => {
            if (this.selectedId <= 0) {
                window.alert("First select the room to be reserved!");
                return;
            }

            this.start = document.getElementById("room-startDate").value;
            this.end = document.getElementById("room-endDate").value;


            const selectedRow = document.querySelector("#cols tr.selected");
            if (selectedRow) {
                const categoryCell = selectedRow.querySelector("td:first-child");
                const typeCell = selectedRow.querySelector("td:nth-child(2)");
                const priceCell = selectedRow.querySelector("td:nth-child(3)");
                const hotelCell = selectedRow.querySelector("td:nth-child(4)");

                thisObject.bookCateg = categoryCell.textContent;
                thisObject.bookType = typeCell.textContent;
                thisObject.bookPrice = priceCell.textContent;
                thisObject.bookHotel = hotelCell.textContent;
            }


            if (this.start === "" || this.end === "") {
                window.alert("First select the dates you want to reserve the room!");
                return;
            }

            const postRequest = new XMLHttpRequest();

            postRequest.open(
                "POST",
                "./InsertBookedRoomPersist?roomCategory=" +
                this.bookCateg +
                "&roomType=" +
                this.bookType +
                "&roomPrice=" +
                this.bookPrice +
                "&roomHotel=" +
                this.bookHotel +
                "&start=" +
                this.start +
                "&end=" +
                this.end
            );
            postRequest.send();

            window.alert("Room was successfully booked! :)");
            this.loadRoomsBooked(this.currentPage2, this);
        });



        document.getElementById("cancel-button").addEventListener("click", function () {
            if (thisObject.selectedIdBooked <= 0) {
                window.alert("First select the room to be canceled!");
                return;
            }

            const roomID = thisObject.selectedIdBooked;
            console.log(thisObject.selectedIdBooked);
            console.log(roomID);
            const deleteRequest = new XMLHttpRequest();

            deleteRequest.open("GET", "./DeleteBookedRoomPersist?roomId=" + roomID);

            deleteRequest.send();

            window.alert("Room was successfully canceled! :)");
            thisObject.loadRoomsBooked(thisObject.currentPage2, thisObject);
        });
    }

    homeBtnClicked(event) {
        document.location.href = "./";
    }

    dbInsertBtnClicked(event) {
        document.location.href = "./InsertRoom";
    }

    dbUpdateBtnClicked(event) {
        document.location.href = "./UpdateRoom";
    }

    dbDeleteBtnClicked(event) {
        document.location.href = "./DeleteRoom";
    }

    changeSelectedId(roomId, category, type, price, hotel) {
        this.selectedId = roomId;
        this.bookCateg = category;
        this.bookType = type;
        this.bookPrice = price;
        this.bookHotel = hotel;
    }

    changeSelectedId2(roomId) {
        this.selectedIdBooked = roomId;
    }

    loadRooms(page, thisObject) {
        const getRequest = new XMLHttpRequest();

        getRequest.open("GET", "./GetAllRoomsFiltered?page=" + page + "&roomCategory=" + this.category + "&roomType=" + this.type + "&roomPrice=" + this.price
            + "&roomHotel=" + this.hotel);
        getRequest.send();

        let table = document.getElementById('cols');


        while (table.firstChild) {
            table.removeChild(table.firstChild);
        }

        getRequest.onload = function () {
            const resultArray = JSON.parse(this.responseText);

            let table = document.getElementById('cols');

            while (table.firstChild) {
                table.removeChild(table.firstChild);
            }

            resultArray.forEach(element => {
                // create the row
                const newRow = document.createElement('tr');
                newRow.id = element.Id;

                // create the category cell and add it to the row
                const categoryCell = document.createElement('td');
                categoryCell.textContent = element.Category;
                newRow.appendChild(categoryCell);

                // create the type cell and add it to the row
                const typeCell = document.createElement('td');
                typeCell.textContent = element.Type;
                newRow.appendChild(typeCell);

                // create the price cell and add it to the row
                const priceCell = document.createElement('td');
                priceCell.textContent = element.Price;
                newRow.appendChild(priceCell);

                // create the hotel cell and add it to the row
                const hotelCell = document.createElement('td');
                hotelCell.textContent = element.Hotel;
                newRow.appendChild(hotelCell);

                newRow.onclick = function () {
                    thisObject.changeSelectedId(element.Id);
                    var rows = document.querySelectorAll("#cols tr");

                    rows.forEach(function (row) {
                        row.addEventListener("click", function () {
                            // Remove the "selected" class from any previously selected rows
                            document.querySelectorAll("#cols tr.selected").forEach(function (selectedRow) {
                                selectedRow.classList.remove("selected");
                            });
                            // Add the "selected" class to the clicked row
                            row.classList.add("selected");
                        });
                    });
                };

                // add the new row to the table
                table.appendChild(newRow);
            });

            for (let i = resultArray.length; i < 4; i++) {
                const newRow = document.createElement('tr');
                table.appendChild(newRow);
            }
        }
    }

    loadRoomsBooked(page, thisObject) {

        const getRequest = new XMLHttpRequest();

        getRequest.open("GET", "./GetAllBookedRooms?page=" + page);

        getRequest.send();

        let table = document.getElementById('cols2');


        while (table.firstChild) {
            table.removeChild(table.firstChild);
        }


        getRequest.onload = function () {
            const resultArray = JSON.parse(this.responseText);


            resultArray.forEach(element => {
                // create the row
                const newRow = document.createElement('tr');
                newRow.id = element.Id;

                // create the category cell and add it to the row
                const categoryCell = document.createElement('td');
                categoryCell.textContent = element.Category;
                newRow.appendChild(categoryCell);

                // create the type cell and add it to the row
                const typeCell = document.createElement('td');
                typeCell.textContent = element.Type;
                newRow.appendChild(typeCell);

                // create the price cell and add it to the row
                const priceCell = document.createElement('td');
                priceCell.textContent = element.Price;
                newRow.appendChild(priceCell);

                // create the hotel cell and add it to the row
                const hotelCell = document.createElement('td');
                hotelCell.textContent = element.Hotel;

                newRow.appendChild(hotelCell);

                // create the start cell and add it to the row
                const startCell = document.createElement('td');
                startCell.textContent = element.Start;

                newRow.appendChild(startCell);

                // create the end cell and add it to the row
                const endCell = document.createElement('td');
                endCell.textContent = element.End;

                newRow.appendChild(endCell);

                // add the new row to the table
                table.appendChild(newRow);

                newRow.onclick = function () {
                    thisObject.changeSelectedId2(element.Id);

                    var rows = document.querySelectorAll("#cols2 tr");

                    rows.forEach(function (row) {
                        row.addEventListener("click", function () {
                            // Remove the "selected" class from any previously selected rows
                            document.querySelectorAll("#cols2 tr.selected").forEach(function (selectedRow) {
                                selectedRow.classList.remove("selected");
                            });
                            // Add the "selected" class to the clicked row
                            row.classList.add("selected");
                        });
                    });
                };
            });

            for (let i = resultArray.length; i < 4; i++) {
                const newRow = document.createElement('tr');
                table.appendChild(newRow);
            }
        }
    }
}

