class EventHandling {
    constructor() {
        this.currentPage = 0;
        const thisObject = this;

        this.selectedId = -1;

        document.getElementById("home-page").addEventListener("click", this.homeBtnClicked);
        document.getElementById("db-insert").addEventListener("click", this.dbInsertBtnClicked);
        document.getElementById("db-update").addEventListener("click", this.dbUpdateBtnClicked);
        document.getElementById("db-delete").addEventListener("click", this.dbDeleteBtnClicked);

        document.getElementById("prev-rooms-btn-delete").addEventListener("click", function () {
            if (thisObject.currentPage > 0) {
                thisObject.currentPage--;
                thisObject.loadRooms(thisObject.currentPage, thisObject);
            }
        });
        document.getElementById("next-rooms-btn-delete").addEventListener("click", function () {
            thisObject.currentPage++;
            thisObject.loadRooms(thisObject.currentPage, thisObject);

        });

        document.getElementById("submit-delete-btn").addEventListener("click", function () {
            if (thisObject.selectedId <= 0) {
                window.alert("First select the room to be deleted!");
                return;
            }

            // Ask for confirmation
            const confirmation = confirm("Are you sure you want to delete it?");
            if (!confirmation) {
                return;
            }

            const roomID = thisObject.selectedId;
            const deleteRequest = new XMLHttpRequest();

            deleteRequest.open("GET", "./DeleteRoomPersist?roomId=" + roomID);

            deleteRequest.send();

            deleteRequest.onload = function () {
                if (deleteRequest.status === 200) {
                    window.alert("Room was successfully deleted! :)");
                    thisObject.loadRooms(thisObject.currentPage, thisObject);
                } else {
                    window.alert("Failed to delete the room. Please try again.");
                }
            };
        });

        this.loadRooms(this.currentPage, thisObject);
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

    changeSelectedId(roomId) {
        this.selectedId = roomId;
    }

    loadRooms(page, thisObject) {
        const getRequest = new XMLHttpRequest();

        getRequest.open("GET", "./GetAllRooms?page=" + page);
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
}


