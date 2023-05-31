using System.ComponentModel.DataAnnotations;

namespace api.Dtos.PrivateDestination
{
    public record UpdatePrivateDestinationDto
    {
        public string Geolocation { get; set; } = string.Empty;
        public string Title { get; set; } = string.Empty;
        public string Image { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
    }
}