using System.Text.RegularExpressions;
using api.Models;

namespace api.Validators;

public class AuthValidator
{
    public string ValidateUser(User user)
    {
        var usernameErrors = ValidateUserName(user.Username);
        var passwordErrors = ValidatePassword(user.Password);
        var roleErrors = ValidateRoles(user.Roles);

        return usernameErrors + passwordErrors + roleErrors;
    }
    
    private static string ValidateUserName(string username)
    {
        var errors = string.Empty;
        
        if (username.Length < 3)
        {
            errors += "Username too short\n";
        }
        else if (username.Length > 20)
        {
            errors += "Username too long\n";
        }

        if (!Regex.IsMatch(username, "^[a-zA-Z0-9_]+$"))
        {
            errors += "Username can only contain alphanumeric characters and '_'\n";
        }
        
        return errors;
    }

    private static string ValidatePassword(string password)
    {

        var errors = string.Empty;
        
        if (password.Length < 8)
        {
            errors += "Password must contain at least 8 characters\n";
        }
        
        if (!Regex.IsMatch(password, "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$"))
        {
            errors += "Password must contain at least one lowercase letter, one uppercase letter and one digit\n";
        }

        return errors;
    }

    private static string ValidateRoles(string role)
    {
        var errors = string.Empty;
        
        if (role != "Admin" && role != "Normal")
        {
            errors += "Invalid Role\n";
        }
        
        return errors;
    }
}