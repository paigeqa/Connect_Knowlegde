# ProtoPie Docs — Connect 관련 섹션

> 원본 `protopie_docs_all.md`에서 ProtoPie **Connect** 및 **Connecting Devices** 관련 페이지만 추출.
> 포함 페이지 (15개):
> - Connect: API Plugin, Arduino Plugin, blokdots Plugin, Connect Embedded, Custom Layer Integrations, Custom Plugins, Gamepad Plugin, Getting Started, IFTTT Plugin, Logitech G29 Steering Wheel Plugin, Testing Prototypes, Feature Comparison (Pro vs Enterprise), Unity Plugin
> - Connecting Devices: Connecting blokdots, Connecting Mobile Devices

---

---
title: "API Plugin"
url: https://www.protopie.io/learn/docs/connect/api-plugin
---

# API Plugin

# Using the API Plugin in ProtoPie Connect

The API plugin lets you quickly bring real data into your prototypes by connecting them to APIs and databases. 

Unlike [Custom Plugins](https://www.protopie.io/learn/docs/connect/custom-plugins), the API plugin does not require coding skills. This plugin handles the task, either sending data to APIs or retrieving data from them and seamlessly incorporating it into your prototypes in JSON format.

## What is an API?

An API, which stands for Application Programming Interface, is a set of rules that allows different computer programs to communicate and work together. It's like a bridge that helps them share information and perform tasks without knowing all the details of how each program works. In simpler terms, APIs make it easier for software to communicate and collaborate.

## Supported API Types

With the API plugin, you can easily start API requests, whether they're GET or POST, and connect with various API types:

- **Public APIs**: This encompasses popular services like Spotify, OpenWeatherMap, YouTube, ChatGPT, live scores, and many more.

- **Internal APIs**: Connect seamlessly with your organization's systems and services.

## How to Make API Requests

Follow these easy steps to use the API plugin in ProtoPie Connect and make API requests in your prototypes.

### Step 1: Creating a Send Response in ProtoPie Studio

- Start by adding a [**Send response**](https://www.protopie.io/learn/docs/interactions/responses#send) to your chosen trigger in [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface).

- Remember to select the `ProtoPie Connect/Studio` channel,  as you usually do when passing information back and forth between ProtoPie Studio and ProtoPie Connect.

- Save your prototype. 

In [this example prototype,](https://cloud.protopie.io/p/20e828f860b8c34456583ece) we want data from the [Useless Facts API](https://uselessfacts.jsph.pl/) when you pick "Random Fact" using the toggle switch. To do this, we begin by creating a Send response with the `ProtoPie Connect/Studio` channel and a unique message value.

![Setting up Send messages to make API calls in ProtoPie](https://cdn.sanity.io/images/vidqzkll/production/9af57fad1a6925eb56ceb0d92cbac260871e14a5-5620x3378.png/send_protopie.png)

**Tip**: Watch [this free lesson](https://learn.protopie.io/course/protopie-connect) on ProtoPie School to master Send and Receive messages between ProtoPie Studio and ProtoPie Connect.

### **Step 2: Configuring API Settings within the API Plugin**

- Open your prototype in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

- Click on `Plugin`, then select the `API` plugin from the list.

- Select one of the two HTTP request methods available: [GET or POST](https://www.baeldung.com/cs/http-get-vs-post). When making API requests, GET retrieves data from the API provider, while POST sends new data to be processed.

- Enter the correct API URL for the API you want to access. Refer to the API's online documentation to obtain the correct URL. In our example, we can see [on this page](https://uselessfacts.jsph.pl/) that the URL we need is `https://uselessfacts.jsph.pl/api/v2/facts/random`

- Include a `Header` and `Body` if the API requires it. Be sure to carefully read the documentation of your chosen API for any additional parameters needed alongside the API URL.

  - The `Header` must be formatted in JSON {}, but the `Body` doesn't always need to follow JSON {} format. You can enter the `Body` in JSON {} format if the API demands it.  

- Click the `Test Request` button to verify that the connection is working properly. If an error message appears, review the information you entered in the previous steps.

![setting up API in the API plugin in ProtoPie Connect ](https://cdn.sanity.io/images/vidqzkll/production/91a654d1d9e4900c1e08a8aac43af5f7595b9b57-5620x3378.png/api-settings-protopie.png)

### Step 3: Connecting the API with your Prototype

- Click the `Message From Pie` input field to access the list of available messages. The API plugin automatically detects the messages within your prototypes. If you donât see your message, copy and paste it from the Send response you created in Step 1.

- Enable `Override URL/Header/Body with msg value` if you need to dynamically override the APIâs URL, Header, or Body with the value of the message sent from the prototype. [Learn more](https://www.protopie.io/learn/docs/connect/api-plugin#overriding-the-api-url-header-body-with-message-values) about overriding API URL/Header/Body with message values.

- In `Message to Pie`, type in a message, which will be sent back to your prototype along with the data obtained from the API request you configured in Step 2.

- Click `Activate` to establish the connection. The plugin will initiate the API request upon receiving the corresponding message from the prototype.

![connecting a prototype to an API using ProtoPie Connect's API plugin ](https://cdn.sanity.io/images/vidqzkll/production/0333b823facc4f099dceb8d9bcf520abf862f090-5620x3378.png/connect-pie-to-api.png)

### Step 4: Creating a Receive trigger in ProtoPie Studio

- Go back to ProtoPie Studio.

- In your prototype, add a [Receive trigger](https://www.protopie.io/learn/docs/interactions/triggers#receive-trigger-properties).

- Remember to choose the `ProtoPie Connect/Studio` channel, as you did when setting up the Send response in Step 1.

- Input the same message you configured in Step 3 under `Message to Pie`.

- Activate the `Assign to Variable` option. Create a [text variable](https://www.protopie.io/learn/docs/variables/getting-started#text) and select it from the list in the Receive trigger. The information obtained from the API is now stored within this variable.

- Since API data are often returned in JSON format, utilizing the [Text response](https://www.protopie.io/learn/docs/interactions/responses#text) with a [parseJson formula](https://www.protopie.io/learn/docs/formulas/functions) is the most efficient method for incorporating API data into your prototypes.

- Save the prototype and then reload it in ProtoPie Connect. Your API-empowered interaction is now ready to be tested through ProtoPie Connect!

![setting up the receive trigger and text response to receive data from APIs in ProtoPie](https://cdn.sanity.io/images/vidqzkll/production/0a88aa67df6a7a0feffde0eb5ed9664510b45f31-5620x3378.png/receive-api-response.png)

## Overriding the API URL/Header/Body With Message Values

`Override URL/Header/Body with msg value` is used to dynamically override the APIâs URL, Header, or Body parameters with the value of the message sent from the prototype.

In [ this example prototype](https://cloud.protopie.io/p/8cbb1b86ff0749093c507d03), we used this feature to override the API URL with the value from the below Send message  in the Pie file. As a result, when you test the prototype in ProtoPie Connect and type a city into the search box, you'll see the precise weather information for that city.

![overriding the API's URL with the message sent from the prototype in ProtoPie ](https://cdn.sanity.io/images/vidqzkll/production/a13ca5a964ae7168c2c6685ca9f22ae67f86178f-4096x2462.png/override-api-url-protopie.png)

 

## Running Simultaneous API Calls

Users of Connect Core and Connect Enterprise can execute multiple API requests simultaneously using the API plugin. Connect Core has the capability to run up to three APIs (provided that no other plugin is running), whereas Connect Enterprise has no limit on the number of API calls that can run simultaneously.

To run multiple API requests simultaneously in your prototype, follow these steps:

- Open the API plugin in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

- Click on the `+` icon situated in the upper-right corner of the API Settings window. This will open a new window where you can configure and run additional API calls simultaneously. You can also duplicate your existing APIs, to keep their original settings.

![configuring multiple simultaneous API requests in ProtoPie Connect ](https://cdn.sanity.io/images/vidqzkll/production/cd021777baf05f26806e8df98c481f2059853f34-5620x3378.png/multiple-api-requests-protopie.png)

 

## API Plugin How-To Tutorials

Discover the API plugin's key features and use cases in this how-to series.

1. [API Plugin Tutorial for Beginners](https://www.protopie.io/blog/api-plugin-tutorial-for-beginners)

1. [API Plugin Advanced Tutorial](https://www.protopie.io/blog/api-plugin-advanced-tutorial)


---

---
title: "Arduino Plugin"
url: https://www.protopie.io/learn/docs/connect/arduino-plugin
---

# Arduino Plugin

# Using Arduino with ProtoPie Connect

Create multi-screen experiences across both software and hardware thanks to ProtoPie Connectâs built-in Arduino plugin.

ProtoPie Connect supportsÂ [serial communication](https://www.arduino.cc/reference/en/language/functions/communication/serial)Â with Arduino boards. The most typical setup would be connecting the Arduino hardware to the machine where ProtoPie Connect is running via USB.

[Learn more](https://www.arduino.cc/en/Guide) about how to use Arduino.

## Connecting Arduino to ProtoPie Connect via USB

1. Select **Arduino** in ProtoPie Connectâs Plugin list.

![Connect Arduino to ProtoPie Connect](https://cdn.sanity.io/images/vidqzkll/production/4d2d9e103a796f0701cdcce18687ba475bad5841-1450x800.png/Arduino-1.png)

2. Select the desired **Port** and **Baud Rate**:

- **Port**: Select the port corresponding to your Arduino board.

![Connect Arduino: select port.](https://cdn.sanity.io/images/vidqzkll/production/b4a04fcb48f281cda451a7981dbd152d24a29d05-1450x814.png/Arduino-2.png)

- **Baud Rate**: This value determines how frequently the serial connection will be checked for updates. You can select the default value 9600.

![Connect Arduino: select the baud rate.](https://cdn.sanity.io/images/vidqzkll/production/ff9fbc8df49077247cf9f451ce384d17a411eaa4-1450x800.png/Arduino-3.png)

*Please note that the Arduino plugin works with any Micro Controller communicating via serial. For exampleâif you want to use an ESP32 microcontroller, after connecting the ESP32âyou can select the appropriate port and baud rate to open the serial port ESP32 and receive data in ProtoPie Connect.

## Using Arduino with ProtoPie Connect

ProtoPie Connect and Arduino communicate using a **Message||Value** format. If the intention is to send a message without a value, **Message** would suffice.

### Sending messages from Arduino

Use the **Serial.println()** function to send messages (and values) to ProtoPie Connect, which then communicates them to all corresponding prototypes.

In the following example, Arduino sends the message **ROTATE** and value **90** every **2 seconds** to ProtoPie Connect.

```c_cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Send "ROTATE" to ProtoPie
  // message: ROTATE
  // value: 90
  Serial.println("ROTATE||90");
  delay(2000);
}
```

### Sending messages to Arduino

The Arduino hardware requires a separate  code to interpret incoming messages in the **Message||Value** format.

In the below example, Arduino receives and interprets messages received from ProtoPie Connect.

```c_cpp
#include <string.h>

// Declare struct
struct MessageValue {
  String message;
  String value; // Note that value is of String type
};

// Declare function that parse message format
struct MessageValue getMessage(String inputtedStr) {
  struct MessageValue result;

  char charArr[50];
  inputtedStr.toCharArray(charArr, 50);
  char* ptr = strtok(charArr, "||");
  result.message = String(ptr);
  ptr = strtok(NULL, "||");

  if (ptr == NULL) {
    result.value = String("");
    return result;
  }

  result.value = String(ptr);

  return result; 
}

// Declare MessageValue struct's instance
struct MessageValue receivedData;

void setup() {
  Serial.begin(9600);

/*
		if you want to make waiting time for reading serial data short,
		set waiting time with `Serial.setTimeout` function.
	*/
	Serial.setTimeout(10);
}

void loop() {
// Take out strings until Serial buffer is empty
	while (Serial.available() > 0) {
// From ProtoPie Connect 1.9.0, We can use '\0' as delimiter in Arduino Serial
		String receivedString = Serial.readStringUntil('\0');

		receivedData = getMessage(receivedString);
  }

	// Do something with received message from ProtoPie Connect

	if (receivedData.message.equals("FIRST")) { // If message from ProtoPie Connect equals "FIRST" do the following 
		l1 = receivedData.value.toInt(); // receivedData.value.toInt() converts the value from ProtoPie Connect to integer type and assigns it to l1
		analogWrite(firstLED, l1); 
	} 
}
```

## Use Cases

 Try recreating the following use case to understand better how Arduino works with ProtoPie Connect.

### Control Your Home Lights

Turn the lights on and off consecutively. Test this yourself using an Arduino board connected to ProtoPie Connect.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dk7-6H6jg1jM&feature=youtu.be)

1. Add [this prototype](https://cloud.protopie.io/p/7763340ee7) to ProtoPie Connect. 
2. Set up your Arduino board and the light controls following this circuit diagram.

![Connect Arduino Use Case](https://cdn.sanity.io/images/vidqzkll/production/995439aa97f7ba1079e38b69ca48252e22270b3e-2110x1554.png/connect-arduino-usecase.png)

3. Connect your Arduino board to ProtoPie Connect.
4. Use this example code to send messages from Arduino to ProtoPie Connect.

```c_cpp
#include <string.h>

struct MessageValue {
  String message;
  String value;
};

struct MessageValue getMessage(String inputtedStr) {
  struct MessageValue result;

  char charArr[50];
  inputtedStr.toCharArray(charArr, 50);
  char* ptr = strtok(charArr, "||");
  result.message = String(ptr);
  ptr = strtok(NULL, "||");

  if (ptr == NULL) {
    result.value = String("");
    return result;
  }

  result.value = String(ptr);

  return result;
}

int firstLED = 3;
int secondLED = 5;
int thirdLED = 6;
struct MessageValue receivedData;

void setup() {
  pinMode(firstLED, OUTPUT);
  pinMode(secondLED, OUTPUT);
  pinMode(thirdLED, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10); // Set waiting time for serial data to 10 milliSeconds
}

void loop() {
  while (Serial.available() > 0) { // Take out strings until Serial is empty
    String receivedString = Serial.readStringUntil('\0'); // From 1.9.0 version, We can use '\0' as delimiter in Arduino Serial
    receivedData = getMessage(receivedString);
  }

  if (receivedData.message.equals("FIRST")) {
    analogWrite(firstLED, receivedData.value.toInt());
    delay(30);
  } else if (receivedData.message.equals("SECOND")) {
    analogWrite(secondLED, receivedData.value.toInt());
    delay(30);
  } else {
    analogWrite(thirdLED, receivedData.value.toInt());
    delay(30);
  }
}
```

### Surgical Robot Arm

Learn how to prototype a robot arm ([Arduino Braccio robot arm](https://store.arduino.cc/products/tinkerkit-braccio-robot)) controlled by a wireless controller.

Check out [this article](https://www.protopie.io/blog/prototyping-for-robotics) to explore the practical application of ProtoPieÂ in robotics prototyping. 

[Code used in Arduino](https://create.arduino.cc/editor/tonykim/f40afc41-f8b4-4ff9-b12a-c677db47d125/preview).


---

---
title: "blokdots Plugin"
url: https://www.protopie.io/learn/docs/connect/blokdots-plugin
---

# blokdots Plugin

# Using blokdots & ProtoPie Connect

[blokdots](https://blokdots.com/) is a code-free software to build interactive hardware prototypes with [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin).

The blokdots & ProtoPie integration is available to all users, regardless of their plan. However, when used with ProtoPie Connect, it unlocks new possibilities, such as the ability to create hardware-software interactions involving three or more devices.

The typical blokdots & ProtoPie Connect ecosystem involves:

- ProtoPie Studio, to create interactions.

- ProtoPie Connect and blokdots plugin, to enable communication between ProtoPie prototypes and blokdots app which connects to Arduino and sensors.

## Getting Set Up****

**  1. Open the Pie file in ProtoPie Connect**.****

**  2. Connect blokdots to ProtoPie Connect.**

![ProtoPie Connect status](https://cdn.sanity.io/images/vidqzkll/production/bce7abd95d31a88ba059e2d43e442957ccf606f8-2220x1414.png/pp-connect-status.png)

  1. Open the blokdots application on your computer and make sure that youâve activated the âblokdots proâ plan or start the 14-day trial.

  1. If youâre running ProtoPie Connect and blokdots on the same computer, the connection should happen automatically

  1. If youâre running ProtoPie Connect and blokdots on different computers, open the connection settings and enter the URL of the ProtoPie Connect server

Once blokdots is connected to ProtoPie Connect, the connection indicator at the ProtoPie icon in the bottom-left corner(under âConnectionsâ) should turn green. You will see a Connected message in ProtoPie Connect as well.

![blokdots plugin in connected mode.](https://cdn.sanity.io/images/vidqzkll/production/117142d1759114355b708afa1ee8bed760417f2a-1450x800.png/blokdots-1 (1).png)

  ** 3. ****Plug in the **[**Arduino board**](https://blokdots.uber.space/documentation/arduino/)**.******

![The Arduino board is ready for use.](https://cdn.sanity.io/images/vidqzkll/production/46c84354be30bd6ca596c1f7f33e49aebb249637-2175x1200.png/Connect-arduino-ready.png)

Once you see that your board is ready in theÂ top-left corner of blokdots, you can start setting up your components.

**4. Connecting the components **

This step is necessary for blokdots to know which components of the Arduino board to control.

       a. Click onÂ **Connect A New Component**Â and pick the ones you want to connect.

       b.  Chose an available Grove slot or hardware pin from the list  

c. Click onÂ **Set Component.**

![Set up your components in the Live View of the blokdots app.](https://cdn.sanity.io/images/vidqzkll/production/66d0d3b352a1effd5119a161bb961d9272c720f4-1224x698.gif/Connect-setting-up-components.gif)

  5. **Configure the components cards.**

      

    a. Start configuring each component card.

![Configure component cards in the blokdots app.](https://cdn.sanity.io/images/vidqzkll/production/b77fb204a23be42de1b7047428f0df796dce5dee-1222x697.gif/Connect-component-cards.gif)

*The blokdots app allows ProtoPie and Arduino to send messages from one to another. To make this happen, you will need to set up Send and Receive in ProtoPie Studio. To learn more about how messages are sent and received between ProtoPie and Arduino, click [here](https://www.protopie.io/learn/docs/blokdots/overview#connecting-proto-pie-with-arduino-via-blokdots).

![Setting up send and receive messages in ProtoPie Studio.](https://cdn.sanity.io/images/vidqzkll/production/a7bfe5e1fdbf598952855f28523e45dbf64c50ee-2175x1200.png/Connect-onoff-message.png)

**  6. Run the project.**

Click on the **Run** **Project** button in blokdots to run your project.

In ProtoPie Connect youâll be able to see messages coming through the blokdots plugin as you control your Arduino board.

![Messages coming through via blokdots.](https://cdn.sanity.io/images/vidqzkll/production/c10adfc267696ad3c54e4ea767ecbf1c4c80d1bc-1427x809.gif/Connect-messages-blokdots.gif)

To learn more about the blokdots and ProtoPie Connect integration, click [here](https://blokdots.com/documentation/components/integrations/protopie-connect/).


---

---
title: "Connect Embedded"
url: https://www.protopie.io/learn/docs/connect/connect-embedded
---

# Connect Embedded

# Connect Embedded

*Exclusively available as an add-on to the Enterprise plan. *

Connect Embedded is for teams who require ProtoPie Connect's functionality within embedded systems like Raspberry Pi.

It's a standalone server application that runs from a terminal and is compatible with operating systems such as Windows, MacOS, and Linux ARM64 (for Raspberry Pi). 

Connect Embedded uses a license file-based authentication and, as it can perfectly run in isolated environments, it allows for advanced product user research and testing. 

![connect-embedded-terminal](https://cdn.sanity.io/images/vidqzkll/production/61d46d8374bd306cdc2e856db187fe5489b5f597-1980x1244.png/connect embedded.png)

- **Supported Platforms:**

  - macOS10.11 El Capitan or above.

  - Windows 10 or above, 64-bit.

  - Ubuntu 12.04 or above, 64-bit.

  - Raspberry Pi OS, 64-bit

  - Fedora 221, 64-bit.

  - Debian 8, 64-bit.

- **Storage:** 500MB or more.

- **RAM:** 1 GB or more.

## Connect Desktop vs. Connect Embedded for the Enterprise Plan

The below table specifies the differences between Connect Desktop and Connect Embedded.

## Installing Connect Embedded

![Installing Connect Embedded ](https://cdn.sanity.io/images/vidqzkll/production/2ab9dc7149d7584205bc5086460d978f3c68f102-800x509.gif/install-connect-embedded.gif)

     1.   Extract the installation file required by your operating system.

  - Linux/Raspberry Pi: tar file.

  - Windows: zip file.

  - macOS: dmg file.

     2.    Move the files in the folder to the directory of your choice.

  - If you want to upgrade your Connect Embedded version, simply replace the existing files with the new ones.

## Logging into Connect Embedded

User authentication in Connect Embedded occurs through a **license file**.

- One license per each machine running Connect Embedded.

- An internet connection is not required.

- Connect Desktop and Connect Embedded cannot run at the same time. 

![connect-embedded-run-in-terminal](https://cdn.sanity.io/images/vidqzkll/production/1a3dcad9f27e316cece2b9927fae9d85d9636961-1980x1244.png/loggin into connect embedded.png)

     1.   Download ProtoPie Connect and run it from the terminal.

  - macOS:`**./pc-mac**`**,**

  - Windows: `.``**/pc-win.exe**`**,**

  - Ubuntu(intel):`**./linux-x64**` ,

  - Raspberry Pi (64bit arm): `**./linux-arm64**`

     2.   The terminal will print a **Device ID**.

     3.   Communicate the Device ID to our team when requesting access. You will be provided with a **license.txt** file.

    4.   Move the license file to the same directory where Connect Embedded is saved.

    5.   Run Connect Embedded from the terminal again, and check whether you see the following log message:Â **Licensed to YOUR NAME until YOUR EXPIRED DATE**.

    6.   Open the link displayed on the terminal in your browser or any other browser within your local area network (LAN).


---

---
title: "Custom Layer Integrations"
url: https://www.protopie.io/learn/docs/connect/custom-layer-integrations
---

# Custom Layer Integrations

# Custom Layer Integrations

ProtoPie Connect's Stage view enables you to integrate ProtoPie prototypes with diverse custom layers, including web, embeds, live cameras, and Unity projects. This integration enhances the user testing experience and renders your designs more dynamic.

## Creating a Stage View

Follow these steps to create a Stage view:

1. Open ProtoPie Connect.

1. Create a new Group and drag & drop your prototypes (Pies) into the group.

1. Select the group.

1. Click on the **View** icon to open the prototypes in a Stage.

## Embedding Custom Layers

After creating the Stage view, access the stage option menu by right-clicking. To begin editing, click the Edit button. An "Edit Mode" message will confirm that editing is enabled.

To add new prototypes or custom layers:

- From the upper-left corner, click on **Add**.

- You can include the following layers in the Stage: 

  - **ProtoPie prototypes**

  - **Web embed** via URL or iframe code (supports Maps, Spline, Rive, Bezi, etc.)

  - **Live camera** (select from available cameras or live streaming options)

  - **Unity projects** (supports import of WebGL build)

![custom layer integrations in stage view](https://cdn.sanity.io/images/vidqzkll/production/d0f1bf0370bf48c309d46b5b586b03b87f31952f-1830x999.png/stage.png)

### Configuring Web Embed Layers

You can set its URL via the properties panel after adding a new Web Embed layer to the Stage.

You can provide a full URL or iframe code. Web embeds support various formats such as Maps, Spline, Rive, and Bezi. It is important to ensure the URL is valid and you have the necessary permissions to access it.

![spline iframe embedding](https://cdn.sanity.io/images/vidqzkll/production/f72fd7677a496655770d7e10d2e4c7e39f153ced-1007x552.png/CleanShot 2024-02-27 at 17.05.17@2x.png)

### Configuring Live Camera Layers

To add camera feeds to your project, utilize the Live Camera layer. This feature supports:

- USB-connected cameras, such as webcams

- Your laptopâs camera

- Live streaming URLs (HLS)

Before using the camera layer, make sure to grant permission to your web browser. After adding the camera layer, configure its properties through the Camera properties panel.

![embed camera feeds in stage view protopie connect](https://cdn.sanity.io/images/vidqzkll/production/3d2b9cb66a97eb113771cc5e9459a4591b890769-1616x916.png/CleanShot 2024-02-27 at 17.14.13.png)

### Configuring Unity Layers

To add Unity scenes to your project, utilize the Unity layer. This feature supports:

- Importing WebGL build of Unity scenes

- ProtoPie Plugin for Unity

It is important to [build your Unity projects using WebGL](https://docs.unity3d.com/Manual/webgl-building.html) as the target platform. The resulting Build folder will contain `.loader.js`, `.framework.js`, `.wasm`, and `.data` files, which you need to archive into a zip file. Insert the zip file as a Source File to import the Unity project as a layer.

![unity layer](https://cdn.sanity.io/images/vidqzkll/production/7bbe42318cbdf41770c9887b81eb2ffd08c2f595-1440x900.png/unity.png)

The [Unity Plugin](https://www.protopie.io/learn/docs/connect/unity-plugin) will allow Send/Receive messages to work together with Unity scenes allowing for increased interactivity between the ProtoPie and Unity layers. It is a package that can be added to the Unity project and downloadable from the [Unity Asset Store](https://www.notion.so/ProtoPie-Connect-Custom-Layer-Integrations-e2b2f9e905b74d9a81f647dc03913e6d?pvs=21). For more information, refer to the [Unity Plugin](https://www.protopie.io/learn/docs/connect/unity-plugin) documentation.

## Previewing the Stage View

After adding and configuring layers, rearrange them within the Stage by dragging. To access positioning options, right-click on a layer. Preview the Stage by clicking **View** when ready.

## FAQs


---

---
title: "Custom Plugins"
url: https://www.protopie.io/learn/docs/connect/custom-plugins
---

# Custom Plugins

# Custom Plugins

Available in the Enterprise plan only.

ProtoPie Connect is equipped with several pre-installed plugins, including [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [Logitech G29 steering wheel](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [Gamepad](https://www.protopie.io/learn/docs/connect/gamepad-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), and [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin). 

Additionally, users on the Enterprise plan can upload their own custom plugins, enabling them to connect their prototypes to any hardware, APIs, or apps that support [Socket.IO](http://socket.io/) via ProtoPie Connect.

## Creating Custom Plugins

Custom integrations in ProtoPie Connect can be achieved using Custom Plugins and Bridge Apps. However, we suggest using Custom Plugins instead of Bridge Apps. As Custom Plugin files are portable, they are easier to work with and share among team members.

Hereâs how you create a Custom Plugin:

1. Write your code or reuse an existing [Bridge App](https://github.com/ProtoPie/protopie-connect-bridge-apps).

1. Compile your Bridge App into a single executable binary using [pkg](https://github.com/vercel/pkg)
Index.js files can be compiled for multiple targets (more details [here](https://github.com/vercel/pkg/blob/main/README.md)).

- `pkg -t node16-macos-arm64 index.js` for Mac ARM

- `pkg -t node16-macos-x64 index.js` for Mac Intel

- `pkg -t node16-win-x64 index.js` for Windows

     3.   Copy the executable file to an empty directory and name it `plugin`. Create a metadata.json file and add the pluginâs name `{ "name": "name of the plugin" }`.

     4.  Compress the file (.zip). Your Custom Plugin is now ready to be used!

![compress-custom-plugins](https://cdn.sanity.io/images/vidqzkll/production/4542a01e8d9505d0645b5d373c0b6f05177c5466-2175x1110.png/compress-custom-plugin-connect.png)

5. Import the Custom Plugin into ProtoPie Connect and run it in the terminal.

![protopie-connect-custom-plugin](https://cdn.sanity.io/images/vidqzkll/production/2bac0a0654769ce45243c1e1cb3910a04a669c40-1450x802.png/custom-plugin.png)

You can find some Custom Plugins examples [here](https://github.com/ProtoPie/protopie-connect-custom-plugins).

## What is a Bridge App?

Bridge Apps enable communication between any hardware, APIs, or app supportingÂ [Socket.IO](http://socket.io/) and ProtoPie Connect. Bridge Apps can catch events, receive data from a server, and even work as a single application.

For your convenience, you can use and customize these [Bridge Apps](https://github.com/ProtoPie/protopie-connect-bridge-apps) available on GitHub.

## Connecting Hardware via Bridge App

The main role of a Bridge App is to convert signals from the hardware into Socket.IO messages - a language ProtoPie can understand - and/or vice versa.

1. Connect the Bridge App to ProtoPie Connect.

1. The bridge app converts hardware signals into Socket.IO messages for ProtoPie to interpret. Usually, messages will have the following format:**
**â¦  **{messageId: "HwEventName", value: "ValueAssociatedWithEvent"}** 

1. Prototypes receiving these messages through ProtoPie Connect will respond accordingly. Some hardware supports bidirectional communication, meaning prototypes can send messages to the hardware. This is only possible if the Bridge App can convert Socket.IO messages into signals that the hardware can interpret.

## Connecting to APIs via Bridge Apps

When connecting to APIs via Bridge Apps, the Bridge App converts API responses (e.g., JSON) into individual [Socket.IO](http://socket.io/) messages.

For example, if a prototype needs to retrieve weather data dynamically from an API, the Bridge App would do the following:

1. Convert the JSON response into Socket.IO messages.
â¦  E.g., **{"weather": "sunny", "temperature-celsius": 30.5}**

1. Send Socket.IO messages to ProtoPie Connect that will, in return, relay them to the corresponding prototypes.**
**â¦  **{messageId: "weather", value: "sunny"}**,**
**â¦  **{messageId: "temperature", value: 30.5}**

In the prototype, you need Receive triggers to receive the messages **âweatherâ** and **âtemperature.â** [Learn more](https://www.protopie.io/learn/docs/interactions/triggers#receive) about the Receive trigger.

## Running the Bridge App on the Same Machine

By default, most of these [Bridge Apps](https://github.com/ProtoPie/protopie-connect-bridge-apps) use the IP address **http://localhost:9981** as they assume the Bridge App and ProtoPie Connect run on the same machine.

![running-bridge-app-same-machine](https://cdn.sanity.io/images/vidqzkll/production/0a9c6e8432b7e48b5534718bcd1dd00c7cc170b1-886x298.png/running bridge app same machine.png)

## Running the Bridge App on a Different Machine

If the Bridge App and ProtoPie Connect run on different machines, you can change the IP address to match ProtoPie Connectâs server.

- ProtoPie Connect Desktop: find the server address in the below left corner of the interface.

![ip-address-connect-desktop](https://cdn.sanity.io/images/vidqzkll/production/075172147b91b3ce3ef367dc7e832040e63578fa-1450x128.png/ip-address-connect-desktop.png)

- ProtoPie Connect Embedded: find the server address right after launching in the terminal. 

![ip-address-embedded-systems](https://cdn.sanity.io/images/vidqzkll/production/fdd3c353047ddbdb7aadabe8e8e15fe14f46c225-2232x366.png/ip-address-embedded-systems.png)


---

---
title: "Gamepad Plugin"
url: https://www.protopie.io/learn/docs/connect/gamepad-plugin
---

# Gamepad Plugin

# Using the Gamepad Plugin in ProtoPie Connect

The Gamepad plugin is one of the many built-in plugins in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started) that allows you to create dynamic, multi-device prototyping experiences. Read along to see how the Gamepad plugin works.

## How It Works

### Prerequisites

In the Security & Privacy Settings of your computer, enable **Input Monitoring** for both ProtoPie Connect and your browser.

![Enable input monitoring.](https://cdn.sanity.io/images/vidqzkll/production/6e166bb1f23aae08718a27a494e8381a44b2936e-2175x1200.png/Gamepad Plugin 2.png)

### Getting Set-Up

1. Open ProtoPie Connect.

2. Connect your Gamepad via USB or Bluetooth to the machine where   ProtoPie Connect is running.

- In the Gamepad Settings window, Device Status will indicate Connected when the Gamepad is detected. If the plugin does not recognize the gamepad, try pressing some buttons on the Gamepad first.

![Connected.](https://cdn.sanity.io/images/vidqzkll/production/e549e2279cc332f36874a06758777cb8f89224d2-1440x900.png/gamepad.png)

3. Press Run to activate the gamepad connection with ProtoPie Connect. 

4. When the Gamepad buttons are pressed, ProtoPie Connect automatically detects the keystrokes and broadcasts message and value pairs to the Pies running on Connect.

## Connecting Multiple Gamepads

ProtoPie Connect supports connections with multiple Gamepads.

- The message will follow the below format:

  - {Gamepad Number}_{Button Name}

- Gamepad Number is assigned from 1 in the following connection order:

  - Gamepad connected first will have Gamepad number of 1.

  - Gamepad connected second will have Gamepad number of 2.

- The number of connected gamepads is displayed in the Gamepad Settings window.

![Gamepad number.](https://cdn.sanity.io/images/vidqzkll/production/1a77cfcfe21140b530e9df0f118c4346a71fb884-2175x1200.png/Gamepad Plugin.png)

## Gamepad Buttons and Messages

Gamepad buttons and messages are as follows (assuming messages are received from the first connected gamepad).

![gamepad buttons](https://cdn.sanity.io/images/vidqzkll/production/8a699ce151a789195f79ff3b7eef3cf7eac73ca1-2000x1675.png/gamepad-plugin-.png)

### Gamepad Plugin â Buttons and Messages

Learn more about ProtoPie Connect's various built-in plugins, such as [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [Logitech G29 Steering Wheel](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), and [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin) plugins.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/connect/getting-started
---

# Getting Started

# What is ProtoPie Connect?

[ProtoPie Connect](https://www.protopie.io/connect) is an extension for ProtoPie Studio that allows you to prototype real-world scenarios involving multiple devices, displays, hardware, and APIs seamlessly. It comes with all ProtoPie plans, including the Free plan. Learn more about the [different versions of Connect](https://www.protopie.io/plans) per price tier.

## How to Get Started?

Download and install ProtoPie Connect to start building dynamic prototypes that go beyond traditional mobile interactions:[ Download ProtoPie Connect here.](https://www.protopie.io/connect)

## How Prototypes Communicate in ProtoPie Connect

Communication between multiple devices connected via ProtoPie Connect occurs through Send and Receive messages. The same messaging system is used to pass information back and forth between scenes and components and to create interactions between two devices using ProtoPie Studio as a hub ([connecting devices](https://www.protopie.io/learn/docs/connecting-devices/getting-started)).

Using the [Send response](https://www.protopie.io/learn/docs/interactions/responses#link), you can send messages to prototypes or hardware devices. You need to use the Receive trigger for other prototypes to hear such messages and respond accordingly.

It is important that both Send and Receive are set up to use the same channel in ProtoPie Studio. For prototypes communicating through ProtoPie Connect, the channel must be "**ProtoPie Connect/ Studio.**"

![protopie connect diagram](https://cdn.sanity.io/images/vidqzkll/production/3d90f7a01a70d41074b69cb17b7130799cdb072c-3920x2480.png/send-receive-connect-protopie.png)

## How ProtoPie Connect Works

At its core, ProtoPie Connect acts as a [socket.IO](http://socket.IO) communication server connecting multiple clients:

- ProtoPie prototypes running on smart devices (iOS, Android)

- ProtoPie prototypes running on web browsers on desktops

- Hardware systems (e.g., Arduino, Logitech G29 steering wheel)

- External services (e.g., IFTTT webhooks, public APIs)

The clients can communicate either locally, through a localhost server, or within a local area network (LAN). ProtoPie Connect listens on port 9981 to all the IP addresses of the machine on which it is running. You can also modify the active IP address on ProtoPie Connect by clicking on Network from the menu bar and selecting another IP address.

Let's take automotive as an example. In the following video, tapping a button on the center display triggers animations on the cluster and head-up display (HUD). This is possible thanks to the flexibility and power of ProtoPie Connect.

[Video: ](https://www.youtube.com/watch?v=702pLk1MnqY)

## Connect Desktop vs. Connect Embedded

There are two different types of ProtoPie Connect:

- ***Connect Desktop***

- ***Connect Embedded***

Connect Desktop runs on macOS and Windows. It allows you to run multiple prototypes simultaneously and create immersive multi-screen experiences. It includes built-in plugins to integrate ProtoPie with external hardware devices and services, including Arduino and IFTTT. Enterprise plan users can also upload their own custom plugins to create even more unique digital experiences.

Learn more about [Connect Desktop](https://www.protopie.io/learn/docs/connect/managing-testing-prototypes) and its [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [G29](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [Gamepad](https://www.protopie.io/learn/docs/connect/gamepad-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin), and [custom](https://www.protopie.io/learn/docs/connect/custom-plugins) plugins. 

As its name suggests, Connect Embedded is designed to run on embedded systems such as Raspberry Pi. Itâs a standalone server application that runs in the terminal. 

Connect Embedded is only available to Enterprise plan users. Learn more about [Connect Embedded.](https://www.protopie.io/learn/docs/connect/connect-embedded) 

## Complete Guide to ProtoPie Connect

![protopie connect free guide](https://cdn.sanity.io/images/vidqzkll/production/9b44362e78be69370302148b5f0a49053dfd30e8-2000x955.png/Frame_3.png)

[ProtoPie School](https://learn.protopie.io/)Â offers aÂ comprehensive guideÂ to ProtoPie Connect in 8 lessons. It starts with a refresher onÂ Send & Receive, then dives into using ProtoPie Connectâs built-in plugins, including how to make yourÂ ownÂ plugins to integrate with just about anything with a screen â and beyond! 
Enroll for freeÂ [here](https://learn.protopie.io/course/protopie-connect).


---

---
title: "IFTTT Plugin"
url: https://www.protopie.io/learn/docs/connect/ifttt-plugin
---

# IFTTT Plugin

# Using IFTTT with ProtoPie Connect

## What is IFTTT?

IFTTT is a web automation service that enables integration with various devices and services including [Twitter](https://ifttt.com/twitter), [Dropbox](https://ifttt.com/dropbox), [Evernote](https://ifttt.com/evernote), [Fitbit](https://ifttt.com/fitbit), [Amazon Alexa](https://ifttt.com/amazon_alexa), andÂ [Google Assistant](https://ifttt.com/google_assistant).

IFTTT stands for 'If This Then That', and the Applets you create in IFTTT work similarly to ProtoPieâs triggers and responses: *If this happens â then that happens.*

Learn more about IFTTT [Applets](https://help.ifttt.com/hc/en-us/articles/4411016949403#Applet).

## How does the IFTTT plugin work?

ProtoPie Connect communicates with IFTTTâs partner services through messages called [Webhooks](https://ifttt.com/maker_webhooks). These work similarly to the Send and Receive messages in ProtoPie. A message (âEventâ) is sent to IFTTT and in response, IFTTT translates the message into an action.

By using ProtoPie Connect with IFTTTâs Webhooks, you can connect your prototypes to all their partner web services and devices.

## Creating Applets in IFTTT

Create an account on the [IFTTT](https://ifttt.com/) website.

### **Configuring the Trigger**

![configuring-trigger-in-ifttt](https://cdn.sanity.io/images/vidqzkll/production/e58bcc7fbae827e5138febf2ae357eb75ee486e0-1345x998.gif/configuring-trigger-ifttt.gif)

1. Once logged in, click on **Create** on the top right corner of the IFTTT page

1. Click on **Add** from the **If This** section and search for **Webhooks**

1. Select â**Receive a web request**â

1. Name your event and click on **Create Trigger**. You can only use letters, numbers, and underscores in the name (for instance: âsend_emailâ)

### Configuring the Action 

![configuring-the-action-in-ifttt](https://cdn.sanity.io/images/vidqzkll/production/40358895da950a8c229133ff5c0449b9989af74a-1345x965.gif/configuring-action-ifttt.gif)

1. Click on the **Add** button in the **Then That** section

1. Search for your desired action in the **Choose a service** field

- For example, âGmailâ - âSend yourself an Emailâ

      3.   Configure the action fields

- Fill in the sections â**Subject, Body, To address, CC address, BCC address, and Attachment URL**â Click on the **Add ingredient** button to add up to 3 customizable values (âValue1, Value2, Value3â) that will have to be configured in ProtoPie Studio (see Configuring Messages in ProtoPie Studio)

- Click on Update Action

- Review your Applet and click on **Finish**

      4.   Your Applet is now active. It can be deactivated and reactivated by switching the **Connected** button.

## Connecting IFTTT to ProtoPie Connect

Configure ProtoPie Connect to send a request to IFTTT.

### Testing your Applet

      1.   Open and log into ProtoPie Connect.

      2.   Select **IFTTT** from the Plugin dropdown menu.

- Copy-paste your private **Webhook Key**, which you can find on the IFTTT website under Explore â âWebhooksâ â Documentation

- Click on the **Run** button

      3.   You can test the Applet in the Test section

- Enter your event name and JSON payload

- Click on **Send**

![testing-your-applet](https://cdn.sanity.io/images/vidqzkll/production/a12a375c72490a11b9e9ff9bdc1a762c12a25c08-4000x1966.png/IFTTT (1).png)

You can verify if your Applet is working correctly by going to My Applets on the IFTTT website and clicking on **View activity**.

![view-activity-applet](https://cdn.sanity.io/images/vidqzkll/production/e1289aafc053a711a7cbecc3efdd22aceec46656-1450x1022.png/ifttt-view-activity-applet.png)

      3.   You will receive an email with the values specified in the JSON payload.

## Configuring Messages in ProtoPie Studio

Now that you have created and tested your Applet, you need to configure the corresponding messages in the prototype using ProtoPie Studio.

Set up the Send responses that will trigger the action in the Applet.

- Use the channel âProtoPie Studioâ to communicate with ProtoPie Connect and activate âSend Value Togetherâ.

- Configure your JSON Payload values if you used one or more in the IFTTT Applet.

![json-upload-ifttt](https://cdn.sanity.io/images/vidqzkll/production/8a88ce4dc739f329525ba9015ac5adf1e9f00aea-1366x660.png/json-payload-protopie-ifttt.png)

- Test the prototype in ProtoPie Connect


---

---
title: "Logitech G29 Steering Wheel Plugin"
url: https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin
---

# Logitech G29 Steering Wheel Plugin

# Using the Logitech G29 Steering Wheel with ProtoPie Connect

Create realistic multi-screen automotive experiences thanks to ProtoPie Connect and the [Logitech G29 Steering Wheel ](https://www.logitechg.com/en-us/products/driving/driving-force-racing-wheel.html)plugin.

[Video: ProtoPie Automotive Solution](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DF2NcgDwJago&feature=youtu.be)

[Learn more](https://www.protopie.io/solutions/automotive) about prototyping with ProtoPie for automotive.

## The Information Flow

The below image illustrates the information flow between ProtoPie and the Logitech G29 steering wheel.

![The information flow between Connect and G29.](https://cdn.sanity.io/images/vidqzkll/production/9859ac65eaf0bd04ce3f42c31bef192079710a5a-2175x1200.png/Connect-steering-wheel-info-flow.png)

- The Logitech G29 steering wheel sends [events and values](https://github.com/nightmode/logitech-g29/blob/HEAD/docs/api.md#events) to ProtoPie Connectâs G29 plugin.

- The G29 plugin converts these events & values to [Socket.IO](http://socket.io) messages for ProtoPie to understand.

- Prototypes added to ProtoPie Connect receive these inputs and respond accordingly using **Send** and **Receive** messages.

## The Ecosystem

Below is a typical ecosystem when using the G29 plugin in ProtoPie Connect.

- 1 machine with USB ports and WiFi/network capabilities

  - To run ProtoPie Connect and connect to the Logitech G29 steering wheel via USB.

- 1 Logitech G29 racing wheel and pedal (optional) set

  - [Example](https://www.amazon.com/Logitech-Dual-motor-Feedback-Responsive-PlayStation/dp/B00Z0UWWYC).

- 2 tablets (iPadOS or Android) or 2 computer monitors

  - For prototypes that need to be opened on a larger display (ProtoPie Connectâs web browser, ProtoPie Player on tablets).

- 1 smartphone (iOS or Android)

  - For prototypes that need to be opened on a mobile display (ProtoPie Player).

## Getting Set Up

Below is the most recommended setup for handling messages between the Logitech G29 steering wheel and prototypes made in ProtoPie. At the end your setup should look like the one shown in the video at the top of this page.

![Connect and G29 - the setup.](https://cdn.sanity.io/images/vidqzkll/production/7980a5b3e44427598c981c1b43c36bf362d30eb0-2175x1200.png/Connect-steering-wheel-setup.png)

- Use 2 **large displays** and 1 **smartphone** for running your prototypes (smartphones, tablets, and monitors can all serve as displays).

- Connect **ProtoPie Player** to **ProtoPie** **Connect** via WiFi (same LAN).

- Connect the **Logitech G29** steering wheel via USB to the machine where **ProtoPie** **Connect** is running:

  - In ProtoPie Connect click on the **Plugins** button in the upper right corner.

  - Select **G29** in the Plugin list.

![The G29 plugin in ProtoPie Connect.](https://cdn.sanity.io/images/vidqzkll/production/92197db76bb519e3f93968b5dc1e0b58a5223b3b-1450x800.png/G29.png)

  - If you have the PlayStation version of the G29, it has a switch that allows you to toggle between PS3 and PS4 compatibility mode. Make sure it is switched to **PS3 mode.**

![PS3 mode in G29 steering wheel.](https://cdn.sanity.io/images/vidqzkll/production/5b168b66db75d0378ca0f5b89f3d8ea4663a18ed-2175x1200.png/Connect-G29-PS3-mode.png)

  - **Plug in** the **G29** USB cord into the computer.

  - Click on the **Run** button.

![Run the G29 plugin in ProtoPie Connect.](https://cdn.sanity.io/images/vidqzkll/production/be974fc2861efbca400ef6e2962f397a49523567-1450x810.png/G29-1.png)

  - The G29 steering wheel is now ready for use.

![G29 plugin is now ready to use.](https://cdn.sanity.io/images/vidqzkll/production/0eef53caf4be79867ff4e444d0afcad992656633-1450x809.png/G29-2.png)

## Examples

### Turning the Steering Wheel Left

Turn the steering wheel left to rotate and change the color of a layer in ProtoPie Studio.

![Turning the Steering Wheel Left.](https://cdn.sanity.io/images/vidqzkll/production/cf3c555274e1aa9ef43258ad588c893b7fdffe06-2175x1200.png/Connect-steering-wheel-left.png)

- When you turn the Logitech G29 steering wheel fully to the left, the G29 plugin converts the incoming event into a message ProtoPie can interpret.

- The prototype loaded to ProtoPie Connect receives this message and assigns it to a variable when triggering the Color and Rotate responses.

### Pressing a Button on the Steering Wheel

Press the triangle button on the steering wheel to trigger actions in two separate prototypes.

![Pressing a Button on the Steering Wheel.](https://cdn.sanity.io/images/vidqzkll/production/155ddbf57bbed9732a202a63c66c4204c8703e7c-2175x1200.png/Connect-steering-wheels-button.png)

- When you press the triangle button on the Logitech G29 steering wheel, the G29 plugin converts the incoming event into a message ProtoPie can interpret.

- The two prototypes loaded to ProtoPie Connect respond to this message accordingly, depending on how you set up your interactions.

  - For example, one prototype recreates a blinking light and the other prototype shows a text saying âEmergencyâ.


---

---
title: "Testing Prototypes"
url: https://www.protopie.io/learn/docs/connect/managing-testing-prototypes
---

# Testing Prototypes

# Testing Prototypes in ProtoPie Connect 

 ProtoPie Connect allows you to test your prototypes on a variety of smart devices and desktop browsers. You can use ProtoPie Connect in the following ways:

- To test prototypes using ProtoPie Connect and ProtoPie Player

- To test prototypes using ProtoPie Connect and ProtoPie Player for Wear OS

- To test prototypes on web browsers

- To test prototypes in [Stage View](https://www.protopie.io/learn/docs/connect/custom-layer-integrations#creating-a-stage-view).

Download ProtoPie Connect [here](https://www.protopie.io/download).

## Adding Prototypes to ProtoPie Connect

Before testing, load your prototypes into ProtoPie Connect by following these simple steps:

- Click the + New button and select the prototypes you want to add. Or drag-and-drop prototypes into ProtoPie Connect's interface.

  - Enterprise users can open prototypes directly from ProtoPie Cloud by selecting Cloud Pie. To fetch the most recent version of a Cloud Pie, click on the circular arrow icon (Reload).

- Select the Pie file and click the trash icon to remove a prototype from the list.

- To replace a prototype, place the cursor on the prototype and click on the two-way arrow icon.

  - Technical note: Adding a new Pie file creates a new ***pieid***. Replacing a Pie file reuses the same pieId of the previous prototype. 

![managing prototypes](https://cdn.sanity.io/images/vidqzkll/production/50a8cf5a6892a40645c7ab6091e76cea313f3dc0-1316x856.gif/import-new-pie-connect.gif)

### Arranging Pies into Groups 

To keep your Pies organized and easy to manage, you can group them together. To create a new **Pie group**, click on the Group icon. To add a Pie to a group, drag and drop it into the group. Be sure to expand the group before doing so.

- To move a Pie from one group to another one, drag and drop it into another group.

- Only groups containing at least one Pie can be expanded/ collapsed.

- Only groups containing at least one Pie can be selected/ deselected.

- To rename a group, double-click on the group name and enter the new name.

- To delete a group, hover over it with the cursor and click the Trash icon.

![users can now group their pies in Protopie connect with the Group feature](https://cdn.sanity.io/images/vidqzkll/production/980ad01bf0ab651f6bb4a251dc6c473a4b44a2a2-1314x858.gif/Pie-groups-connect.gif)

## Testing Prototypes Using ProtoPie Connect & ProtoPie Player

[ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) is a free companion app for ProtoPie Studio and ProtoPie Connect. You can view, experience, and test any prototypes added to ProtoPie Connect on iOS, iPadOS, and Android devices. 

There are three ways to connect ProtoPie Player to ProtoPie Connect:

1. Scanning the QR code

1. Entering the IP address

1. Using a USB cable  

### Connect ProtoPie Player to ProtoPie Connect Scanning the QR Code

1. Ensure your computer and smart device are connected to the same WiFi network.

1. Click on Connect for the prototype you want to open in ProtoPie Connect.

1. Select ***QR Code*** from the list.

1. Tap on theÂ Scan QR CodeÂ button in ProtoPie Player.

1. Scan the QR code to run the prototype in the Player.

![scan qr code player connect](https://cdn.sanity.io/images/vidqzkll/production/e3dbf19b1d56b9f9d3a4b2429599566384f2780c-1450x800.png/1-Connect-managing.png)

### Connect ProtoPie Player to ProtoPie Connect Entering the IP Address

1. Make sure your computer and smart device are connected to the same WiFi network.

1. Tap onÂ Type IP AddressÂ from the dropdown menu in ProtoPie Player.

1. Enter the IP address shown in ProtoPie Connect. 

1. Tap on the Connect button to run the prototype on your smart device.

![entering ip address connect](https://cdn.sanity.io/images/vidqzkll/production/9d1ff670e4977f89dfe1a23f1daf5fe95dfe6095-1450x800.png/2-Connect-managing.png)

## Testing Prototypes Using ProtoPie Connect & ProtoPie Player for Wear OS

[ProtoPie Player for Wear OS](https://www.protopie.io/learn/docs/player/player-for-wear-os), unlike the regular ProtoPie Player, only works in conjunction with Connect Enterprise. 

1. Make sure both ProtoPie Player for Wear OS and ProtoPie Connect are connected to the same internet network.

1. Open themâProtoPie Player for Wear OS and ProtoPie Connect will automatically detect each other 

1. Click on Tap to connect in the ProtoPie Player for Wear OS to pair it with ProtoPie Connect.

1. Add a smartwatch prototype to ProtoPie Connect.

1. Click on the Run button at the top of ProtoPie Connect's interface to open the prototype in the Player for Wear OS.

1. To restart or exit the prototype, double-tap the smartwatch screen. 

## Testing Prototypes on Web Browsers

To view a prototype on a browser, it is recommended to use a Chromium browser for optimal performance. There are two ways to open a prototype on a desktop web browser from ProtoPie Connect. 

- On the same machine where ProtoPie Connect is running 

- On a different machine 

### Testing Prototypes On the Same Machine

1. Click on the Web Browser icon next to the prototype you want to open.

1. In the browser, the URL will have the following format: http://localhost:9981/.

![ProtoPie Connect IP address ](https://cdn.sanity.io/images/vidqzkll/production/cd974abbca5dade134c7f187e6b24446bcfcaef3-1450x800.png/3-Connect-managing.png)

### Testing Prototypes On a Different Machine

1. Ensure your computer and the other machine are connected to the same WiFi network with ProtoPie Connect.

1. Open any web browser on the other machine.

1. Enter your ProtoPie Connect IP address in the address bar. The ProtoPie Connect interface will be displayed.

1. Click on the Web Browser icon next to the prototype you want to open.

1. In the browser, the URL will have the following format: http://protopie.connect.ip.address:9981/.

### Using Voice Prototyping Features in the Web Browser

Starting from ProtoPie Connect 1.8.0, voice prototyping features are supported in the Web Player, just like they are in the ProtoPie Player app for iOS/Android and ProtoPie Studio's Preview window. Currently, the supported features are:

- [Voice Command Trigger](https://www.protopie.io/learn/docs/voice-prototyping/voice-command-trigger)

- [Speak Response](https://www.protopie.io/learn/docs/voice-prototyping/speak-response)

- [Listen Response](https://www.protopie.io/learn/docs/voice-prototyping/listen-response)

#### Compatible web browsers

Each browser behaves differently when dealing with microphone permissions. To use the Voice Command Trigger and Listen Response, the browser needs microphone permission from the user. The browser will ask for **microphone permission** when the microphone needs to be enabled in the prototype, like in the screenshot below. To enable microphone access, click Allow.

![Enabling microphone access](https://cdn.sanity.io/images/vidqzkll/production/4bd9f730ca9d37a41b217ca6f8ab5169799ac329-2175x1200.png/ProtoPie Connect - enable mic.png)

Voice prototyping features for the ProtoPie Connectâs Web Player work best in Chromium browsers such as **Google Chrome** and **Microsoft Edge**. To properly play voice interactions some setup may be required on the browser side depending on the browser used and how the prototype is loaded.

#### Web Browser Setup

There are two ways to play prototypes in the web browser:

1. On IP address

1. On http://localhost:9981/

Playing prototypes on http://localhost:9981/ requires no setup and works across browsers.

Playing prototypes on IP address (e.g., http://192.168.0.40:9981/) requires a **one-time browser setup** to enable microphone usage, and is supported on **Google Chrome** and **Microsoft Edge**.

Chromium browsers will only allow your device's microphone permission when a site has a secure origin â i.e. serve from https or localhost.

The following one-time setup is required to use a microphone with ProtoPie Connect's Web Player.

1. In the Chrome/Edge browser, navigate to `flags`.

`chrome://flags/#unsafely-treat-insecure-origin-as-secure`

`edge://flags/#unsafely-treat-insecure-origin-as-secure `

2. Enable `Insecure origins treated as secure`.

![Adding the ProtoPie Connect server details.](https://cdn.sanity.io/images/vidqzkll/production/cc621829db8308280082ec0de1995857686b21d2-2175x1200.png/ProtoPie Connect - one time browser set up.png)

3. Add the ProtoPie Connect server address with port number 9981.

Note: The server address can be found in the bottom left corner of ProtoPie Connect.

![ProtoPie Connect server address](https://cdn.sanity.io/images/vidqzkll/production/9d1ff670e4977f89dfe1a23f1daf5fe95dfe6095-1450x800.png/2-Connect-managing.png)

4. Relaunch (Restart) the Chrome/Edge browser.

![Relaunch Google Chrome.](https://cdn.sanity.io/images/vidqzkll/production/a789cbf5c1d64f5792117bb008a4adb3f1c4d078-2175x1200.png/ProtoPie Connect - relaunch chrome.png)

### Customizing View Options

As on [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#managing-display-options), you can customize how prototypes display on the web browser using **URL parameters.**

- URLs with such parameters have the following format: http://localhost:9981/pie?pieid=[ number]&name=[pie name]â¦

- Use the â**&â** symbol to separate parameters in the URL.

- If you use a browser on a different machine, replace **localhost** with the IP address shown in ProtoPie Connect. For example, http://192.168.123.101:9981/pie?pieid=23.

**Some examples of URLs with parameters:**

- Change the background color to white, show hotspot hints, and scale the prototype to fit the screen.

  - **http://localhost:9981/pie?pieid=1&bg=white&touchHint=true&scaleToFit=true**

- Change the background color to yellow, and hide the cursor

  - **http://localhost:9981/pie?pieid=1&bg=yellow&cursorHide=true**

## FAQs


---

---
title: "Feature Comparison"
url: https://www.protopie.io/learn/docs/connect/protopie-connect-pro-vs-enterprise
---

# Feature Comparison

# ProtoPie Connect Feature Comparison

**ProtoPie Connect** is available for all plans and comes in three tiers: **Connect Free**, **Connect Core**,** **and** Connect Enterprise**.

- **Free Plan** users have access to **Connect Free**, which includes essential features to get started.

- [**Basic Plan**](https://www.protopie.io/plans/basic) and [**Pro Plan**](https://www.protopie.io/plans/pro) users can upgrade their experience by **adding Connect Core**.

- [**Enterprise Plan**](https://www.protopie.io/plans/enterprise) users get **Connect Enterprise** included as part of their plan, offering the most advanced capabilities.

Below is a feature comparison table that highlights the differences between the different versions of Connect. For a more detailed feature breakdown, [check out our pricing page](https://www.protopie.io/plans).


---

---
title: "Unity Plugin"
url: https://www.protopie.io/learn/docs/connect/unity-plugin
---

# Unity Plugin

# Unity Plugin

The Unity plugin is free for anyone to download and install. When integrating with ProtoPie Connect, Connect Core Add-on users can display up to one Unity layer. However, full message-based interactivityâsuch as animating Unity models or passing valuesâalong with support for unlimited layers, is exclusively available with Connect Enterprise.


![Plan Feature Availability](https://cdn.sanity.io/images/vidqzkll/production/6ccf21b86d29c8321802042da394a95f9da81a86-1780x730.png/Asset #1 (4).png)

 

Click here to [download the ProtoPie Connect Unity plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1).

## **Workflow for Integrating Unity with ProtoPie**

To prototype integrated interactions between ProtoPie and Unity, we suggest the following workflow:

1. Define the message set (mapping table) to be used for communicating with Unity. The Pies will interact with Unity via messages using Send/Receive features.

- In ProtoPie, messages in the Send response trigger events in Unity. When Unity sends a message to ProtoPie, messages in the Receive trigger serve as the identifier for the appropriate responses in ProtoPie.

2. [Install the Unity plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1) for the Unity project.

3. Define the mapping between ProtoPie messages and Unity events.

4. When ready to test together, [export the Unity scene as a WebGL build](https://www.protopie.io/learn/docs/connect/custom-layer-integrations#configuring-unity-layers) and add the build files as source files to the Unity layer in ProtoPie Connect.

5. Arrange the ProtoPie and Unity layers according to the desired layout and test the interactions together on the [Stage View](https://www.protopie.io/learn/docs/connect/custom-layer-integrations) in ProtoPie Connect.

## Unity Plugin Overview

- The plugin is installed in the Unity project as a package and allows one to map ProtoPie messages with Unity events without having to write any code. The plugin can be added to existing Unity projects in an unobtrusive manner and doesnât interfere with or break any existing Unity components.

- The plugin works by creating a **ProtoPie object** inside the Unity scene and utilizing the script component **Message Interaction** (provided by the package). The ProtoPie object is responsible for mapping the ProtoPie messages with events in Unity. Because the ProtoPie object handles all the mapping between the two platforms, there is no need to customize the Unity code elsewhere to make this integration happen.

- In the **Message Interaction** script component, one assigns a mapping table to use with the Unity scene. The mapping table is a list of messages to be used between ProtoPie and Unity. Once a mapping table has been assigned, the user can add the **Event(Unity)-Message(ProtoPie) Mappings** to be used in the Unity scene.

- In the **Event(Unity)-Message(ProtoPie) Mappings**, the user can designate the message mapping to use in the scene, the message direction, the desired action in Unity, the values to send back to ProtoPie, etc.

## **Unity Plugin Installation and Setup**

1. In the Unity Project, [install the ](https://www.protopie.io/14d4029732554ac1830c56c6a92eada1?pvs=25)[ProtoPie Unity](https://www.protopie.io/14d4029732554ac1830c56c6a92eada1?pvs=25)[ plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1).

2. In the Unity scene, create an empty object and name it "**ProtoPie**".

- The name must be "**ProtoPie**" (case sensitive) because ProtoPie Connect detects the object for message interactions using that name

3. Add âMessageInteraction.csâ (from ProtoPie Unity Package) script component to the **ProtoPie object**.

4. Select Add Component â Scripts â ProtoPie.Interaction â Message Interaction.

![Select Add Component â Scripts â ProtoPie.Interaction â Message Interaction](https://cdn.sanity.io/images/vidqzkll/production/4f4bb7b826e25df929121a0c978c51bd606551f1-1440x900.png/connect-msg.png)

4. Add **MappingTable** to the **Message Data** field in the Message Interaction component.

![Add MappingTable to the Message Data field in the Message Interaction component. ](https://cdn.sanity.io/images/vidqzkll/production/bc61936b5bdacd5fafde55818d02cf8a3ed9e76a-2000x2153.png/Screenshot_2024-05-07_at_1.00.34_PM.png)

- The MappingTable, in essence, defines the message set to be communicated between ProtoPie and Unity.

- It is a configuration file in YAML format, which allows you to specify the labels, the message to be transmitted, and the message flow direction.

- The mapping table is located in the package folder named MappingTablet.asset. Here, you can add/remove/edit the entries in the message mapping list.

5. The Unity scene is now ready to be used with ProtoPie Connect. Add your first mapping by pressing the **Add Mapping** button under Event(Unity)-Message(ProtoPie) Mappings.

## Message Mapping in the Unity Plugin

![message mapping](https://cdn.sanity.io/images/vidqzkll/production/c17311d578070519de8853f8b1fa6a142fe3d667-2000x2762.png/Screenshot_2024-05-07_at_1.09.09_PM.png)

ProtoPie and Unity layers communicate via messages to add interactivity between them. 

To add a message mapping, select **Add Mapping** to define which mapping to utilize. For each mapping, you will be able to select one of the mappingsÂ defined in the mapping table (the one used in the Message Data field).

### Attribute Definitions

- **Mapping Label**: the label or index of the mapping defined in the mapping table.

- **Message**: The message (or messageID in [socket.IO](http://socket.IO) terms) to send/receive between ProtoPie and Unity. This will correspond to the message in ProtoPieâs Send Response and Receive Trigger.

- **Message Direction:** The direction of message communication (ProtoPie to Unity, Unity to ProtoPie, Both Ways, None).

- **Desired Action (String)**: The action (method/function) that should be executed in Unity when ProtoPie sends the corresponding message to Unity (Applicable only when Message Direction is ProtoPie to Unity and Both Ways).

![message mapping](https://cdn.sanity.io/images/vidqzkll/production/daa5d3e85481a18b46441712e01fbb1d162aadb5-2000x1882.png/better.png)

  - The user should select the source object and the method to execute the action.

  - If ProtoPie sends a value along with the message, that value can be passed along as a String parameter to the action (method/function)

  - Note: The 'addCube(string)' option under 'Static Parameters' is not configurable at runtime. Instead, the string value must be predefined within the Unity Editor prior to building the project.

- **Event Object & Event to trigger message**: The Unity object and event that would trigger Unity to send the message to ProtoPie (Application only when Message Direction is Unity to ProtoPie and Both Ways).

- **Value Source Object & Value to Send:** (Optional) When sending a message from Unity to ProtoPie, additional data can be sent to ProtoPie via the messageâs value. The **Value Source Object** and **Value to Send** attributes define what kind of data to send back to ProtoPie.

  - Note: The plugin will recognize public string variables attached to the source object.


---

---
title: "Connecting blokdots"
url: https://www.protopie.io/learn/docs/connecting-devices/blokdots
---

# Connecting blokdots

# blokdots & ProtoPie

[blokdots](https://blokdots.com/) is a code-free software used to build interactive hardware prototypes with [Arduino](https://www.protopie.io/learn/docs/connect/arduino-with-connect). By using [ProtoPie](https://www.protopie.io) and blokdots together, you can bridge the gap between hardware and software prototyping without a line of code.

This integration is available with all plans. However, by using blokdots with [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started) you can unlock new possibilities, such as the ability to create hardware-software interactions involving three or more devices. Learn more about how the [blokdots plugin works](https://www.protopie.io/learn/docs/connect/blokdots-plugin) in ProtoPie Connect. 

Here is the simplest ecosystem for connecting ProtoPie to blokdots:

- ProtoPie Studio - for creating interactions.

- [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) - for running prototypes on smart devices.

- blokdots - to facilitate the communication between Arduino and prototypes via [socket.IO](http://socket.io/). 

![blokdots_and_protopie_environment](https://cdn.sanity.io/images/vidqzkll/production/e6281a443275cb3fd116a17ca4081b7dbb04e22d-2984x1172.png/blokdots_and_protopie_environment.png)

## Getting Ready

To use blokdots with ProtoPie you will need the following:

- Have the [blokdots app](https://blokdots.com/) installed on your desktop.

- Set up your Arduino board. Check the supported boards [here](https://blokdots.com/documentation/#Supported-Boards).

- A USB cable to connect your Arduino board to your laptop or PC.




- Activate the free trial of blokdots pro.

## Connecting Arduino to blokdots

Open blokdots and connect your Arduino board to your laptop or PC. 

Once you see that your board is ready in the top-left corner, you can start setting up your components.

### Setting Up Components in blokdots

1. Click  **Connect A New Component** and pick the ones you want to connect.

1. Choose an available Grove slot or hardware pin from the list

1. Click on **Set Component.**

This step is necessary for blokdots to know which components of the Arduino board to control.

![blokdots wizard bg](https://cdn.sanity.io/images/vidqzkll/production/091b7da8514db455c765eeab447293683e4328ab-2248x1696.png/blokdots-wizard-bg.png)

       

## Connecting ProtoPie with Arduino via blokdots

The blokdots app allows ProtoPie and Arduino to send messages from one to another. To make this happen, you will need to:

1. **Set up Send and Receive in ProtoPie Studio**

In ProtoPie Studio, the [**Receive Trigger**](https://www.protopie.io/learn/docs/interactions/triggers#receive) and the [**Send Response**](https://www.protopie.io/learn/docs/interactions/responses#send) will initiate communication between the devices. Make sure to set the **Channel** to **ProtoPie Studio.** The **Message** and **Value** can be set to whatever you wish.

**      **2.**   Create condition cards in blokdots**

To add logic to a blokdots component, you need to add and configure cards in the main area of the Project View. There are two types of cards in blokdots: âIf This Then Thatâ cards and âMappingâ cards.

As the final interactions take place between **ProtoPie Player** and **Arduino,** the combination of both will make communication possible.

### Receiving messages from blokdots to ProtoPie

To send a message from blokdots to ProtoPie, a condition card should have the following structure:

- If `the action of any input hardware component`

- Then `ProtoPie Player` should `send`Â `message`

In the smart home prototype example below, turning the Potentiometer on the Arduino board will change the temperature degree value displayed on the pie file running in the ProtoPie Player.

![blokdots to protopie](https://cdn.sanity.io/images/vidqzkll/production/d0195bc31ad8bb1db4d9685b5d61d4b907147b0d-1188x262.png/blokdots-to-protopie.png)

To receive messages from blokdots, use the **Receive** trigger in ProtoPie Studio as below.

![receive_trigger_protopie_studio](https://cdn.sanity.io/images/vidqzkll/production/4fef2678c0e1f920bd7804cabfbb0414bbe7313e-1760x953.png/receive_trigger_protopie_studio.png)

### **Sending messages from ProtoPie to blokdots**

To send messages from ProtoPie Studio to blokdots, use the **Send** response.

![send_response_protopie_studio](https://cdn.sanity.io/images/vidqzkll/production/c4c280987357b6a60faae371988bf02a7124ea2f-1760x952.png/send_response_protopie_studio.png)

To receive a message from ProtoPie, the condition card in blokdots should have the following structure:

- If `ProtoPie Player` is `receiving`Â `message`

- Then `the action of any input hardware component`

![protopie to blokdots](https://cdn.sanity.io/images/vidqzkll/production/397453f25df630ca995f48fdb0ccef9f8be012ca-1192x266.png/protopie-to-blokdots.png)

## Testing your Interactions

To test your interactions, do the following:

  1.    Connect ProtoPie Player with blokdots (iOS only for now)

Scan the QR code that blokdots will show when hovering above the ProtoPie icon in the lower-left cornerÂ or type the IP address. The ProtoPie Player component will change to green once it is set up.

![connecting_player_with_blokdots](https://cdn.sanity.io/images/vidqzkll/production/86e224f171452ed5458f8fa8e46185be7af031ea-725x400.png/connect-blokdots-player.png)

 2.  Connect ProtoPie Studio with ProtoPie Player

[Learn more](https://www.protopie.io/learn/docs/player/getting-started) about how to connect ProtoPie Player.

3.   Run your project in blokdots

Click on the **Run Project** button** **at the top of the project window.** **

![run blokdots project](https://cdn.sanity.io/images/vidqzkll/production/4202f5b40ffbabef84d5f07340c14408b9ac3e74-1072x712.png/run-blokdots-project.png)

If you want to learn more about the ProtoPie and blokdots integration and test it out on your own, check out this step-by-step [tutorial.](https://www.protopie.io/blog/protopie-and-blokdots-no-code-arduino-prototyping) 

## FAQs


---

---
title: "Connecting Mobile Devices"
url: https://www.protopie.io/learn/docs/connecting-devices/connecting-mobile-devices
---

# Connecting Mobile Devices

# Connecting Mobile Devices

In addition to designing interactions on a single device, ProtoPie enables prototyping interactions involving multiple devices communicating with each other. For example, you can easily simulate a chat or money transfer experience between connected devices.

[Video: Money Transfer - Video](https://www.youtube.com/watch?v=8HFkT2PsOQc)


There are two ways of creating connected experiences in ProtoPie:

- using ProtoPie Studio as a hub

- using ProtoPie Connect

You can connect two prototypes using [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem#proto-pie-studio) as a hub. This feature is available with all plans. ProtoPie Studio must remain open while testing interactions using this method.

You have two options for connecting prototypes via ProtoPie Studio:

1. You can connect two prototypes running in [the Player app](https://www.protopie.io/learn/docs/player/getting-started). Ensure that both devices and the computer running ProtoPie Studio are connected to the same network.

1. You can connect a prototype in ProtoPie Studio with another prototype running in the Player app. Both ProtoPie Studio and the Player app should be connected to the same network.

Alternatively, you can connect your smart devices to a computer via USB. This method eliminates the dependency on the network connection.

[Learn more](https://www.protopie.io/learn/docs/player/getting-started)Â about connecting smart devices to ProtoPie Studio.

If you are subscribed to a Pro or Enterprise plan, you can create a wider array of connected experiences using [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

## Getting Started

To enable cross-device interactions, ProtoPie utilizes [Send responses](https://www.protopie.io/learn/docs/interactions/responses#send) and [Receive triggers](https://www.protopie.io/learn/docs/interactions/triggers#receive-trigger-properties). A response is triggered when a device with the Receive trigger accepts a message sent from another device using a Send response. It is essential for the received message on one device to match the message sent from the other device.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DZxgxlLiEelQ)

### Setting up the Send Response

### Setting up the Receive Trigger

### Example

![bridge ex](https://cdn.sanity.io/images/vidqzkll/production/b00f588a19d492bdb17821f494cb11a931438fd9-1076x540.gif/bridge_ex.gif)


---
