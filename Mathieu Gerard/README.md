# WS18A - Indoor location-based services using Wi-Fi 

Thanks for joining this workshop at DevNet Create 2018.

## Objectives

The objectives of the workshop are

- Learn about location-based services inside buildings
- Listen for Meraki location notifications
- Build a simple map of the conference venue using Mapwize
- Display a device location on the venue map
- Get a notification on Spark when a device enters or leaves an area

## BYOD Requirements

The following tools will be required for the workshop. To save time, please ensure your have them installed on your own laptop.

- Node.js - Install from [nodejs.org](https://nodejs.org)
- Redis - Check instructions from [redis.io](https://redis.io/topics/quickstart)
- Git - Get started at [git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- ngrok - Download from [ngrok.com/download](https://ngrok.com/download)

If you have some experience with mobile development, on either iOS or Android, or if you want to get started compiling your first simple app, bring XCode or Android Studio as well as your mobile device and a USB cable.

Also, you'll need the following accounts. Don't hesitate to sign-up before the workshop.

- Mapwize - Sign up for free at [mapwize.io](https://www.mapwize.io)
- Cisco Spark - Get started free at [ciscospark.com](https://www.ciscospark.com/)

## 1 - Get location notifications from Meraki

The Meraki wifi network is collecting location of the mobile devices being seen. Those locations can be pushed to a listener so you can make use of them.

All the details about the Meraki positioning can be found on [github.com/IndoorLocation/meraki-indoor-location](https://github.com/IndoorLocation/meraki-indoor-location). In this workshop, we will only focus on a little part of it.

### Import the Meraki configuration in Mapwize

In this step, we will create a venue in Mapwize using the Meraki floorplan configuration.

First, make sure you have your Mapwize account ready or sign up for free at [mapwize.io](https://www.mapwize.io). Go to [studio.mapwize.io](https://studio.mapwize.io) and sign in.

In your Mapwize account, create a venue for "DevNet Create 2018" at the Computer Science Museum in Mountain View. When asked, draw a simple rectangle around the building, don't worry about the exact shape.

In the venue config screen, on the right side, scroll down to retrieve your venueId and organizationId.

Go back to the home page then in the left venue select "API key" and create an API key.

Download the Meraki floorplan configuration file. Usually you would get this from the Meraki portal but I've made a copy of it as I cannot grant everyone access to the Meraki network of the event. **TODO The file will be available after the network is deployed**.

Clone the [github.com/IndoorLocation/meraki-indoor-location](https://github.com/IndoorLocation/meraki-indoor-location) repository on your machine.

```
git clone https://github.com/IndoorLocation/meraki-indoor-location
```

Use the configurator to inject the Meraki floorplan config to your Mapwize venue:

```
./meraki-configurator/merakiFloorplansToMapwize.js --merakiFloorPlansConfig [FILEPATH_FOR_FLOORPLANS_JSON] --mapwizeUser [YOUR_MAPWIZE_EMAIL] --mapwizePwd [YOUR_MAPWIZE_PWD] --mapwizeApiKey [YOUR_MAPWIZE_API_KEY] --mapwizeOrganizationId [YOUR_MAPWIZE_ORGANIZATIONID] --mapwizeVenueId [YOUR_MAPWIZE_VENUEID]
```

Go to [Mapwize Studio](https://studio.mapwize.io), enter your venue and go to the Layers section. You'll see that a "Meraki - xx" layer has been created. That's the image that was used in Meraki, positionned precisely like in the Meraki portal.

As Meraki does not support proper configuration of floors in the Meraki Portal, you'll need to manually edit the layer and set floor=2. Also, toggle the publish status to true. And save.

Here the event is on a single floor but of course multiple floor buildings would be as easily supported.

### Listen for Meraki notifications

Now that the layer is correctly configured in Mapwize, with the right floor and alignment, we can generate the JSON configuration file for the listener.

```
./meraki-configurator/configureFromMapwize --merakiFloorPlansConfig [FILEPATH_FOR_FLOORPLANS_JSON] --mapwizeUser [YOUR_MAPWIZE_EMAIL] --mapwizePwd [YOUR_MAPWIZE_PWD] --mapwizeApiKey [YOUR_MAPWIZE_API_KEY] --mapwizeOrganizationId [YOUR_MAPWIZE_ORGANIZATIONID] --mapwizeVenueId [YOUR_MAPWIZE_VENUEID] --output [OUTPUT_PATH_FOR_LISTENER_CONFIGURATION]
```

Now it's time to start a local Redis database on your machine. The database will allow to store the last position received for each device. 

```
redis-server
```

We need to activate redis notifications for the system to work by using the following comand:

```
redis-cli config set notify-keyspace-events K$
```

The listener is available in the same Meraki IndoorLocation Github repository, in the listener directory.

You can set the configuration of the listener directly in the `config/all.js` file or using environment variables.

Assuming your Redis server is running with default configuration (localhost:6379 without auth), the only variable you'll need are:

  * FLOOR_PLANS: copy paste the content of the JSON file produced by the `configureFromMapwize` command
  * MAC_ADDRESS_ENABLED: true (better for the asset tracking cases)
  * SECRET: "devnetcreate2018"
  * VALIDATOR: "devnetcreate2018"

By default, your listener will be running on `localhost:3004`.

Note:
To correctly serialize the Meraki configuration, you can execute
```
export FLOOR_PLANS=$(node -e 'var json = require("FILEPATH"); console.log(JSON.stringify(json));')
```
Or if you want to put this variable into your clipboard instead to paste it in the config file, please execute
```
node -e 'var json = require("FILEPATH"); console.log(JSON.stringify(json));' | pbcopy
```

And now you can start the listener server with

```
npm run start-listener
```

Now your listener server is ready to retrieve notifications.

In normal cases, you would add your listener server as `post URL` in your Meraki "Location and scanning" configuration. However, for this workshop, it is not really handy to manually add the url of each participant. Therefore, we are going to use this little [post-boradcast](https://github.com/mathieugerard/post-broadcast) project that can propagate post requests.

**Please ask Mathieu for the URL where the broadcast server was deployed.**

Clone the repo on your machine

```
git clone https://github.com/mathieugerard/post-broadcast
```

And start the client using

```
SERVER=[THE BROADCAST SERVER URL] node client.js
```

Everytime a notification is received by the boradcast server, your broadcast client will make the same post request to your Meraki listener server. If your Meraki listener server is not running on `localhost:3004`, you'll need to use the `POSTTO` environment variable to configure it.

Now you should start receiving notifications and your Redis database will be populated with locations.

You can use [RDM](https://redisdesktop.com/) or your favourite Redis explorer to see the records.

### Setup the emitter server

Now we have locations flowing to our Redis database but so far no one can use it. The next step is to setup the emitter server to allow other systems (apps or other components) to retrieve location updates for specific IP or MAC using websocket.

The emitter server is located in the same Meraki IndoorLocation Github repository, in the emitter directory.

You can set the configuration of the listener directly in the `config/all.js` file or using environment variables.

Assuming your Redis server is running with default configuration (localhost:6379 without auth), you don't need any particular configuration.

Start the server using

```
npm run start-emitter
```

By default, your emitter will be running on `localhost:3003`.

So now you have everything you need to retrieve the location of any device using websocket. Cool right :-)

## 2 - See your location on the map

So now you can see your position on the map ... or even the position of anyone at the conference as long as you know their local IP address or their Mac address. Of course that opens lots of questions regarding privacy but that's not the point right now.

### View your location on maps.mapwize.io

The simplest way to see your location is to use maps.mapwize.io as there is nothing to code or compile.

Go back to [Mapwize Studio](https://studio.mapwize.io). From the home screen, on the left menu, go to the "Access groups". Create a group containing all venues and all universes.

Then head to "Access keys" and create a key for the access group you just created.

Go to venues and then select your venue. Make sure that your venue is published by setting the published flag to true and saving it.

Then, inside your venue, head to the URL generator and create an URL to see your venue using the access key you created.

Open the link in your browser and you should be able to see the map of DevNet Create. But your location is not on it yet.

To do so, add the `indoorLocationSocketUrl` and `indoorLocationUserId` parameters to your URL. It should look like this:

```
https://maps.mapwize.io/#/v/[VENUE_ALIAS]?k=[ACCESS_KEY]&indoorLocationSocketUrl=localhost:3003& indoorLocationUserId=[YOUR_LOCAL_IP_OR_MAC]
```

To use your local IP address, you need to be connected to the Meraki Wifi. Ask me for credentials.

Refresh the page and you should see your position as provided by Meraki.

### View your location in a simple mobile app

Of you are familiar with mobile developement or if you feel excited to run your first app, you can use a sample app to see your location.

The sample app is available for

* **iOS** [github.com/indoorlocation/socket-indoor-location-provider-ios](https://github.com/indoorlocation/socket-indoor-location-provider-ios)
* **Android** [github.com/indoorlocation/socket-indoor-location-provider-android](https://github.com/indoorlocation/socket-indoor-location-provider-android)

You will need to set your credentials in SocketIndoorLocationProviderDemoApp and MapActivity. You need to change 2 things:

* Set your API key in SocketIndoorLocationProviderDemoApp. (see below)
* Set the URL of your emitter server in MapActivity on line 48. (see below)

In order to see your venue in the app, you'll need to add the rights on your API key. To do so, go to [Mapwize Studio](https://studio.mapwize.io) and then to "API keys". Edit the API key you already have and add your access group in it.

Using `localhost` in your app as socket URL is not going to work. The best option to solve that is to use `ngrok`. Ngrok will create a tunnel to your local machine that is available from the cloud. Run

```
ngrok http 3003
```

and use the address provided by ngrok in your app. You need to keep ngrok running on your maching for the connection to be maintained.

On mobile, your locap IP address is used automatically to fetch your position. Therefore, **your device must be connected to the Meraki network**. Ask me for credentials.

### Make the map look nicer

The map that you are seeing is the technical drawing that was used to configure Meraki. Usually, this is not the map you want to show your users.

My collague Manon has designed a better looking map of the venue. You can [download the image here](https://www.dropbox.com/s/v9fbp2hp54wo6ii/Devnetcreate2018_floor2.png?dl=0).

Go to [Mapwize Studio](https://studio.mapwize.io), enter your venue and go to "Layers". Create a new layer for the 2nd floor. 

When created, drag and drop the image to import it. In the aligment editor, on the top left, select the Meraki layer from the list to display it as reference. Align the new floorplan with the Meraki one moving the pins. When done, import.

When the import job is finished, publish the layer by setting the published flag to true and saving.

Go to the layer list, select the Meraki one and unpublish it.

Refresh maps.mapwize.io or relaunch your app to see the difference.

If you want to build an interactive map, follow the Mapwize tutorials to app places and directions.

### Advanced: build the full Mapwize app

If you want to go further with mobile development, you can build the open-source Mapwize mobile app adding the socketIndoorLocationProvider in it.

The source code of the Mapwize app is available for

* [iOS](https://github.com/Mapwize/mapwize-app-ios)
* [Android](https://github.com/Mapwize/mapwize-app-android)

## 3 - Track assets

So far, you have seen how to retrieve locations and see them on a map. There are a lot of use cases where you would like to track assests and get notified when they move, enter or leave certains areas etc. Think about medical material in a hospital, or goods in logistics, or kids in shopping malls. Ok, kids are not really assests but you get the point :-)

## Get a notification on Spark if an asset enters or leaves an area

Since an emitter server is available to share device positions, we are going to use it again and connect it to an alerter.

For the sake of the demo, and since we are at DevNet afterall, we are going to use Cisco Spark to get notifications. Please make sure you have a Cisco Spark account and that you have a Cisco Spark client installed (desktop, mobile or web).

Navigate to [developer.ciscospark.com/getting-started.html](https://developer.ciscospark.com/getting-started.html). Make sure you are logged in and retrieve your token (it's in the page after you scroll a bit).

Then go to [Mapwize Studio](https://studio.mapwize.io), enter your venue, and go to "Places". Use the polygon tool on the top left of the map to create a polygonal place. Click on the map to create the polygon edges and close the polygon cliking on the first point again. Give a name to your place and select a place type (you can choose anything, it doesn't matter). Save your place. Then edit it to view it's id all the way at the end of the edition window.

**The code of the alerter is being finalized and will be published soon**.

Further instructions will follow.
