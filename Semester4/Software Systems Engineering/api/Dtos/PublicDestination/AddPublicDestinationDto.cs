using System.ComponentModel.DataAnnotations;

namespace api.Dtos.PublicDestinations
{
    public record AddPublicDestinationDto
    {
        [Required]
        public string Geolocation { get; set; } = string.Empty;
        [Required]
        public string Title { get; set; } = string.Empty;
        [Required]
        public string Image { get; set; } = string.Empty;
        [Required]
        public string Description { get; set; } = string.Empty;
    }
}