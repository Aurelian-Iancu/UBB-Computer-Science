using System.Text.RegularExpressions;
using api.Dtos.PublicDestinations;
using api.Models;

namespace api.Validators;

public class PublicDestinationValidator
{
    public string ValidatePublicDestination(Destination destination)
    {
        var geolocationErros = ValidateDestinationGeolocation(destination.Geolocation);
        var titleErrors = ValidateDestinationTitle(destination.Title);
        var imageErrors = ValidateDestinationImage(destination.Image);
        var descriptionErrors = ValidateDestinationDescription(destination.Description);
        return geolocationErros + titleErrors + imageErrors + descriptionErrors;
    }
    
    public string ValidatePublicDestinationDto(UpdatePublicDestinationDto destination)
    {
        var geolocationErros = ValidateDestinationGeolocation(destination.Geolocation);
        var titleErrors = ValidateDestinationTitle(destination.Title);
        var imageErrors = ValidateDestinationImage(destination.Image);
        var descriptionErrors = ValidateDestinationDescription(destination.Description);
        return geolocationErros + titleErrors + imageErrors + descriptionErrors;
    }

    private static string ValidateDestinationGeolocation(string geolocation)
    {
        var errors = string.Empty;

        const string pattern = @"^latitude:\s*(-?\d+(\.\d+)?),\s*longitude:\s*(-?\d+(\.\d+)?)$";
        var match = Regex.Match(geolocation, pattern);
        
        if (match.Success)
        {
            var latitude = double.Parse(match.Groups[1].Value);
            var longitude = double.Parse(match.Groups[3].Value);

            if (latitude is <= -90 or >= 90)
            {
                errors += "Latitude is not in correct range, must be in [-90, 90]\n";
            }
            
            if (longitude is <= -180 or >= 180)
            {
                errors += "Longitude is not in correct range, must be in [-180, 180]\n";
            }
        }
        else
        {
            errors += "Invalid geolocation type\n";
        }

        return errors;
    }
    
    private static string ValidateDestinationTitle(string title)
    {
        var errors = string.Empty;

        const string pattern = @"^(?i)(?:[A-Z\d][a-z\d.'\-\s,]*)+$";
        var match = Regex.Match(title, pattern);

        if (!match.Success)
        {
            errors += "Title must only contain alphanumeric characters, spaces, `'-.'`, and ','.\n";
        }

        var words = title.Split(' ');
        foreach (var word in words)
        {
            if (string.IsNullOrEmpty(word) || (!char.IsUpper(word[0]) && !char.IsNumber(word[0])))
            {
                errors += $"'{word}' must start with an uppercase letter\n";
            }
        }

        return errors;
    }

    private static string ValidateDestinationImage(string image)
    {
        var errors = string.Empty;
        
        // Maybe add more sites later like imgur 
        if (!image.StartsWith("https://fastly.picsum.photos/") && !image.StartsWith("fastly.picsum.photos/"))
        {
            errors += "Image URL is not valid\n";
        }

        return errors;
    }

    private static string ValidateDestinationDescription(string description)
    {
        var errors = string.Empty;
        
        if (description.Length > 200)
        {
            errors += "Description is too long, keep it under 200 characters\n";
        }
        
        return errors;
    }
}