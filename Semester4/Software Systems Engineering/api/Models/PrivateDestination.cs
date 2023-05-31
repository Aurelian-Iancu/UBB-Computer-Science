namespace api.Models
{
    public record PrivateDestination
    {
        public Guid Id { get; set; }
        public string Geolocation { get; set; } = string.Empty;
        public string Title { get; set; } = string.Empty;
        public string Image { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }

        // Navigation propterties
        public Guid UserId { get; set; }
        public User? User { get; set; }
    }
}