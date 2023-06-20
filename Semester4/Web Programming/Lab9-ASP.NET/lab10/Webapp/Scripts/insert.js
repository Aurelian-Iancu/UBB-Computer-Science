class EventHandling {
    constructor() {
        document.getElementById("home-page").addEventListener("click", this.homeBtnClicked);
        document.getElementById("db-insert").addEventListener("click", this.dbInsertBtnClicked);
        document.getElementById("db-update").addEventListener("click", this.dbUpdateBtnClicked);
        document.getElementById("db-delete").addEventListener("click", this.dbDeleteBtnClicked);

        document.getElementById("submit-insert-btn").addEventListener("click", this.submitBtnClicked);
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

    submitBtnClicked(event) {
        const category = document.getElementById("room-category").value;
        const type = document.getElementById("room-type").value;
        const price = document.getElementById("room-price").value;
        const hotel = document.getElementById("room-hotel").value;

        if (category === "" || type === "" || price === "" || hotel === "") {
            window.alert("Please fill in all attributes before inserting!");
            return;
        }

        if (price < 0) {
            window.alert("Price must be greater than zero!");
            return;
        }

        const postRequestBody = "roomCategory=" + category + "&roomType=" + type + "&roomPrice=" + price + "&roomHotel=" + hotel;
        const postRequest = new XMLHttpRequest();

        postRequest.open("POST", "./InsertRoomPersist");
        postRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        postRequest.send(postRequestBody);

        window.alert("Room was successfully inserted! :)");
    }
}