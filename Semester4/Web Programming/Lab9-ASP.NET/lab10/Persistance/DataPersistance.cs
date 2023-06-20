using lab10.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MySql.Data.MySqlClient;

namespace lab10.Persistance
{
    public class DataPersistence
    {
        private string myConnectionString = "datasource=127.0.0.1;port=3306;username=root;password=Aurelian2002;database=hotelchain;";
        public List<User> GetAllUsers()
        {
            var conn = new MySqlConnection(myConnectionString);
            conn.Open();
            var sql = "SELECT * FROM `user`";

            List<User> users = new List<User>();
            var cmd = new MySqlCommand(sql, conn);

            MySqlDataReader mysqlDataReader = cmd.ExecuteReader();
            while (mysqlDataReader.Read())
            {
                users.Add(new User(mysqlDataReader.GetString(0), mysqlDataReader.GetString(1)));
            }

            return users;
        }

        public List<Room> GetAllRooms(int pageNumber)
        {
            var conn = new MySqlConnection(myConnectionString);
            conn.Open();

            var limit = 4;
            var offset = limit * pageNumber;

            var sql = $"SELECT * FROM room ";
           
            sql += $"LIMIT {limit} OFFSET {offset};";

            List<Room> rooms = new List<Room>();
            var cmd = new MySqlCommand(sql, conn);

            MySqlDataReader mysqlDataReader = cmd.ExecuteReader();
            while (mysqlDataReader.Read())
            {
                rooms.Add(new Room(mysqlDataReader.GetInt32(0), mysqlDataReader.GetString(1), mysqlDataReader.GetString(2), mysqlDataReader.GetInt32(3), mysqlDataReader.GetString(4)));
            }

            return rooms;
        }

        public List<BookedRoom> GetAllBookedRooms(int pageNumber)
        {
            var conn = new MySqlConnection(myConnectionString);
            conn.Open();

            var limit = 4;
            var offset = limit * pageNumber;

            var sql = $"SELECT * FROM bookedroom ";

            sql += $"LIMIT {limit} OFFSET {offset};";

            List<BookedRoom> rooms = new List<BookedRoom>();
            var cmd = new MySqlCommand(sql, conn);

            MySqlDataReader mysqlDataReader = cmd.ExecuteReader();
            while (mysqlDataReader.Read())
            {
                rooms.Add(new BookedRoom(
                mysqlDataReader.GetInt32(0),
                mysqlDataReader.GetString(1),
                mysqlDataReader.GetString(2),
                mysqlDataReader.GetInt32(3),
                mysqlDataReader.GetString(4),
                mysqlDataReader.GetString(5),
                mysqlDataReader.GetString(6)
                ));
            }

            return rooms;
        }


        public List<Room> GetAllRoomsFiltered(int pageNumber, string roomCategory, string roomType, int roomPrice, string roomHotel)
        {
            var conn = new MySqlConnection(myConnectionString);
            conn.Open();

            var limit = 4;
            var offset = limit * pageNumber;

            var sql = $"SELECT * FROM room WHERE category='{roomCategory}' AND type='{roomType}' AND price={roomPrice} AND hotel='{roomHotel}'";

            sql += $"LIMIT {limit} OFFSET {offset};";

            List<Room> rooms = new List<Room>();
            var cmd = new MySqlCommand(sql, conn);

            MySqlDataReader mysqlDataReader = cmd.ExecuteReader();
            while (mysqlDataReader.Read())
            {
                rooms.Add(new Room(mysqlDataReader.GetInt32(0), mysqlDataReader.GetString(1), mysqlDataReader.GetString(2), mysqlDataReader.GetInt32(3), mysqlDataReader.GetString(4)));
            }

            return rooms;
        }

        public void InsertRoom(Room room)
        {
            try
            {
                var conn = new MySqlConnection(myConnectionString);
                conn.Open();

                var sql = $"INSERT INTO room(category, type, price, hotel) VALUES ('{room.Category}', '{room.Type}', {room.Price}, '{room.Hotel}');";
                var cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

        public void InsertBookedRoom(BookedRoom room)
        {
            try
            {
                var conn = new MySqlConnection(myConnectionString);
                conn.Open();

                var sql = $"INSERT INTO bookedroom(category, type, price, hotel, start, end) VALUES ('{room.Category}', '{room.Type}', {room.Price}, '{room.Hotel}', '{room.Start}', '{room.End}');";
                var cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }

        }

        public void RemoveRoom(int roomId)
        {
            try
            {
                var conn = new MySqlConnection(myConnectionString);
                conn.Open();

                var sql = $"DELETE FROM room WHERE id = {roomId};";
                var cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

        public void RemoveBookedRoom(int roomId)
        {
            try
            {
                var conn = new MySqlConnection(myConnectionString);
                conn.Open();

                var sql = $"DELETE FROM bookedroom WHERE id = {roomId};";
                var cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

        public void UpdateRoom(Room room)
        {
            try
            {
                var conn = new MySqlConnection(myConnectionString);
                conn.Open();

                var sql = $"UPDATE room SET category = '{room.Category}', type = '{room.Type}', price = {room.Price}, hotel= '{room.Hotel}' WHERE id = {room.Id};";
                var cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

    }
 }