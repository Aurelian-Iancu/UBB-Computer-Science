namespace api.Services
{
    public interface IPermission
    {
        public void Check(Guid id);
    }
}