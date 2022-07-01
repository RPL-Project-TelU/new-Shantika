 from dotenv import load_dotenv

 load_dotenv()

 try:
    from API import (app,api,HealthController,docs)

except Exception as e:
    print("Modules are Missing:{}".format(e))

api.add_resource(HealthController, '/awesome')
docs.register(HealthController)