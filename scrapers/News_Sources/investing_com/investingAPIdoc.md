## Documentation for Investing-com GitHub API


1. Installation

        npm i investing-com-api

        This will install the necessary modules and package.json/package-lock.json

        This is JavaScript so make sure you have essential packages such as Node.js


2. Usage

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
        



    
