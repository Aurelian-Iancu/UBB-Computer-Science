using lab10.Models;
using lab10.Persistance;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Web.Mvc;

namespace lab10.Controllers
{
    public class RoomsController : Controller
    {
        private DataPersistence dataPersistence = new DataPersistence();

        public ActionResult Index()
        {
            if (Session["username"] == null)
            {
                return RedirectToAction("Index", "Login/");
            }

            return Rooms();
        }

        private ActionResult Rooms()
        {
            if (Session["username"] == null)
            {
                return RedirectToAction("Index", "Login/");
            }

            return View("RoomsHomeView");
        }

        public ActionResult InsertRoom()
        {
            if (Session["username"] == null)
            {
                return RedirectToAction("Index", "Login/");
            }

            return View("RoomsInsertView");
        }

        public ActionResult UpdateRoom()
        {
            if (Session["username"] == null)
            {
                return RedirectToAction("Index", "Login/");
            }

            return View("RoomsUpdateView");
        }

        public ActionResult DeleteRoom()
        {
            if (Session["username"] == null)
            {
                return RedirectToAction("Index", "Login/");
            }

            return View("RoomsDeleteView");
        }

        public string GetAllRooms(int page)
        {
            List<Room> rooms = dataPersistence.GetAllRooms(page);
            string json = JsonConvert.SerializeObject(rooms);
            return json;
        }

        public string GetAllBookedRooms(int page)
        {
            List<BookedRoom> rooms = dataPersistence.GetAllBookedRooms(page);
            string json = JsonConvert.SerializeObject(rooms);
            return json;
        }

        public string GetAllRoomsFiltered(int page, string roomCategory, string roomType, string roomPrice, string roomHotel)
        {
            List<Room> rooms;
            int intRoomPrice;
            if (!int.TryParse(roomPrice, out intRoomPrice))
            {
                return null;
            }

            if (roomCategory == "all")
            {
                rooms = dataPersistence.GetAllRooms(page);
            }
            else
            {
                rooms = dataPersistence.GetAllRoomsFiltered(page, roomCategory, roomType, intRoomPrice, roomHotel);
            }
           
            string json = JsonConvert.SerializeObject(rooms);
            return json;
        }

        public void InsertRoomPersist(string roomCategory, string roomType, string roomPrice, string roomHotel)
        {
            if (Session["username"] == null)
            {
                return;
            }

            int intRoomPrice;
            if (!int.TryParse(roomPrice, out intRoomPrice))
            {
                return;
            }

            dataPersistence.InsertRoom(new Room(-1, roomCategory, roomType, intRoomPrice, roomHotel));
        }

        public void InsertBookedRoomPersist(string roomCategory, string roomType, string roomPrice, string roomHotel, string start, string end)
        {
            if (Session["username"] == null)
            {
                return;
            }

            int intRoomPrice;
            if (!int.TryParse(roomPrice, out intRoomPrice))
            {
                return;
            }

            dataPersistence.InsertBookedRoom(new BookedRoom(-1, roomCategory, roomType, intRoomPrice, roomHotel, start, end));
        }

        public void DeleteRoomPersist(string roomId)
        {
            if (Session["username"] == null)
            {
                return;
            }

            int intRoomId;
            if (!int.TryParse(roomId, out intRoomId))
            {
                return;
            }

            dataPersistence.RemoveRoom(intRoomId);
        }

        public void DeleteBookedRoomPersist(string roomId)
        {
            if (Session["username"] == null)
            {
                return;
            }

            int intRoomId;
            if (!int.TryParse(roomId, out intRoomId))
            {
                return;
            }

            dataPersistence.RemoveBookedRoom(intRoomId);

        }

        public void UpdateRoomPersist(string roomId, string roomCategory, string roomType, string roomPrice, string roomHotel)
        {
            if (Session["username"] == null)
            {
                return;
            }

            int intRoomId;
            if (!int.TryParse(roomId, out intRoomId))
            {
                return;
            }

            int intRoomPrice;
            if (!int.TryParse(roomPrice, out intRoomPrice))
            {
                return;
            }

            dataPersistence.UpdateRoom(new Room(intRoomId, roomCategory, roomType, intRoomPrice, roomHotel));
        }

    }
}