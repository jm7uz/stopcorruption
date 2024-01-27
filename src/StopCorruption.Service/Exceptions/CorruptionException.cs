namespace StopCorruption.Service.Exceptions;

public class CorruptionException : Exception
{
    public int StatusCode { get; set; }

    public CorruptionException(int code, string message) : base(message)
    {
        StatusCode = code;
    }
}
