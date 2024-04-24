## Documentation for Investing-com GitHub API


 ### **Installation**

        npm i investing-com-api

        This will install the necessary modules and package.json/package-lock.json

        This is JavaScript so make sure you have essential packages such as Node.js


### **Usage**

        Example Code:
        
            const { investing } = require('investing-com-api');

            async function main() {
                try {
                    const response1 = await investing('currencies/eur-usd'); // Providing a valid mapping.js key
                    const response2 = await investing('currencies/eur-usd', 'P1M', 'P1D'); // With optional params
                    const response3 = await investing('1'); // Providing the pairId directly, even if not present in mapping.js
                } catch (err) {
                    console.error(err);
                }
            }

            main();
        
### **Package.json Modifcation**

        If you are new to JavaScript, in order to run the code you have to 
        do the following:

        1. Go to package.json which will look like this:
        {
            "dependencies": {
                "investing-com-api": "^4.3.3"
            }
        }

        2. Change the package.json to look like the following:
        {
            "dependencies": {
                "investing-com-api": "^4.3.3"
            },
            "scripts": {
                "curr": "node currencies.js",
                "stock": "node stocks.js",
                "future": "node futures.js"
            }
        }

        The file name after "node" is what your js file is called

        3. Finally, in terminal you will do "npm run {script key}"

        The "script key" in this case can either be "curr", "stock", or "future"

        If you create more files don't forget to modify the package.json
    


Here is the Investing-Com API Repository:
https://github.com/DavideViolante/investing-com-api



        


    
