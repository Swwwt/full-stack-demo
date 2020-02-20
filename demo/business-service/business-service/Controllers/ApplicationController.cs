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
using Microsoft.AspNetCore.Cors;

[Route("api/[controller]")]
[ApiController]
public class ApplicationController : ControllerBase
{
  public static Channel channel;
  public static DataService.DataServiceClient client;

  public ApplicationController()//构造函数
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

  // GET api/application/?name=app1
  [HttpGet]
  public ActionResult<Application> Get(string name)
  {
    Application application = client.GetApplication(new Application { Name = name });
    if (application == null)
    {
      Console.WriteLine("Application not found.");
    }
    else
    {
      Console.WriteLine($"id: {application.Id}. name : {application.Name}");
    }
    return application;
  }

  // POST api/application/
  /*
  {
    "id": 1,
    "name": "app1",
    "description": "The first test",
    "date": "0213",
    "creator": "swt"  
  }
  调成json
  */
  [HttpPost]
  public void Post([FromBody] Application application)
  {
    Console.WriteLine($"Post Application id :{application.Id}, name :{application.Name} ");
    client.CreateApplication(application);
    // Application application = client.GetApplication(new Application { Name = name });
    // Console.WriteLine($"Post Application id is {application.Id}.");
  }

  // DELETE api/application/?name=app1
  [HttpDelete]
  public void Delete(string name)
  {
    Console.WriteLine($"Delete Application name is {name}.");
    client.DeleteApplication(new Application { Name = name });
  }
}