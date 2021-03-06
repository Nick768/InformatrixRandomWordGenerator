# Informatrix Random Word Generator

### How to use?

-   Clone this repository or download the sourcecode as zip file
-   Navigate to the cloned directory (or extract the zip file and navigate to this directory)
-   Start the Main.py as you would start every Python 3 file or start one of the start scripts fitting your OS
-   In your terminal window there should be something like this: `Server started: localhost:8080`
-   open your browser and open the given url (in our example it is `localhost:8080`)
-   That's it!

#### Hint:
If you want your browser to start automatically and go to the url, you have to set
```python
isDevelopmentVersion = False
```
in Main.py
(doesn't work on Android)

#### How to use on Android?

-   install Termux (search for it on Google Play or fdroid)
-   run these commands:
    ```bash
    apt update && apt upgrade && apt install python git
    git clone https://github.com/Nick768/InformatrixRandomWordGenerator
    cd InformatrixRandomWordGenerator/
    python Main.py
    ```
-   open your browser and navigate to the given url (see instructions above)

---

If you want/need a java version, please have a look at:
https://github.com/Nick768/InformatrixRandomWordGenerator-Java
