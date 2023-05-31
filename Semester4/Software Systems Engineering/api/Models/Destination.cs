namespace api.Models
{
    public record Destination 
    {
        public Guid Id { get; set; }
        public string Geolocation { get; set; } = string.Empty;
        public string Title { get; set; } = string.Empty;
        public string Image { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
    }
}