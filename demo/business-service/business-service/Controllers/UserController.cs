using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Grpc.Core;
using System;
using System.Linq;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

[Route("api/[controller]")]
[ApiController]
public class UserController : ControllerBase
{
  public static Channel channel;
  public static DataService.DataServiceClient client;

  public UserController()//构造函数
  {
    try
    {
      channel = new Channel("business-grpc:50051", ChannelCredentials.Insecure);
      client = new DataService.DataServiceClient(channel);
    }
    catch (Exception ex)
    {
      Console.WriteLine($"Exception encountered: {ex}");
    }
  }

  // GET api/user/?name=app1
  [HttpGet]
  public ActionResult<User> Get(string name)
  {
    User user = client.GetUser(new User { Name = name });
    if (User == null)
    {
      Console.WriteLine("User not found.");
    }
    else
    {
      Console.WriteLine($"id: {user.Id}. name : {user.Name}");
    }
    return user;
  }
}