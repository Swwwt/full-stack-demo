using Grpc.Core;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace business_service
{
  public class Program
  {
    public static void Main(string[] args)
    {
      /*try
      {
        Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);
        var client = new DataService.DataServiceClient(channel);

        // 1. CreateApplication
        client.CreateApplication(new Application { Id = 1, Name = "app1" });

        // 2. GetApplication (Name required)
        Application application = client.GetApplication(new Application { Name = "app1" });
        if (application == null)
        {
          Console.WriteLine("Application not found.");
        }
        else
        {
          Console.WriteLine($"The Application name is {application.Name}.");
        }

        // 3. GetUser
        User user = client.GetUser(new User { Name = "swt" });
        if (user == null)
        {
          Console.WriteLine("User not found.");
        }
        else
        {
          Console.WriteLine($"The User gender is {user.Gender}.");
        }

        // 4. DeleteApplication
        client.DeleteApplication(new Application { Id = 1 });

        channel.ShutdownAsync().Wait();
        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
      }
      catch (Exception ex)
      {
        Console.WriteLine($"Exception encountered: {ex}");
      }*/

      CreateHostBuilder(args).Build().Run();
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder =>
            {
              webBuilder.UseStartup<Startup>();
            });
  }
}
