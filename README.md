# AnnoyTheStreamer

## Description

Python Flask web application allowing viewers to fill in the form and send their meme to be displayed in one of two ways: either using top and bottom text layered on top of the streamer's face or a normal meme with top and bottom text on an image.
The page displaying the meme on top of the camera will refresh every 30 seconds while the page with normal meme will update every 60 seconds.
All the memes will be queued in the database and displayed in order of being submitted.

## Limitations

1. To share the form you have to share your IP address

## Requirements

- For library requirements refer to requirements.txt
- MongoDB Community Server
- MongoDBCompass (optional, but needed to follow instructions below)
- OBS Studio
- [xObsBrowserAutoRefresh](https://github.com/YorVeX/xObsBrowserAutoRefresh)

## Instructions
 
1. Install the following
    - required libraries from requirements.txt.
    - MongoDB Community Server
    - MongoDBCompass
    - OBS Studio
    - [xObsBrowserAutoRefresh](https://github.com/YorVeX/xObsBrowserAutoRefresh)

2. Run MongoDBCompass
    - add new connection
    - just set the name
        - if you want to edit anything else, be sure to copy the URI and update the following line in the client.py file
        ```
        CONNECTION_STRING = "mongodb://localhost:27017"
        ```
    - pick the created connection and choose "connect"
    - create a new database and name it "annoythestreamer"
        - if you want to use a differnt name, be sure to update the following line in the client.py file
        ```
        return client['annoythestreamer']
        ```

3. Be sure to open port 2137 on both your Windows firewall and router
    - If you don't want to open the port, update the following line in the annoythestreamer.py file and steps 5.2, 5.8, 6, 7 to an open port of your choosing
    ```
    app.run(host='0.0.0.0', debug=True, port=2137)    
    ```

4. Open the console in the application directory or navigate to it
    - run the command
    ```
    python annoythestreamer.py
    ```
    - to stop the server click Ctrl+C in the console

5. Run OBS Studio
    - add new source, choose "Browser" and name it "Face Meme"
    - URL: http://localhost:2137/FaceMeme, width: 300, height: 200
    - position it on top of your camera
    - to adjust size change properties of source and the following lines in FaceMeme.html
    ```
    <body style="height: 200px; width: 300px;">
        <div id="image" style="height: 200px; width: 300px; background-size: 300px 200px; background-repeat: no-repeat; background-attachment: fixed"class="parent">
    ```
    - right click the source and choose "filters"
    - add "Browser Auto-refresh" to Effect Filters
    - add new source, choose "Browser" and name it "Normal Meme"
    - URL: http://localhost:2137/NormalMeme, width: 400, height: 250
    - position it wherever you want the meme to be displayed
    - to adjust size change properties of source and the following lines in FaceMeme.html
    ```
    <body style="height: 250px; width: 400px;">
        <div id="image" style="height: 250px; width: 400px; background-size: 400px 250px; background-repeat: no-repeat; background-attachment: fixed"class="parent">
    ```
    - right click the source and choose "filters"
    - add "Browser Auto-refresh" to Effect Filters

6. Open http://localhost:2137 in your browser
    - choose whether you want to use the "Face Meme" or "Normal Meme" form
    - fill in the form and click "submit"
    - to send the photo you need to input an URL

7. To share the form with other people you have to replace "localhost" in the address with either your local IP address (for people using your WiFi network) or public IP address (for people not using your WiFi network)
    (WARNING: Never share your public address with people you don't trust!)
    - to check your local IP address open the command prompt, type "ipconfig" and look for "IPv4 Address"
    - to check your public IP address visit https://www.whatismyip.com/

8. For any subsequent use follow steps 2.3, 4 and 6