using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace lab10.Models
{
    public class Room
    {
        private int id;
        private string category;
        private string type;
        private int price;
        private string hotel;

        public Room(int id, string category, string type, int price, string hotel)
        {
            this.id = id;
            this.category = category;
            this.type = type;
            this.price = price;
            this.hotel = hotel;
        }

        public int Id
        {
            get { return id; }
            set { id = value; }
        }

        public string Category
        {
            get { return category; }
            set { category = value; }

        }

        public string Type
        {
            get { return type; }
            set { type = value; }

        }
        public int Price
        {
            get { return price; }
            set { price = value; }

        }

        public string Hotel
        {
            get { return hotel; }
            set { hotel = value; }

        }

    }
}